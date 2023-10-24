# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

import re
import time
import sys
# PyQt5_class_029

from PyQt5.QtWidgets import QApplication,QHBoxLayout,QWidget,QMainWindow,QPushButton,QToolTip
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
	def __init__(self):
		super(TooltipForm, self).__init__()
		self.initUI()

	def initUI(self):
		# 设置字体及字体大小
		QToolTip.setFont(QFont('ScansSerif', 12))
		self.setToolTip('今天是<b>星期一</b>')
		self.setGeometry(300,300,200,200)
		self.setWindowTitle('设置空间提示信息')
		self.creat_button()

	def creat_button(self):
		btn = QPushButton('设置的按钮')
		btn.setToolTip('are you sure?')
		btn.clicked.connect(self.onClick_button)
		layout = QHBoxLayout()
		layout.addWidget(btn)

		mainFrame = QWidget()
		mainFrame.setLayout(layout)
		self.setCentralWidget(mainFrame)

	def print_geometry(self):
		print('窗口')
		print('widget.x() = {}'.format(self.geometry().x()))  # 窗口横坐标
		print('widget.y() = {}'.format(self.geometry().y()))  # 窗口纵坐标
		print('widget.width() = {}'.format(self.geometry().width()))  # 工作区宽度
		print('widget.height() = {}'.format(self.geometry().height()))  # 工作区高度

	def onClick_button(self):
		sender = self.sender()
		self.print_geometry()
		print('sender:{}'.format(sender.text()))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = TooltipForm()
	main.show()
	sys.exit(app.exec_())



