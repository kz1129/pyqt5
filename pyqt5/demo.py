#coding = 'utf-8'
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_untitled
import time

#demo
def buttonClicked(girl):
    girl.textBrowser.append("hello world")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() #创建窗口对象
    ui = Ui_untitled.Ui_MainWindow()#调用模块的类
    ui.setupUi(MainWindow)#调用模块的类方法 即创建ui
    MainWindow.show()
    sys.exit(app.exec_())