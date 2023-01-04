# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barraCategoriaiLKbEr.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget, QMainWindow)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(272, 58)
        self.pequenoHistoricoEntrada = QFrame(Form)
        self.pequenoHistoricoEntrada.setObjectName(u"pequenoHistoricoEntrada")
        self.pequenoHistoricoEntrada.setGeometry(QRect(10, 10, 251, 40))
        self.pequenoHistoricoEntrada.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada.setMaximumSize(QSize(16777215, 40))
        self.pequenoHistoricoEntrada.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:4px;")
        self.pequenoHistoricoEntrada.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_281 = QHBoxLayout(self.pequenoHistoricoEntrada)
        self.horizontalLayout_281.setSpacing(0)
        self.horizontalLayout_281.setObjectName(u"horizontalLayout_281")
        self.horizontalLayout_281.setContentsMargins(20, 0, 0, 0)
        self.frame_525 = QFrame(self.pequenoHistoricoEntrada)
        self.frame_525.setObjectName(u"frame_525")
        self.frame_525.setStyleSheet(u"")
        self.frame_525.setFrameShape(QFrame.StyledPanel)
        self.frame_525.setFrameShadow(QFrame.Raised)
        self.verticalLayout_381 = QVBoxLayout(self.frame_525)
        self.verticalLayout_381.setSpacing(0)
        self.verticalLayout_381.setObjectName(u"verticalLayout_381")
        self.verticalLayout_381.setContentsMargins(0, 0, 0, 0)
        self.text = QLabel(self.frame_525)
        self.text.setObjectName(u"text")
        self.text.setMaximumSize(QSize(16777215, 38))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(11)
        self.text.setFont(font)
        self.text.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_381.addWidget(self.text)


        self.horizontalLayout_281.addWidget(self.frame_525)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text.setText(QCoreApplication.translate("Form", u"Alimenta\u00e7\u00e3o", None))
    # retranslateUi


class BarraCategoria(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.bc = Ui_Form()
        self.bc.setupUi(self)

    def setValores(self, txt):
        self.bc.text.setText(txt)

