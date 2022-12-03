# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MovimentaçãoCKAgDF.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(343, 373)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CentraFrame = QFrame(Form)
        self.CentraFrame.setObjectName(u"CentraFrame")
        self.CentraFrame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.CentraFrame.setFrameShape(QFrame.StyledPanel)
        self.CentraFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.CentraFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.CentraFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 7, 6, -1)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(28, 25))
        self.pushButton.setMaximumSize(QSize(28, 26))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../img/24x24/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(28, 26))
        self.pushButton_2.setMaximumSize(QSize(28, 26))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../img/24x24/cil-x-f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.CentraFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.BuscarStatus_4 = QLineEdit(self.frame)
        self.BuscarStatus_4.setObjectName(u"BuscarStatus_4")
        self.BuscarStatus_4.setGeometry(QRect(20, 20, 290, 36))
        self.BuscarStatus_4.setMinimumSize(QSize(290, 36))
        self.BuscarStatus_4.setMaximumSize(QSize(290, 36))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(11)
        self.BuscarStatus_4.setFont(font1)
        self.BuscarStatus_4.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.BuscarStatus_5 = QLineEdit(self.frame)
        self.BuscarStatus_5.setObjectName(u"BuscarStatus_5")
        self.BuscarStatus_5.setGeometry(QRect(20, 80, 290, 36))
        self.BuscarStatus_5.setMinimumSize(QSize(290, 36))
        self.BuscarStatus_5.setMaximumSize(QSize(290, 36))
        self.BuscarStatus_5.setFont(font1)
        self.BuscarStatus_5.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 140, 130, 36))
        self.pushButton_3.setMinimumSize(QSize(130, 36))
        self.pushButton_3.setMaximumSize(QSize(130, 36))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../img/cil-vertical-align-top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 20))
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(180, 140, 130, 36))
        self.pushButton_4.setMinimumSize(QSize(130, 36))
        self.pushButton_4.setMaximumSize(QSize(130, 36))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../img/cil-vertical-align-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(20, 20))
        self.comboBox_5 = QComboBox(self.frame)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(20, 200, 290, 36))
        self.comboBox_5.setMinimumSize(QSize(290, 36))
        self.comboBox_5.setMaximumSize(QSize(290, 36))
        self.comboBox_5.setFont(font2)
        self.comboBox_5.setStyleSheet(u"\n"
"\n"
"\n"
"QComboBox{\n"
"background-color:rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"padding: 5px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
" border: 2px solid rgb(170, 85, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 25px; \n"
"border-left-width: 3px;\n"
"border-left-color: rgb(255, 255, 255);\n"
"border-left-style: solid;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"color: rgb(255, 255, 255);	\n"
"background-color:rgb(170, 85, 255);\n"
"padding: 10px;\n"
"selection-background-color: rgb(195, 155, 255);\n"
"border:2px solid  rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(70, 260, 180, 36))
        self.pushButton_5.setMinimumSize(QSize(180, 36))
        self.pushButton_5.setMaximumSize(QSize(180, 1234567))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_5.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.CentraFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nova Movimenta\u00e7\u00e3o", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.BuscarStatus_4.setPlaceholderText(QCoreApplication.translate("Form", u"Titulo", None))
        self.BuscarStatus_5.setPlaceholderText(QCoreApplication.translate("Form", u"Valor", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Entrada", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Saida", None))
        self.comboBox_5.setCurrentText("")
        self.comboBox_5.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione a categoria", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Movimentar", None))
    # retranslateUi

