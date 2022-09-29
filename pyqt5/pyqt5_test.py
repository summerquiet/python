#-*- coding:UTF-8 -*-

import sys
from PyQt5 import QtWidgets,QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360,160)
widget.setWindowTitle("Pyqt5 测试")

menuBar = widget.menuBar() 
menuFile = menuBar.addMenu('文件(&F)')
menuOption = menuBar.addMenu('操作(&O')
menuHelp = menuBar.addMenu('帮助(&H)')
        
actionExit = QAction('退出(&X)', self)
actionExit.triggered.connect(QApplication.instance().quit)
menuFile.addAction(actionExit)

widget.show()
sys.exit(app.exec_())
