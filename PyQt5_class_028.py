# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

import re
import time
import sys
# PyQt5_class_028
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QWidget,QMainWindow,QPushButton
# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

import re
import time
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QDialog
from PyQt5.QtGui import QIcon

'''
窗口的setWindowIcon方法用于设置窗口的图标，只在windous中可用
QAapplication中的setWindowIcon方法用于设置主窗口的图标和应用程序的图标，但是调用了窗口的setWindowIcon方法
QAapplication中的setWindowIcon方法就只能用于设置应用程序图标了
'''

class FirstMainWin(QMainWindow):
	def __init__(self, parent=None):
		super(FirstMainWin,self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 250, 250)
		self.setWindowTitle('设置窗口图标')
		self.setWindowIcon(QIcon(r'D:\python_study\ICO\QQ_ICON.ico'))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon(r'D:\python_study\ICO\favicon.ico'))
	mainwin = QMainWindow()
	firstmainwin = FirstMainWin()
	firstmainwin.show()
	sys.exit(app.exec_())


