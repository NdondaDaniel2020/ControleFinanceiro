# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SystemSCkIvgrU.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_SplashCreen(object):
    def setupUi(self, SplashCreen):
        if not SplashCreen.objectName():
            SplashCreen.setObjectName(u"SplashCreen")
        SplashCreen.resize(418, 421)
        SplashCreen.setStyleSheet(u"")
        self.centralwidget = QWidget(SplashCreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border:0px")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CentralFrame = QFrame(self.centralwidget)
        self.CentralFrame.setObjectName(u"CentralFrame")
        self.CentralFrame.setMinimumSize(QSize(400, 240))
        self.CentralFrame.setMaximumSize(QSize(400, 240))
        font = QFont()
        font.setPointSize(7)
        self.CentralFrame.setFont(font)
        self.CentralFrame.setStyleSheet(u"QToolTip{\n"
"	background-color: rgb(170, 85, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border-left: 3px solid rgb(255, 255, 255);\n"
"	pedding-left: 8px;\n"
"}")
        self.CentralFrame.setFrameShape(QFrame.StyledPanel)
        self.CentralFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.CentralFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_SC = QFrame(self.CentralFrame)
        self.frame_SC.setObjectName(u"frame_SC")
        self.frame_SC.setMinimumSize(QSize(400, 240))
        self.frame_SC.setMaximumSize(QSize(400, 240))
        self.frame_SC.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius: 15px; ")
        self.frame_SC.setFrameShape(QFrame.StyledPanel)
        self.frame_SC.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_SC)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.linhaBranca_9 = QFrame(self.frame_SC)
        self.linhaBranca_9.setObjectName(u"linhaBranca_9")
        self.linhaBranca_9.setMinimumSize(QSize(398, 238))
        self.linhaBranca_9.setMaximumSize(QSize(398, 238))
        self.linhaBranca_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px; ")
        self.linhaBranca_9.setFrameShape(QFrame.StyledPanel)
        self.linhaBranca_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.linhaBranca_9)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_4 = QStackedWidget(self.linhaBranca_9)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setMinimumSize(QSize(396, 236))
        self.stackedWidget_4.setMaximumSize(QSize(396, 236))
        self.stackedWidget_4.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius: 15px; ")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.verticalLayout = QVBoxLayout(self.page_login)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_login = QFrame(self.page_login)
        self.title_login.setObjectName(u"title_login")
        self.title_login.setMinimumSize(QSize(0, 50))
        self.title_login.setMaximumSize(QSize(16777215, 50))
        self.title_login.setFrameShape(QFrame.StyledPanel)
        self.title_login.setFrameShadow(QFrame.Raised)
        self.fechar_3 = QToolButton(self.title_login)
        self.fechar_3.setObjectName(u"fechar_3")
        self.fechar_3.setGeometry(QRect(370, 7, 21, 21))
        self.fechar_3.setStyleSheet(u"QToolButton:hover{\n"
"	background-color: rgb(170, 0, 255);\n"
"	border-radius:10px;\n"
"}\n"
"QToolButton:pressed{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../img/cancel_512px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fechar_3.setIcon(icon)
        self.fechar_3.setIconSize(QSize(20, 20))
        self.criadoPor_3 = QLabel(self.title_login)
        self.criadoPor_3.setObjectName(u"criadoPor_3")
        self.criadoPor_3.setGeometry(QRect(20, 30, 110, 16))
        self.criadoPor_3.setStyleSheet(u"color:#ffffff;\n"
"")
        self.data_3 = QLabel(self.title_login)
        self.data_3.setObjectName(u"data_3")
        self.data_3.setGeometry(QRect(20, 10, 91, 16))
        self.data_3.setStyleSheet(u"")
        self.camera_2 = QToolButton(self.title_login)
        self.camera_2.setObjectName(u"camera_2")
        self.camera_2.setGeometry(QRect(330, 7, 31, 31))
        self.camera_2.setStyleSheet(u"QToolButton:hover{\n"
"	background-color: rgb(150, 76, 228);\n"
"	border-radius:10px;\n"
"}\n"
"QToolButton:pressed{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../img/Instagram_90px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera_2.setIcon(icon1)
        self.camera_2.setIconSize(QSize(100, 200))

        self.verticalLayout.addWidget(self.title_login)

        self.container_login = QFrame(self.page_login)
        self.container_login.setObjectName(u"container_login")
        self.container_login.setMinimumSize(QSize(261, 0))
        self.container_login.setFrameShape(QFrame.StyledPanel)
        self.container_login.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.container_login)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.login = QFrame(self.container_login)
        self.login.setObjectName(u"login")
        self.login.setMinimumSize(QSize(0, 0))
        self.login.setMaximumSize(QSize(1234, 1234))
        self.login.setFrameShape(QFrame.StyledPanel)
        self.login.setFrameShadow(QFrame.Raised)
        self.email_login = QLineEdit(self.login)
        self.email_login.setObjectName(u"email_login")
        self.email_login.setGeometry(QRect(30, 20, 201, 25))
        self.email_login.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(150, 76, 228);\n"
"border:1px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(208, 208, 208);\n"
"padding-left:3px;}\n"
"QLineEdit:hover{\n"
"background-color: rgb(141, 72, 215);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;}\n"
"QLineEdit:focus{\n"
"background-color: rgb(134, 69, 208);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(230, 187, 255);}")
        self.email_login.setEchoMode(QLineEdit.Normal)
        self.email_login.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sengup = QPushButton(self.login)
        self.sengup.setObjectName(u"sengup")
        self.sengup.setGeometry(QRect(130, 120, 90, 27))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(8)
        self.sengup.setFont(font1)
        self.sengup.setStyleSheet(u"QPushButton{\n"
"color: rgb(150, 76, 228);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border: 1.3px solid rgb(150, 76, 228);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(132, 68, 205);\n"
"border-radius:5px;\n"
"border: 2px solid rgb(170, 0, 255)\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(170, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border: 1.3px solid rgb(150, 76, 228);\n"
"}\n"
"")
        self.login_btn = QPushButton(self.login)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(32, 120, 90, 27))
        self.login_btn.setFont(font1)
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"border: 1.3px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"color:#aa00ff;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.password = QLineEdit(self.login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 70, 201, 25))
        self.password.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(150, 76, 228);\n"
