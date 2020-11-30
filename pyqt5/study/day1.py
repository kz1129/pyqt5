import sys
from PyQt5.QtWidgets import QApplication, QWidget
#QApplication代表应用程序 QWidget代表窗口，必须导入的

if __name__ == '__main__':
    #__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
    # 这句话的意思就是，当模块被直接运行时，以下代码块将被运行，
    # 当模块是被导入时，代码块不被运行。

    #应用类的实现
    app = QApplication(sys.argv)#sys.argv 获取命令行输入的参数，是一个数组
    #创建一个窗口对象
    w = QWidget()
    #设置窗口的尺寸
    w.resize(300, 150)
    #移动窗口
    w.move(300, 300)

    #标题
    w.setWindowTitle('窗口名')
    #显示窗口
    w.show()

    #进入程序主循环，并通过exit函数确保主循环安全结束，没有这一行代码的话程序会闪退
    sys.exit(app.exec_())

