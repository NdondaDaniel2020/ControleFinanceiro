# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HistoricoEntradaSaidaDcVrEr.ui'
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
    QPushButton, QSizePolicy, QWidget, QMainWindow)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(536, 127)
        self.pequenoHistoricoSaida = QFrame(Form)
        self.pequenoHistoricoSaida.setObjectName(u"pequenoHistoricoSaida")
        self.pequenoHistoricoSaida.setGeometry(QRect(10, 10, 510, 38))
        self.pequenoHistoricoSaida.setMaximumSize(QSize(16777215, 38))
        self.pequenoHistoricoSaida.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;}")
        self.pequenoHistoricoSaida.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoSaida.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.pequenoHistoricoSaida)
        self.horizontalLayout_116.setSpacing(3)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(10, 0, 3, 0)
        self.pushButton_16 = QPushButton(self.pequenoHistoricoSaida)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(30, 30))
        self.pushButton_16.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(2)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"border-color: rgb(170, 85, 255);\n"
"border: 1px solid rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"border-radius:15px}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(170, 85, 255);\n"
"border: 1px solid rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"border-radius:15px}\n"
"\n"
"QPushButton:pressed{\n"
"border-color: rgb(170, 85, 255);\n"
"border: 1px solid rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"padding: 0px}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../img/Money Bag Franc_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon)
        self.pushButton_16.setIconSize(QSize(24, 26))

        self.horizontalLayout_116.addWidget(self.pushButton_16)

        self.frame_243 = QFrame(self.pequenoHistoricoSaida)
        self.frame_243.setObjectName(u"frame_243")
        self.frame_243.setStyleSheet(u"")
        self.frame_243.setFrameShape(QFrame.StyledPanel)
        self.frame_243.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_243)
        self.horizontalLayout_118.setSpacing(0)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.frame_245 = QFrame(self.frame_243)
        self.frame_245.setObjectName(u"frame_245")
        self.frame_245.setStyleSheet(u"")
        self.frame_245.setFrameShape(QFrame.StyledPanel)
        self.frame_245.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_245)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.nomeSaida = QLabel(self.frame_245)
        self.nomeSaida.setObjectName(u"nomeSaida")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(11)
        self.nomeSaida.setFont(font1)
        self.nomeSaida.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.nomeSaida.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_120.addWidget(self.nomeSaida)


        self.horizontalLayout_118.addWidget(self.frame_245)


        self.horizontalLayout_116.addWidget(self.frame_243)

        self.frame_244 = QFrame(self.pequenoHistoricoSaida)
        self.frame_244.setObjectName(u"frame_244")
        self.frame_244.setStyleSheet(u"")
        self.frame_244.setFrameShape(QFrame.StyledPanel)
        self.frame_244.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_244)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.dataSaida = QLabel(self.frame_244)
        self.dataSaida.setObjectName(u"dataSaida")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(10)
        self.dataSaida.setFont(font2)
        self.dataSaida.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.dataSaida.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.dataSaida)

        self.valorSaida = QLabel(self.frame_244)
        self.valorSaida.setObjectName(u"valorSaida")
        self.valorSaida.setMaximumSize(QSize(147, 16777215))
        self.valorSaida.setFont(font2)
        self.valorSaida.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.valorSaida.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.valorSaida)


        self.horizontalLayout_116.addWidget(self.frame_244)

        self.iconSis = QPushButton(self.pequenoHistoricoSaida)
        self.iconSis.setObjectName(u"iconSis")
        self.iconSis.setMinimumSize(QSize(30, 30))
        self.iconSis.setMaximumSize(QSize(30, 30))
        self.iconSis.setFont(font)
        self.iconSis.setStyleSheet(u"QPushButton{\n"
"border-color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;\n"
"border-radius:15px}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;\n"
"border-radius:15px}\n"
"\n"
"QPushButton:pressed{\n"
"border-color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"padding: 0px\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../img/logoFC.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconSis.setIcon(icon1)
        self.iconSis.setIconSize(QSize(24, 26))

        self.horizontalLayout_116.addWidget(self.iconSis)

        self.pequenoHistoricoEntrada = QFrame(Form)
        self.pequenoHistoricoEntrada.setObjectName(u"pequenoHistoricoEntrada")
        self.pequenoHistoricoEntrada.setGeometry(QRect(10, 70, 511, 38))
        self.pequenoHistoricoEntrada.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;}")
        self.pequenoHistoricoEntrada.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.pequenoHistoricoEntrada)
        self.horizontalLayout_98.setSpacing(3)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(10, 0, 3, 0)
        self.frame_228 = QFrame(self.pequenoHistoricoEntrada)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setStyleSheet(u"")
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_228)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.frame_228)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(30, 30))
        self.pushButton_15.setMaximumSize(QSize(30, 30))
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"border-color: rgb(170, 85, 255);\n"
"border: 1px solid rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"border-radius:15px}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(170, 85, 255);\n"
"border: 1px solid rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"border-radius:15px}\n"
"\n"
"QPushButton:pressed{\n"
"border-color: rgb(170, 85, 255);\n"
"border: 1px solid rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"padding: 0px}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../img/Money Bag Pounds_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setIconSize(QSize(22, 24))

        self.horizontalLayout_100.addWidget(self.pushButton_15)

        self.frame_227 = QFrame(self.frame_228)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setStyleSheet(u"")
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_227)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.nomeEntrada = QLabel(self.frame_227)
        self.nomeEntrada.setObjectName(u"nomeEntrada")
        self.nomeEntrada.setFont(font1)
        self.nomeEntrada.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.nomeEntrada.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_99.addWidget(self.nomeEntrada)


        self.horizontalLayout_100.addWidget(self.frame_227)


        self.horizontalLayout_98.addWidget(self.frame_228)

        self.frame_230 = QFrame(self.pequenoHistoricoEntrada)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setStyleSheet(u"")
        self.frame_230.setFrameShape(QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_230)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.dataEntrada = QLabel(self.frame_230)
        self.dataEntrada.setObjectName(u"dataEntrada")
        self.dataEntrada.setFont(font2)
        self.dataEntrada.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.dataEntrada.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.dataEntrada)

        self.valorEntrada = QLabel(self.frame_230)
        self.valorEntrada.setObjectName(u"valorEntrada")
        self.valorEntrada.setMaximumSize(QSize(147, 16777215))
        self.valorEntrada.setFont(font2)
        self.valorEntrada.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.valorEntrada.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.valorEntrada)


        self.horizontalLayout_98.addWidget(self.frame_230)

        self.iconSis_2 = QPushButton(self.pequenoHistoricoEntrada)
        self.iconSis_2.setObjectName(u"iconSis_2")
        self.iconSis_2.setMinimumSize(QSize(30, 30))
        self.iconSis_2.setMaximumSize(QSize(30, 30))
        self.iconSis_2.setFont(font)
        self.iconSis_2.setStyleSheet(u"QPushButton{\n"
"border-color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;\n"
"border-radius:15px}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;\n"
"border-radius:15px}\n"
"\n"
"QPushButton:pressed{\n"
"border-color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"padding: 0px}\n"
"")
        self.iconSis_2.setIcon(icon1)
        self.iconSis_2.setIconSize(QSize(24, 26))

        self.horizontalLayout_98.addWidget(self.iconSis_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_16.setText("")
        self.nomeSaida.setText(QCoreApplication.translate("Form", u"  Teiser", None))
        self.dataSaida.setText(QCoreApplication.translate("Form", u"2022-04-12", None))
        self.valorSaida.setText(QCoreApplication.translate("Form", u"Kz 100", None))
        self.iconSis.setText("")
        self.pushButton_15.setText("")
        self.nomeEntrada.setText(QCoreApplication.translate("Form", u"  Esferografica", None))
        self.dataEntrada.setText(QCoreApplication.translate("Form", u"2022-04-12", None))
        self.valorEntrada.setText(QCoreApplication.translate("Form", u"Kz 200 ", None))
        self.iconSis_2.setText("")
    # retranslateUi


class HistoricoEntradaSaida(QMainWindow):
      def __init__(self):
          QMainWindow.__init__(self)
          self.hes = Ui_Form()
          self.hes.setupUi(self)


      def setEntrada(self, nome, data, valor):
          self.hes.nomeEntrada.setText(nome)
          self.hes.dataEntrada.setText(data)
          self.hes.valorEntrada.setText(valor)


      def setSaida(self, nome, data, valor):
          self.hes.nomeSaida.setText(nome)
          self.hes.dataSaida.setText(data)
          self.hes.valorSaida.setText(valor)
