# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barraFluxoGhCXcf.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget, QMainWindow)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(731, 59)
        self.pequenoHistoricoEntrada_22 = QFrame(Form)
        self.pequenoHistoricoEntrada_22.setObjectName(u"pequenoHistoricoEntrada_22")
        self.pequenoHistoricoEntrada_22.setGeometry(QRect(10, 10, 714, 40))
        self.pequenoHistoricoEntrada_22.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_22.setMaximumSize(QSize(16777215, 40))
        self.pequenoHistoricoEntrada_22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;")
        self.pequenoHistoricoEntrada_22.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_221 = QHBoxLayout(self.pequenoHistoricoEntrada_22)
        self.horizontalLayout_221.setSpacing(0)
        self.horizontalLayout_221.setObjectName(u"horizontalLayout_221")
        self.horizontalLayout_221.setContentsMargins(20, 0, 0, 0)
        self.frame_425 = QFrame(self.pequenoHistoricoEntrada_22)
        self.frame_425.setObjectName(u"frame_425")
        self.frame_425.setStyleSheet(u"")
        self.frame_425.setFrameShape(QFrame.StyledPanel)
        self.frame_425.setFrameShadow(QFrame.Raised)
        self.verticalLayout_309 = QVBoxLayout(self.frame_425)
        self.verticalLayout_309.setSpacing(0)
        self.verticalLayout_309.setObjectName(u"verticalLayout_309")
        self.verticalLayout_309.setContentsMargins(0, 0, 0, 0)
        self.data = QLabel(self.frame_425)
        self.data.setObjectName(u"data")
        self.data.setMaximumSize(QSize(16777215, 38))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(11)
        self.data.setFont(font)
        self.data.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_309.addWidget(self.data)


        self.horizontalLayout_221.addWidget(self.frame_425)

        self.frame_426 = QFrame(self.pequenoHistoricoEntrada_22)
        self.frame_426.setObjectName(u"frame_426")
        self.frame_426.setStyleSheet(u"")
        self.frame_426.setFrameShape(QFrame.StyledPanel)
        self.frame_426.setFrameShadow(QFrame.Raised)
        self.verticalLayout_310 = QVBoxLayout(self.frame_426)
        self.verticalLayout_310.setSpacing(0)
        self.verticalLayout_310.setObjectName(u"verticalLayout_310")
        self.verticalLayout_310.setContentsMargins(0, 0, 0, 0)
        self.entrada = QLabel(self.frame_426)
        self.entrada.setObjectName(u"entrada")
        self.entrada.setFont(font)
        self.entrada.setStyleSheet(u"color: rgb(85, 255, 127)")
        self.entrada.setAlignment(Qt.AlignCenter)

        self.verticalLayout_310.addWidget(self.entrada)


        self.horizontalLayout_221.addWidget(self.frame_426)

        self.frame_427 = QFrame(self.pequenoHistoricoEntrada_22)
        self.frame_427.setObjectName(u"frame_427")
        self.frame_427.setStyleSheet(u"")
        self.frame_427.setFrameShape(QFrame.StyledPanel)
        self.frame_427.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_222 = QHBoxLayout(self.frame_427)
        self.horizontalLayout_222.setSpacing(0)
        self.horizontalLayout_222.setObjectName(u"horizontalLayout_222")
        self.horizontalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.frame_428 = QFrame(self.frame_427)
        self.frame_428.setObjectName(u"frame_428")
        self.frame_428.setStyleSheet(u"")
        self.frame_428.setFrameShape(QFrame.StyledPanel)
        self.frame_428.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_223 = QHBoxLayout(self.frame_428)
        self.horizontalLayout_223.setObjectName(u"horizontalLayout_223")
        self.horizontalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.saida = QLabel(self.frame_428)
        self.saida.setObjectName(u"saida")
        self.saida.setFont(font)
        self.saida.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.saida.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_223.addWidget(self.saida)


        self.horizontalLayout_222.addWidget(self.frame_428)


        self.horizontalLayout_221.addWidget(self.frame_427)

        self.frame_429 = QFrame(self.pequenoHistoricoEntrada_22)
        self.frame_429.setObjectName(u"frame_429")
        self.frame_429.setStyleSheet(u"")
        self.frame_429.setFrameShape(QFrame.StyledPanel)
        self.frame_429.setFrameShadow(QFrame.Raised)
        self.verticalLayout_311 = QVBoxLayout(self.frame_429)
        self.verticalLayout_311.setObjectName(u"verticalLayout_311")
        self.verticalLayout_311.setContentsMargins(0, 0, 0, 0)
        self.total = QLabel(self.frame_429)
        self.total.setObjectName(u"total")
        self.total.setFont(font)
        self.total.setStyleSheet(u"color: rgb(185, 85, 255)")
        self.total.setAlignment(Qt.AlignCenter)

        self.verticalLayout_311.addWidget(self.total)


        self.horizontalLayout_221.addWidget(self.frame_429)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.data.setText(QCoreApplication.translate("Form", u"12/04/2022", None))
        self.entrada.setText(QCoreApplication.translate("Form", u"0", None))
        self.saida.setText(QCoreApplication.translate("Form", u"0", None))
        self.total.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi


class BarraFluxo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.bf = Ui_Form()
        self.bf.setupUi(self)

    def setValues(self, data, entrada, saida, total):
        self.bf.data.setText(data)
        self.bf.entrada.setText(entrada)
        self.bf.saida.setText(saida)
        self.bf.total.setText(total)
