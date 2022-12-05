# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contasAreceberpmcHcZ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QMainWindow, QGraphicsDropShadowEffect)
from packeg.database import database

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(343, 373)
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
        self.horizontalLayout.setContentsMargins(6, 4, 4, -1)
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
        self.adicionarConta.setGeometry(QRect(70, 260, 180, 36))
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
        self.dataVenciamento = QDateEdit(self.frame)
        self.dataVenciamento.setObjectName(u"dataVenciamento")
        self.dataVenciamento.setGeometry(QRect(20, 200, 291, 36))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.dataVenciamento.setFont(font2)
        self.dataVenciamento.setStyleSheet(u"QDateEdit{\n"
"background-color:rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"padding: 5px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit:hover{\n"
" border: 2px solid rgb(170, 85, 255);\n"
"}\n"
"")
        self.dataVenciamento.setDate(QDate(2022, 12, 4))

        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.CentralFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Adicionar conta a receber", None))
        self.minimizar.setText("")
        self.fechar.setText("")

        self.database = database("ControleFinanceiro")

        self.categoria.setPlaceholderText("Selecione a categoria")
        self.database.connect_database()
        dados = self.database.executarFetchall("SELECT * FROM Categoria")
        self.database.disconnect_database()
        for dado in dados:
            self.categoria.addItem("")
            self.categoria.setItemText(dado[0]-1, QCoreApplication.translate("Form", dado[1], None))


        self.cliente.setPlaceholderText("Selecione o cliente")
        self.database.connect_database()
        dados = self.database.executarFetchall("SELECT * FROM Cliente")
        self.database.disconnect_database()
        for dado in dados:
            self.cliente.addItem("")
            self.cliente.setItemText(dado[0]-1, QCoreApplication.translate("Form", dado[1], None))

        self.valorTotal.setPlaceholderText(QCoreApplication.translate("Form", u"Valor Total", None))
    # retranslateUi


class ContasAreceber(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ca = Ui_Form()
        self.ca.setupUi(self)

        self.ca.CentralFrame.setGeometry(9, 9, 325, 355)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(255, 255, 255, 120))
        self.ca.CentralFrame.setGraphicsEffect(self.shadow)

        self.ca.fechar.clicked.connect(lambda: self.closefrom())
        self.ca.minimizar.clicked.connect(lambda: self.showMinimized())
        self.ca.categoria.currentTextChanged.connect(self.selectCategoria)
        self.ca.cliente.currentTextChanged.connect(self.selectCliente)

        self.cliente = ''
        self.categoria = ''

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ca.barraTitulo.mouseMoveEvent = moveWindow


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def selectCategoria(self, txt):
        self.categoria = txt

    def selectCliente(self, txt):
        self.cliente = txt

    def closefrom(self):
        self.ca.valorTotal.setText("")
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ContasAreceber()
    sys.exit(app.exec())
