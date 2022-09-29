#-*- coding:UTF-8 -*-

import sys,math
from PyQt5.QtCore import (Qt, pyqtSignal, QObject, QPoint, QPointF,
                          QRect, QSize, QStandardPaths, QUrl)
from PyQt5.QtGui import (QColor, QImage, QPixmap, QPainter, QPainterPath,
                         QRadialGradient, QDesktopServices)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QMenuBar, 
                             QMenu, QAction, QActionGroup, QMessageBox)
from PyQt5.QtNetwork import (QNetworkAccessManager, QNetworkRequest, QNetworkDiskCache)
 
#瓷砖尺寸(以像素为单位)
# tile(瓷砖)，我们的地图图像就是有一小块小块的图像平铺而成，就是铺瓷砖，形成整个地面
TILE_DIM = 256
 
class MyPoint(QPoint):
    def __init__(self, *par):
        if par:
            super(MyPoint, self).__init__(*par)
        else:
            super(MyPoint, self).__init__()
    
    #提供hash值，作为字典的键值        
    def __hash__(self):
        return self.x() * 17 ^ self.y()
    
    def __repr__(self):
        return 'Point(%s, %s)' % (self.x(), self.y())
    
#根据地图坐标(维度lat， 经度lng, 缩放系数zoom),计算瓷砖位置
def tileForCoordinate(lat, lng, zoom):
    zn = float(1 << zoom)
    tx = float(lng + 180.0) / 360.0
    ty = (1.0 - math.log(math.tan(lat * math.pi / 180.0) +
          1.0 / math.cos(lat * math.pi / 180.0)) / math.pi) / 2.0
    
    return QPointF(tx * zn, ty * zn)
 
#根据瓷砖x方向位置计算经度
def longitudeFromTile(tx, zoom):
    zn = float(1 << zoom)
    lng = tx / zn * 360.0 - 180.0
    return lng
 
#根据瓷砖y方向位置计算纬度
def latitudeFromTile(ty, zoom):
    zn = float(1 << zoom)
    n = math.pi - 2 * math.pi * ty / zn
    lat = 180.0 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n)))
    return lat
 
class MyMap(QObject):
    updated = pyqtSignal(QRect)
    
    def __init__(self, parent = None):
        super(MyMap, self).__init__(parent)
        
        self._offset = QPoint()     
        self._tilesRect = QRect()   
        self._tilePixmaps = {} #MyPoint(x, y) to QPixmap mapping
        self._nam = QNetworkAccessManager()
        self._url = QUrl()      
        #公共变量
        self.width = 480      
        self.height = 300
        self.zoom = 14  #地图缩放系数
        self.latitude = 39.9   #纬度
        self.longitude = 116.4 #经度
        
        self._emptyTile = QPixmap(TILE_DIM, TILE_DIM)
        self._emptyTile.fill(Qt.lightGray)
        
        cache = QNetworkDiskCache()
        cache.setCacheDirectory(QStandardPaths.writableLocation(QStandardPaths.CacheLocation))
        self._nam.setCache(cache)
        self._nam.finished.connect(self.handleNetworkData)
        
    #刷新
    def invalidate(self):
        if self.width <= 0 or self.height <= 0:
            return
        ct = tileForCoordinate(self.latitude, self.longitude, self.zoom)
        tx = ct.x()
        ty = ct.y()
        
        #中心位置瓷砖的左上角坐标
        xp = int(self.width / 2 - (tx - math.floor(tx)) * TILE_DIM)
        yp = int(self.height / 2 - (ty - math.floor(ty)) * TILE_DIM)
        
        #第一块瓷砖水平和垂直起始位置
        xa = (xp + TILE_DIM - 1) / TILE_DIM
        ya = (yp + TILE_DIM - 1) / TILE_DIM
        xs = int(tx) - xa
        ys = int(ty) - ya
        
        #左上角瓷砖的位置偏移量
        self._offset = QPoint(xp - xa * TILE_DIM, yp - ya * TILE_DIM)
        
        #最后一块瓷砖水平和垂直结束位置
        xe = int(tx) + (self.width - xp - 1) / TILE_DIM
        ye = int(ty) + (self.height - yp - 1) / TILE_DIM
        
        #构建整个地图平铺区域
        self._tilesRect = QRect(xs, ys, xe - xs + 1, ye - ys + 1)

        if self._url.isEmpty():
            self.download()
            
        #通知刷新
        self.updated.emit(QRect(0, 0, self.width, self.height))
        
    #渲染
    def render(self, p, rect):
        for x in range(self._tilesRect.width()):
            for y in range(self._tilesRect.height()):
                tp = MyPoint(x + self._tilesRect.left(), y + self._tilesRect.top())
                box = self.tileRect(tp)
                if rect.intersects(box):
                    p.drawPixmap(box, self._tilePixmaps.get(tp, self._emptyTile))
    
    #平移
    def pan(self, delta):
        dx = QPointF(delta) / float(TILE_DIM)
        center = tileForCoordinate(self.latitude, self.longitude, self.zoom) - dx
        self.latitude = latitudeFromTile(center.y(), self.zoom)
        self.longitude = longitudeFromTile(center.x(), self.zoom)
        self.invalidate()
        
    #slots, 处理接收到的网路数据
    def handleNetworkData(self, reply):
        img = QImage()
        tp = MyPoint(reply.request().attribute(QNetworkRequest.User))
        if not reply.error():
            #将下载的数据保存到位图中
            if img.load(reply, None):
                self._tilePixmaps[tp] = QPixmap.fromImage(img)
            reply.deleteLater()
            self.updated.emit(self.tileRect(tp))
        else :
            print('下载失败: %s.' % reply.errorString())
            
        #将为使用的瓷砖清理掉
        bound = self._tilesRect.adjusted(-2, -2, 2, 2)
        for tp in list(self._tilePixmaps.keys()):
            if not bound.contains(tp):
                del self._tilePixmaps[tp]
        
        self.download()
        
    #从网络上下载数据
    def download(self):
        grab = None
        #计算抓取位置
        for x in range(self._tilesRect.width()):
            for y in range(self._tilesRect.height()):
                tp = MyPoint(self._tilesRect.topLeft() + QPoint(x, y))
                if tp not in self._tilePixmaps:
                    grab = QPoint(tp)
                    break
        
        if grab is None:
            self._url = QUrl()
            return
         
        path = 'https://tile.openstreetmap.org/%d/%d/%d.png' % (self.zoom, grab.x(), grab.y())
        self._url = QUrl(path)
        request = QNetworkRequest()
        request.setUrl(self._url)
        request.setAttribute(QNetworkRequest.User, grab)
        self._nam.get(request)

    def tileRect(self, tp):
        t = tp - self._tilesRect.topLeft()
        x = t.x() * TILE_DIM + self._offset.x()
        y = t.y() * TILE_DIM + self._offset.y() 
        
        return QRect(x, y, TILE_DIM, TILE_DIM)  
    
