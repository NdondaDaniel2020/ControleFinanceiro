# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barraReceberContaYDSzwL.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QCborMap)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMainWindow)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1036, 90)
        self.pequenoHistoricoEntrada_10 = QFrame(Form)
        self.pequenoHistoricoEntrada_10.setObjectName(u"pequenoHistoricoEntrada_10")
        self.pequenoHistoricoEntrada_10.setGeometry(QRect(10, 30, 1016, 40))
        self.pequenoHistoricoEntrada_10.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;")
        self.pequenoHistoricoEntrada_10.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.pequenoHistoricoEntrada_10)
        self.horizontalLayout_137.setSpacing(0)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(15, 0, 0, 0)
        self.frame_274 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setMinimumSize(QSize(110, 0))
        self.frame_274.setMaximumSize(QSize(110, 16777215))
        self.frame_274.setStyleSheet(u"")
        self.frame_274.setFrameShape(QFrame.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Raised)
        self.verticalLayout_210 = QVBoxLayout(self.frame_274)
        self.verticalLayout_210.setSpacing(0)
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.verticalLayout_210.setContentsMargins(0, 0, 0, 0)
        self.numero = QLabel(self.frame_274)
        self.numero.setObjectName(u"numero")
        self.numero.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(11)
        self.numero.setFont(font)
        self.numero.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.numero.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_210.addWidget(self.numero)


        self.horizontalLayout_137.addWidget(self.frame_274)

        self.frame_289 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_289.setObjectName(u"frame_289")
        self.frame_289.setMinimumSize(QSize(110, 0))
        self.frame_289.setMaximumSize(QSize(110, 16777215))
        self.frame_289.setStyleSheet(u"")
        self.frame_289.setFrameShape(QFrame.StyledPanel)
        self.frame_289.setFrameShadow(QFrame.Raised)
        self.verticalLayout_216 = QVBoxLayout(self.frame_289)
        self.verticalLayout_216.setSpacing(0)
        self.verticalLayout_216.setObjectName(u"verticalLayout_216")
        self.verticalLayout_216.setContentsMargins(0, 0, 0, 0)
        self.emissao = QLabel(self.frame_289)
        self.emissao.setObjectName(u"emissao")
        self.emissao.setMaximumSize(QSize(16777215, 38))
        self.emissao.setFont(font)
        self.emissao.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.emissao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_216.addWidget(self.emissao)


        self.horizontalLayout_137.addWidget(self.frame_289)

        self.frame_290 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_290.setObjectName(u"frame_290")
        self.frame_290.setMinimumSize(QSize(190, 0))
        self.frame_290.setMaximumSize(QSize(190, 16777215))
        self.frame_290.setStyleSheet(u"")
        self.frame_290.setFrameShape(QFrame.StyledPanel)
        self.frame_290.setFrameShadow(QFrame.Raised)
        self.verticalLayout_217 = QVBoxLayout(self.frame_290)
        self.verticalLayout_217.setSpacing(0)
        self.verticalLayout_217.setObjectName(u"verticalLayout_217")
        self.verticalLayout_217.setContentsMargins(1, 0, 0, 0)
        self.categoria = QLabel(self.frame_290)
        self.categoria.setObjectName(u"categoria")
        self.categoria.setFont(font)
        self.categoria.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.categoria.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_217.addWidget(self.categoria)


        self.horizontalLayout_137.addWidget(self.frame_290)

        self.frame_291 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_291.setObjectName(u"frame_291")
        self.frame_291.setMinimumSize(QSize(125, 0))
        self.frame_291.setMaximumSize(QSize(125, 16777215))
        self.frame_291.setStyleSheet(u"")
        self.frame_291.setFrameShape(QFrame.StyledPanel)
        self.frame_291.setFrameShadow(QFrame.Raised)
        self.verticalLayout_218 = QVBoxLayout(self.frame_291)
        self.verticalLayout_218.setSpacing(0)
        self.verticalLayout_218.setObjectName(u"verticalLayout_218")
        self.verticalLayout_218.setContentsMargins(3, 0, 0, 0)
        self.cliente = QLabel(self.frame_291)
        self.cliente.setObjectName(u"cliente")
        self.cliente.setMaximumSize(QSize(16777215, 38))
        self.cliente.setFont(font)
        self.cliente.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.cliente.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_218.addWidget(self.cliente)


        self.horizontalLayout_137.addWidget(self.frame_291)

        self.frame_292 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_292.setObjectName(u"frame_292")
        self.frame_292.setMinimumSize(QSize(117, 0))
        self.frame_292.setMaximumSize(QSize(119, 16777215))
        self.frame_292.setStyleSheet(u"")
        self.frame_292.setFrameShape(QFrame.StyledPanel)
        self.frame_292.setFrameShadow(QFrame.Raised)
        self.verticalLayout_219 = QVBoxLayout(self.frame_292)
        self.verticalLayout_219.setSpacing(0)
        self.verticalLayout_219.setObjectName(u"verticalLayout_219")
        self.verticalLayout_219.setContentsMargins(10, 0, 0, 0)
        self.vencimento = QLabel(self.frame_292)
        self.vencimento.setObjectName(u"vencimento")
        self.vencimento.setMaximumSize(QSize(16777215, 38))
        self.vencimento.setFont(font)
        self.vencimento.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.vencimento.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_219.addWidget(self.vencimento)


        self.horizontalLayout_137.addWidget(self.frame_292)

        self.frame_293 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_293.setObjectName(u"frame_293")
        self.frame_293.setMaximumSize(QSize(12345678, 16777215))
        self.frame_293.setStyleSheet(u"")
        self.frame_293.setFrameShape(QFrame.StyledPanel)
        self.frame_293.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.frame_293)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(2, 0, 0, 0)
        self.valorTotal = QLabel(self.frame_293)
        self.valorTotal.setObjectName(u"valorTotal")
        self.valorTotal.setFont(font)
        self.valorTotal.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.valorTotal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_141.addWidget(self.valorTotal)


        self.horizontalLayout_137.addWidget(self.frame_293)

        self.frame_294 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_294.setObjectName(u"frame_294")
        self.frame_294.setStyleSheet(u"")
        self.frame_294.setFrameShape(QFrame.StyledPanel)
        self.frame_294.setFrameShadow(QFrame.Raised)
        self.verticalLayout_220 = QVBoxLayout(self.frame_294)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.verticalLayout_220.setContentsMargins(7, 0, 0, 0)
        self.valorPago = QLabel(self.frame_294)
        self.valorPago.setObjectName(u"valorPago")
        self.valorPago.setMinimumSize(QSize(96, 0))
        self.valorPago.setFont(font)
        self.valorPago.setStyleSheet(u"color:rgb(170, 85, 255)")
        self.valorPago.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_220.addWidget(self.valorPago)


        self.horizontalLayout_137.addWidget(self.frame_294)

        self.frame_295 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_295.setObjectName(u"frame_295")
        self.frame_295.setMinimumSize(QSize(0, 25))
        self.frame_295.setMaximumSize(QSize(79, 35))
        self.frame_295.setStyleSheet(u"")
        self.frame_295.setFrameShape(QFrame.StyledPanel)
        self.frame_295.setFrameShadow(QFrame.Raised)
        self.verticalLayout_221 = QVBoxLayout(self.frame_295)
        self.verticalLayout_221.setSpacing(0)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.verticalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.status = QPushButton(self.frame_295)
        self.status.setObjectName(u"status")
        self.status.setMinimumSize(QSize(62, 31))
        self.status.setMaximumSize(QSize(57, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.status.setFont(font1)
        self.status.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_221.addWidget(self.status, 0, Qt.AlignLeft)


        self.horizontalLayout_137.addWidget(self.frame_295)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.numero.setText(QCoreApplication.translate("Form", u"1", None))
        self.emissao.setText(QCoreApplication.translate("Form", u"12/04/2022", None))
        self.categoria.setText(QCoreApplication.translate("Form", u"presta\u00e7\u00e3o de servi\u00e7o", None))
        self.cliente.setText(QCoreApplication.translate("Form", u"Beltrano", None))
        self.vencimento.setText(QCoreApplication.translate("Form", u"12/04/2022", None))
        self.valorTotal.setText(QCoreApplication.translate("Form", u"20.000", None))
        self.valorPago.setText(QCoreApplication.translate("Form", u"100,00", None))
        self.status.setText(QCoreApplication.translate("Form", u"Aberto", None))
    # retranslateUi



class BarraReceberConta(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.brc = Ui_Form()
        self.brc.setupUi(self)

    def setValues(self, numero, emissao, categoria, cliente, vencimento, valorTotal, valorPago):
        self.brc.numero.setText(numero)
        self.brc.emissao.setText(emissao)
        self.brc.categoria.setText(categoria)
        self.brc.cliente.setText(cliente)
        self.brc.vencimento.setText(vencimento)
        self.brc.valorTotal.setText(valorTotal)
        self.brc.valorPago.setText(valorPago)