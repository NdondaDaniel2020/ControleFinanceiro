import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


from tests import Ui_MainWindow
from stackedWidgets import SlidingStackedWidget

class Test (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.slide = SlidingStackedWidget()
        self.slide.setAnimation(QEasingCurve.OutCirc)

        self.widget = QWidget()
        self.widget.setObjectName(u"frame_2")
        self.widget.setStyleSheet("background-color: rgb(85, 255, 255);")

        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"frame_2")
        self.widget_2.setStyleSheet("background-color: rgb(255, 0, 0);")

        self.widget_3 = QWidget()
        self.widget_3.setObjectName(u"frame_2")
        self.widget_3.setStyleSheet("background-color: rgb(85, 255, 127);")

        self.widget_4 = QWidget()
        self.widget_4.setObjectName(u"frame_2")
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 0);")

        self.slide.addWidget(self.widget)
        self.slide.addWidget(self.widget_2)
        self.slide.addWidget(self.widget_3)
        self.slide.addWidget(self.widget_4)

        self.widget_5 = QWidget()
        self.widget_5.setObjectName(u"frame_2")
        self.widget_5.setStyleSheet("background-color: rgb(170, 255, 255);")

        self.ui.verticalLayout_2.addWidget(self.slide)

        # self.ui.pushButton.clicked.connect(self.slide.slideInPrev)
        # self.ui.pushButton_2.clicked.connect(self.slide.slideInNext)
        self.ui.pushButton.clicked.connect(lambda: self.slide.slideInIdx(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.slide.slideInIdx(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.slide.slideInIdx(2))
        self.ui.pushButton_4.clicked.connect(lambda: self.tesInwdt())

        self.show()


    def testSlide(self):
        self.slide.setDirection(Qt.Vertical)
        self.slide.setAnimation(QEasingCurve.OutCubic)
        self.slide.slideInIdx(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    exit(app.exec())