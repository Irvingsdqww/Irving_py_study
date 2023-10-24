# -*- coding:utf-8 -*-
# @Time :2021/8/7 19:59
# @Author :Irving

import re
import time
import sys
from PyQt5.QtWidgets import QApplication,QWidget



if __name__ == '__main__':
	app = QApplication(sys.argv)

	w = QWidget()

	w.resize(300,150)
	w.move(300,300)
	w.setWindowTitle('first PyQt5')
	w.show()

	sys.exit(app.exec_())
