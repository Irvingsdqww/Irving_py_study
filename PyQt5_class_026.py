# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

import re
import time
import sys
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QMainWindow,QWidget,QPushButton

class quitApplication(QMainWindow):
	def __init__(self):
		super(quitApplication,self).__init__()
		self.resize(400,300)
		self.setWindowTitle('退出应用程序')

		# 添加button
		self.button = QPushButton('退出应用程序')
		# 将信号与槽关联
		self.button.clicked.connect(self.onClick_Button)

		layout = QHBoxLayout()
		layout.addWidget(self.button)
		mainFrame = QWidget()
		mainFrame.setLayout(layout)
		self.setCentralWidget(mainFrame)


	def onClick_Button(self):
		sender = self.sender()
		print(sender.text()+"按钮被按下")
		app = QApplication.instance()
		#退出应用程序
		app.quit()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = quitApplication()
	main.show()
	sys.exit(app.exec_())