"border:1px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(208, 208, 208);\n"
"padding-left:3px;\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(141, 72, 215);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;}\n"
"\n"
"QLineEdit:focus{\n"
"background-color: rgb(134, 69, 208);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(230, 187, 255);}")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.senhaIncorreta_2 = QLabel(self.login)
        self.senhaIncorreta_2.setObjectName(u"senhaIncorreta_2")
        self.senhaIncorreta_2.setGeometry(QRect(150, 100, 81, 10))
        font2 = QFont()
        font2.setPointSize(8)
        self.senhaIncorreta_2.setFont(font2)
        self.senhaIncorreta_2.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.login)

        self.zone_logo = QFrame(self.container_login)
        self.zone_logo.setObjectName(u"zone_logo")
        self.zone_logo.setMinimumSize(QSize(145, 0))
        self.zone_logo.setMaximumSize(QSize(145, 12345))
        self.zone_logo.setFrameShape(QFrame.StyledPanel)
        self.zone_logo.setFrameShadow(QFrame.Raised)
        self.logoPrincipal_2 = QLabel(self.zone_logo)
        self.logoPrincipal_2.setObjectName(u"logoPrincipal_2")
        self.logoPrincipal_2.setGeometry(QRect(4, 0, 139, 121))
        self.logoPrincipal_2.setStyleSheet(u"")
        self.logoPrincipal_2.setPixmap(QPixmap(u"../img/finacialControrlEffct.png"))
        self.logoPrincipal_2.setAlignment(Qt.AlignCenter)
        self.faceid_login = QPushButton(self.zone_logo)
        self.faceid_login.setObjectName(u"faceid_login")
        self.faceid_login.setGeometry(QRect(25, 140, 95, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.faceid_login.setFont(font3)
        self.faceid_login.setStyleSheet(u"QPushButton{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"color:#ffffff;\n"
"background-color:rgb(132, 68, 205);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"}\n"
"QToolTip{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:3px;\n"
"border:3px solid rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.zone_logo)

        self.singup = QFrame(self.container_login)
        self.singup.setObjectName(u"singup")
        self.singup.setMinimumSize(QSize(0, 0))
        self.singup.setMaximumSize(QSize(0, 16777215))
        self.singup.setFrameShape(QFrame.StyledPanel)
        self.singup.setFrameShadow(QFrame.Raised)
        self.login_btn_singup = QPushButton(self.singup)
        self.login_btn_singup.setObjectName(u"login_btn_singup")
        self.login_btn_singup.setGeometry(QRect(30, 130, 90, 27))
        self.login_btn_singup.setFont(font1)
        self.login_btn_singup.setStyleSheet(u"QPushButton{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"border: 1.3px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"color:#aa00ff;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.email_singup = QLineEdit(self.singup)
        self.email_singup.setObjectName(u"email_singup")
        self.email_singup.setGeometry(QRect(20, 10, 201, 25))
        self.email_singup.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(150, 76, 228);\n"
"border:1px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(208, 208, 208);\n"
"padding-left:3px;\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(141, 72, 215);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;}\n"
"\n"
"QLineEdit:focus{\n"
"background-color: rgb(134, 69, 208);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(230, 187, 255);}")
        self.email_singup.setEchoMode(QLineEdit.Normal)
        self.email_singup.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.singup_singup = QPushButton(self.singup)
        self.singup_singup.setObjectName(u"singup_singup")
        self.singup_singup.setGeometry(QRect(130, 130, 90, 27))
        self.singup_singup.setFont(font1)
        self.singup_singup.setStyleSheet(u"QPushButton{\n"
"color: rgb(150, 76, 228);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border: 1.3px solid rgb(170, 0, 255);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(132, 68, 205);\n"
"border-radius:5px;\n"
"border: 2px solid rgb(170, 0, 255)\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(170, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border: 1.3px solid rgb(170, 0, 255);\n"
"}\n"
"")
        self.password1 = QLineEdit(self.singup)
        self.password1.setObjectName(u"password1")
        self.password1.setGeometry(QRect(20, 50, 201, 25))
        self.password1.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(150, 76, 228);\n"
"border:1px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(208, 208, 208);\n"
"padding-left:3px;\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(141, 72, 215);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;}\n"
"\n"
"QLineEdit:focus{\n"
"background-color: rgb(134, 69, 208);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(230, 187, 255);}")
        self.password1.setEchoMode(QLineEdit.Password)
        self.password1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.password2 = QLineEdit(self.singup)
        self.password2.setObjectName(u"password2")
        self.password2.setGeometry(QRect(20, 90, 201, 25))
        self.password2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(150, 76, 228);\n"
"border:1px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(208, 208, 208);\n"
"padding-left:3px;\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(141, 72, 215);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;}\n"
"\n"
"QLineEdit:focus{\n"
"background-color: rgb(134, 69, 208);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(230, 187, 255);}")
        self.password2.setEchoMode(QLineEdit.Password)
        self.password2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.senhaIncorreta_3 = QLabel(self.singup)
        self.senhaIncorreta_3.setObjectName(u"senhaIncorreta_3")
        self.senhaIncorreta_3.setGeometry(QRect(142, 115, 81, 10))
        self.senhaIncorreta_3.setFont(font2)
        self.senhaIncorreta_3.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.singup)


        self.verticalLayout.addWidget(self.container_login)

        self.stackedWidget_4.addWidget(self.page_login)
        self.page_central = QWidget()
        self.page_central.setObjectName(u"page_central")
        self.page_central.setStyleSheet(u"QToolTip{\n"
"	background-color: rgb(170, 85, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border-left: 3px solid rgb(255, 255, 255);\n"
"	pedding-left: 8px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.page_central)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.centro = QFrame(self.page_central)
        self.centro.setObjectName(u"centro")
        self.centro.setMinimumSize(QSize(396, 234))
        self.centro.setMaximumSize(QSize(396, 237))
        self.centro.setStyleSheet(u"")
        self.centro.setFrameShape(QFrame.StyledPanel)
        self.centro.setFrameShadow(QFrame.Raised)
        self.Nome = QLabel(self.centro)
        self.Nome.setObjectName(u"Nome")
        self.Nome.setGeometry(QRect(20, 197, 170, 20))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semibold"])
        font4.setPointSize(17)
        font4.setBold(True)
        self.Nome.setFont(font4)
        self.Nome.setStyleSheet(u"color:#ffffff")
        self.Nome.setAlignment(Qt.AlignCenter)
        self.TrocaDeUsuario = QPushButton(self.centro)
        self.TrocaDeUsuario.setObjectName(u"TrocaDeUsuario")
        self.TrocaDeUsuario.setGeometry(QRect(249, 194, 130, 28))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Semibold"])
        font5.setPointSize(11)
        font5.setBold(False)
        self.TrocaDeUsuario.setFont(font5)
        self.TrocaDeUsuario.setStyleSheet(u"QPushButton{\n"
"color:#ffffff;\n"
"background-color: rgb(150, 76, 228);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:#ffffff;\n"
"background-color: rgb(150, 76, 228);\n"
"border-radius:5px;\n"
"}\n"
"QToolTip{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:3px;\n"
"border:3px solid rgb(255, 255, 255);\n"
"}")
        self.camera = QToolButton(self.centro)
        self.camera.setObjectName(u"camera")
        self.camera.setGeometry(QRect(330, 7, 31, 31))
        self.camera.setStyleSheet(u"QToolButton:hover{\n"
"	background-color: rgb(150, 76, 228);\n"
"	border-radius:10px;\n"
"}\n"
"QToolButton:pressed{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:10px;\n"
"}")
        self.camera.setIcon(icon1)
        self.camera.setIconSize(QSize(100, 200))
        self.data = QLabel(self.centro)
        self.data.setObjectName(u"data")
        self.data.setGeometry(QRect(16, 16, 91, 16))
        self.data.setStyleSheet(u"")
        self.criadoPor = QLabel(self.centro)
        self.criadoPor.setObjectName(u"criadoPor")
        self.criadoPor.setGeometry(QRect(16, 32, 110, 16))
        self.criadoPor.setStyleSheet(u"color:#ffffff;\n"
"")
        self.fechar_1 = QToolButton(self.centro)
        self.fechar_1.setObjectName(u"fechar_1")
        self.fechar_1.setGeometry(QRect(370, 7, 21, 21))
        self.fechar_1.setStyleSheet(u"QToolButton:hover{\n"
"	background-color: rgb(150, 76, 228);\n"
"	border-radius:10px;\n"
"}\n"
"QToolButton:pressed{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:10px;\n"
"}")
        self.fechar_1.setIcon(icon)
        self.fechar_1.setIconSize(QSize(20, 20))
        self.logoPrincipal = QLabel(self.centro)
        self.logoPrincipal.setObjectName(u"logoPrincipal")
        self.logoPrincipal.setGeometry(QRect(99, 50, 206, 131))
        self.logoPrincipal.setStyleSheet(u"")
        self.logoPrincipal.setPixmap(QPixmap(u"../img/logoCinacilaControl.png"))
        self.logoPrincipal.setAlignment(Qt.AlignCenter)
        self.logo = QLabel(self.centro)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(24, 80, 81, 81))
        font6 = QFont()
        font6.setPointSize(4)
        self.logo.setFont(font6)
        self.logo.setStyleSheet(u"border-radius:40px;\n"
"")
        self.logo.setPixmap(QPixmap(u"../img/cinacisl control2.png"))
        self.versao = QLabel(self.centro)
        self.versao.setObjectName(u"versao")
        self.versao.setGeometry(QRect(16, 2, 110, 16))
        font7 = QFont()
        font7.setPointSize(9)
        self.versao.setFont(font7)
        self.versao.setStyleSheet(u"color:#ffffff;\n"
"")

        self.verticalLayout_3.addWidget(self.centro)

        self.stackedWidget_4.addWidget(self.page_central)
        self.page_webCam = QWidget()
        self.page_webCam.setObjectName(u"page_webCam")
        self.horizontalLayout_14 = QHBoxLayout(self.page_webCam)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.WebCam = QLabel(self.page_webCam)
        self.WebCam.setObjectName(u"WebCam")
        self.WebCam.setMinimumSize(QSize(340, 240))
        self.WebCam.setMaximumSize(QSize(340, 16777215))
        self.WebCam.setStyleSheet(u"\n"
"border-radius:25px;")
        self.WebCam.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.WebCam)

        self.frame = QFrame(self.page_webCam)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.faceid_login_2 = QPushButton(self.frame)
        self.faceid_login_2.setObjectName(u"faceid_login_2")
        self.faceid_login_2.setGeometry(QRect(2, 190, 51, 31))
        self.faceid_login_2.setFont(font3)
        self.faceid_login_2.setStyleSheet(u"QPushButton{\n"
"color:#ffffff;\n"
"background-color: rgb(150, 76, 228);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:#ffffff;\n"
"background-color: rgb(150, 76, 228);\n"
"border-radius:5px;\n"
"}\n"
"QToolTip{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:3px;\n"
"border:3px solid rgb(255, 255, 255);\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 36, 41))
        font8 = QFont()
        font8.setPointSize(25)
        self.label_2.setFont(font8)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.fechar_2 = QToolButton(self.frame)
        self.fechar_2.setObjectName(u"fechar_2")
        self.fechar_2.setGeometry(QRect(30, 7, 21, 21))
        self.fechar_2.setStyleSheet(u"QToolButton:hover{\n"
"	background-color: rgb(170, 0, 255);\n"
"	border-radius:10px;\n"
"}\n"
"QToolButton:pressed{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:10px;\n"
"}")
        self.fechar_2.setIcon(icon)
        self.fechar_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.frame)

        self.stackedWidget_4.addWidget(self.page_webCam)

        self.horizontalLayout_13.addWidget(self.stackedWidget_4)


        self.horizontalLayout_12.addWidget(self.linhaBranca_9)


        self.verticalLayout_2.addWidget(self.frame_SC)

        self.frame_log = QFrame(self.CentralFrame)
        self.frame_log.setObjectName(u"frame_log")
        self.frame_log.setMinimumSize(QSize(350, 0))
        self.frame_log.setMaximumSize(QSize(350, 300))
        self.frame_log.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.frame_log.setFrameShape(QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_log)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 1)
        self.linhaBranca_7 = QFrame(self.frame_log)
        self.linhaBranca_7.setObjectName(u"linhaBranca_7")
        self.linhaBranca_7.setMinimumSize(QSize(348, 0))
        self.linhaBranca_7.setMaximumSize(QSize(348, 228))
        self.linhaBranca_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.linhaBranca_7.setFrameShape(QFrame.StyledPanel)
        self.linhaBranca_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.linhaBranca_7)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 1)
        self.linhaBranca_8 = QFrame(self.linhaBranca_7)
        self.linhaBranca_8.setObjectName(u"linhaBranca_8")
        self.linhaBranca_8.setMinimumSize(QSize(346, 0))
        self.linhaBranca_8.setMaximumSize(QSize(346, 227))
        self.linhaBranca_8.setStyleSheet(u"background-color: rgb(160, 80, 240);\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.linhaBranca_8.setFrameShape(QFrame.StyledPanel)
        self.linhaBranca_8.setFrameShadow(QFrame.Raised)
        self.troca = QPushButton(self.linhaBranca_8)
        self.troca.setObjectName(u"troca")
        self.troca.setGeometry(QRect(16, 58, 104, 29))
        self.troca.setFont(font3)
        self.troca.setStyleSheet(u"QPushButton{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"color:#ffffff;\n"
"background-color:rgb(132, 68, 205);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:#ffffff;\n"
"background-color: rgb(141, 72, 215);\n"
"border-radius:5px;\n"
"}\n"
"QToolTip{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:3px;\n"
"border:3px solid rgb(255, 255, 255);\n"
"}")
        self.desbloquear = QLabel(self.linhaBranca_8)
        self.desbloquear.setObjectName(u"desbloquear")
        self.desbloquear.setGeometry(QRect(17, 30, 110, 16))
        self.desbloquear.setStyleSheet(u"color: rgb(230, 187, 255);\n"
"")
        self.desbloquear.setAlignment(Qt.AlignCenter)
        self.NameEmp = QLabel(self.linhaBranca_8)
        self.NameEmp.setObjectName(u"NameEmp")
        self.NameEmp.setGeometry(QRect(18, 10, 151, 20))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Semibold"])
        font9.setPointSize(13)
        font9.setBold(False)
        self.NameEmp.setFont(font9)
        self.NameEmp.setStyleSheet(u"color: rgb(230, 187, 255);\n"
"")
        self.NameEmp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.senha = QLineEdit(self.linhaBranca_8)
        self.senha.setObjectName(u"senha")
        self.senha.setGeometry(QRect(210, 25, 130, 25))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(False)
        self.senha.setFont(font10)
        self.senha.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(150, 76, 228);\n"
"border:1px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(208, 208, 208)\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(141, 72, 215);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;}\n"
"\n"
"QLineEdit:focus{\n"
"background-color: rgb(134, 69, 208);\n"
"border:2px solid rgb(230, 187, 255);\n"
"border-radius:5px;\n"
"color: rgb(230, 187, 255);}")
        self.senha.setEchoMode(QLineEdit.Password)
        self.senha.setAlignment(Qt.AlignCenter)
        self.logoCamera = QLabel(self.linhaBranca_8)
        self.logoCamera.setObjectName(u"logoCamera")
        self.logoCamera.setGeometry(QRect(160, 5, 81, 91))
        self.logoCamera.setPixmap(QPixmap(u"../img/Instagram_90px.png"))
        self.senhaIncorreta = QLabel(self.linhaBranca_8)
        self.senhaIncorreta.setObjectName(u"senhaIncorreta")
        self.senhaIncorreta.setGeometry(QRect(260, 50, 81, 10))
        self.senhaIncorreta.setFont(font2)
        self.senhaIncorreta.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.troca.raise_()
        self.desbloquear.raise_()
        self.NameEmp.raise_()
        self.logoCamera.raise_()
        self.senha.raise_()
        self.senhaIncorreta.raise_()

        self.horizontalLayout_11.addWidget(self.linhaBranca_8)


        self.horizontalLayout_10.addWidget(self.linhaBranca_7)


        self.verticalLayout_2.addWidget(self.frame_log, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.CentralFrame, 0, Qt.AlignVCenter)

        SplashCreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashCreen)

        self.stackedWidget_4.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SplashCreen)
    # setupUi

    def retranslateUi(self, SplashCreen):
        SplashCreen.setWindowTitle(QCoreApplication.translate("SplashCreen", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.fechar_3.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><span style=\" color:#ffffff;\">Fechar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fechar_3.setText(QCoreApplication.translate("SplashCreen", u"...", None))
        self.criadoPor_3.setText(QCoreApplication.translate("SplashCreen", u"Criado por: NdDaniel", None))
#if QT_CONFIG(whatsthis)
        self.data_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.data_3.setText(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><span style=\" color:#dcbbff;\">data:  </span><span style=\" color:#c297ff;\"/><span style=\" color:#ffffff;\">28/06/2022</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.camera_2.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><span style=\" color:#ffffff;\">WebCamOFF</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.camera_2.setText(QCoreApplication.translate("SplashCreen", u"...", None))
        self.email_login.setPlaceholderText(QCoreApplication.translate("SplashCreen", u"Email", None))
#if QT_CONFIG(tooltip)
        self.sengup.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sengup.setText(QCoreApplication.translate("SplashCreen", u"Sing up", None))
#if QT_CONFIG(tooltip)
        self.login_btn.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.login_btn.setText(QCoreApplication.translate("SplashCreen", u"Login", None))
        self.password.setPlaceholderText(QCoreApplication.translate("SplashCreen", u"Password", None))
        self.senhaIncorreta_2.setText(QCoreApplication.translate("SplashCreen", u"senha incorreta", None))
        self.logoPrincipal_2.setText("")
#if QT_CONFIG(tooltip)
        self.faceid_login.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p>Alterar a froma de login</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.faceid_login.setText(QCoreApplication.translate("SplashCreen", u"Face id", None))
#if QT_CONFIG(tooltip)
        self.login_btn_singup.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.login_btn_singup.setText(QCoreApplication.translate("SplashCreen", u"Login", None))
        self.email_singup.setPlaceholderText(QCoreApplication.translate("SplashCreen", u"Email", None))
#if QT_CONFIG(tooltip)
        self.singup_singup.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.singup_singup.setText(QCoreApplication.translate("SplashCreen", u"Sing up", None))
        self.password1.setPlaceholderText(QCoreApplication.translate("SplashCreen", u"Password", None))
        self.password2.setPlaceholderText(QCoreApplication.translate("SplashCreen", u"Repeat-password", None))
        self.senhaIncorreta_3.setText(QCoreApplication.translate("SplashCreen", u"senha incorreta", None))
        self.Nome.setText(QCoreApplication.translate("SplashCreen", u"Finacial Control", None))
#if QT_CONFIG(tooltip)
        self.TrocaDeUsuario.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p>Deslogar da conta atual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TrocaDeUsuario.setText(QCoreApplication.translate("SplashCreen", u"Troca de Usuario", None))
#if QT_CONFIG(tooltip)
        self.camera.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><span style=\" color:#ffffff;\">WebCamOFF</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.camera.setText(QCoreApplication.translate("SplashCreen", u"...", None))
#if QT_CONFIG(whatsthis)
        self.data.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.data.setText(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><span style=\" color:#dcbbff;\">data:  </span><span style=\" color:#c297ff;\"/><span style=\" color:#ffffff;\">28/06/2022</span></p></body></html>", None))
        self.criadoPor.setText(QCoreApplication.translate("SplashCreen", u"Criado por: NdDaniel", None))
#if QT_CONFIG(tooltip)
        self.fechar_1.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><span style=\" color:#ffffff;\">Fechar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fechar_1.setText(QCoreApplication.translate("SplashCreen", u"...", None))
        self.logoPrincipal.setText("")
        self.logo.setText("")
        self.versao.setText(QCoreApplication.translate("SplashCreen", u"Vers\u00e3o: 0.1.2", None))
        self.WebCam.setText("")
#if QT_CONFIG(tooltip)
        self.faceid_login_2.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p>Alterar a froma de login</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.faceid_login_2.setText(QCoreApplication.translate("SplashCreen", u"Face id", None))
        self.label_2.setText(QCoreApplication.translate("SplashCreen", u"0", None))
#if QT_CONFIG(tooltip)
        self.fechar_2.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p><span style=\" color:#ffffff;\">Fechar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fechar_2.setText(QCoreApplication.translate("SplashCreen", u"...", None))
#if QT_CONFIG(tooltip)
        self.troca.setToolTip(QCoreApplication.translate("SplashCreen", u"<html><head/><body><p>Alterar a froma de login</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.troca.setText(QCoreApplication.translate("SplashCreen", u"Usar Face id", None))
        self.desbloquear.setText(QCoreApplication.translate("SplashCreen", u"Desbloquear sua app", None))
        self.NameEmp.setText(QCoreApplication.translate("SplashCreen", u"Nd Daniel", None))
        self.senha.setPlaceholderText(QCoreApplication.translate("SplashCreen", u"Digite a sua senha", None))
        self.logoCamera.setText("")
        self.senhaIncorreta.setText(QCoreApplication.translate("SplashCreen", u"senha incorreta", None))
    # retranslateUi

