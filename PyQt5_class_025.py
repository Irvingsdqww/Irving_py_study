# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

import re
import time
import sys
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QDialog,QDesktopWidget
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
	def __init__(self):
		super(CenterForm,self).__init__()
		self.setWindowTitle('让窗口居中')
		self.resize(400,300)
		self.status = self.statusBar()
		self.status.showMessage('只存在5秒窗口',5000)

	def center(self):
		# 获取屏幕大小对象
		screen = QDesktopWidget().screenGeometry()
		# 获取窗口大小对象
		size = self.geometry()
		newLeft = (screen.width() - size.width())/2 + 300
		newTop = (screen.height() - size.height())/2 + 300
		self.move(newLeft,newTop)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\QQ_ICON.ico'))
	main = CenterForm()
	main.show()
	sys.exit(app.exec_())