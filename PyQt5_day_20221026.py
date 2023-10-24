# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from class_20 import Ui_MainWindow

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainwin = QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(mainwin)
	mainwin.show()
	sys.exit(app.exec_())