# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReceberPagamentonVURLd.ui'
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
        Form.resize(343, 356)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CentralFrame = QFrame(Form)
        self.CentralFrame.setObjectName(u"CentralFrame")
        self.CentralFrame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.CentralFrame.setFrameShape(QFrame.StyledPanel)
        self.CentralFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.CentralFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.barraTitulo = QFrame(self.CentralFrame)
        self.barraTitulo.setObjectName(u"barraTitulo")
        self.barraTitulo.setMaximumSize(QSize(16777215, 40))
        self.barraTitulo.setFrameShape(QFrame.StyledPanel)
        self.barraTitulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.barraTitulo)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 4, 4, -1)
        self.label = QLabel(self.barraTitulo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minimizar = QPushButton(self.barraTitulo)
        self.minimizar.setObjectName(u"minimizar")
        self.minimizar.setMinimumSize(QSize(28, 25))
        self.minimizar.setMaximumSize(QSize(28, 26))
        self.minimizar.setStyleSheet(u"QPushButton{\n"
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
        self.minimizar.setIcon(icon)
        self.minimizar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.minimizar)

        self.fechar = QPushButton(self.barraTitulo)
        self.fechar.setObjectName(u"fechar")
        self.fechar.setMinimumSize(QSize(28, 26))
        self.fechar.setMaximumSize(QSize(28, 26))
        self.fechar.setStyleSheet(u"QPushButton{\n"
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
        self.fechar.setIcon(icon1)
        self.fechar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.fechar)


        self.verticalLayout_2.addWidget(self.barraTitulo)

        self.frame = QFrame(self.CentralFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.adicionarConta = QPushButton(self.frame)
        self.adicionarConta.setObjectName(u"adicionarConta")
        self.adicionarConta.setGeometry(QRect(70, 200, 180, 36))
        self.adicionarConta.setMinimumSize(QSize(180, 36))
        self.adicionarConta.setMaximumSize(QSize(180, 1234567))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(11)
        self.adicionarConta.setFont(font1)
        self.adicionarConta.setStyleSheet(u"QPushButton{\n"
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
        self.adicionarConta.setIconSize(QSize(20, 20))
        self.categoria = QComboBox(self.frame)
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.setObjectName(u"categoria")
        self.categoria.setGeometry(QRect(20, 20, 290, 36))
        self.categoria.setMinimumSize(QSize(290, 36))
        self.categoria.setMaximumSize(QSize(290, 36))
        self.categoria.setFont(font1)
        self.categoria.setStyleSheet(u"\n"
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
        self.cliente = QComboBox(self.frame)
        self.cliente.addItem("")
        self.cliente.addItem("")
        self.cliente.addItem("")
        self.cliente.setObjectName(u"cliente")
        self.cliente.setGeometry(QRect(20, 80, 290, 36))
        self.cliente.setMinimumSize(QSize(290, 36))
        self.cliente.setMaximumSize(QSize(290, 36))
        self.cliente.setFont(font1)
        self.cliente.setStyleSheet(u"\n"
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
        self.valorTotal = QLineEdit(self.frame)
        self.valorTotal.setObjectName(u"valorTotal")
        self.valorTotal.setGeometry(QRect(20, 140, 290, 36))
        self.valorTotal.setMinimumSize(QSize(290, 36))
        self.valorTotal.setMaximumSize(QSize(290, 36))
        self.valorTotal.setFont(font1)
        self.valorTotal.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 250, 170, 27))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.CentralFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Receber Pagamento", None))
        self.minimizar.setText("")
        self.fechar.setText("")
        self.adicionarConta.setText(QCoreApplication.translate("Form", u"Adicionar conta", None))
        self.categoria.setItemText(0, "")
        self.categoria.setItemText(1, QCoreApplication.translate("Form", u"Presta\u00e7\u00e3o de servi\u00e7o", None))
        self.categoria.setItemText(2, QCoreApplication.translate("Form", u"Casa", None))
        self.categoria.setItemText(3, QCoreApplication.translate("Form", u"Produto", None))

        self.categoria.setCurrentText("")
        self.categoria.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione a categoria", None))
        self.cliente.setItemText(0, "")
        self.cliente.setItemText(1, QCoreApplication.translate("Form", u"Daniel", None))
        self.cliente.setItemText(2, QCoreApplication.translate("Form", u"WhiteSpot", None))

        self.cliente.setCurrentText("")
        self.cliente.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione o cliente", None))
        self.valorTotal.setPlaceholderText(QCoreApplication.translate("Form", u"Valor", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Total a Pagar: Kz 0", None))
    # retranslateUi

