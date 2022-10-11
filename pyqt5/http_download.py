#-*- UTF-8 -*-

import sys
from PyQt5.QtCore import Qt, QDir, QFile, QFileInfo, QIODevice, QUrl
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                             QHBoxLayout, QVBoxLayout, QLabel, QLineEdit,
                             QProgressDialog, QMessageBox, QPushButton)
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest,QNetworkReply
 
class DemoDownloadFile(QDialog):
    def __init__(self, parent=None):
        super(DemoDownloadFile, self).__init__(parent)   
        
         # 设置窗口标题
        self.setWindowTitle('实战 Qt for Python: 文件下载')      
        # 设置窗口大小
        self.resize(400, 120)
      
        self.url = QUrl()
        self.nam = QNetworkAccessManager()
        self.reply = None
        self.outFile = None
        self.httpGetId = 0
        self.httpRequestAborted = False
    
        self.initUi()    
    
    def initUi(self):
        #编辑下载地址
        self.urlLineEdit = QLineEdit('https://www.qt.io')
        
        urlLabel = QLabel('网址(&U):')
        urlLabel.setBuddy(self.urlLineEdit)
        
        #状态信息
        self.statusLabel = QLabel('在这里输入要下载的文件的网址。')  
        self.statusLabel.setWordWrap(True)
        
        #下载和退出按钮
        self.btnDownload = QPushButton('下载')
        self.btnDownload.setDefault(True)
        self.btnQuit = QPushButton('退出')
        self.btnQuit.setAutoDefault(False)
        
        buttonBox = QDialogButtonBox()
        buttonBox.addButton(self.btnDownload, QDialogButtonBox.ActionRole)
        buttonBox.addButton(self.btnQuit, QDialogButtonBox.RejectRole)
        
        #进度显示对话框
        self.progressDialog = None
    
        #连接slot函数
        self.urlLineEdit.textChanged.connect(self.enableDownloadButton)
        self.nam.authenticationRequired.connect(self.slotAuthenticationRequired)
        self.nam.sslErrors.connect(self.sslErrors)
        self.btnDownload.clicked.connect(self.downloadFile)
        self.btnQuit.clicked.connect(self.close)
        
        topLayout = QHBoxLayout()
        topLayout.addWidget(urlLabel)
        topLayout.addWidget(self.urlLineEdit)
        
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(16)
        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(self.statusLabel)
        mainLayout.addWidget(buttonBox)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        
        self.urlLineEdit.setFocus()
        
    #发出下载请求
    def startRequest(self, url):
        self.reply = self.nam.get(QNetworkRequest(url))
        self.reply.finished.connect(self.httpFinished)
        self.reply.readyRead.connect(self.httpReadyRead)
        self.reply.downloadProgress.connect(self.updateDataReadProgress)
        
    #下载文件
    def downloadFile(self):
        self.url = QUrl(self.urlLineEdit.text())
        fileInfo = QFileInfo(self.url.path())
        filename = fileInfo.fileName()
        
        #如果没有文件名，就假定一个缺省文件
        if not filename:
            filename = 'index.html'
         
        #如果存储目录有相同文件名称，则询问是否覆盖   
        if QFile.exists(filename):
            ret = QMessageBox.question(self, '下载文件', 
                                       '在当前目录下已经存着文件 %s。覆盖它吗?' % filename,
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if ret == QMessageBox.No:
                return
            
            #删除原来的文件
            QFile.remove(filename)
            
        self.outFile = QFile(filename)
        if not self.outFile.open(QIODevice.WriteOnly):
            QMessageBox.information(self, '下载文件', 
                                    '不能保存文件 %s: %s.' % (filename, self.outFile.errorString()))
            self.outFile = None
            return
        
        self.progressDialog = QProgressDialog(self)
        self.progressDialog.canceled.connect(self.cancelDownload)
        self.progressDialog.setWindowTitle('下载文件')
        self.progressDialog.setLabelText('正在下载 %s.' % filename)
        
        self.btnDownload.setEnabled(False)
        self.httpRequestAborted = False
        self.startRequest(self.url)

    #终止下载
    def cancelDownload(self):
        self.statusLabel.setText('下载被取消了.')   
        self.httpRequestAborted = True
        if self.reply is not None:
            self.reply.abort()
        self.btnDownload.setEnabled(True)
        
    #下载完成后
    def httpFinished(self): 
               
        #释放进度对话框
        if self.progressDialog is not None:
            self.progressDialog.hide()
            self.progressDialog.deleteLater()
            self.progressDialog = None   
               
        #如果被终止下载了，做相应的善后处理
        if self.httpRequestAborted:
            if self.outFile is not None:
                self.outFile.close()
                self.outFile.remove()
                self.outFile = None
                
            self.reply.deleteLater()
            self.reply = None
            return 
        
        self.outFile.flush()
        self.outFile.close()
        
        redirectionTarget = self.reply.attribute(QNetworkRequest.RedirectionTargetAttribute)
        
        if self.reply.error():
            self.outFile.remove()
            QMessageBox.information(self, '文件下载',
                                    '下载失败: %s.' % self.reply.errorString())
            self.btnDownload.setEnabled(True)
        elif redirectionTarget is not None:
            newUrl = self.url.resolved(redirectionTarget)
            
            ret = QMessageBox.question(self, '下载文件', '重定向到文件 %s?' % newUrl.toString(),
                                       QMessageBox.Yes | QMessageBox.No)
            
            if ret == QMessageBox.Yes:
                self.url = newUrl
                self.reply.deleteLater()
                self.reply = None
                self.outFile.open(QIODevice.WriteOnly)
                self.outFile.resize(0)
                self.startRequest(self.url)
                return
        else:
            filename = QFileInfo(QUrl(self.urlLineEdit.text()).path()).fileName()
            self.statusLabel.setText('文件 %s 下载到 %s.' % (filename, QDir.currentPath()))
            self.btnDownload.setEnabled(True)
            
        self.reply.deleteLater()
        self.reply = None
        self.outFile = None
     
    #保存下载的数据   
    def httpReadyRead(self):
        if self.outFile is not None:
            self.outFile.write(self.reply.readAll())
            
    #更新进度对话框的进度显示信息
    def updateDataReadProgress(self, bytesRead, totalBytes):
        if self.httpRequestAborted:
            return
        
        if self.progressDialog is not None:
            self.progressDialog.setMaximum(totalBytes)
            self.progressDialog.setValue(bytesRead)
        
    #下载地址发生了改变，如果地址为空，则禁用下载按钮，否则启用
    def enableDownloadButton(self):
        self.btnDownload.setEnabled(self.urlLineEdit.text() != '')
        
    #处理许可下载信息
    def slotAuthenticationRequired(self, authenticator):
        import os
        from PyQt5 import uic
        
        ui = os.path.join(os.path.dirname(__file__), 'authenticationdialog.ui')
        dlg = uic.loadUi(ui)
        dlg.adjustSize()
        dlg.siteDescription.setText('%s at %s' % (authenticator.realm(), self.url.host()))
        
        dlg.userEdit.setText(self.url.userName())
        dlg.passwordEdit.setText(self.url.password())
        
        if dlg.exec() == QDialog.Accepted:
            authenticator.setUser(dlg.userEdit.text())
            authenticator.setPassword(dlg.passwordEdit.text())
            
    #SSL 错误处理
    def sslErrors(self, reply, errors):
        errorString = ", ".join([str(error.errorString()) for error in errors])
        
        ret = QMessageBox.warning(self, 'HTTP 文件下载示例',
                                  '发生了SSL错误: %s' % errorString,
                                  QMessageBox.Ignore | QMessageBox.Abort)
        
        if ret == QMessageBox.Ignore:
            self.reply.ignoreSslErrors()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoDownloadFile()
    window.show()
    sys.exit(app.exec())
