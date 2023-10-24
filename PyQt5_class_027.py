# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

# PyQt5_class_027
import re
import time
import sys
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QWidget,QMainWindow,QPushButton

class creen_Coordinate(QWidget):
	def __init__(self,widget=None):
		super(creen_Coordinate, self).__init__()
		self.widget = widget
		self.init_ui()

	def init_ui(self):
		btn = QPushButton(self.widget)
		btn.setText('按钮')
		btn.clicked.connect(self.onClick_Button)
		btn.move(24,52)
		self.widget.resize(300, 240) #设置工作区的尺寸
		self.widget.move(250,200)
		self.widget.setWindowTitle('屏幕坐标系')

	def onClick_Button(self):
		sender = self.sender()
		print('点击按钮: {}'.format(sender.text()))
		print('窗口')
		print('widget.x() = {}'.format(self.widget.x())) #窗口横坐标
		print('widget.y() = {}'.format(self.widget.y())) #窗口纵坐标
		print('widget.width() = {}'.format(self.widget.width())) #工作区宽度
		print('widget.height() = {}'.format(self.widget.height())) #工作区高度
		print('工作区')
		print('widget.geometry().x() = {}'.format(self.widget.geometry().x()))
		print('widget.geometry().y() = {}'.format(self.widget.geometry().y()))
		print('widget.geometry().width() = {}'.format(self.widget.geometry().width()))
		print('widget.geometry().height() = {}'.format(self.widget.geometry().height()))
		print('工作区1')
		print('widget.frameGeometry().x() = {}'.format(self.widget.frameGeometry().x()))
		print('widget.frameGeometry().y() = {}'.format(self.widget.frameGeometry().y()))
		print('widget.frameGeometry().width() = {}'.format(self.widget.frameGeometry().width()))
		print('widget.frameGeometry().height() = {}'.format(self.widget.frameGeometry().height()))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = QWidget()
	creen = creen_Coordinate(widget=widget)
	widget.show()
	sys.exit(app.exec_())
