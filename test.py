import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import loginwindow
import tkinter


# class MyMain(QtWidgets.QMainWindow, loginwindow.Ui_MainWindow):
#     def __init__(self):
#         super(MyMain, self).__init__()
#         self.setupUi(self)
#
#     def tj(self):
#         print('sucess')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = loginwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    result = ui.btu_even()
    MainWindow.show()

    if result == 0:
        # tkinter.messagebox.showinfo(title='kingbell', message='ooxx未授权xxoo')
        messagewin = tkinter.Tk()
        messagewin.title('金贝')
        messagewin.geometry('588x417+500+200', )
        messagewin.wm_attributes('-topmost', -1)
        tkinter.Label(messagewin, text="未授权21313", font=('Arial', 14)).place(x=50, y=50)
        messagewin.mainloop()
    elif result == 1:
        tkinter.messagebox.showinfo(title='kingbell', message='密码错误')
    elif result == 2:
        tkinter.messagebox.showinfo(title='kingbell', message='登录成功')

    sys.exit(app.exec_())
