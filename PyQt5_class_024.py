# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

import re
import time
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QDialog
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
	def __init__(self, parent=None):
		super(FirstMainWin,self).__init__(parent)
		self.setWindowTitle('第一个主窗口应用')

		# 设置窗口尺寸
		self.resize(400,300)

		# 设置状态栏
		self.status = self.statusBar()

		# 编辑状态栏内容
		self.status.showMessage('只存在5秒的消息', 5000)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\QQ_ICON.ico'))
	mainwin = QMainWindow()
	firstmainwin = FirstMainWin()
	firstmainwin.show()
	sys.exit(app.exec_())

