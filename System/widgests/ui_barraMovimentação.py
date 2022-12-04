# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barraMovimentaçãoWaDJOa.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1018, 88)
        self.pequenoHistoricoEntrada_5 = QFrame(Form)
        self.pequenoHistoricoEntrada_5.setObjectName(u"pequenoHistoricoEntrada_5")
        self.pequenoHistoricoEntrada_5.setGeometry(QRect(0, 10, 1011, 40))
        self.pequenoHistoricoEntrada_5.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;")
        self.pequenoHistoricoEntrada_5.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.pequenoHistoricoEntrada_5)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(20, 0, 0, 0)
        self.frame_196 = QFrame(self.pequenoHistoricoEntrada_5)
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
        self.codigo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_167.addWidget(self.codigo)


        self.horizontalLayout_126.addWidget(self.frame_196)

        self.frame_197 = QFrame(self.pequenoHistoricoEntrada_5)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setStyleSheet(u"")
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_197)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.data_2 = QLabel(self.frame_197)
        self.data_2.setObjectName(u"data_2")
        self.data_2.setMaximumSize(QSize(16777215, 38))
        self.data_2.setFont(font)
        self.data_2.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.data_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_169.addWidget(self.data_2)


        self.horizontalLayout_126.addWidget(self.frame_197)

        self.frame_198 = QFrame(self.pequenoHistoricoEntrada_5)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setStyleSheet(u"")
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_198)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.categoria_2 = QLabel(self.frame_198)
        self.categoria_2.setObjectName(u"categoria_2")
        self.categoria_2.setFont(font)
        self.categoria_2.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.categoria_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_170.addWidget(self.categoria_2)


        self.horizontalLayout_126.addWidget(self.frame_198)

        self.frame_250 = QFrame(self.pequenoHistoricoEntrada_5)
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

        self.frame_199 = QFrame(self.pequenoHistoricoEntrada_5)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setStyleSheet(u"")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_199)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.label_223 = QLabel(self.frame_199)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setFont(font)
        self.label_223.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.label_223.setAlignment(Qt.AlignCenter)

        self.verticalLayout_171.addWidget(self.label_223)


        self.horizontalLayout_126.addWidget(self.frame_199)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.codigo.setText(QCoreApplication.translate("Form", u"1", None))
        self.data_2.setText(QCoreApplication.translate("Form", u"12/04/2022", None))
        self.categoria_2.setText(QCoreApplication.translate("Form", u"Alimenta\u00e7\u00e3o", None))
        self.complemento.setText(QCoreApplication.translate("Form", u"P\u00f3 de cafe", None))
        self.label_223.setText(QCoreApplication.translate("Form", u"100,00", None))
    # retranslateUi