#地图显示交互部件
class LightMaps(QWidget):  
    def __init__(self, parent = None):
        super(LightMaps, self).__init__(parent)
        
        self.invert = False #白天夜晚模式切换
        
        self._normalMap = MyMap(self)     
        self._normalMap.updated.connect(self.updateMap)
     
    #设置中心位置   
    def setCenter(self, lat, lng):
        self._normalMap.latitude = lat
        self._normalMap.longitude = lng
        self._normalMap.invalidate()
        
    #slot
    def toggleNightMode(self):
        self.invert = not self.invert
        self.update()
    
    #更新地图    
    def updateMap(self, rct):
        self.update(rct)
    
    def resizeEvent(self, event):
        self._normalMap.width = self.width()
        self._normalMap.height = self.height()
        self._normalMap.invalidate()
        
    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        self._normalMap.render(p, event.rect())
        p.end()
        
        if self.invert:
            p = QPainter(self)
            p.setCompositionMode(QPainter.CompositionMode_Difference)
            p.fillRect(event.rect(), Qt.white)
            p.end()
        
 
class DemoLightMap(QMainWindow):
    def __init__(self, parent=None):
        super(DemoLightMap, self).__init__(parent)   
        
        #设置窗口标题
        self.setWindowTitle('实战Qt for Python: 一个轻量级的地图应用')      
        #设置窗口大小
        self.resize(640, 480)
        
        self.lightMap = LightMaps(self)
        self.setCentralWidget(self.lightMap)
        self.lightMap.setFocus()
      
        self.initUi()
        
    def initUi(self):
        self.initMenuBar()
    
    def initMenuBar(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        menuFile = menuBar.addMenu('文件(&F)')
        menuOption = menuBar.addMenu('操作(&O')
        menuHelp = menuBar.addMenu('帮助(&H)')
        
        actionExit = QAction('退出(&X)', self)
        actionExit.triggered.connect(QApplication.instance().quit)
        menuFile.addAction(actionExit)
        
        aBeijing = QAction('北京(&B)', self)
        aBeijing.setCheckable(True)
        aBeijing.setChecked(True)
        aBeijing.triggered.connect(lambda: self.chooseCity(39.92, 116.46))
        aShangHai = QAction('上海(&S)', self)
        aShangHai.setCheckable(True)
        aShangHai.setChecked(False)
        aShangHai.triggered.connect(lambda: self.chooseCity(31.22, 121.48))
        aTianjin = QAction('天津(&T)', self)
        aTianjin.setCheckable(True)
        aTianjin.setChecked(False)
        aTianjin.triggered.connect(lambda: self.chooseCity(39.13, 117.2))
        aChongQing = QAction('重庆(&C)', self)
        aChongQing.setCheckable(True)
        aChongQing.setChecked(False)
        aChongQing.triggered.connect(lambda: self.chooseCity(29.55, 106.58))
        
        aGrp = QActionGroup(self)
        aGrp.addAction(aBeijing)
        aGrp.addAction(aShangHai)
        aGrp.addAction(aTianjin)
        aGrp.addAction(aChongQing)
        
        aNightMode = QAction('夜晚模式', self)
        aNightMode.setCheckable(True)
        aNightMode.setChecked(False)
        aNightMode.triggered.connect(self.lightMap.toggleNightMode)  
        
        menuOption.addAction(aBeijing)
        menuOption.addAction(aShangHai)
        menuOption.addAction(aTianjin)
        menuOption.addAction(aChongQing)
        menuOption.addSeparator()
        menuOption.addAction(aNightMode)
        
        osmAction = QAction("关于OpenStreetMap", self)
        osmAction.triggered.connect(self.aboutOsm)
        menuHelp.addAction(osmAction)
        
    def chooseCity(self, lat, lng):
        self.lightMap.setCenter(lat, lng)
        
    def aboutOsm(self):
        QDesktopServices.openUrl(QUrl('https://www.openstreetmap.org'))
                 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoLightMap()
    window.show()
    sys.exit(app.exec())   
