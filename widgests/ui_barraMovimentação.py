# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barraMovimentaçãoDZLRMd.ui'
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
        Form.resize(1018, 88)
        self.pequenoHistoricoEntrada = QFrame(Form)
        self.pequenoHistoricoEntrada.setObjectName(u"pequenoHistoricoEntrada")
        self.pequenoHistoricoEntrada.setGeometry(QRect(0, 10, 1011, 40))
        self.pequenoHistoricoEntrada.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                                   "border-radius:4px;")
        self.pequenoHistoricoEntrada.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.pequenoHistoricoEntrada)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(20, 0, 0, 0)
        self.frame_196 = QFrame(self.pequenoHistoricoEntrada)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMaximumSize(QSize(152, 16777215))
        self.frame_196.setStyleSheet(u"")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_196)
        self.verticalLayout_167.setSpacing(0)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalLayout_167.setContentsMargins(0, 0, 0, 0)
        self.codigo = QLabel(self.frame_196)
        self.codigo.setObjectName(u"codigo")
        self.codigo.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(11)
        self.codigo.setFont(font)
        self.codigo.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.codigo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_167.addWidget(self.codigo)

        self.horizontalLayout_126.addWidget(self.frame_196)

        self.frame_197 = QFrame(self.pequenoHistoricoEntrada)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setStyleSheet(u"")
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_197)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.data = QLabel(self.frame_197)
        self.data.setObjectName(u"data")
        self.data.setMaximumSize(QSize(16777215, 38))
        self.data.setFont(font)
        self.data.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.data.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_169.addWidget(self.data)

        self.horizontalLayout_126.addWidget(self.frame_197)

        self.frame_198 = QFrame(self.pequenoHistoricoEntrada)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setStyleSheet(u"")
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_198)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.categoria = QLabel(self.frame_198)
        self.categoria.setObjectName(u"categoria")
        self.categoria.setFont(font)
        self.categoria.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.categoria.setAlignment(Qt.AlignCenter)

        self.verticalLayout_170.addWidget(self.categoria)

        self.horizontalLayout_126.addWidget(self.frame_198)

        self.frame_250 = QFrame(self.pequenoHistoricoEntrada)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setStyleSheet(u"")
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_250)
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.frame_251 = QFrame(self.frame_250)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setStyleSheet(u"")
        self.frame_251.setFrameShape(QFrame.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.frame_251)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.complemento = QLabel(self.frame_251)
        self.complemento.setObjectName(u"complemento")
        self.complemento.setFont(font)
        self.complemento.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.complemento.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_128.addWidget(self.complemento)

        self.horizontalLayout_127.addWidget(self.frame_251)

        self.horizontalLayout_126.addWidget(self.frame_250)

        self.frame_199 = QFrame(self.pequenoHistoricoEntrada)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setStyleSheet(u"")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_199)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.valor = QLabel(self.frame_199)
        self.valor.setObjectName(u"valor")
        self.valor.setFont(font)
        self.valor.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.valor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_171.addWidget(self.valor)

        self.horizontalLayout_126.addWidget(self.frame_199)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.codigo.setText(QCoreApplication.translate("Form", u"1", None))
        self.data.setText(QCoreApplication.translate("Form", u"12/04/2022", None))
        self.categoria.setText(QCoreApplication.translate("Form", u"Alimenta\u00e7\u00e3o", None))
        self.complemento.setText(QCoreApplication.translate("Form", u"P\u00f3 de cafe", None))
        self.valor.setText(QCoreApplication.translate("Form", u"100,00", None))
    # retranslateUi

class BarraMovimentacao(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.bm = Ui_Form()
        self.bm.setupUi(self)

    def setValues(self, codigo, data, categoria, titulo, valor, tranzacao):
        if tranzacao == "entrada":
            self.bm.valor.setStyleSheet("color: rgb(85, 255, 127);")
        else:
            self.bm.valor.setStyleSheet("color: rgb(255, 0, 0);")

        self.bm.codigo.setText(str(codigo))
        self.bm.data.setText(data)
        self.bm.categoria.setText(categoria)
        self.bm.complemento.setText(titulo)
        self.bm.valor.setText(str(valor))
