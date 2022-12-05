# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MovimentaçãoVDJsdK.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget, QMainWindow, QGraphicsDropShadowEffect)

from packeg.database import database

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(343, 373)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CentralFrame = QFrame(Form)
        self.CentralFrame.setObjectName(u"CentraFrame")
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
        self.horizontalLayout.setContentsMargins(-1, 7, 6, -1)
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
        self.Titulo = QLineEdit(self.frame)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(20, 20, 290, 36))
        self.Titulo.setMinimumSize(QSize(290, 36))
        self.Titulo.setMaximumSize(QSize(290, 36))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(11)
        self.Titulo.setFont(font1)
        self.Titulo.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.valor = QLineEdit(self.frame)
        self.valor.setObjectName(u"valor")
        self.valor.setGeometry(QRect(20, 80, 290, 36))
        self.valor.setMinimumSize(QSize(290, 36))
        self.valor.setMaximumSize(QSize(290, 36))
        self.valor.setFont(font1)
        self.valor.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.entrada = QPushButton(self.frame)
        self.entrada.setObjectName(u"entrada")
        self.entrada.setGeometry(QRect(20, 140, 130, 36))
        self.entrada.setMinimumSize(QSize(130, 36))
        self.entrada.setMaximumSize(QSize(130, 36))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        self.entrada.setFont(font2)
        self.entrada.setStyleSheet(u"QPushButton{\n"
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
        self.entrada.setIcon(icon2)
        self.entrada.setIconSize(QSize(20, 20))
        self.saida = QPushButton(self.frame)
        self.saida.setObjectName(u"saida")
        self.saida.setGeometry(QRect(180, 140, 130, 36))
        self.saida.setMinimumSize(QSize(130, 36))
        self.saida.setMaximumSize(QSize(130, 36))
        self.saida.setFont(font2)
        self.saida.setStyleSheet(u"QPushButton{\n"
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
        self.saida.setIcon(icon3)
        self.saida.setIconSize(QSize(20, 20))
        self.categoria = QComboBox(self.frame)
        self.categoria.setObjectName(u"categoria")
        self.categoria.setGeometry(QRect(20, 200, 290, 36))
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
        self.movimentar = QPushButton(self.frame)
        self.movimentar.setObjectName(u"movimentar")
        self.movimentar.setGeometry(QRect(70, 260, 180, 36))
        self.movimentar.setMinimumSize(QSize(180, 36))
        self.movimentar.setMaximumSize(QSize(180, 1234567))
        self.movimentar.setFont(font1)
        self.movimentar.setStyleSheet(u"QPushButton{\n"
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
        self.movimentar.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.CentralFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nova Movimenta\u00e7\u00e3o", None))
        self.minimizar.setText("")
        self.fechar.setText("")
        self.Titulo.setPlaceholderText(QCoreApplication.translate("Form", u"Titulo", None))
        self.valor.setPlaceholderText(QCoreApplication.translate("Form", u"Valor", None))
        self.entrada.setText(QCoreApplication.translate("Form", u"Entrada", None))
        self.saida.setText(QCoreApplication.translate("Form", u"Saida", None))


        self.categoria.setPlaceholderText("Selecione a categoria")
        self.database = database("ControleFinanceiro")
        self.database.connect_database()
        dados = self.database.executarFetchall("SELECT * FROM Categoria")
        self.database.close_connection_database()

        for dado in dados:
            self.categoria.addItem("")
            self.categoria.setItemText(dado[0]-1, QCoreApplication.translate("Form", dado[1], None))

        self.movimentar.setText(QCoreApplication.translate("Form", u"Movimentar", None))
    # retranslateUi



class Movimentacao(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.mov = Ui_Form()
        self.mov.setupUi(self)

        self.mov.CentralFrame.setGeometry(9, 9, 325, 355)
        self.dados = ''
        self.categoria = ''
        self.movimentarNome = ''


        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(255, 255, 255, 120))
        self.mov.CentralFrame.setGraphicsEffect(self.shadow)

        self.mov.fechar.clicked.connect(lambda: self.closefrom())
        self.mov.minimizar.clicked.connect(lambda: self.showMinimized())
        self.mov.entrada.clicked.connect(self.entradaSanida)
        self.mov.saida.clicked.connect(self.entradaSanida)
        self.mov.categoria.currentTextChanged.connect(self.selectCategoria)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.mov.barraTitulo.mouseMoveEvent = moveWindow


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def selectCategoria(self, txt):
        self.categoria = txt

    def entradaSanida(self):
        object = self.sender().objectName()

        if object == "entrada":
            self.movimentarNome = "entrada"
        elif object == "saida":
            self.movimentarNome = "saida"

    def closefrom(self):
        self.mov.Titulo.setText("")
        self.mov.valor.setText("")
        self.close()




if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Movimentacao()
    sys.exit(app.exec())
