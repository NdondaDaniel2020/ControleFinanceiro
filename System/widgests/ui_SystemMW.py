# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SystemMWSUIhUT.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindowMW(object):
    def setupUi(self, MainWindowMW):
        if not MainWindowMW.objectName():
            MainWindowMW.setObjectName(u"MainWindowMW")
        MainWindowMW.resize(1138, 703)
        self.centralwidget_styleSheet = QWidget(MainWindowMW)
        self.centralwidget_styleSheet.setObjectName(u"centralwidget_styleSheet")
        self.centralwidget_styleSheet.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background:rgb(170, 50, 255);\n"
"    height: 5px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(170, 50, 255);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(170, 50, 255);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
""
                        "{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(170, 50, 255);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(170, 50, 255);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(170, 50, 255);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical"
                        ", QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	border-radius:0px\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color:rgb(165, 83, 248);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(170, 97, 253);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(170, 85, 255);\n"
"	width: 23px;\n"
"	height: 23px;\n"
"	border-radius: 9px;\n"
"    background: rgb(44, 49, 60)"
                        ";\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid rgb(58, 66, 81);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(159, 80, 239);\n"
"	border: 3px solid rgb(58, 66, 81);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"border-radius: 9px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget_styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.primeiro_container = QFrame(self.centralwidget_styleSheet)
        self.primeiro_container.setObjectName(u"primeiro_container")
        self.primeiro_container.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:15px;")
        self.primeiro_container.setFrameShape(QFrame.StyledPanel)
        self.primeiro_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.primeiro_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.linha = QFrame(self.primeiro_container)
        self.linha.setObjectName(u"linha")
        self.linha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.linha.setFrameShape(QFrame.StyledPanel)
        self.linha.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.linha)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.frame_central = QFrame(self.linha)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setStyleSheet(u"background-color: rgb(159, 80, 239);\n"
"border-radius:15px;\n"
"overflow:hidden;")
        self.frame_central.setFrameShape(QFrame.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_central)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 8)
        self.frame_centaralCentral = QFrame(self.frame_central)
        self.frame_centaralCentral.setObjectName(u"frame_centaralCentral")
        self.frame_centaralCentral.setStyleSheet(u"background-color: rgb(159, 80, 239);")
        self.frame_centaralCentral.setFrameShape(QFrame.StyledPanel)
        self.frame_centaralCentral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_centaralCentral)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(self.frame_centaralCentral)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setStyleSheet(u"background-color: rgb(159, 80, 239);\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.central_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.central_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.barraTitulo = QFrame(self.frame_2)
        self.barraTitulo.setObjectName(u"barraTitulo")
        self.barraTitulo.setMinimumSize(QSize(0, 38))
        self.barraTitulo.setMaximumSize(QSize(16777215, 38))
        self.barraTitulo.setStyleSheet(u"QFrame{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:13px;\n"
"}")
        self.barraTitulo.setFrameShape(QFrame.StyledPanel)
        self.barraTitulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.barraTitulo)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.barraTitulo)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font1 = QFont()
        font1.setPointSize(2)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"border-color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;")
        icon = QIcon()
        icon.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/logoFC.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.NameEmp = QLabel(self.barraTitulo)
        self.NameEmp.setObjectName(u"NameEmp")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.NameEmp.setFont(font2)
        self.NameEmp.setStyleSheet(u"color: rgb(230, 187, 255);\n"
"padding-bottom:2px;\n"
"")
        self.NameEmp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.NameEmp)

        self.horizontalSpacer_3 = QSpacerItem(38, 37, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.frame_btn_zone_3 = QFrame(self.barraTitulo)
        self.frame_btn_zone_3.setObjectName(u"frame_btn_zone_3")
        self.frame_btn_zone_3.setMinimumSize(QSize(120, 0))
        self.frame_btn_zone_3.setMaximumSize(QSize(120, 16777215))
        self.frame_btn_zone_3.setStyleSheet(u"\n"
"QToolButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"QToolButton:hover{\n"
"	background-color: rgb(153, 71, 234);\n"
"	border-radius:3px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:3px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_btn_zone_3.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_zone_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_btn_zone_3)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.minimisar = QToolButton(self.frame_btn_zone_3)
        self.minimisar.setObjectName(u"minimisar")
        icon1 = QIcon()
        icon1.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimisar.setIcon(icon1)
        self.minimisar.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.minimisar)

        self.NormalMax = QToolButton(self.frame_btn_zone_3)
        self.NormalMax.setObjectName(u"NormalMax")
        self.NormalMax.setMinimumSize(QSize(0, 0))
        icon2 = QIcon()
        icon2.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NormalMax.setIcon(icon2)
        self.NormalMax.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.NormalMax)

        self.fechar = QToolButton(self.frame_btn_zone_3)
        self.fechar.setObjectName(u"fechar")
        icon3 = QIcon()
        icon3.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fechar.setIcon(icon3)
        self.fechar.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.fechar)


        self.horizontalLayout_9.addWidget(self.frame_btn_zone_3)


        self.verticalLayout_8.addWidget(self.barraTitulo)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame = QFrame(self.central_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 5, 0, 0)
        self.xone_btn_left = QFrame(self.frame)
        self.xone_btn_left.setObjectName(u"xone_btn_left")
        self.xone_btn_left.setMinimumSize(QSize(45, 0))
        self.xone_btn_left.setMaximumSize(QSize(45, 16777215))
        self.xone_btn_left.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:17px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left:6px;\n"
"    text-align: left;	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 83, 248);\n"
"	border-radius:17px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left:6px;\n"
"    text-align: left;	\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:17px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left:6px;\n"
"    text-align: left;	\n"
"}")
        self.xone_btn_left.setFrameShape(QFrame.StyledPanel)
        self.xone_btn_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.xone_btn_left)
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 5, 0)
        self.Home = QPushButton(self.xone_btn_left)
        self.Home.setObjectName(u"Home")
        self.Home.setMinimumSize(QSize(0, 35))
        self.Home.setMaximumSize(QSize(35, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home.setIcon(icon4)
        self.Home.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.Home, 0, Qt.AlignRight)

        self.web_btn_2 = QPushButton(self.xone_btn_left)
        self.web_btn_2.setObjectName(u"web_btn_2")
        self.web_btn_2.setMinimumSize(QSize(0, 35))
        self.web_btn_2.setMaximumSize(QSize(35, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/web_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.web_btn_2.setIcon(icon5)
        self.web_btn_2.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.web_btn_2)

        self.conntrole_finace = QPushButton(self.xone_btn_left)
        self.conntrole_finace.setObjectName(u"conntrole_finace")
        self.conntrole_finace.setMinimumSize(QSize(0, 35))
        self.conntrole_finace.setMaximumSize(QSize(35, 35))
        icon6 = QIcon()
        icon6.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/money_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conntrole_finace.setIcon(icon6)
        self.conntrole_finace.setIconSize(QSize(27, 27))

        self.verticalLayout_9.addWidget(self.conntrole_finace)

        self.settings = QPushButton(self.xone_btn_left)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 35))
        self.settings.setMaximumSize(QSize(35, 16777215))
        icon7 = QIcon()
        icon7.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon7)
        self.settings.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.settings, 0, Qt.AlignRight)

        self.double_up = QPushButton(self.xone_btn_left)
        self.double_up.setObjectName(u"double_up")
        self.double_up.setMinimumSize(QSize(0, 35))
        self.double_up.setMaximumSize(QSize(35, 35))
        icon8 = QIcon()
        icon8.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-chevron-double-up-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.double_up.setIcon(icon8)
        self.double_up.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.double_up, 0, Qt.AlignRight)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.xone_btn_left)

        self.left_menu = QFrame(self.frame)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(8, 0))
        self.left_menu.setMaximumSize(QSize(0, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.QRcode = QLabel(self.left_menu)
        self.QRcode.setObjectName(u"QRcode")
        self.QRcode.setGeometry(QRect(40, 10, 111, 121))
        self.QRcode.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/qr_code_120px.png"))
        self.data = QLabel(self.left_menu)
        self.data.setObjectName(u"data")
        self.data.setGeometry(QRect(40, 130, 91, 16))
        self.data.setStyleSheet(u"")
        self.criadoPor = QLabel(self.left_menu)
        self.criadoPor.setObjectName(u"criadoPor")
        self.criadoPor.setGeometry(QRect(40, 150, 110, 16))
        self.criadoPor.setStyleSheet(u"color:#ffffff;\n"
"")
        self.frame_zone_btn = QFrame(self.left_menu)
        self.frame_zone_btn.setObjectName(u"frame_zone_btn")
        self.frame_zone_btn.setGeometry(QRect(10, 170, 180, 300))
        self.frame_zone_btn.setMinimumSize(QSize(180, 300))
        self.frame_zone_btn.setMaximumSize(QSize(180, 300))
        self.frame_zone_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    text-align: left;\n"
"	padding-left: 18px;\n"
"	border-radius:4px;\n"
"}\n"
"QFrame{\n"
"	background-color: rgb(159, 80, 239);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	border-ra\n"
"    text-align: left;\n"
"	padding-left: 18px;\n"
"	border-radius:4px;\n"
"	background-color: rgb(170, 85, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: rgb(255, 255, 255);\n"
"    text-align: left;\n"
"	padding-left: 18px;\n"
"	border-radius:4px;\n"
"	background-color: rgb(159, 80, 239);\n"
"}")
        self.frame_zone_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_zone_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_zone_btn)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.help_btn = QPushButton(self.frame_zone_btn)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setMinimumSize(QSize(0, 34))
        self.help_btn.setMaximumSize(QSize(16777215, 34))
        icon9 = QIcon()
        icon9.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/help_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btn.setIcon(icon9)
        self.help_btn.setIconSize(QSize(18, 18))
        self.help_btn.setCheckable(False)

        self.verticalLayout_10.addWidget(self.help_btn)

        self.perfil_btn = QPushButton(self.frame_zone_btn)
        self.perfil_btn.setObjectName(u"perfil_btn")
        self.perfil_btn.setMinimumSize(QSize(0, 34))
        self.perfil_btn.setMaximumSize(QSize(16777215, 34))
        icon10 = QIcon()
        icon10.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfil_btn.setIcon(icon10)
        self.perfil_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.perfil_btn)

        self.web_btn = QPushButton(self.frame_zone_btn)
        self.web_btn.setObjectName(u"web_btn")
        self.web_btn.setMinimumSize(QSize(0, 34))
        self.web_btn.setMaximumSize(QSize(16777215, 34))
        icon11 = QIcon()
        icon11.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/website_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.web_btn.setIcon(icon11)
        self.web_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.web_btn)

        self.setting_btn = QPushButton(self.frame_zone_btn)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setMinimumSize(QSize(0, 34))
        self.setting_btn.setMaximumSize(QSize(16777215, 34))
        icon12 = QIcon()
        icon12.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/settings_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon12)
        self.setting_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.setting_btn)

        self.coins_btn = QPushButton(self.frame_zone_btn)
        self.coins_btn.setObjectName(u"coins_btn")
        self.coins_btn.setMinimumSize(QSize(0, 34))
        self.coins_btn.setMaximumSize(QSize(16777215, 34))
        self.coins_btn.setIcon(icon6)
        self.coins_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_10.addWidget(self.coins_btn)

        self.setting_user_btn = QPushButton(self.frame_zone_btn)
        self.setting_user_btn.setObjectName(u"setting_user_btn")
        self.setting_user_btn.setMinimumSize(QSize(0, 34))
        self.setting_user_btn.setMaximumSize(QSize(16777215, 34))
        icon13 = QIcon()
        icon13.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/admin_settings_male_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_user_btn.setIcon(icon13)
        self.setting_user_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.setting_user_btn)

        self.editTest = QPushButton(self.frame_zone_btn)
        self.editTest.setObjectName(u"editTest")
        self.editTest.setMinimumSize(QSize(0, 34))
        self.editTest.setMaximumSize(QSize(16777215, 34))
        icon14 = QIcon()
        icon14.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/edit_folder_24px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editTest.setIcon(icon14)
        self.editTest.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.editTest)

        self.editTestFrame = QFrame(self.frame_zone_btn)
        self.editTestFrame.setObjectName(u"editTestFrame")
        self.editTestFrame.setMinimumSize(QSize(0, 0))
        self.editTestFrame.setMaximumSize(QSize(16777215, 0))
        self.editTestFrame.setFrameShape(QFrame.StyledPanel)
        self.editTestFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.editTestFrame)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(11, 0, 8, 0)
        self.horizontalSlider = QSlider(self.editTestFrame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.horizontalSlider)

        self.toolButton = QToolButton(self.editTestFrame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(20, 20))
        self.toolButton.setMaximumSize(QSize(20, 20))
        icon15 = QIcon()
        icon15.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-volume-off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon15)

        self.horizontalLayout_10.addWidget(self.toolButton)


        self.verticalLayout_10.addWidget(self.editTestFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(159, 80, 239);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.page_Home = QWidget()
        self.page_Home.setObjectName(u"page_Home")
        self.verticalLayout_12 = QVBoxLayout(self.page_Home)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.logo_principal_Contaner = QFrame(self.page_Home)
        self.logo_principal_Contaner.setObjectName(u"logo_principal_Contaner")
        self.logo_principal_Contaner.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-top-right-radius:0px;\n"
"")
        self.logo_principal_Contaner.setFrameShape(QFrame.StyledPanel)
        self.logo_principal_Contaner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.logo_principal_Contaner)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(4, 4, 4, 4)
        self.logo_principal_2 = QLabel(self.logo_principal_Contaner)
        self.logo_principal_2.setObjectName(u"logo_principal_2")
        font3 = QFont()
        font3.setFamilies([u"Bauhaus 93"])
        font3.setPointSize(64)
        self.logo_principal_2.setFont(font3)
        self.logo_principal_2.setStyleSheet(u"color: rgb(219, 218, 218);\n"
"padding-bottom:0px;\n"
"\n"
"")
        self.logo_principal_2.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/SystemMW.png"))
        self.logo_principal_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.logo_principal_2)


        self.verticalLayout_12.addWidget(self.logo_principal_Contaner)

        self.stackedWidget.addWidget(self.page_Home)
        self.page_Extras = QWidget()
        self.page_Extras.setObjectName(u"page_Extras")
        self.verticalLayout_38 = QVBoxLayout(self.page_Extras)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_182 = QFrame(self.page_Extras)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-top-right-radius: 0px;")
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_182)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, 4, 0, 4)
        self.webEngineView_2 = QWebEngineView(self.frame_182)
        self.webEngineView_2.setObjectName(u"webEngineView_2")
        self.webEngineView_2.setUrl(QUrl(u"file:///C:/Users/Fam\u00edlia Matondo/PycharmProjects/pythonProject1/System/html/sc.html"))

        self.horizontalLayout_4.addWidget(self.webEngineView_2)


        self.verticalLayout_38.addWidget(self.frame_182)

        self.stackedWidget.addWidget(self.page_Extras)
        self.page_web = QWidget()
        self.page_web.setObjectName(u"page_web")
        self.verticalLayout_16 = QVBoxLayout(self.page_web)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_web)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 49))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 5)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 46))
        self.frame_9.setMaximumSize(QSize(16777215, 46))
        self.frame_9.setStyleSheet(u"QFrame{background-color: rgb(170, 85, 255);\n"
"border-radius:8px;}\n"
"\n"
"QPushButton{background-color: rgb(159, 80, 239);\n"
"border-radius:8px;}\n"
"QPushButton:hover{;\n"
"	background-color: rgb(163, 83, 248);\n"
"border-radius:8px;}\n"
"QPushButton:pressed{background-color: rgb(159, 80, 239);\n"
"border-radius:8px;}\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 8, 5)
        self.pesquisar_btn = QPushButton(self.frame_9)
        self.pesquisar_btn.setObjectName(u"pesquisar_btn")
        self.pesquisar_btn.setMinimumSize(QSize(34, 34))
        self.pesquisar_btn.setMaximumSize(QSize(34, 34))
        self.pesquisar_btn.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/search_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pesquisar_btn.setIcon(icon16)
        self.pesquisar_btn.setIconSize(QSize(23, 23))

        self.horizontalLayout_7.addWidget(self.pesquisar_btn)

        self.update = QPushButton(self.frame_9)
        self.update.setObjectName(u"update")
        self.update.setMinimumSize(QSize(34, 34))
        self.update.setMaximumSize(QSize(34, 34))
        self.update.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update.setIcon(icon17)
        self.update.setIconSize(QSize(23, 23))

        self.horizontalLayout_7.addWidget(self.update)

        self.LineUrl = QLineEdit(self.frame_9)
        self.LineUrl.setObjectName(u"LineUrl")
        self.LineUrl.setMinimumSize(QSize(0, 36))
        self.LineUrl.setMaximumSize(QSize(16777215, 36))
        font4 = QFont()
        font4.setPointSize(13)
        self.LineUrl.setFont(font4)
        self.LineUrl.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(159, 80, 239);\n"
"color: rgb(170, 85, 255);\n"
"border-radius:10px;\n"
"color: rgb(223, 223, 223);\n"
"padding-left:10px}\n"
"\n"
"QLineEdit:hover{\n"
"background-color: rgb(150, 76, 229);\n"
"color: rgb(170, 85, 255);\n"
"border-radius:10px;\n"
"color:rgb(223, 223, 223);}\n"
"\n"
"QLineEdit:focus{\n"
"background-color: rgb(143, 73, 218);\n"
"border-radius:10px;\n"
"color:rgb(223, 223, 223);}\n"
"")
        self.LineUrl.setFrame(True)
        self.LineUrl.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.LineUrl)

        self.voz_btn = QPushButton(self.frame_9)
        self.voz_btn.setObjectName(u"voz_btn")
        self.voz_btn.setMinimumSize(QSize(34, 34))
        self.voz_btn.setMaximumSize(QSize(34, 34))
        self.voz_btn.setStyleSheet(u"")
        icon18 = QIcon()
        icon18.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/microphone_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.voz_btn.setIcon(icon18)
        self.voz_btn.setIconSize(QSize(23, 23))

        self.horizontalLayout_7.addWidget(self.voz_btn)

        self.arrow_left = QPushButton(self.frame_9)
        self.arrow_left.setObjectName(u"arrow_left")
        self.arrow_left.setMinimumSize(QSize(34, 34))
        self.arrow_left.setMaximumSize(QSize(34, 34))
        self.arrow_left.setStyleSheet(u"")
        icon19 = QIcon()
        icon19.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrow_left.setIcon(icon19)
        self.arrow_left.setIconSize(QSize(22, 22))

        self.horizontalLayout_7.addWidget(self.arrow_left)

        self.arrow_right = QPushButton(self.frame_9)
        self.arrow_right.setObjectName(u"arrow_right")
        self.arrow_right.setMinimumSize(QSize(34, 34))
        self.arrow_right.setMaximumSize(QSize(34, 34))
        self.arrow_right.setStyleSheet(u"")
        icon20 = QIcon()
        icon20.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrow_right.setIcon(icon20)
        self.arrow_right.setIconSize(QSize(22, 22))

        self.horizontalLayout_7.addWidget(self.arrow_right)


        self.horizontalLayout_8.addWidget(self.frame_9, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_8)

        self.frame_16 = QFrame(self.page_web)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-top-right-radius:0px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_16)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(4, 4, 0, 4)
        self.webEngineView = QWebEngineView(self.frame_16)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"file:///C:/Users/Fam\u00edlia Matondo/PycharmProjects/pythonProject1/System/html/ss.html"))

        self.verticalLayout_39.addWidget(self.webEngineView)


        self.verticalLayout_16.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.page_web)
        self.page_edit = QWidget()
        self.page_edit.setObjectName(u"page_edit")
        self.verticalLayout_17 = QVBoxLayout(self.page_edit)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.page_edit)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_99 = QFrame(self.frame_25)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setStyleSheet(u"background-color: rgb(158, 80, 238);\n"
"border-radius:15px;")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_99)
        self.verticalLayout_32.setSpacing(3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(2, 0, 0, 0)
        self.frame_102 = QFrame(self.frame_99)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_102)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(2, 2, 2, 2)
        self.plainTextEdit = QPlainTextEdit(self.frame_102)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font5 = QFont()
        font5.setPointSize(15)
        self.plainTextEdit.setFont(font5)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"background-color: rgb(159, 80, 239);\n"
"color: rgb(255, 255, 255);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right:0px;\n"
"border-bottom-right:0px;\n"
"}\n"
"QPlainTextEdit:hover{\n"
"background-color: rgb(159, 80, 239);\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(190, 190, 190);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right:0px;\n"
"border-bottom-right:0px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"background-color: rgb(159, 80, 239);\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(220, 220, 220);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right:0px;\n"
"border-bottom-right:0px;\n"
"}\n"
"")

        self.verticalLayout_33.addWidget(self.plainTextEdit)


        self.verticalLayout_32.addWidget(self.frame_102)

        self.frame_98 = QFrame(self.frame_99)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(0, 43))
        self.frame_98.setMaximumSize(QSize(16777215, 40))
        self.frame_98.setStyleSheet(u"QFrame{background-color: rgb(170, 85, 255);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(159, 80, 239);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{;\n"
"background-color: rgb(162, 99, 239);\n"
"border-radius:10px;\n"
"border: 2px solid rgb(244, 244, 244);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{background-color: rgb(159, 80, 239);\n"
"border-radius:10px;\n"
"border: 1px solid rgb(244, 244, 244);\n"
"padding-top: 1px;\n"
"padding-left: 1px;}\n"
"")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 15, 0)
        self.horizontalSpacer_40 = QSpacerItem(480, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_40)

        self.open = QPushButton(self.frame_98)
        self.open.setObjectName(u"open")
        self.open.setMinimumSize(QSize(75, 30))
        font6 = QFont()
        font6.setPointSize(11)
        self.open.setFont(font6)

        self.horizontalLayout_34.addWidget(self.open)

        self.save = QPushButton(self.frame_98)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(75, 30))
        self.save.setMaximumSize(QSize(75, 30))
        self.save.setFont(font6)

        self.horizontalLayout_34.addWidget(self.save)


        self.verticalLayout_32.addWidget(self.frame_98)


        self.horizontalLayout_31.addWidget(self.frame_99)


        self.verticalLayout_17.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.page_edit)
        self.page_perfil = QWidget()
        self.page_perfil.setObjectName(u"page_perfil")
        self.verticalLayout_30 = QVBoxLayout(self.page_perfil)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.page_perfil)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(400, 0))
        self.frame_101.setStyleSheet(u";\n"
"background-color: rgb(170, 85, 255);")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.verticalLayout_252 = QVBoxLayout(self.frame_101)
        self.verticalLayout_252.setObjectName(u"verticalLayout_252")
        self.verticalLayout_252.setContentsMargins(-1, 0, 0, -1)
        self.frame_363 = QFrame(self.frame_101)
        self.frame_363.setObjectName(u"frame_363")
        self.frame_363.setMinimumSize(QSize(0, 184))
        self.frame_363.setMaximumSize(QSize(16777215, 185))
        self.frame_363.setFrameShape(QFrame.StyledPanel)
        self.frame_363.setFrameShadow(QFrame.Raised)
        self.verticalLayout_251 = QVBoxLayout(self.frame_363)
        self.verticalLayout_251.setSpacing(10)
        self.verticalLayout_251.setObjectName(u"verticalLayout_251")
        self.verticalLayout_251.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.frame_363)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMinimumSize(QSize(0, 0))
        self.scrollArea_6.setMaximumSize(QSize(16777215, 172))
        self.scrollArea_6.setStyleSheet(u"")
        self.scrollArea_6.setFrameShadow(QFrame.Sunken)
        self.scrollArea_6.setLineWidth(1)
        self.scrollArea_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1550, 159))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:15px;\n"
"")
        self.horizontalLayout_108 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_108.setSpacing(8)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(5, 0, 5, 9)
        self.frame_Browsin_history = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_Browsin_history.setObjectName(u"frame_Browsin_history")
        self.frame_Browsin_history.setMinimumSize(QSize(250, 125))
        self.frame_Browsin_history.setMaximumSize(QSize(250, 150))
        self.frame_Browsin_history.setStyleSheet(u"background-color: rgb(255, 255, 255)\n"
"")
        self.frame_Browsin_history.setFrameShape(QFrame.StyledPanel)
        self.frame_Browsin_history.setFrameShadow(QFrame.Raised)
        self.frame_Browsin_history_lbl = QLabel(self.frame_Browsin_history)
        self.frame_Browsin_history_lbl.setObjectName(u"frame_Browsin_history_lbl")
        self.frame_Browsin_history_lbl.setGeometry(QRect(16, 100, 171, 30))
        font7 = QFont()
        font7.setPointSize(17)
        self.frame_Browsin_history_lbl.setFont(font7)
        self.frame_Browsin_history_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_Browsin_history_btn = QPushButton(self.frame_Browsin_history)
        self.frame_Browsin_history_btn.setObjectName(u"frame_Browsin_history_btn")
        self.frame_Browsin_history_btn.setGeometry(QRect(13, 13, 90, 71))
        icon21 = QIcon()
        icon21.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/web_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_Browsin_history_btn.setIcon(icon21)
        self.frame_Browsin_history_btn.setIconSize(QSize(100, 100))

        self.horizontalLayout_108.addWidget(self.frame_Browsin_history)

        self.frame_opening_history = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_opening_history.setObjectName(u"frame_opening_history")
        self.frame_opening_history.setMinimumSize(QSize(250, 150))
        self.frame_opening_history.setMaximumSize(QSize(250, 150))
        self.frame_opening_history.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.frame_opening_history.setFrameShape(QFrame.StyledPanel)
        self.frame_opening_history.setFrameShadow(QFrame.Raised)
        self.frame_opening_history_btn = QPushButton(self.frame_opening_history)
        self.frame_opening_history_btn.setObjectName(u"frame_opening_history_btn")
        self.frame_opening_history_btn.setGeometry(QRect(13, 13, 90, 71))
        icon22 = QIcon()
        icon22.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/close_pane_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_opening_history_btn.setIcon(icon22)
        self.frame_opening_history_btn.setIconSize(QSize(100, 100))
        self.frame_opening_history_lbl = QLabel(self.frame_opening_history)
        self.frame_opening_history_lbl.setObjectName(u"frame_opening_history_lbl")
        self.frame_opening_history_lbl.setGeometry(QRect(16, 100, 171, 30))
        font8 = QFont()
        font8.setPointSize(12)
        self.frame_opening_history_lbl.setFont(font8)
        self.frame_opening_history_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_108.addWidget(self.frame_opening_history)

        self.frame_user_list = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_user_list.setObjectName(u"frame_user_list")
        self.frame_user_list.setMinimumSize(QSize(250, 150))
        self.frame_user_list.setMaximumSize(QSize(250, 150))
        self.frame_user_list.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_user_list.setFrameShape(QFrame.StyledPanel)
        self.frame_user_list.setFrameShadow(QFrame.Raised)
        self.frame_user_list_btn = QPushButton(self.frame_user_list)
        self.frame_user_list_btn.setObjectName(u"frame_user_list_btn")
        self.frame_user_list_btn.setGeometry(QRect(10, 17, 91, 71))
        icon23 = QIcon()
        icon23.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/user_menu_female_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_user_list_btn.setIcon(icon23)
        self.frame_user_list_btn.setIconSize(QSize(115, 115))
        self.frame_user_list_lbl = QLabel(self.frame_user_list)
        self.frame_user_list_lbl.setObjectName(u"frame_user_list_lbl")
        self.frame_user_list_lbl.setGeometry(QRect(16, 100, 100, 30))
        self.frame_user_list_lbl.setFont(font8)
        self.frame_user_list_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_108.addWidget(self.frame_user_list)

        self.frame_password_faceId = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_password_faceId.setObjectName(u"frame_password_faceId")
        self.frame_password_faceId.setMinimumSize(QSize(250, 150))
        self.frame_password_faceId.setMaximumSize(QSize(250, 150))
        self.frame_password_faceId.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame_password_faceId.setFrameShape(QFrame.StyledPanel)
        self.frame_password_faceId.setFrameShadow(QFrame.Raised)
        self.password_faceId_btn_2 = QPushButton(self.frame_password_faceId)
        self.password_faceId_btn_2.setObjectName(u"password_faceId_btn_2")
        self.password_faceId_btn_2.setGeometry(QRect(13, 10, 90, 90))
        icon24 = QIcon()
        icon24.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/instagram_logo_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.password_faceId_btn_2.setIcon(icon24)
        self.password_faceId_btn_2.setIconSize(QSize(110, 130))
        self.lineEdit_2 = QLineEdit(self.frame_password_faceId)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(59, 53, 106, 32))
        self.lineEdit_2.setFont(font5)
        self.lineEdit_2.setStyleSheet(u"border-radius:7px;\n"
"color:rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px solid rgb(170, 85, 255)")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.password_faceId_lbl_6 = QLabel(self.frame_password_faceId)
        self.password_faceId_lbl_6.setObjectName(u"password_faceId_lbl_6")
        self.password_faceId_lbl_6.setGeometry(QRect(18, 101, 186, 30))
        self.password_faceId_lbl_6.setFont(font8)
        self.password_faceId_lbl_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_29 = QLabel(self.frame_password_faceId)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(60, 47, 114, 37))
        self.label_29.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_108.addWidget(self.frame_password_faceId)

        self.frame_IOs_2 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_IOs_2.setObjectName(u"frame_IOs_2")
        self.frame_IOs_2.setMinimumSize(QSize(250, 150))
        self.frame_IOs_2.setMaximumSize(QSize(250, 150))
        self.frame_IOs_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.frame_IOs_2.setFrameShape(QFrame.StyledPanel)
        self.frame_IOs_2.setFrameShadow(QFrame.Raised)
        self.ios_lbl_2 = QLabel(self.frame_IOs_2)
        self.ios_lbl_2.setObjectName(u"ios_lbl_2")
        self.ios_lbl_2.setGeometry(QRect(14, 70, 70, 20))
        self.ios_lbl_2.setFont(font8)
        self.ios_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ios_btn_2 = QPushButton(self.frame_IOs_2)
        self.ios_btn_2.setObjectName(u"ios_btn_2")
        self.ios_btn_2.setGeometry(QRect(7, 7, 50, 50))
        icon25 = QIcon()
        icon25.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/mac_client_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ios_btn_2.setIcon(icon25)
        self.ios_btn_2.setIconSize(QSize(60, 60))
        self.iconWindow_4 = QLabel(self.frame_IOs_2)
        self.iconWindow_4.setObjectName(u"iconWindow_4")
        self.iconWindow_4.setGeometry(QRect(70, 110, 30, 30))
        self.iconWindow_4.setMinimumSize(QSize(20, 20))
        self.iconWindow_4.setMaximumSize(QSize(30, 30))
        self.iconWindow_4.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/ncicon.png"))
        self.iconWindow_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_108.addWidget(self.frame_IOs_2)

        self.frame_IBM_2 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_IBM_2.setObjectName(u"frame_IBM_2")
        self.frame_IBM_2.setMinimumSize(QSize(250, 150))
        self.frame_IBM_2.setMaximumSize(QSize(250, 150))
        self.frame_IBM_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.frame_IBM_2.setFrameShape(QFrame.StyledPanel)
        self.frame_IBM_2.setFrameShadow(QFrame.Raised)
        self.ibm_lbl_2 = QLabel(self.frame_IBM_2)
        self.ibm_lbl_2.setObjectName(u"ibm_lbl_2")
        self.ibm_lbl_2.setGeometry(QRect(10, 70, 80, 20))
        self.ibm_lbl_2.setFont(font8)
        self.ibm_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ibm_btn_2 = QPushButton(self.frame_IBM_2)
        self.ibm_btn_2.setObjectName(u"ibm_btn_2")
        self.ibm_btn_2.setGeometry(QRect(10, 15, 50, 30))
        icon26 = QIcon()
        icon26.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/ibm_70px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ibm_btn_2.setIcon(icon26)
        self.ibm_btn_2.setIconSize(QSize(50, 50))

        self.horizontalLayout_108.addWidget(self.frame_IBM_2)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_251.addWidget(self.scrollArea_6, 0, Qt.AlignBottom)


        self.verticalLayout_252.addWidget(self.frame_363)

        self.frame_167 = QFrame(self.frame_101)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setMinimumSize(QSize(3, 0))
        self.frame_167.setMaximumSize(QSize(123456, 16777215))
        self.frame_167.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_167)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget_2 = QStackedWidget(self.frame_167)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_66.addWidget(self.stackedWidget_2)


        self.verticalLayout_252.addWidget(self.frame_167)


        self.horizontalLayout_3.addWidget(self.frame_101)

        self.frame_173 = QFrame(self.frame_100)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setMinimumSize(QSize(3, 0))
        self.frame_173.setMaximumSize(QSize(220, 16777215))
        self.frame_173.setStyleSheet(u"QFrame{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;\n"
"}\n"
"")
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_173)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(8, 8, 8, 8)
        self.frame_174 = QFrame(self.frame_173)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setMinimumSize(QSize(3, 0))
        self.frame_174.setMaximumSize(QSize(210, 16777215))
        self.frame_174.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_174)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_175 = QFrame(self.frame_174)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setMinimumSize(QSize(0, 200))
        self.frame_175.setMaximumSize(QSize(16777215, 200))
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame_175)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 190, 184, 2))
        self.line.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_17 = QLabel(self.frame_175)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 137, 150, 30))
        font9 = QFont()
        font9.setPointSize(14)
        self.label_17.setFont(font9)
        self.label_17.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.frame_175)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 120, 110, 20))
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.frame_176 = QFrame(self.frame_175)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setGeometry(QRect(50, 10, 110, 111))
        self.frame_176.setMinimumSize(QSize(110, 110))
        self.frame_176.setMaximumSize(QSize(107, 154))
        self.frame_176.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:53px;")
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_176)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 3, 0, 0)
        self.label_7 = QLabel(self.frame_176)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 108))
        self.label_7.setMaximumSize(QSize(100, 100))
        self.label_7.setStyleSheet(u"border-radius:49px;\n"
"background-color: transparent;")
        self.label_7.setPixmap(QPixmap(u"../../../../Pictures/asd.png"))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_35.addWidget(self.frame_175)

        self.frame_177 = QFrame(self.frame_174)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_177)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.frame_178 = QFrame(self.frame_177)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setMinimumSize(QSize(0, 70))
        self.frame_178.setMaximumSize(QSize(16777215, 70))
        self.frame_178.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)

        self.verticalLayout_65.addWidget(self.frame_178)

        self.frame_179 = QFrame(self.frame_177)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setMinimumSize(QSize(0, 181))
        self.frame_179.setMaximumSize(QSize(16777215, 185))
        self.frame_179.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_179)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(5, 5, 5, 5)
        self.frame_180 = QFrame(self.frame_179)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setMinimumSize(QSize(0, 40))
        self.frame_180.setMaximumSize(QSize(16777215, 40))
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_180)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(15, 0, 10, 0)
        self.label_67 = QLabel(self.frame_180)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font8)
        self.label_67.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_67.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_67)

        self.horizontalSpacer_41 = QSpacerItem(87, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_41)

        self.label_64 = QLabel(self.frame_180)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(7, 7))
        self.label_64.setMaximumSize(QSize(7, 7))
        self.label_64.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"border-radius:3px;")

        self.horizontalLayout_36.addWidget(self.label_64)


        self.verticalLayout_37.addWidget(self.frame_180)

        self.line_7 = QFrame(self.frame_179)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_7)

        self.frame_181 = QFrame(self.frame_179)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_181)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(15, 0, 10, 0)
        self.label_23 = QLabel(self.frame_181)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font8)
        self.label_23.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_23)

        self.horizontalSpacer_42 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_42)

        self.label_11 = QLabel(self.frame_181)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 0))
        self.label_11.setMaximumSize(QSize(60, 16777215))
        font10 = QFont()
        font10.setPointSize(10)
        self.label_11.setFont(font10)
        self.label_11.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_11)


        self.verticalLayout_37.addWidget(self.frame_181)

        self.line_5 = QFrame(self.frame_179)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_5)

        self.frame_365 = QFrame(self.frame_179)
        self.frame_365.setObjectName(u"frame_365")
        self.frame_365.setMinimumSize(QSize(0, 40))
        self.frame_365.setMaximumSize(QSize(16777215, 40))
        self.frame_365.setFrameShape(QFrame.StyledPanel)
        self.frame_365.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_365)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(15, 0, 10, 0)
        self.label_91 = QLabel(self.frame_365)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font8)
        self.label_91.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_91.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_91)

        self.horizontalSpacer_44 = QSpacerItem(23, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_44)

        self.label_93 = QLabel(self.frame_365)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(50, 0))
        self.label_93.setMaximumSize(QSize(50, 16777215))
        self.label_93.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_93.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_93)


        self.verticalLayout_37.addWidget(self.frame_365)

        self.line_2 = QFrame(self.frame_179)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_2)

        self.frame_366 = QFrame(self.frame_179)
        self.frame_366.setObjectName(u"frame_366")
        self.frame_366.setMinimumSize(QSize(0, 40))
        self.frame_366.setMaximumSize(QSize(16777215, 40))
        self.frame_366.setFrameShape(QFrame.StyledPanel)
        self.frame_366.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_366)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(15, 0, 10, 0)
        self.label_58 = QLabel(self.frame_366)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font8)
        self.label_58.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_58)

        self.horizontalSpacer_43 = QSpacerItem(42, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_43)

        self.label_21 = QLabel(self.frame_366)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 0))
        self.label_21.setMaximumSize(QSize(50, 16777215))
        self.label_21.setFont(font10)
        self.label_21.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_21)


        self.verticalLayout_37.addWidget(self.frame_366)


        self.verticalLayout_65.addWidget(self.frame_179)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_4)

        self.label_19 = QLabel(self.frame_177)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font10)
        self.label_19.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_65.addWidget(self.label_19)


        self.verticalLayout_35.addWidget(self.frame_177)


        self.verticalLayout_34.addWidget(self.frame_174)


        self.horizontalLayout_3.addWidget(self.frame_173)


        self.verticalLayout_30.addWidget(self.frame_100)

        self.stackedWidget.addWidget(self.page_perfil)
        self.page_ControlFinace = QWidget()
        self.page_ControlFinace.setObjectName(u"page_ControlFinace")
        self.verticalLayout_11 = QVBoxLayout(self.page_ControlFinace)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.page_ControlFinace)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"border-radius:10px;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_42)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(8, 0, 8, 0)
        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(16777215, 250))
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_44)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 52))
        self.frame_45.setMaximumSize(QSize(16777215, 81))
        self.frame_45.setStyleSheet(u"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, 0, 0, 0)
        self.label_8 = QLabel(self.frame_45)
        self.label_8.setObjectName(u"label_8")
        font11 = QFont()
        font11.setFamilies([u"Raleway"])
        font11.setPointSize(28)
        self.label_8.setFont(font11)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-bottom:10px;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_8)


        self.verticalLayout_67.addWidget(self.frame_45)

        self.frame_50 = QFrame(self.frame_44)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(8, 0, 8, -1)
        self.frame_66 = QFrame(self.frame_50)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 170))
        self.frame_66.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_49.addWidget(self.frame_66)

        self.frame_183 = QFrame(self.frame_50)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setMinimumSize(QSize(0, 170))
        font12 = QFont()
        font12.setFamilies([u"Raleway"])
        self.frame_183.setFont(font12)
        self.frame_183.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_49.addWidget(self.frame_183)

        self.frame_185 = QFrame(self.frame_50)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setMinimumSize(QSize(0, 170))
        self.frame_185.setStyleSheet(u"background-color: rgb(119, 236, 160);")
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_49.addWidget(self.frame_185)


        self.verticalLayout_67.addWidget(self.frame_50)


        self.verticalLayout_68.addWidget(self.frame_44)

        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_43)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_184 = QFrame(self.frame_43)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setMinimumSize(QSize(0, 45))
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_184)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_216 = QFrame(self.frame_184)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setMaximumSize(QSize(16777215, 70))
        self.frame_216.setStyleSheet(u"QFrame{\n"
"background-color: rgb(,0,0,0);\n"
"border-radius:10px;}")
        self.frame_216.setFrameShape(QFrame.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_216)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.frame_217 = QFrame(self.frame_216)
        self.frame_217.setObjectName(u"frame_217")
        self.frame_217.setStyleSheet(u"")
        self.frame_217.setFrameShape(QFrame.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_217)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.label_190 = QLabel(self.frame_217)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setFont(font4)
        self.label_190.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_91.addWidget(self.label_190)


        self.horizontalLayout_90.addWidget(self.frame_217)

        self.frame_218 = QFrame(self.frame_216)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setStyleSheet(u"")
        self.frame_218.setFrameShape(QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_218)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.label_191 = QLabel(self.frame_218)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setFont(font4)
        self.label_191.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_191.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_92.addWidget(self.label_191)


        self.horizontalLayout_90.addWidget(self.frame_218)

        self.frame_219 = QFrame(self.frame_216)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setStyleSheet(u"")
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_219)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.label_192 = QLabel(self.frame_219)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setFont(font4)
        self.label_192.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_192.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_93.addWidget(self.label_192)


        self.horizontalLayout_90.addWidget(self.frame_219)

        self.frame_220 = QFrame(self.frame_216)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setStyleSheet(u"")
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_220)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.label_193 = QLabel(self.frame_220)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setFont(font4)
        self.label_193.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_193.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_193)


        self.horizontalLayout_90.addWidget(self.frame_220)

        self.frame_221 = QFrame(self.frame_216)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setMinimumSize(QSize(250, 0))
        self.frame_221.setStyleSheet(u"")
        self.frame_221.setFrameShape(QFrame.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_221)
        self.horizontalLayout_95.setSpacing(5)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(9, 0, 9, 0)
        self.label_198 = QLabel(self.frame_221)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setFont(font4)
        self.label_198.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_198.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_95.addWidget(self.label_198)


        self.horizontalLayout_90.addWidget(self.frame_221)


        self.horizontalLayout_89.addWidget(self.frame_216)


        self.verticalLayout_69.addWidget(self.frame_184)

        self.scrollArea_5 = QScrollArea(self.frame_43)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 573, 352))
        self.verticalLayout_71 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.frame_203 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setMaximumSize(QSize(16777215, 70))
        self.frame_203.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;}")
        self.frame_203.setFrameShape(QFrame.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_203)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.frame_204 = QFrame(self.frame_203)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setStyleSheet(u"")
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_204)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_151 = QLabel(self.frame_204)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font6)

        self.horizontalLayout_78.addWidget(self.label_151)


        self.horizontalLayout_77.addWidget(self.frame_204)

        self.frame_205 = QFrame(self.frame_203)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setStyleSheet(u"")
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_205)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_153 = QLabel(self.frame_205)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setFont(font6)
        self.label_153.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.label_153)


        self.horizontalLayout_77.addWidget(self.frame_205)

        self.frame_206 = QFrame(self.frame_203)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setStyleSheet(u"")
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_206)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_155 = QLabel(self.frame_206)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setFont(font6)
        self.label_155.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_80.addWidget(self.label_155)


        self.horizontalLayout_77.addWidget(self.frame_206)

        self.frame_207 = QFrame(self.frame_203)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setStyleSheet(u"")
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_207)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_174 = QLabel(self.frame_207)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setFont(font6)
        self.label_174.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_81.addWidget(self.label_174)


        self.horizontalLayout_77.addWidget(self.frame_207)

        self.frame_208 = QFrame(self.frame_203)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMinimumSize(QSize(250, 0))
        self.frame_208.setStyleSheet(u"")
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_208)
        self.horizontalLayout_82.setSpacing(5)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(9, 0, 9, 0)
        self.pushButton_9 = QPushButton(self.frame_208)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(8, 44))
        self.pushButton_9.setMaximumSize(QSize(80, 16777215))
        self.pushButton_9.setFont(font6)
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(70, 210, 100);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_82.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_208)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 44))
        self.pushButton_10.setFont(font6)
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(200, 52, 15);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_82.addWidget(self.pushButton_10)


        self.horizontalLayout_77.addWidget(self.frame_208)


        self.verticalLayout_71.addWidget(self.frame_203)

        self.frame_186 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setMaximumSize(QSize(16777215, 70))
        self.frame_186.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;}")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_186)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.frame_187 = QFrame(self.frame_186)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setStyleSheet(u"")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_187)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_61 = QLabel(self.frame_187)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font6)

        self.horizontalLayout_55.addWidget(self.label_61)


        self.horizontalLayout_52.addWidget(self.frame_187)

        self.frame_188 = QFrame(self.frame_186)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setStyleSheet(u"")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_188)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_101 = QLabel(self.frame_188)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font6)
        self.label_101.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.label_101)


        self.horizontalLayout_52.addWidget(self.frame_188)

        self.frame_189 = QFrame(self.frame_186)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setStyleSheet(u"")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_103 = QLabel(self.frame_189)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font6)
        self.label_103.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_103)


        self.horizontalLayout_52.addWidget(self.frame_189)

        self.frame_190 = QFrame(self.frame_186)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setStyleSheet(u"")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_190)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_111 = QLabel(self.frame_190)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font6)
        self.label_111.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_111)


        self.horizontalLayout_52.addWidget(self.frame_190)

        self.frame_191 = QFrame(self.frame_186)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setMinimumSize(QSize(250, 0))
        self.frame_191.setStyleSheet(u"")
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_191)
        self.horizontalLayout_64.setSpacing(5)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(9, 0, 9, 0)
        self.pushButton_3 = QPushButton(self.frame_191)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(8, 44))
        self.pushButton_3.setMaximumSize(QSize(80, 16777215))
        self.pushButton_3.setFont(font6)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(70, 210, 100);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_64.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_191)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 44))
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(200, 52, 15);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_64.addWidget(self.pushButton_2)


        self.horizontalLayout_52.addWidget(self.frame_191)


        self.verticalLayout_71.addWidget(self.frame_186)

        self.frame_197 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setMaximumSize(QSize(16777215, 70))
        self.frame_197.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;}")
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_197)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.frame_198 = QFrame(self.frame_197)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setStyleSheet(u"")
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_198)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_131 = QLabel(self.frame_198)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setFont(font6)

        self.horizontalLayout_72.addWidget(self.label_131)


        self.horizontalLayout_71.addWidget(self.frame_198)

        self.frame_199 = QFrame(self.frame_197)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setStyleSheet(u"")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_199)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_133 = QLabel(self.frame_199)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font6)
        self.label_133.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_73.addWidget(self.label_133)


        self.horizontalLayout_71.addWidget(self.frame_199)

        self.frame_200 = QFrame(self.frame_197)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setStyleSheet(u"")
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_200)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_141 = QLabel(self.frame_200)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setFont(font6)
        self.label_141.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.label_141)


        self.horizontalLayout_71.addWidget(self.frame_200)

        self.frame_201 = QFrame(self.frame_197)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setStyleSheet(u"")
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_201)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_143 = QLabel(self.frame_201)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setFont(font6)
        self.label_143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_143)


        self.horizontalLayout_71.addWidget(self.frame_201)

        self.frame_202 = QFrame(self.frame_197)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setMinimumSize(QSize(250, 0))
        self.frame_202.setStyleSheet(u"")
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_202)
        self.horizontalLayout_76.setSpacing(5)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(9, 0, 9, 0)
        self.pushButton_7 = QPushButton(self.frame_202)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(8, 44))
        self.pushButton_7.setMaximumSize(QSize(80, 16777215))
        self.pushButton_7.setFont(font6)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(70, 210, 100);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_76.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_202)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 44))
        self.pushButton_8.setFont(font6)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(200, 52, 15);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_76.addWidget(self.pushButton_8)


        self.horizontalLayout_71.addWidget(self.frame_202)


        self.verticalLayout_71.addWidget(self.frame_197)

        self.frame_192 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setMaximumSize(QSize(16777215, 70))
        self.frame_192.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;}")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_192)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.frame_193 = QFrame(self.frame_192)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setStyleSheet(u"")
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_193)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_113 = QLabel(self.frame_193)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font6)

        self.horizontalLayout_66.addWidget(self.label_113)


        self.horizontalLayout_65.addWidget(self.frame_193)

        self.frame_194 = QFrame(self.frame_192)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setStyleSheet(u"")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_194)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_121 = QLabel(self.frame_194)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setFont(font6)
        self.label_121.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.label_121)


        self.horizontalLayout_65.addWidget(self.frame_194)

        self.frame_195 = QFrame(self.frame_192)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setStyleSheet(u"")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_195)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_123 = QLabel(self.frame_195)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font6)
        self.label_123.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.label_123)


        self.horizontalLayout_65.addWidget(self.frame_195)

        self.frame_196 = QFrame(self.frame_192)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setStyleSheet(u"")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_196)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_185 = QLabel(self.frame_196)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setFont(font6)
        self.label_185.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.label_185)


        self.horizontalLayout_65.addWidget(self.frame_196)

        self.frame_215 = QFrame(self.frame_192)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setMinimumSize(QSize(250, 0))
        self.frame_215.setStyleSheet(u"")
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_70.setSpacing(5)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(9, 0, 9, 0)
        self.pushButton_4 = QPushButton(self.frame_215)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(8, 44))
        self.pushButton_4.setMaximumSize(QSize(80, 16777215))
        self.pushButton_4.setFont(font6)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(70, 210, 100);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_70.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.frame_215)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 44))
        self.pushButton_6.setFont(font6)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(200, 52, 15);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_70.addWidget(self.pushButton_6)


        self.horizontalLayout_65.addWidget(self.frame_215)


        self.verticalLayout_71.addWidget(self.frame_192)

        self.frame_209 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setMaximumSize(QSize(16777215, 70))
        self.frame_209.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;}")
        self.frame_209.setFrameShape(QFrame.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_209)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.frame_210 = QFrame(self.frame_209)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setStyleSheet(u"")
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_210)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_175 = QLabel(self.frame_210)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setFont(font6)

        self.horizontalLayout_84.addWidget(self.label_175)


        self.horizontalLayout_83.addWidget(self.frame_210)

        self.frame_211 = QFrame(self.frame_209)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setStyleSheet(u"")
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_211)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_180 = QLabel(self.frame_211)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setFont(font6)
        self.label_180.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_180)


        self.horizontalLayout_83.addWidget(self.frame_211)

        self.frame_212 = QFrame(self.frame_209)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setStyleSheet(u"")
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_212)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_182 = QLabel(self.frame_212)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setFont(font6)
        self.label_182.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_86.addWidget(self.label_182)


        self.horizontalLayout_83.addWidget(self.frame_212)

        self.frame_213 = QFrame(self.frame_209)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setStyleSheet(u"")
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_213)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_184 = QLabel(self.frame_213)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setFont(font6)
        self.label_184.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_87.addWidget(self.label_184)


        self.horizontalLayout_83.addWidget(self.frame_213)

        self.frame_214 = QFrame(self.frame_209)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setMinimumSize(QSize(250, 0))
        self.frame_214.setStyleSheet(u"")
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_214)
        self.horizontalLayout_88.setSpacing(5)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(9, 0, 9, 0)
        self.pushButton_11 = QPushButton(self.frame_214)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(8, 44))
        self.pushButton_11.setMaximumSize(QSize(80, 16777215))
        self.pushButton_11.setFont(font6)
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(70, 210, 100);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 227, 111);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_88.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_214)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 44))
        self.pushButton_12.setFont(font6)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(200, 52, 15);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(210, 55, 16);\n"
"border-radius: 7px;\n"
"color:rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_88.addWidget(self.pushButton_12)


        self.horizontalLayout_83.addWidget(self.frame_214)


        self.verticalLayout_71.addWidget(self.frame_209)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_69.addWidget(self.scrollArea_5)


        self.verticalLayout_68.addWidget(self.frame_43)


        self.verticalLayout_11.addWidget(self.frame_42)

        self.stackedWidget.addWidget(self.page_ControlFinace)
        self.page_CoinsQuote = QWidget()
        self.page_CoinsQuote.setObjectName(u"page_CoinsQuote")
        self.verticalLayout_15 = QVBoxLayout(self.page_CoinsQuote)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.page_CoinsQuote)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_Coins_2 = QWidget()
        self.scrollAreaWidgetContents_Coins_2.setObjectName(u"scrollAreaWidgetContents_Coins_2")
        self.scrollAreaWidgetContents_Coins_2.setGeometry(QRect(0, 0, 862, 1830))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_Coins_2)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.scrollAreaWidgetContents_Coins_2)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 1830))
        self.frame_41.setStyleSheet(u"")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_41)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_scrollBTC = QFrame(self.frame_41)
        self.frame_scrollBTC.setObjectName(u"frame_scrollBTC")
        self.frame_scrollBTC.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollBTC.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollBTC.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_scrollBTC)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_scrollBTC)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(8, 8, 8, 8)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_4)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 40))
        self.frame_14.setMaximumSize(QSize(16777215, 40))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(43, 10, 141, 16))
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(5, 6, 30, 30))
        self.label_13.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/exchange_bitcoinn_30px.png"))

        self.verticalLayout_41.addWidget(self.frame_14)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.bitcoin_lbl = QLabel(self.frame_10)
        self.bitcoin_lbl.setObjectName(u"bitcoin_lbl")
        self.bitcoin_lbl.setGeometry(QRect(10, 5, 20, 40))
        font13 = QFont()
        font13.setPointSize(31)
        font13.setBold(True)
        self.bitcoin_lbl.setFont(font13)
        self.bitcoin_lbl.setStyleSheet(u"color: #FFF0F03F;")
        self.data_bitcoins = QLabel(self.frame_10)
        self.data_bitcoins.setObjectName(u"data_bitcoins")
        self.data_bitcoins.setGeometry(QRect(21, 100, 160, 15))
        self.data_bitcoins.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 6, 50, 41))
        self.label_9.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/bitcoin_50px.png"))
        self.bitcoin_aoa_lbl = QLabel(self.frame_10)
        self.bitcoin_aoa_lbl.setObjectName(u"bitcoin_aoa_lbl")
        self.bitcoin_aoa_lbl.setGeometry(QRect(20, 67, 210, 30))
        font14 = QFont()
        font14.setPointSize(18)
        font14.setBold(True)
        self.bitcoin_aoa_lbl.setFont(font14)
        self.bitcoin_aoa_lbl.setStyleSheet(u"color: rgb(90, 173, 253);")

        self.verticalLayout_41.addWidget(self.frame_10)


        self.verticalLayout_20.addWidget(self.frame_4)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_scrollBTC)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_5)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_18)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 35))
        self.frame_19.setMaximumSize(QSize(16777215, 35))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_19)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(15, 15, 15, 0)
        self.progressBar_1 = QProgressBar(self.frame_19)
        self.progressBar_1.setObjectName(u"progressBar_1")
        self.progressBar_1.setMaximumSize(QSize(16777215, 10))
        self.progressBar_1.setStyleSheet(u"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.395765 rgba(89, 242, 124, 255), stop:0.711726 rgba(90, 173, 253, 255), stop:0.941368 rgba(90, 173, 253, 255), stop:0.960912 rgba(239, 73, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_1.setValue(100)
        self.progressBar_1.setTextVisible(False)
        self.progressBar_1.setInvertedAppearance(True)

        self.verticalLayout_43.addWidget(self.progressBar_1)


        self.verticalLayout_42.addWidget(self.frame_19)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 30, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(120, 60))
        self.frame_22.setMaximumSize(QSize(120, 60))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_22)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, -1)
        self.label_2 = QLabel(self.frame_22)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_2)

        self.label = QLabel(self.frame_22)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label)


        self.horizontalLayout_19.addWidget(self.frame_22)

        self.horizontalSpacer_6 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_6)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(200, 0))
        self.frame_23.setMaximumSize(QSize(200, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_23)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, -1)
        self.label_10 = QLabel(self.frame_23)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_45.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_23)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_3)


        self.horizontalLayout_19.addWidget(self.frame_23)

        self.horizontalSpacer_7 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_7)

        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(250, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_24)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, -1)
        self.label_15 = QLabel(self.frame_24)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(157, 0))
        self.label_15.setMaximumSize(QSize(157, 16777215))
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.label_15)

        self.label_14 = QLabel(self.frame_24)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.label_14)


        self.horizontalLayout_19.addWidget(self.frame_24)


        self.verticalLayout_42.addWidget(self.frame_21)


        self.verticalLayout_27.addWidget(self.frame_18)

        self.frame_15 = QFrame(self.frame_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_15)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_15)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(15, 10, 28, 0)
        self.site = QLabel(self.frame_27)
        self.site.setObjectName(u"site")
        self.site.setFont(font8)
        self.site.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.site)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer)

        self.bitcoin_LEdit = QLineEdit(self.frame_27)
        self.bitcoin_LEdit.setObjectName(u"bitcoin_LEdit")
        self.bitcoin_LEdit.setMinimumSize(QSize(250, 27))
        self.bitcoin_LEdit.setMaximumSize(QSize(190, 27))
        self.bitcoin_LEdit.setFont(font14)
        self.bitcoin_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.bitcoin_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.bitcoin_LEdit)

        self.label_20 = QLabel(self.frame_27)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(32, 20))
        self.label_20.setMaximumSize(QSize(32, 20))
        font15 = QFont()
        font15.setPointSize(14)
        font15.setBold(True)
        self.label_20.setFont(font15)
        self.label_20.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_20)


        self.verticalLayout_47.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.frame_15)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(15, -1, 20, 10)
        self.font = QLabel(self.frame_26)
        self.font.setObjectName(u"font")
        self.font.setFont(font8)
        self.font.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.font)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_2)

        self.bitcoin_aoa_LEdit = QLineEdit(self.frame_26)
        self.bitcoin_aoa_LEdit.setObjectName(u"bitcoin_aoa_LEdit")
        self.bitcoin_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.bitcoin_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.bitcoin_aoa_LEdit.setFont(font14)
        self.bitcoin_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.bitcoin_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.bitcoin_aoa_LEdit)

        self.label_22 = QLabel(self.frame_26)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(40, 20))
        self.label_22.setMaximumSize(QSize(40, 20))
        self.label_22.setFont(font15)
        self.label_22.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_22)


        self.verticalLayout_47.addWidget(self.frame_26)


        self.verticalLayout_27.addWidget(self.frame_15)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_19.addWidget(self.frame_scrollBTC)

        self.frame_scrollKWD = QFrame(self.frame_41)
        self.frame_scrollKWD.setObjectName(u"frame_scrollKWD")
        self.frame_scrollKWD.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollKWD.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollKWD.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_scrollKWD)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_scrollKWD)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(300, 0))
        self.frame_6.setMaximumSize(QSize(300, 16777215))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_6)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(8, 8, 8, 8)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_7)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_7)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 40))
        self.frame_29.setMaximumSize(QSize(16777215, 40))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_29)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(43, 10, 210, 16))
        self.label_24.setFont(font8)
        self.label_24.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_25 = QLabel(self.frame_29)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 0, 40, 41))
        self.label_25.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_75 = QLabel(self.frame_29)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(10, 8, 20, 20))
        font16 = QFont()
        font16.setBold(True)
        self.label_75.setFont(font16)
        self.label_75.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_48.addWidget(self.frame_29)

        self.frame_28 = QFrame(self.frame_7)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.dk_lbl = QLabel(self.frame_28)
        self.dk_lbl.setObjectName(u"dk_lbl")
        self.dk_lbl.setGeometry(QRect(10, 5, 20, 40))
        self.dk_lbl.setFont(font13)
        self.dk_lbl.setStyleSheet(u"color: #FFF0F03F;")
        self.data_dk = QLabel(self.frame_28)
        self.data_dk.setObjectName(u"data_dk")
        self.data_dk.setGeometry(QRect(21, 100, 160, 15))
        self.data_dk.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_18 = QLabel(self.frame_28)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 6, 50, 41))
        self.label_18.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.dk_aoa_lbl = QLabel(self.frame_28)
        self.dk_aoa_lbl.setObjectName(u"dk_aoa_lbl")
        self.dk_aoa_lbl.setGeometry(QRect(20, 67, 210, 30))
        self.dk_aoa_lbl.setFont(font14)
        self.dk_aoa_lbl.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_160 = QLabel(self.frame_28)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setGeometry(QRect(42, 18, 23, 14))
        font17 = QFont()
        font17.setPointSize(10)
        font17.setBold(True)
        self.label_160.setFont(font17)
        self.label_160.setStyleSheet(u"color: rgb(240, 240, 63);\n"
"border-radius:3px")

        self.verticalLayout_48.addWidget(self.frame_28)


        self.verticalLayout_21.addWidget(self.frame_7)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_11 = QFrame(self.frame_scrollKWD)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_11)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_11)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_67)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_67)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_30)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_31)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 35))
        self.frame_32.setMaximumSize(QSize(16777215, 35))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_32)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(15, 15, 15, 0)
        self.progressBar_2 = QProgressBar(self.frame_32)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMaximumSize(QSize(16777215, 10))
        self.progressBar_2.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.318182 rgba(89, 242, 124, 255), stop:0.335227 rgba(90, 172, 252, 255), stop:0.835227 rgba(90, 173, 253, 255), stop:0.846591 rgba(218, 66, 0, 255));\n"
"border-radius:5px;\n"
"}\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_2.setValue(100)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setInvertedAppearance(True)

        self.verticalLayout_51.addWidget(self.progressBar_2)


        self.verticalLayout_50.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 0, 30, 0)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(120, 60))
        self.frame_34.setMaximumSize(QSize(120, 60))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_34)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, -1)
        self.label_4 = QLabel(self.frame_34)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_34)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_5)


        self.horizontalLayout_20.addWidget(self.frame_34)

        self.horizontalSpacer_22 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_22)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(200, 0))
        self.frame_35.setMaximumSize(QSize(200, 16777215))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_35)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, -1)
        self.label_26 = QLabel(self.frame_35)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_26)

        self.label_6 = QLabel(self.frame_35)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_6)


        self.horizontalLayout_20.addWidget(self.frame_35)

        self.horizontalSpacer_23 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_23)

        self.frame_36 = QFrame(self.frame_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(157, 0))
        self.frame_36.setMaximumSize(QSize(157, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_36)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, -1)
        self.label_27 = QLabel(self.frame_36)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)
        self.label_27.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_36)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_28)


        self.horizontalLayout_20.addWidget(self.frame_36)


        self.verticalLayout_50.addWidget(self.frame_33)


        self.verticalLayout_49.addWidget(self.frame_31)

        self.frame_37 = QFrame(self.frame_30)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_37)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(15, 10, 17, 0)
        self.site_2 = QLabel(self.frame_38)
        self.site_2.setObjectName(u"site_2")
        self.site_2.setFont(font8)
        self.site_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.site_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_4)

        self.DK_LEdit = QLineEdit(self.frame_38)
        self.DK_LEdit.setObjectName(u"DK_LEdit")
        self.DK_LEdit.setMinimumSize(QSize(250, 27))
        self.DK_LEdit.setMaximumSize(QSize(250, 27))
        self.DK_LEdit.setFont(font14)
        self.DK_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.DK_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.DK_LEdit)

        self.label_30 = QLabel(self.frame_38)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(44, 20))
        self.label_30.setMaximumSize(QSize(44, 20))
        self.label_30.setFont(font15)
        self.label_30.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_30)


        self.verticalLayout_55.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(15, -1, 20, 10)
        self.font_2 = QLabel(self.frame_39)
        self.font_2.setObjectName(u"font_2")
        self.font_2.setFont(font8)
        self.font_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.font_2)

        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_5)

        self.DK_aoa_LEdit = QLineEdit(self.frame_39)
        self.DK_aoa_LEdit.setObjectName(u"DK_aoa_LEdit")
        self.DK_aoa_LEdit.setMinimumSize(QSize(250, 27))
        self.DK_aoa_LEdit.setMaximumSize(QSize(250, 27))
        self.DK_aoa_LEdit.setFont(font14)
        self.DK_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.DK_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.DK_aoa_LEdit)

        self.label_32 = QLabel(self.frame_39)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(40, 20))
        self.label_32.setMaximumSize(QSize(40, 20))
        self.label_32.setFont(font15)
        self.label_32.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_32)


        self.verticalLayout_55.addWidget(self.frame_39)


        self.verticalLayout_49.addWidget(self.frame_37)


        self.verticalLayout_56.addWidget(self.frame_30)


        self.verticalLayout_28.addWidget(self.frame_67)


        self.horizontalLayout_6.addWidget(self.frame_11)


        self.verticalLayout_19.addWidget(self.frame_scrollKWD)

        self.frame_scrollBHD = QFrame(self.frame_41)
        self.frame_scrollBHD.setObjectName(u"frame_scrollBHD")
        self.frame_scrollBHD.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollBHD.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollBHD.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_scrollBHD)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_scrollBHD)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(300, 0))
        self.frame_12.setMaximumSize(QSize(300, 16777215))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_12)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(8, 8, 8, 8)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_13)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.frame_13)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 40))
        self.frame_65.setMaximumSize(QSize(16777215, 40))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.label_33 = QLabel(self.frame_65)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(43, 10, 220, 16))
        self.label_33.setFont(font8)
        self.label_33.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_78 = QLabel(self.frame_65)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(0, 0, 40, 41))
        self.label_78.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_77 = QLabel(self.frame_65)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(5, 10, 26, 20))
        self.label_77.setFont(font16)
        self.label_77.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_57.addWidget(self.frame_65)

        self.frame_68 = QFrame(self.frame_13)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.label_35 = QLabel(self.frame_68)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 5, 20, 40))
        self.label_35.setFont(font13)
        self.label_35.setStyleSheet(u"color: #FFF0F03F;")
        self.label_36 = QLabel(self.frame_68)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(21, 100, 160, 15))
        self.label_36.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_38 = QLabel(self.frame_68)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(20, 67, 210, 30))
        self.label_38.setFont(font14)
        self.label_38.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_79 = QLabel(self.frame_68)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(42, 18, 25, 13))
        self.label_79.setFont(font17)
        self.label_79.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_34 = QLabel(self.frame_68)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(30, 6, 50, 41))
        self.label_34.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.label_34.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_38.raise_()
        self.label_79.raise_()

        self.verticalLayout_57.addWidget(self.frame_68)


        self.verticalLayout_22.addWidget(self.frame_13)


        self.horizontalLayout_12.addWidget(self.frame_12)

        self.frame_69 = QFrame(self.frame_scrollBHD)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_69)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.frame_69)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_103)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_104)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 35))
        self.frame_105.setMaximumSize(QSize(16777215, 35))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_105)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(15, 15, 15, 0)
        self.progressBar_3 = QProgressBar(self.frame_105)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setMaximumSize(QSize(16777215, 10))
        self.progressBar_3.setStyleSheet(u"QProgressBar::chunk{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.318182 rgba(89, 242, 124, 255), stop:0.335227 rgba(90, 172, 252, 255), stop:0.806818 rgba(90, 173, 253, 255), stop:0.829545 rgba(218, 66, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_3.setValue(100)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setInvertedAppearance(True)

        self.verticalLayout_75.addWidget(self.progressBar_3)


        self.verticalLayout_74.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_104)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 0, 30, 0)
        self.frame_107 = QFrame(self.frame_106)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(120, 60))
        self.frame_107.setMaximumSize(QSize(120, 60))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_107)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, -1)
        self.label_85 = QLabel(self.frame_107)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font5)
        self.label_85.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_85.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_76.addWidget(self.label_85)

        self.label_86 = QLabel(self.frame_107)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.label_86)


        self.horizontalLayout_21.addWidget(self.frame_107)

        self.horizontalSpacer_25 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_25)

        self.frame_108 = QFrame(self.frame_106)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(200, 0))
        self.frame_108.setMaximumSize(QSize(200, 16777215))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_108)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, -1)
        self.label_87 = QLabel(self.frame_108)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font5)
        self.label_87.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.label_87)

        self.label_88 = QLabel(self.frame_108)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_88.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.label_88)


        self.horizontalLayout_21.addWidget(self.frame_108)

        self.horizontalSpacer_24 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_24)

        self.frame_109 = QFrame(self.frame_106)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(157, 0))
        self.frame_109.setMaximumSize(QSize(157, 16777215))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_109)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, -1)
        self.label_89 = QLabel(self.frame_109)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font5)
        self.label_89.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_89.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.label_89)

        self.label_90 = QLabel(self.frame_109)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_90.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.label_90)


        self.horizontalLayout_21.addWidget(self.frame_109)


        self.verticalLayout_74.addWidget(self.frame_106)


        self.verticalLayout_73.addWidget(self.frame_104)

        self.frame_110 = QFrame(self.frame_103)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_110)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(15, 10, 19, 0)
        self.site_3 = QLabel(self.frame_111)
        self.site_3.setObjectName(u"site_3")
        self.site_3.setFont(font8)
        self.site_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.site_3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_8)

        self.DB_LEdit = QLineEdit(self.frame_111)
        self.DB_LEdit.setObjectName(u"DB_LEdit")
        self.DB_LEdit.setMinimumSize(QSize(250, 25))
        self.DB_LEdit.setMaximumSize(QSize(250, 25))
        self.DB_LEdit.setFont(font14)
        self.DB_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.DB_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.DB_LEdit)

        self.label_92 = QLabel(self.frame_111)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(40, 20))
        self.label_92.setMaximumSize(QSize(32, 20))
        self.label_92.setFont(font15)
        self.label_92.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_92.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_92)


        self.verticalLayout_79.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_110)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(15, -1, 20, 10)
        self.font_3 = QLabel(self.frame_112)
        self.font_3.setObjectName(u"font_3")
        self.font_3.setFont(font8)
        self.font_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.font_3)

        self.horizontalSpacer_9 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_9)

        self.DB_aoa_LEdit = QLineEdit(self.frame_112)
        self.DB_aoa_LEdit.setObjectName(u"DB_aoa_LEdit")
        self.DB_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.DB_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.DB_aoa_LEdit.setFont(font14)
        self.DB_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.DB_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.DB_aoa_LEdit)

        self.label_94 = QLabel(self.frame_112)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(40, 20))
        self.label_94.setMaximumSize(QSize(40, 20))
        self.label_94.setFont(font15)
        self.label_94.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_94.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.label_94)


        self.verticalLayout_79.addWidget(self.frame_112)


        self.verticalLayout_73.addWidget(self.frame_110)


        self.verticalLayout_72.addWidget(self.frame_103)


        self.horizontalLayout_12.addWidget(self.frame_69)


        self.verticalLayout_19.addWidget(self.frame_scrollBHD)

        self.frame_scrollOMR = QFrame(self.frame_41)
        self.frame_scrollOMR.setObjectName(u"frame_scrollOMR")
        self.frame_scrollOMR.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollOMR.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollOMR.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_scrollOMR)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_scrollOMR)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(300, 0))
        self.frame_17.setMaximumSize(QSize(300, 16777215))
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_17)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(8, 8, 8, 8)
        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_20)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.frame_20)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 40))
        self.frame_83.setMaximumSize(QSize(16777215, 40))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.label_39 = QLabel(self.frame_83)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(43, 10, 180, 16))
        self.label_39.setFont(font8)
        self.label_39.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_80 = QLabel(self.frame_83)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(0, 0, 40, 41))
        self.label_80.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_81 = QLabel(self.frame_83)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(10, 6, 20, 20))
        font18 = QFont()
        font18.setPointSize(11)
        font18.setBold(True)
        self.label_81.setFont(font18)
        self.label_81.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_58.addWidget(self.frame_83)

        self.frame_84 = QFrame(self.frame_20)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.label_41 = QLabel(self.frame_84)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 5, 20, 40))
        self.label_41.setFont(font13)
        self.label_41.setStyleSheet(u"color: #FFF0F03F;")
        self.label_42 = QLabel(self.frame_84)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(21, 100, 160, 15))
        self.label_42.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_44 = QLabel(self.frame_84)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(20, 67, 210, 30))
        self.label_44.setFont(font14)
        self.label_44.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_37 = QLabel(self.frame_84)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(30, 6, 50, 41))
        self.label_37.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.label_82 = QLabel(self.frame_84)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(43, 14, 22, 18))
        font19 = QFont()
        font19.setPointSize(13)
        font19.setBold(True)
        self.label_82.setFont(font19)
        self.label_82.setStyleSheet(u"color: rgb(240, 240, 63);\n"
"border-radius:9px;\n"
"")

        self.verticalLayout_58.addWidget(self.frame_84)


        self.verticalLayout_23.addWidget(self.frame_20)


        self.horizontalLayout_13.addWidget(self.frame_17)

        self.frame_71 = QFrame(self.frame_scrollOMR)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_71)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.frame_72 = QFrame(self.frame_71)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_72)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_113 = QFrame(self.frame_72)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_113)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.frame_114 = QFrame(self.frame_113)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(0, 35))
        self.frame_114.setMaximumSize(QSize(16777215, 35))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_114)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(15, 15, 15, 0)
        self.progressBar_4 = QProgressBar(self.frame_114)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setMaximumSize(QSize(16777215, 10))
        self.progressBar_4.setStyleSheet(u"QProgressBar::chunk{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.318182 rgba(89, 242, 124, 255), stop:0.335227 rgba(90, 172, 252, 255), stop:0.778409 rgba(90, 173, 253, 255), stop:0.795455 rgba(218, 66, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_4.setValue(100)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setInvertedAppearance(True)

        self.verticalLayout_83.addWidget(self.progressBar_4)


        self.verticalLayout_82.addWidget(self.frame_114)

        self.frame_115 = QFrame(self.frame_113)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(10, -1, 30, -1)
        self.frame_116 = QFrame(self.frame_115)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(120, 60))
        self.frame_116.setMaximumSize(QSize(120, 60))
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_116)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, -1)
        self.label_95 = QLabel(self.frame_116)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font5)
        self.label_95.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_95.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_84.addWidget(self.label_95)

        self.label_96 = QLabel(self.frame_116)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_96.setAlignment(Qt.AlignCenter)

        self.verticalLayout_84.addWidget(self.label_96)


        self.horizontalLayout_23.addWidget(self.frame_116)

        self.horizontalSpacer_28 = QSpacerItem(66, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_28)

        self.frame_117 = QFrame(self.frame_115)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setMinimumSize(QSize(0, 0))
        self.frame_117.setMaximumSize(QSize(200, 16777215))
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_117)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, -1)
        self.label_97 = QLabel(self.frame_117)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font5)
        self.label_97.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_97.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.label_97)

        self.label_98 = QLabel(self.frame_117)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_98.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.label_98)


        self.horizontalLayout_23.addWidget(self.frame_117)

        self.horizontalSpacer_29 = QSpacerItem(65, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_29)

        self.frame_118 = QFrame(self.frame_115)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMinimumSize(QSize(157, 0))
        self.frame_118.setMaximumSize(QSize(157, 16777215))
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_118)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, -1)
        self.label_99 = QLabel(self.frame_118)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMaximumSize(QSize(1235, 16777215))
        self.label_99.setFont(font5)
        self.label_99.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_99.setAlignment(Qt.AlignCenter)

        self.verticalLayout_86.addWidget(self.label_99)

        self.label_100 = QLabel(self.frame_118)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_100.setAlignment(Qt.AlignCenter)

        self.verticalLayout_86.addWidget(self.label_100)


        self.horizontalLayout_23.addWidget(self.frame_118)


        self.verticalLayout_82.addWidget(self.frame_115)


        self.verticalLayout_81.addWidget(self.frame_113)

        self.frame_119 = QFrame(self.frame_72)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_119)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.frame_120 = QFrame(self.frame_119)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(15, 10, 17, 0)
        self.site_5 = QLabel(self.frame_120)
        self.site_5.setObjectName(u"site_5")
        self.site_5.setFont(font8)
        self.site_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.site_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_10)

        self.RO_LEdit = QLineEdit(self.frame_120)
        self.RO_LEdit.setObjectName(u"RO_LEdit")
        self.RO_LEdit.setMinimumSize(QSize(250, 25))
        self.RO_LEdit.setMaximumSize(QSize(250, 25))
        self.RO_LEdit.setFont(font14)
        self.RO_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.RO_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.RO_LEdit)

        self.label_102 = QLabel(self.frame_120)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(45, 20))
        self.label_102.setMaximumSize(QSize(32, 20))
        self.label_102.setFont(font15)
        self.label_102.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_102.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_102)


        self.verticalLayout_87.addWidget(self.frame_120)

        self.frame_121 = QFrame(self.frame_119)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(15, -1, 20, 10)
        self.font_4 = QLabel(self.frame_121)
        self.font_4.setObjectName(u"font_4")
        self.font_4.setFont(font8)
        self.font_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.font_4)

        self.horizontalSpacer_11 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_11)

        self.RO_aoa_LEdit = QLineEdit(self.frame_121)
        self.RO_aoa_LEdit.setObjectName(u"RO_aoa_LEdit")
        self.RO_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.RO_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.RO_aoa_LEdit.setFont(font14)
        self.RO_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.RO_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.RO_aoa_LEdit)

        self.label_104 = QLabel(self.frame_121)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(40, 20))
        self.label_104.setMaximumSize(QSize(40, 20))
        self.label_104.setFont(font15)
        self.label_104.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_104.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.label_104)


        self.verticalLayout_87.addWidget(self.frame_121)


        self.verticalLayout_81.addWidget(self.frame_119)


        self.verticalLayout_80.addWidget(self.frame_72)


        self.horizontalLayout_13.addWidget(self.frame_71)


        self.verticalLayout_19.addWidget(self.frame_scrollOMR)

        self.frame_scrollJOD = QFrame(self.frame_41)
        self.frame_scrollJOD.setObjectName(u"frame_scrollJOD")
        self.frame_scrollJOD.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollJOD.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollJOD.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_scrollJOD)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.frame_scrollJOD)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(300, 0))
        self.frame_40.setMaximumSize(QSize(300, 16777215))
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_40)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(8, 8, 8, 8)
        self.frame_51 = QFrame(self.frame_40)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_51)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_51)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(0, 40))
        self.frame_85.setMaximumSize(QSize(16777215, 40))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.label_45 = QLabel(self.frame_85)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(43, 10, 220, 16))
        self.label_45.setFont(font8)
        self.label_45.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_83 = QLabel(self.frame_85)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(0, 0, 40, 41))
        self.label_83.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_84 = QLabel(self.frame_85)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(7, 10, 20, 20))
        self.label_84.setFont(font16)
        self.label_84.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_59.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_51)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.label_47 = QLabel(self.frame_86)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 5, 20, 40))
        self.label_47.setFont(font13)
        self.label_47.setStyleSheet(u"color: #FFF0F03F;")
        self.label_48 = QLabel(self.frame_86)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(21, 100, 160, 15))
        self.label_48.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_50 = QLabel(self.frame_86)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(20, 67, 210, 30))
        self.label_50.setFont(font14)
        self.label_50.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_40 = QLabel(self.frame_86)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(30, 6, 50, 41))
        self.label_40.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.label_159 = QLabel(self.frame_86)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setGeometry(QRect(43, 15, 20, 20))
        self.label_159.setFont(font18)
        self.label_159.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_59.addWidget(self.frame_86)


        self.verticalLayout_24.addWidget(self.frame_51)


        self.horizontalLayout_14.addWidget(self.frame_40)

        self.frame_73 = QFrame(self.frame_scrollJOD)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_73)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_73)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_52)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.frame_52)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_55)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_55)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(0, 35))
        self.frame_58.setMaximumSize(QSize(16777215, 35))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_58)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(15, 15, 15, 0)
        self.progressBar_5 = QProgressBar(self.frame_58)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setMaximumSize(QSize(16777215, 10))
        self.progressBar_5.setStyleSheet(u"QProgressBar::chunk{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.318182 rgba(89, 242, 124, 255), stop:0.335227 rgba(90, 172, 252, 255), stop:0.744318 rgba(90, 173, 253, 255), stop:0.772727 rgba(218, 66, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_5.setValue(100)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setInvertedAppearance(True)

        self.verticalLayout_91.addWidget(self.progressBar_5)


        self.verticalLayout_90.addWidget(self.frame_58)

        self.frame_74 = QFrame(self.frame_55)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 0, 30, 0)
        self.frame_75 = QFrame(self.frame_74)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(120, 60))
        self.frame_75.setMaximumSize(QSize(120, 60))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_75)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, -1)
        self.label_105 = QLabel(self.frame_75)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font5)
        self.label_105.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_105.setAlignment(Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.label_105)

        self.label_106 = QLabel(self.frame_75)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_106.setAlignment(Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.label_106)


        self.horizontalLayout_24.addWidget(self.frame_75)

        self.horizontalSpacer_30 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_30)

        self.frame_76 = QFrame(self.frame_74)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(200, 0))
        self.frame_76.setMaximumSize(QSize(200, 16777215))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_76)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, -1)
        self.label_107 = QLabel(self.frame_76)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font5)
        self.label_107.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_107.setAlignment(Qt.AlignCenter)

        self.verticalLayout_93.addWidget(self.label_107)

        self.label_108 = QLabel(self.frame_76)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_108.setAlignment(Qt.AlignCenter)

        self.verticalLayout_93.addWidget(self.label_108)


        self.horizontalLayout_24.addWidget(self.frame_76)

        self.horizontalSpacer_31 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_31)

        self.frame_77 = QFrame(self.frame_74)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(157, 0))
        self.frame_77.setMaximumSize(QSize(157, 16777215))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_77)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, -1)
        self.label_109 = QLabel(self.frame_77)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font5)
        self.label_109.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_109.setAlignment(Qt.AlignCenter)

        self.verticalLayout_94.addWidget(self.label_109)

        self.label_110 = QLabel(self.frame_77)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_110.setAlignment(Qt.AlignCenter)

        self.verticalLayout_94.addWidget(self.label_110)


        self.horizontalLayout_24.addWidget(self.frame_77)


        self.verticalLayout_90.addWidget(self.frame_74)


        self.verticalLayout_89.addWidget(self.frame_55)

        self.frame_78 = QFrame(self.frame_52)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_78)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.frame_122 = QFrame(self.frame_78)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(15, 10, 23, 0)
        self.site_6 = QLabel(self.frame_122)
        self.site_6.setObjectName(u"site_6")
        self.site_6.setFont(font8)
        self.site_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.site_6)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_12)

        self.DJ_LEdit = QLineEdit(self.frame_122)
        self.DJ_LEdit.setObjectName(u"DJ_LEdit")
        self.DJ_LEdit.setMinimumSize(QSize(250, 25))
        self.DJ_LEdit.setMaximumSize(QSize(250, 25))
        self.DJ_LEdit.setFont(font14)
        self.DJ_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.DJ_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.DJ_LEdit)

        self.label_112 = QLabel(self.frame_122)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(36, 20))
        self.label_112.setMaximumSize(QSize(36, 20))
        self.label_112.setFont(font15)
        self.label_112.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_112.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.label_112)


        self.verticalLayout_95.addWidget(self.frame_122)

        self.frame_123 = QFrame(self.frame_78)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(15, -1, 20, 10)
        self.font_5 = QLabel(self.frame_123)
        self.font_5.setObjectName(u"font_5")
        self.font_5.setFont(font8)
        self.font_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.font_5)

        self.horizontalSpacer_13 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_13)

        self.DJ_aoa_LEdit = QLineEdit(self.frame_123)
        self.DJ_aoa_LEdit.setObjectName(u"DJ_aoa_LEdit")
        self.DJ_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.DJ_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.DJ_aoa_LEdit.setFont(font14)
        self.DJ_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.DJ_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.DJ_aoa_LEdit)

        self.label_114 = QLabel(self.frame_123)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(40, 20))
        self.label_114.setMaximumSize(QSize(40, 20))
        self.label_114.setFont(font15)
        self.label_114.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_114.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.label_114)


        self.verticalLayout_95.addWidget(self.frame_123)


        self.verticalLayout_89.addWidget(self.frame_78)


        self.verticalLayout_88.addWidget(self.frame_52)


        self.horizontalLayout_14.addWidget(self.frame_73)


        self.verticalLayout_19.addWidget(self.frame_scrollJOD)

        self.frame_scrollKYD = QFrame(self.frame_41)
        self.frame_scrollKYD.setObjectName(u"frame_scrollKYD")
        self.frame_scrollKYD.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollKYD.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollKYD.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_scrollKYD)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_scrollKYD)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(300, 0))
        self.frame_56.setMaximumSize(QSize(300, 16777215))
        self.frame_56.setStyleSheet(u"")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_56)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(8, 8, 8, 8)
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_57)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_89 = QFrame(self.frame_57)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(0, 40))
        self.frame_89.setMaximumSize(QSize(16777215, 40))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.label_57 = QLabel(self.frame_89)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(43, 10, 231, 20))
        self.label_57.setFont(font8)
        self.label_57.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_162 = QLabel(self.frame_89)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setGeometry(QRect(0, 0, 40, 41))
        self.label_162.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_163 = QLabel(self.frame_89)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setGeometry(QRect(15, 9, 10, 20))
        self.label_163.setFont(font15)
        self.label_163.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_61.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.frame_57)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.label_59 = QLabel(self.frame_90)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(10, 5, 20, 40))
        self.label_59.setFont(font13)
        self.label_59.setStyleSheet(u"color: #FFF0F03F;")
        self.label_60 = QLabel(self.frame_90)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(21, 100, 160, 15))
        self.label_60.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_62 = QLabel(self.frame_90)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(20, 67, 210, 30))
        self.label_62.setFont(font14)
        self.label_62.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_46 = QLabel(self.frame_90)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(30, 6, 50, 41))
        self.label_46.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.label_164 = QLabel(self.frame_90)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(48, 13, 13, 20))
        font20 = QFont()
        font20.setPointSize(17)
        font20.setBold(True)
        self.label_164.setFont(font20)
        self.label_164.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_61.addWidget(self.frame_90)


        self.verticalLayout_25.addWidget(self.frame_57)


        self.horizontalLayout_16.addWidget(self.frame_56)

        self.frame_140 = QFrame(self.frame_scrollKYD)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_140)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.frame_141 = QFrame(self.frame_140)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_141)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.frame_142 = QFrame(self.frame_141)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_142)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.frame_143 = QFrame(self.frame_142)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMinimumSize(QSize(0, 35))
        self.frame_143.setMaximumSize(QSize(16777215, 35))
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_143)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(15, 15, 15, 0)
        self.progressBar_6 = QProgressBar(self.frame_143)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setMaximumSize(QSize(16777215, 10))
        self.progressBar_6.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.232955 rgba(89, 242, 124, 255), stop:0.255682 rgba(90, 172, 252, 255), stop:0.715909 rgba(90, 173, 253, 255), stop:0.732955 rgba(218, 66, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_6.setValue(100)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setInvertedAppearance(True)

        self.verticalLayout_115.addWidget(self.progressBar_6)


        self.verticalLayout_114.addWidget(self.frame_143)

        self.frame_144 = QFrame(self.frame_142)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(10, 0, 30, 0)
        self.frame_145 = QFrame(self.frame_144)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setMinimumSize(QSize(120, 60))
        self.frame_145.setMaximumSize(QSize(120, 60))
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_145)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, -1)
        self.label_135 = QLabel(self.frame_145)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font5)
        self.label_135.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_135.setAlignment(Qt.AlignCenter)

        self.verticalLayout_116.addWidget(self.label_135)

        self.label_136 = QLabel(self.frame_145)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_136.setAlignment(Qt.AlignCenter)

        self.verticalLayout_116.addWidget(self.label_136)


        self.horizontalLayout_25.addWidget(self.frame_145)

        self.horizontalSpacer_32 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_32)

        self.frame_146 = QFrame(self.frame_144)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(200, 0))
        self.frame_146.setMaximumSize(QSize(200, 16777215))
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_146)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, -1)
        self.label_137 = QLabel(self.frame_146)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setFont(font5)
        self.label_137.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_137.setAlignment(Qt.AlignCenter)

        self.verticalLayout_117.addWidget(self.label_137)

        self.label_138 = QLabel(self.frame_146)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_138.setAlignment(Qt.AlignCenter)

        self.verticalLayout_117.addWidget(self.label_138)


        self.horizontalLayout_25.addWidget(self.frame_146)

        self.horizontalSpacer_33 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_33)

        self.frame_147 = QFrame(self.frame_144)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMinimumSize(QSize(157, 0))
        self.frame_147.setMaximumSize(QSize(157, 16777215))
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_147)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, -1)
        self.label_139 = QLabel(self.frame_147)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setFont(font5)
        self.label_139.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.verticalLayout_118.addWidget(self.label_139)

        self.label_140 = QLabel(self.frame_147)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_140.setAlignment(Qt.AlignCenter)

        self.verticalLayout_118.addWidget(self.label_140)


        self.horizontalLayout_25.addWidget(self.frame_147)


        self.verticalLayout_114.addWidget(self.frame_144)


        self.verticalLayout_113.addWidget(self.frame_142)

        self.frame_148 = QFrame(self.frame_141)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_148)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.frame_149 = QFrame(self.frame_148)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(15, 10, 19, 0)
        self.site_7 = QLabel(self.frame_149)
        self.site_7.setObjectName(u"site_7")
        self.site_7.setFont(font8)
        self.site_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.site_7)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_18)

        self.DC_LEdit = QLineEdit(self.frame_149)
        self.DC_LEdit.setObjectName(u"DC_LEdit")
        self.DC_LEdit.setMinimumSize(QSize(250, 25))
        self.DC_LEdit.setMaximumSize(QSize(250, 25))
        self.DC_LEdit.setFont(font14)
        self.DC_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.DC_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.DC_LEdit)

        self.label_142 = QLabel(self.frame_149)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(36, 20))
        self.label_142.setMaximumSize(QSize(38, 20))
        self.label_142.setFont(font15)
        self.label_142.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_142.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_142)


        self.verticalLayout_119.addWidget(self.frame_149)

        self.frame_150 = QFrame(self.frame_148)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(15, -1, 20, 8)
        self.font_6 = QLabel(self.frame_150)
        self.font_6.setObjectName(u"font_6")
        self.font_6.setFont(font8)
        self.font_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_54.addWidget(self.font_6)

        self.horizontalSpacer_19 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_19)

        self.DC_aoa_LEdit = QLineEdit(self.frame_150)
        self.DC_aoa_LEdit.setObjectName(u"DC_aoa_LEdit")
        self.DC_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.DC_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.DC_aoa_LEdit.setFont(font14)
        self.DC_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.DC_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_54.addWidget(self.DC_aoa_LEdit)

        self.label_144 = QLabel(self.frame_150)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(40, 20))
        self.label_144.setMaximumSize(QSize(40, 20))
        self.label_144.setFont(font15)
        self.label_144.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_144.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_54.addWidget(self.label_144)


        self.verticalLayout_119.addWidget(self.frame_150)


        self.verticalLayout_113.addWidget(self.frame_148)


        self.verticalLayout_112.addWidget(self.frame_141)


        self.horizontalLayout_16.addWidget(self.frame_140)


        self.verticalLayout_19.addWidget(self.frame_scrollKYD)

        self.frame_scrollGBP = QFrame(self.frame_41)
        self.frame_scrollGBP.setObjectName(u"frame_scrollGBP")
        self.frame_scrollGBP.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollGBP.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollGBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_scrollGBP)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_scrollGBP)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(300, 0))
        self.frame_53.setMaximumSize(QSize(300, 16777215))
        self.frame_53.setStyleSheet(u"")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_53)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(8, 8, 8, 8)
        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_54)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_87 = QFrame(self.frame_54)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(0, 40))
        self.frame_87.setMaximumSize(QSize(16777215, 40))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.label_51 = QLabel(self.frame_87)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(43, 10, 190, 16))
        self.label_51.setFont(font8)
        self.label_51.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_157 = QLabel(self.frame_87)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setGeometry(QRect(0, 0, 40, 41))
        self.label_157.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_158 = QLabel(self.frame_87)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setGeometry(QRect(15, 8, 10, 20))
        self.label_158.setFont(font15)
        self.label_158.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_60.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.frame_54)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.label_53 = QLabel(self.frame_88)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 5, 20, 40))
        self.label_53.setFont(font13)
        self.label_53.setStyleSheet(u"color: #FFF0F03F;")
        self.label_54 = QLabel(self.frame_88)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(21, 100, 160, 15))
        self.label_54.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_56 = QLabel(self.frame_88)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(20, 67, 210, 30))
        self.label_56.setFont(font14)
        self.label_56.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_43 = QLabel(self.frame_88)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(30, 6, 50, 41))
        self.label_43.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.label_161 = QLabel(self.frame_88)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(48, 13, 10, 20))
        self.label_161.setFont(font20)
        self.label_161.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_60.addWidget(self.frame_88)


        self.verticalLayout_26.addWidget(self.frame_54)


        self.horizontalLayout_15.addWidget(self.frame_53)

        self.frame_124 = QFrame(self.frame_scrollGBP)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_124)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.frame_125 = QFrame(self.frame_124)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_125)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_126)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.frame_127 = QFrame(self.frame_126)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setMinimumSize(QSize(0, 35))
        self.frame_127.setMaximumSize(QSize(16777215, 35))
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_127)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(15, 15, 15, 0)
        self.progressBar_7 = QProgressBar(self.frame_127)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setMaximumSize(QSize(16777215, 10))
        self.progressBar_7.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.215909 rgba(89, 242, 124, 255), stop:0.238636 rgba(90, 172, 252, 255), stop:0.670455 rgba(90, 173, 253, 255), stop:0.693182 rgba(218, 66, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_7.setValue(100)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setInvertedAppearance(True)

        self.verticalLayout_99.addWidget(self.progressBar_7)


        self.verticalLayout_98.addWidget(self.frame_127)

        self.frame_128 = QFrame(self.frame_126)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(10, 0, 30, 0)
        self.frame_129 = QFrame(self.frame_128)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMinimumSize(QSize(120, 60))
        self.frame_129.setMaximumSize(QSize(120, 60))
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_129)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, -1)
        self.label_115 = QLabel(self.frame_129)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font5)
        self.label_115.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_115.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_100.addWidget(self.label_115)

        self.label_116 = QLabel(self.frame_129)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_116.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.label_116)


        self.horizontalLayout_26.addWidget(self.frame_129)

        self.horizontalSpacer_34 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_34)

        self.frame_130 = QFrame(self.frame_128)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(200, 0))
        self.frame_130.setMaximumSize(QSize(200, 16777215))
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_130)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, -1)
        self.label_117 = QLabel(self.frame_130)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(175, 0))
        self.label_117.setFont(font5)
        self.label_117.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_117.setAlignment(Qt.AlignCenter)

        self.verticalLayout_101.addWidget(self.label_117)

        self.label_118 = QLabel(self.frame_130)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_118.setAlignment(Qt.AlignCenter)

        self.verticalLayout_101.addWidget(self.label_118)


        self.horizontalLayout_26.addWidget(self.frame_130)

        self.horizontalSpacer_35 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_35)

        self.frame_131 = QFrame(self.frame_128)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setMinimumSize(QSize(157, 0))
        self.frame_131.setMaximumSize(QSize(157, 16777215))
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_131)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, -1)
        self.label_119 = QLabel(self.frame_131)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font5)
        self.label_119.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.label_119)

        self.label_120 = QLabel(self.frame_131)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_120.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.label_120)


        self.horizontalLayout_26.addWidget(self.frame_131)


        self.verticalLayout_98.addWidget(self.frame_128)


        self.verticalLayout_97.addWidget(self.frame_126)

        self.frame_132 = QFrame(self.frame_125)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_132)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.frame_133 = QFrame(self.frame_132)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(15, 10, 18, 0)
        self.site_8 = QLabel(self.frame_133)
        self.site_8.setObjectName(u"site_8")
        self.site_8.setFont(font8)
        self.site_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.site_8)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_14)

        self.LE_LEdit = QLineEdit(self.frame_133)
        self.LE_LEdit.setObjectName(u"LE_LEdit")
        self.LE_LEdit.setMinimumSize(QSize(250, 25))
        self.LE_LEdit.setMaximumSize(QSize(250, 25))
        self.LE_LEdit.setFont(font14)
        self.LE_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.LE_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.LE_LEdit)

        self.label_122 = QLabel(self.frame_133)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(40, 20))
        self.label_122.setMaximumSize(QSize(36, 20))
        self.label_122.setFont(font15)
        self.label_122.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_122.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.label_122)


        self.verticalLayout_103.addWidget(self.frame_133)

        self.frame_134 = QFrame(self.frame_132)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_134)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(15, -1, 20, 7)
        self.lfont = QLabel(self.frame_134)
        self.lfont.setObjectName(u"lfont")
        self.lfont.setFont(font8)
        self.lfont.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lfont.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.lfont)

        self.horizontalSpacer_15 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_15)

        self.LE_aoa_LEdit = QLineEdit(self.frame_134)
        self.LE_aoa_LEdit.setObjectName(u"LE_aoa_LEdit")
        self.LE_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.LE_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.LE_aoa_LEdit.setFont(font14)
        self.LE_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.LE_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.LE_aoa_LEdit)

        self.label_124 = QLabel(self.frame_134)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(40, 20))
        self.label_124.setMaximumSize(QSize(40, 20))
        self.label_124.setFont(font15)
        self.label_124.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_124.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.label_124)


        self.verticalLayout_103.addWidget(self.frame_134)


        self.verticalLayout_97.addWidget(self.frame_132)


        self.verticalLayout_96.addWidget(self.frame_125)


        self.horizontalLayout_15.addWidget(self.frame_124)


        self.verticalLayout_19.addWidget(self.frame_scrollGBP)

        self.frame_scrollEUR = QFrame(self.frame_41)
        self.frame_scrollEUR.setObjectName(u"frame_scrollEUR")
        self.frame_scrollEUR.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollEUR.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollEUR.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_scrollEUR)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_59 = QFrame(self.frame_scrollEUR)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(300, 0))
        self.frame_59.setMaximumSize(QSize(300, 16777215))
        self.frame_59.setStyleSheet(u"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_59)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(8, 8, 8, 8)
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_60)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_91 = QFrame(self.frame_60)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 40))
        self.frame_91.setMaximumSize(QSize(16777215, 40))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.label_63 = QLabel(self.frame_91)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(43, 10, 141, 16))
        self.label_63.setFont(font8)
        self.label_63.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_165 = QLabel(self.frame_91)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(0, 0, 40, 41))
        self.label_165.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_166 = QLabel(self.frame_91)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(13, 10, 10, 20))
        self.label_166.setFont(font15)
        self.label_166.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_62.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.frame_60)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.label_65 = QLabel(self.frame_92)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(10, 5, 20, 40))
        self.label_65.setFont(font13)
        self.label_65.setStyleSheet(u"color: #FFF0F03F;")
        self.label_66 = QLabel(self.frame_92)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(21, 100, 160, 15))
        self.label_66.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_68 = QLabel(self.frame_92)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(20, 67, 210, 30))
        self.label_68.setFont(font14)
        self.label_68.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_49 = QLabel(self.frame_92)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(30, 6, 50, 41))
        self.label_49.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.label_167 = QLabel(self.frame_92)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(47, 14, 10, 20))
        self.label_167.setFont(font20)
        self.label_167.setStyleSheet(u"color: rgb(240, 240, 63);")

        self.verticalLayout_62.addWidget(self.frame_92)


        self.verticalLayout_29.addWidget(self.frame_60)


        self.horizontalLayout_17.addWidget(self.frame_59)

        self.frame_79 = QFrame(self.frame_scrollEUR)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_79)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.frame_79)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_61)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.frame_64 = QFrame(self.frame_61)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_64)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.frame_80 = QFrame(self.frame_64)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(0, 35))
        self.frame_80.setMaximumSize(QSize(16777215, 35))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_80)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(15, 15, 15, 0)
        self.progressBar_8 = QProgressBar(self.frame_80)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setMaximumSize(QSize(16777215, 10))
        self.progressBar_8.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.176136 rgba(89, 242, 124, 255), stop:0.221591 rgba(90, 172, 252, 255), stop:0.642045 rgba(90, 173, 253, 255), stop:0.664773 rgba(218, 66, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_8.setValue(100)
        self.progressBar_8.setTextVisible(False)
        self.progressBar_8.setInvertedAppearance(True)

        self.verticalLayout_107.addWidget(self.progressBar_8)


        self.verticalLayout_106.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_64)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, 0, 30, 0)
        self.frame_82 = QFrame(self.frame_81)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(120, 60))
        self.frame_82.setMaximumSize(QSize(120, 60))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_82)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, -1)
        self.label_125 = QLabel(self.frame_82)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font5)
        self.label_125.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_125.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_108.addWidget(self.label_125)

        self.label_126 = QLabel(self.frame_82)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.verticalLayout_108.addWidget(self.label_126)


        self.horizontalLayout_27.addWidget(self.frame_82)

        self.horizontalSpacer_36 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_36)

        self.frame_135 = QFrame(self.frame_81)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(200, 0))
        self.frame_135.setMaximumSize(QSize(200, 16777215))
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_135)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, -1)
        self.label_127 = QLabel(self.frame_135)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(175, 0))
        self.label_127.setFont(font5)
        self.label_127.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.verticalLayout_109.addWidget(self.label_127)

        self.label_128 = QLabel(self.frame_135)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_128.setAlignment(Qt.AlignCenter)

        self.verticalLayout_109.addWidget(self.label_128)


        self.horizontalLayout_27.addWidget(self.frame_135)

        self.horizontalSpacer_37 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_37)

        self.frame_136 = QFrame(self.frame_81)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMinimumSize(QSize(157, 0))
        self.frame_136.setMaximumSize(QSize(157, 16777215))
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_136)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, -1)
        self.label_129 = QLabel(self.frame_136)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font5)
        self.label_129.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.verticalLayout_110.addWidget(self.label_129)

        self.label_130 = QLabel(self.frame_136)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.verticalLayout_110.addWidget(self.label_130)


        self.horizontalLayout_27.addWidget(self.frame_136)


        self.verticalLayout_106.addWidget(self.frame_81)


        self.verticalLayout_105.addWidget(self.frame_64)

        self.frame_137 = QFrame(self.frame_61)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_137)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.frame_138 = QFrame(self.frame_137)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(15, 10, 22, 8)
        self.site_9 = QLabel(self.frame_138)
        self.site_9.setObjectName(u"site_9")
        self.site_9.setFont(font8)
        self.site_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.site_9)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_16)

        self.E_LEdit = QLineEdit(self.frame_138)
        self.E_LEdit.setObjectName(u"E_LEdit")
        self.E_LEdit.setMinimumSize(QSize(250, 25))
        self.E_LEdit.setMaximumSize(QSize(250, 25))
        self.E_LEdit.setFont(font14)
        self.E_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.E_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.E_LEdit)

        self.label_132 = QLabel(self.frame_138)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(36, 20))
        self.label_132.setMaximumSize(QSize(36, 20))
        self.label_132.setFont(font15)
        self.label_132.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_132.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.label_132)


        self.verticalLayout_111.addWidget(self.frame_138)

        self.frame_139 = QFrame(self.frame_137)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(15, -1, 20, 8)
        self.font_7 = QLabel(self.frame_139)
        self.font_7.setObjectName(u"font_7")
        self.font_7.setFont(font8)
        self.font_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.font_7)

        self.horizontalSpacer_17 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_17)

        self.E_aoa_LEdit = QLineEdit(self.frame_139)
        self.E_aoa_LEdit.setObjectName(u"E_aoa_LEdit")
        self.E_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.E_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.E_aoa_LEdit.setFont(font14)
        self.E_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.E_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.E_aoa_LEdit)

        self.label_134 = QLabel(self.frame_139)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(40, 20))
        self.label_134.setMaximumSize(QSize(40, 20))
        self.label_134.setFont(font15)
        self.label_134.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_134.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.label_134)


        self.verticalLayout_111.addWidget(self.frame_139)


        self.verticalLayout_105.addWidget(self.frame_137)


        self.verticalLayout_104.addWidget(self.frame_61)


        self.horizontalLayout_17.addWidget(self.frame_79)


        self.verticalLayout_19.addWidget(self.frame_scrollEUR)

        self.frame_scrollCHF = QFrame(self.frame_41)
        self.frame_scrollCHF.setObjectName(u"frame_scrollCHF")
        self.frame_scrollCHF.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollCHF.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollCHF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_scrollCHF)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.frame_scrollCHF)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(300, 0))
        self.frame_62.setMaximumSize(QSize(300, 16777215))
        self.frame_62.setStyleSheet(u"")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_62)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(8, 8, 8, 8)
        self.frame_63 = QFrame(self.frame_62)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_63)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_93 = QFrame(self.frame_63)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(0, 40))
        self.frame_93.setMaximumSize(QSize(16777215, 40))
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.label_69 = QLabel(self.frame_93)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(43, 10, 220, 16))
        self.label_69.setFont(font8)
        self.label_69.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_168 = QLabel(self.frame_93)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(14, 8, 10, 20))
        self.label_168.setFont(font15)
        self.label_168.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_169 = QLabel(self.frame_93)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(0, 0, 40, 41))
        self.label_169.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_169.raise_()
        self.label_69.raise_()
        self.label_168.raise_()

        self.verticalLayout_63.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.frame_63)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.label_71 = QLabel(self.frame_94)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(10, 5, 20, 40))
        self.label_71.setFont(font13)
        self.label_71.setStyleSheet(u"color: #FFF0F03F;")
        self.label_72 = QLabel(self.frame_94)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(21, 100, 160, 15))
        self.label_72.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_74 = QLabel(self.frame_94)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(20, 67, 210, 30))
        self.label_74.setFont(font14)
        self.label_74.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_170 = QLabel(self.frame_94)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(50, 14, 10, 20))
        self.label_170.setFont(font20)
        self.label_170.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_52 = QLabel(self.frame_94)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(30, 6, 50, 41))
        self.label_52.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.label_52.raise_()
        self.label_71.raise_()
        self.label_72.raise_()
        self.label_74.raise_()
        self.label_170.raise_()

        self.verticalLayout_63.addWidget(self.frame_94)


        self.verticalLayout_31.addWidget(self.frame_63)


        self.horizontalLayout_18.addWidget(self.frame_62)

        self.frame_151 = QFrame(self.frame_scrollCHF)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_151)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.frame_152 = QFrame(self.frame_151)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_152)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.frame_153 = QFrame(self.frame_152)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_153)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.frame_154 = QFrame(self.frame_153)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setMinimumSize(QSize(0, 35))
        self.frame_154.setMaximumSize(QSize(16777215, 35))
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_154)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(15, 15, 15, 0)
        self.progressBar_9 = QProgressBar(self.frame_154)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setMaximumSize(QSize(16777215, 10))
        self.progressBar_9.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.158301 rgba(89, 242, 124, 255), stop:0.202703 rgba(90, 172, 252, 255), stop:0.6139 rgba(90, 173, 253, 255), stop:0.635135 rgba(218, 66, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_9.setValue(100)
        self.progressBar_9.setTextVisible(False)
        self.progressBar_9.setInvertedAppearance(True)

        self.verticalLayout_123.addWidget(self.progressBar_9)


        self.verticalLayout_122.addWidget(self.frame_154)

        self.frame_155 = QFrame(self.frame_153)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(10, 0, 30, 0)
        self.frame_156 = QFrame(self.frame_155)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMinimumSize(QSize(120, 60))
        self.frame_156.setMaximumSize(QSize(120, 60))
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_156)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, -1)
        self.label_145 = QLabel(self.frame_156)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setFont(font5)
        self.label_145.setStyleSheet(u"color: rgb(89, 242, 124);")
        self.label_145.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_124.addWidget(self.label_145)

        self.label_146 = QLabel(self.frame_156)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_146.setAlignment(Qt.AlignCenter)

        self.verticalLayout_124.addWidget(self.label_146)


        self.horizontalLayout_28.addWidget(self.frame_156)

        self.horizontalSpacer_38 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_38)

        self.frame_157 = QFrame(self.frame_155)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setMinimumSize(QSize(200, 0))
        self.frame_157.setMaximumSize(QSize(200, 16777215))
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.frame_157)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, -1)
        self.label_147 = QLabel(self.frame_157)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setFont(font5)
        self.label_147.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_147.setAlignment(Qt.AlignCenter)

        self.verticalLayout_125.addWidget(self.label_147)

        self.label_148 = QLabel(self.frame_157)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_148.setAlignment(Qt.AlignCenter)

        self.verticalLayout_125.addWidget(self.label_148)


        self.horizontalLayout_28.addWidget(self.frame_157)

        self.horizontalSpacer_39 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_39)

        self.frame_158 = QFrame(self.frame_155)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(157, 0))
        self.frame_158.setMaximumSize(QSize(157, 16777215))
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.frame_158)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, -1)
        self.label_149 = QLabel(self.frame_158)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setFont(font5)
        self.label_149.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_149.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_149)

        self.label_150 = QLabel(self.frame_158)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_150.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_150)


        self.horizontalLayout_28.addWidget(self.frame_158)


        self.verticalLayout_122.addWidget(self.frame_155)


        self.verticalLayout_121.addWidget(self.frame_153)

        self.frame_159 = QFrame(self.frame_152)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_159)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.frame_160 = QFrame(self.frame_159)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(15, 10, 20, 0)
        self.site_10 = QLabel(self.frame_160)
        self.site_10.setObjectName(u"site_10")
        self.site_10.setFont(font8)
        self.site_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_56.addWidget(self.site_10)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_20)

        self.FS_LEdit = QLineEdit(self.frame_160)
        self.FS_LEdit.setObjectName(u"FS_LEdit")
        self.FS_LEdit.setMinimumSize(QSize(250, 25))
        self.FS_LEdit.setMaximumSize(QSize(250, 25))
        self.FS_LEdit.setFont(font14)
        self.FS_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.FS_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_56.addWidget(self.FS_LEdit)

        self.label_152 = QLabel(self.frame_160)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMinimumSize(QSize(40, 20))
        self.label_152.setMaximumSize(QSize(40, 20))
        self.label_152.setFont(font15)
        self.label_152.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_152.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_56.addWidget(self.label_152)


        self.verticalLayout_127.addWidget(self.frame_160)

        self.frame_161 = QFrame(self.frame_159)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(15, -1, 20, 10)
        self.font_8 = QLabel(self.frame_161)
        self.font_8.setObjectName(u"font_8")
        self.font_8.setFont(font8)
        self.font_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.font_8)

        self.horizontalSpacer_21 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_21)

        self.FS_aoa_LEdit = QLineEdit(self.frame_161)
        self.FS_aoa_LEdit.setObjectName(u"FS_aoa_LEdit")
        self.FS_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.FS_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.FS_aoa_LEdit.setFont(font14)
        self.FS_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.FS_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.FS_aoa_LEdit)

        self.label_154 = QLabel(self.frame_161)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMinimumSize(QSize(40, 20))
        self.label_154.setMaximumSize(QSize(40, 20))
        self.label_154.setFont(font15)
        self.label_154.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_154.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.label_154)


        self.verticalLayout_127.addWidget(self.frame_161)


        self.verticalLayout_121.addWidget(self.frame_159)


        self.verticalLayout_120.addWidget(self.frame_152)


        self.horizontalLayout_18.addWidget(self.frame_151)


        self.verticalLayout_19.addWidget(self.frame_scrollCHF)

        self.frame_scrollUSD = QFrame(self.frame_41)
        self.frame_scrollUSD.setObjectName(u"frame_scrollUSD")
        self.frame_scrollUSD.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_scrollUSD.setFrameShape(QFrame.StyledPanel)
        self.frame_scrollUSD.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_scrollUSD)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.frame_scrollUSD)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(300, 0))
        self.frame_70.setMaximumSize(QSize(300, 16777215))
        self.frame_70.setStyleSheet(u"")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_70)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(8, 8, 8, 8)
        self.frame_95 = QFrame(self.frame_70)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_95)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(0, 40))
        self.frame_96.setMaximumSize(QSize(16777215, 40))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.label_70 = QLabel(self.frame_96)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(40, 10, 240, 16))
        self.label_70.setFont(font8)
        self.label_70.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_171 = QLabel(self.frame_96)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setGeometry(QRect(14, 8, 10, 20))
        self.label_171.setFont(font15)
        self.label_171.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_172 = QLabel(self.frame_96)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setGeometry(QRect(0, 0, 40, 41))
        self.label_172.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/synchronize_40px.png"))
        self.label_172.raise_()
        self.label_70.raise_()
        self.label_171.raise_()

        self.verticalLayout_64.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.frame_95)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setStyleSheet(u"background-color: rgb(85, 42, 127);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.label_73 = QLabel(self.frame_97)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(10, 5, 20, 40))
        self.label_73.setFont(font13)
        self.label_73.setStyleSheet(u"color: #FFF0F03F;")
        self.label_76 = QLabel(self.frame_97)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(21, 100, 160, 15))
        self.label_76.setStyleSheet(u"color: rgb(182, 182, 182)")
        self.label_156 = QLabel(self.frame_97)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setGeometry(QRect(20, 67, 210, 30))
        self.label_156.setFont(font14)
        self.label_156.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_173 = QLabel(self.frame_97)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setGeometry(QRect(48, 14, 16, 20))
        self.label_173.setFont(font20)
        self.label_173.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_55 = QLabel(self.frame_97)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(30, 6, 50, 41))
        self.label_55.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/round_50px.png"))
        self.label_55.raise_()
        self.label_73.raise_()
        self.label_76.raise_()
        self.label_156.raise_()
        self.label_173.raise_()

        self.verticalLayout_64.addWidget(self.frame_97)


        self.verticalLayout_40.addWidget(self.frame_95)


        self.horizontalLayout_22.addWidget(self.frame_70)

        self.frame_162 = QFrame(self.frame_scrollUSD)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_162)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.frame_163 = QFrame(self.frame_162)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.frame_163)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.frame_164 = QFrame(self.frame_163)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.frame_164)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.frame_165 = QFrame(self.frame_164)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setMinimumSize(QSize(0, 35))
        self.frame_165.setMaximumSize(QSize(16777215, 35))
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_165)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(15, 15, 15, 0)
        self.progressBar_10 = QProgressBar(self.frame_165)
        self.progressBar_10.setObjectName(u"progressBar_10")
        self.progressBar_10.setMaximumSize(QSize(16777215, 10))
        self.progressBar_10.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(90, 172, 252, 255), stop:0.551136 rgba(90, 173, 253, 255), stop:0.579545 rgba(218, 66, 0, 255));\n"
"border-radius:5px;}\n"
"\n"
"QProgressBar{\n"
"border-radius:5px;\n"
"}")
        self.progressBar_10.setValue(100)
        self.progressBar_10.setTextVisible(False)
        self.progressBar_10.setInvertedAppearance(True)

        self.verticalLayout_131.addWidget(self.progressBar_10)


        self.verticalLayout_130.addWidget(self.frame_165)

        self.frame_166 = QFrame(self.frame_164)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_166)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, -1, 6)
        self.frame_168 = QFrame(self.frame_166)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_168)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, -1)
        self.label_176 = QLabel(self.frame_168)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setFont(font5)
        self.label_176.setStyleSheet(u"color: rgb(90, 173, 253);")
        self.label_176.setAlignment(Qt.AlignCenter)

        self.verticalLayout_133.addWidget(self.label_176)

        self.label_177 = QLabel(self.frame_168)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_177.setAlignment(Qt.AlignCenter)

        self.verticalLayout_133.addWidget(self.label_177)


        self.horizontalLayout_58.addWidget(self.frame_168)

        self.frame_169 = QFrame(self.frame_166)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.frame_169)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, -1)
        self.label_178 = QLabel(self.frame_169)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setFont(font5)
        self.label_178.setStyleSheet(u"color: rgb(239, 73, 0);")
        self.label_178.setAlignment(Qt.AlignCenter)

        self.verticalLayout_134.addWidget(self.label_178)

        self.label_179 = QLabel(self.frame_169)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.label_179.setAlignment(Qt.AlignCenter)

        self.verticalLayout_134.addWidget(self.label_179)


        self.horizontalLayout_58.addWidget(self.frame_169)


        self.verticalLayout_130.addWidget(self.frame_166)


        self.verticalLayout_129.addWidget(self.frame_164)

        self.frame_170 = QFrame(self.frame_163)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_170)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.frame_171 = QFrame(self.frame_170)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(15, 10, 24, 0)
        self.site_11 = QLabel(self.frame_171)
        self.site_11.setObjectName(u"site_11")
        self.site_11.setFont(font8)
        self.site_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.site_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_59.addWidget(self.site_11)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_26)

        self.DNA_LEdit = QLineEdit(self.frame_171)
        self.DNA_LEdit.setObjectName(u"DNA_LEdit")
        self.DNA_LEdit.setMinimumSize(QSize(250, 25))
        self.DNA_LEdit.setMaximumSize(QSize(250, 25))
        self.DNA_LEdit.setFont(font14)
        self.DNA_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253)\n"
"}")
        self.DNA_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_59.addWidget(self.DNA_LEdit)

        self.label_181 = QLabel(self.frame_171)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setMinimumSize(QSize(40, 20))
        self.label_181.setMaximumSize(QSize(40, 20))
        self.label_181.setFont(font15)
        self.label_181.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_181.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_59.addWidget(self.label_181)


        self.verticalLayout_135.addWidget(self.frame_171)

        self.frame_172 = QFrame(self.frame_170)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_172)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(15, -1, 20, 10)
        self.font_9 = QLabel(self.frame_172)
        self.font_9.setObjectName(u"font_9")
        self.font_9.setFont(font8)
        self.font_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.font_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_60.addWidget(self.font_9)

        self.horizontalSpacer_27 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_27)

        self.DNA_aoa_LEdit = QLineEdit(self.frame_172)
        self.DNA_aoa_LEdit.setObjectName(u"DNA_aoa_LEdit")
        self.DNA_aoa_LEdit.setMinimumSize(QSize(250, 25))
        self.DNA_aoa_LEdit.setMaximumSize(QSize(250, 25))
        self.DNA_aoa_LEdit.setFont(font14)
        self.DNA_aoa_LEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(240, 240, 63);\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid  rgb(153, 76, 229);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(90, 173, 253);\n"
"}")
        self.DNA_aoa_LEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_60.addWidget(self.DNA_aoa_LEdit)

        self.label_183 = QLabel(self.frame_172)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setMinimumSize(QSize(40, 20))
        self.label_183.setMaximumSize(QSize(40, 20))
        self.label_183.setFont(font15)
        self.label_183.setStyleSheet(u"color: rgb(240, 240, 63);")
        self.label_183.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_60.addWidget(self.label_183)


        self.verticalLayout_135.addWidget(self.frame_172)


        self.verticalLayout_129.addWidget(self.frame_170)


        self.verticalLayout_128.addWidget(self.frame_163)


        self.horizontalLayout_22.addWidget(self.frame_162)


        self.verticalLayout_19.addWidget(self.frame_scrollUSD)


        self.verticalLayout_18.addWidget(self.frame_41)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_Coins_2)

        self.verticalLayout_15.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.page_CoinsQuote)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.central_frame)

        self.frame_MarcaTech = QFrame(self.frame_centaralCentral)
        self.frame_MarcaTech.setObjectName(u"frame_MarcaTech")
        self.frame_MarcaTech.setMinimumSize(QSize(0, 170))
        self.frame_MarcaTech.setMaximumSize(QSize(16777215, 16777215))
        self.frame_MarcaTech.setStyleSheet(u"background-color: rgb(159, 80, 239);\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.frame_MarcaTech.setFrameShape(QFrame.StyledPanel)
        self.frame_MarcaTech.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_MarcaTech)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 0, 2, 0)
        self.scrollArea = QScrollArea(self.frame_MarcaTech)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 120))
        self.scrollArea.setMaximumSize(QSize(16777215, 100))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-362, 0, 1490, 119))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius:15px;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 9)
        self.frame_GoogleFinance = QFrame(self.scrollAreaWidgetContents)
        self.frame_GoogleFinance.setObjectName(u"frame_GoogleFinance")
        self.frame_GoogleFinance.setMinimumSize(QSize(160, 110))
        self.frame_GoogleFinance.setMaximumSize(QSize(90, 101))
        self.frame_GoogleFinance.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"")
        self.frame_GoogleFinance.setFrameShape(QFrame.StyledPanel)
        self.frame_GoogleFinance.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_GoogleFinance)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.GoogleFinance_btl = QPushButton(self.frame_GoogleFinance)
        self.GoogleFinance_btl.setObjectName(u"GoogleFinance_btl")
        icon27 = QIcon()
        icon27.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/fina.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GoogleFinance_btl.setIcon(icon27)
        self.GoogleFinance_btl.setIconSize(QSize(153, 130))

        self.verticalLayout_13.addWidget(self.GoogleFinance_btl)


        self.horizontalLayout.addWidget(self.frame_GoogleFinance)

        self.frame_YahooFinance = QFrame(self.scrollAreaWidgetContents)
        self.frame_YahooFinance.setObjectName(u"frame_YahooFinance")
        self.frame_YahooFinance.setMinimumSize(QSize(160, 110))
        self.frame_YahooFinance.setMaximumSize(QSize(90, 101))
        self.frame_YahooFinance.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"\n"
"")
        self.frame_YahooFinance.setFrameShape(QFrame.StyledPanel)
        self.frame_YahooFinance.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_YahooFinance)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.YahooFinance_btn = QPushButton(self.frame_YahooFinance)
        self.YahooFinance_btn.setObjectName(u"YahooFinance_btn")
        icon28 = QIcon()
        icon28.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/yahoo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.YahooFinance_btn.setIcon(icon28)
        self.YahooFinance_btn.setIconSize(QSize(136, 111))

        self.verticalLayout_70.addWidget(self.YahooFinance_btn)


        self.horizontalLayout.addWidget(self.frame_YahooFinance)

        self.frame_Investing = QFrame(self.scrollAreaWidgetContents)
        self.frame_Investing.setObjectName(u"frame_Investing")
        self.frame_Investing.setMinimumSize(QSize(160, 110))
        self.frame_Investing.setMaximumSize(QSize(90, 101))
        self.frame_Investing.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_Investing.setFrameShape(QFrame.StyledPanel)
        self.frame_Investing.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.frame_Investing)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.Investing_btn = QPushButton(self.frame_Investing)
        self.Investing_btn.setObjectName(u"Investing_btn")
        icon29 = QIcon()
        icon29.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/investing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Investing_btn.setIcon(icon29)
        self.Investing_btn.setIconSize(QSize(152, 114))

        self.verticalLayout_132.addWidget(self.Investing_btn)


        self.horizontalLayout.addWidget(self.frame_Investing)

        self.frame_BLHL = QFrame(self.scrollAreaWidgetContents)
        self.frame_BLHL.setObjectName(u"frame_BLHL")
        self.frame_BLHL.setMinimumSize(QSize(160, 110))
        self.frame_BLHL.setMaximumSize(QSize(90, 101))
        self.frame_BLHL.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_BLHL.setFrameShape(QFrame.StyledPanel)
        self.frame_BLHL.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_BLHL)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.BLHL_btn = QPushButton(self.frame_BLHL)
        self.BLHL_btn.setObjectName(u"BLHL_btn")
        icon30 = QIcon()
        icon30.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/BLHL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BLHL_btn.setIcon(icon30)
        self.BLHL_btn.setIconSize(QSize(150, 105))

        self.verticalLayout_136.addWidget(self.BLHL_btn)


        self.horizontalLayout.addWidget(self.frame_BLHL)

        self.frame_Infomaney = QFrame(self.scrollAreaWidgetContents)
        self.frame_Infomaney.setObjectName(u"frame_Infomaney")
        self.frame_Infomaney.setMinimumSize(QSize(160, 110))
        self.frame_Infomaney.setMaximumSize(QSize(90, 101))
        self.frame_Infomaney.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_Infomaney.setFrameShape(QFrame.StyledPanel)
        self.frame_Infomaney.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.frame_Infomaney)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.Infomaney_btn = QPushButton(self.frame_Infomaney)
        self.Infomaney_btn.setObjectName(u"Infomaney_btn")
        icon31 = QIcon()
        icon31.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/infomaney.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Infomaney_btn.setIcon(icon31)
        self.Infomaney_btn.setIconSize(QSize(132, 81))

        self.verticalLayout_137.addWidget(self.Infomaney_btn)


        self.horizontalLayout.addWidget(self.frame_Infomaney)

        self.frame_Dinherama = QFrame(self.scrollAreaWidgetContents)
        self.frame_Dinherama.setObjectName(u"frame_Dinherama")
        self.frame_Dinherama.setMinimumSize(QSize(160, 110))
        self.frame_Dinherama.setMaximumSize(QSize(90, 101))
        self.frame_Dinherama.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_Dinherama.setFrameShape(QFrame.StyledPanel)
        self.frame_Dinherama.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_Dinherama)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.Dinherama_btn = QPushButton(self.frame_Dinherama)
        self.Dinherama_btn.setObjectName(u"Dinherama_btn")
        icon32 = QIcon()
        icon32.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/dinherama.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dinherama_btn.setIcon(icon32)
        self.Dinherama_btn.setIconSize(QSize(153, 108))

        self.verticalLayout_138.addWidget(self.Dinherama_btn)


        self.horizontalLayout.addWidget(self.frame_Dinherama)

        self.frame_CMEgroup = QFrame(self.scrollAreaWidgetContents)
        self.frame_CMEgroup.setObjectName(u"frame_CMEgroup")
        self.frame_CMEgroup.setMinimumSize(QSize(160, 110))
        self.frame_CMEgroup.setMaximumSize(QSize(90, 101))
        self.frame_CMEgroup.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_CMEgroup.setFrameShape(QFrame.StyledPanel)
        self.frame_CMEgroup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_CMEgroup)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.CMEgroup_btn = QPushButton(self.frame_CMEgroup)
        self.CMEgroup_btn.setObjectName(u"CMEgroup_btn")
        icon33 = QIcon()
        icon33.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/cme.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CMEgroup_btn.setIcon(icon33)
        self.CMEgroup_btn.setIconSize(QSize(143, 123))

        self.verticalLayout_139.addWidget(self.CMEgroup_btn)


        self.horizontalLayout.addWidget(self.frame_CMEgroup)

        self.frame_Economia = QFrame(self.scrollAreaWidgetContents)
        self.frame_Economia.setObjectName(u"frame_Economia")
        self.frame_Economia.setMinimumSize(QSize(160, 110))
        self.frame_Economia.setMaximumSize(QSize(90, 101))
        self.frame_Economia.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_Economia.setFrameShape(QFrame.StyledPanel)
        self.frame_Economia.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_Economia)
        self.verticalLayout_140.setSpacing(0)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.Economia_btn = QPushButton(self.frame_Economia)
        self.Economia_btn.setObjectName(u"Economia_btn")
        icon34 = QIcon()
        icon34.addFile(u"../img/uol economia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Economia_btn.setIcon(icon34)
        self.Economia_btn.setIconSize(QSize(160, 100))

        self.verticalLayout_140.addWidget(self.Economia_btn)


        self.horizontalLayout.addWidget(self.frame_Economia)

        self.frame_Helpe = QFrame(self.scrollAreaWidgetContents)
        self.frame_Helpe.setObjectName(u"frame_Helpe")
        self.frame_Helpe.setMinimumSize(QSize(160, 110))
        self.frame_Helpe.setMaximumSize(QSize(90, 101))
        self.frame_Helpe.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_Helpe.setFrameShape(QFrame.StyledPanel)
        self.frame_Helpe.setFrameShadow(QFrame.Raised)
        self.help_lbl = QLabel(self.frame_Helpe)
        self.help_lbl.setObjectName(u"help_lbl")
        self.help_lbl.setGeometry(QRect(10, 70, 60, 20))
        self.help_lbl.setFont(font8)
        self.help_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.help_btnF_2 = QPushButton(self.frame_Helpe)
        self.help_btnF_2.setObjectName(u"help_btnF_2")
        self.help_btnF_2.setGeometry(QRect(10, 10, 40, 40))
        icon35 = QIcon()
        icon35.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/help_70px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btnF_2.setIcon(icon35)
        self.help_btnF_2.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.frame_Helpe)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_MarcaTech, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_centaralCentral)


        self.verticalLayout_3.addWidget(self.frame_central)


        self.verticalLayout_2.addWidget(self.linha)


        self.verticalLayout.addWidget(self.primeiro_container)

        MainWindowMW.setCentralWidget(self.centralwidget_styleSheet)

        self.retranslateUi(MainWindowMW)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindowMW)
    # setupUi

    def retranslateUi(self, MainWindowMW):
        MainWindowMW.setWindowTitle(QCoreApplication.translate("MainWindowMW", u"MainWindow", None))
        self.pushButton_5.setText("")
        self.NameEmp.setText(QCoreApplication.translate("MainWindowMW", u"Finacial Control", None))
#if QT_CONFIG(tooltip)
        self.minimisar.setToolTip(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p>Minimizar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.minimisar.setText(QCoreApplication.translate("MainWindowMW", u"...", None))
#if QT_CONFIG(tooltip)
        self.NormalMax.setToolTip(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p>Maximizar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.NormalMax.setText(QCoreApplication.translate("MainWindowMW", u"...", None))
#if QT_CONFIG(tooltip)
        self.fechar.setToolTip(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p>Fechar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fechar.setText(QCoreApplication.translate("MainWindowMW", u"...", None))
        self.Home.setText("")
        self.web_btn_2.setText("")
        self.conntrole_finace.setText("")
        self.settings.setText("")
        self.double_up.setText("")
        self.QRcode.setText("")
#if QT_CONFIG(whatsthis)
        self.data.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.data.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" color:#dcbbff;\">date: </span><span style=\" color:#ffffff;\">28/06/2022</span></p></body></html>", None))
        self.criadoPor.setText(QCoreApplication.translate("MainWindowMW", u"created by: NdDaniel", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindowMW", u"     Help", None))
        self.perfil_btn.setText(QCoreApplication.translate("MainWindowMW", u"     Perfil", None))
        self.web_btn.setText(QCoreApplication.translate("MainWindowMW", u"     Web", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindowMW", u"     Setting", None))
        self.coins_btn.setText(QCoreApplication.translate("MainWindowMW", u"   Coins Quote", None))
        self.setting_user_btn.setText(QCoreApplication.translate("MainWindowMW", u"     User settings", None))
        self.editTest.setText(QCoreApplication.translate("MainWindowMW", u"     Edit Text", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindowMW", u"...", None))
        self.logo_principal_2.setText("")
        self.pesquisar_btn.setText("")
        self.update.setText("")
        self.LineUrl.setInputMask("")
        self.LineUrl.setPlaceholderText(QCoreApplication.translate("MainWindowMW", u"Procurar no Google ou Introduza uma URL", None))
        self.voz_btn.setText("")
        self.arrow_left.setText("")
        self.arrow_right.setText("")
        self.plainTextEdit.setPlainText("")
        self.open.setText(QCoreApplication.translate("MainWindowMW", u"Open", None))
        self.save.setText(QCoreApplication.translate("MainWindowMW", u"Save", None))
#if QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; color:#aa55ff;\">Browsing history</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.frame_Browsin_history_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_Browsin_history_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.frame_opening_history_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_opening_history_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.frame_opening_history_lbl.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_opening_history_lbl.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; font-size:18pt; color:#aa55ff;\">Opening history</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.frame_user_list_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_user_list_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.frame_user_list_lbl.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_user_list_lbl.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; font-size:18pt; color:#aa55ff;\">User list</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.password_faceId_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.password_faceId_btn_2.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindowMW", u"123456789", None))
#if QT_CONFIG(whatsthis)
        self.password_faceId_lbl_6.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.password_faceId_lbl_6.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; font-size:18pt; color:#aa55ff;\">Password face id </span></p></body></html>", None))
        self.label_29.setText("")
#if QT_CONFIG(whatsthis)
        self.ios_lbl_2.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ios_lbl_2.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" color:#ffffff;\">IOS</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.ios_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ios_btn_2.setText("")
        self.iconWindow_4.setText("")
#if QT_CONFIG(whatsthis)
        self.ibm_lbl_2.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ibm_lbl_2.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" color:#ffffff;\">IBM</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.ibm_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ibm_btn_2.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindowMW", u"Deskop Eginer", None))
        self.label_16.setText(QCoreApplication.translate("MainWindowMW", u"User Name", None))
        self.label_7.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindowMW", u"Internet", None))
        self.label_64.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindowMW", u"Fast Internet", None))
        self.label_11.setText(QCoreApplication.translate("MainWindowMW", u"2.6 Mbps", None))
        self.label_91.setText(QCoreApplication.translate("MainWindowMW", u"Total Users", None))
        self.label_93.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_58.setText(QCoreApplication.translate("MainWindowMW", u" Version", None))
        self.label_21.setText(QCoreApplication.translate("MainWindowMW", u"0.8.9", None))
        self.label_19.setText(QCoreApplication.translate("MainWindowMW", u"07/09/2022", None))
        self.label_8.setText(QCoreApplication.translate("MainWindowMW", u"Controle de Finaceiro", None))
        self.label_190.setText(QCoreApplication.translate("MainWindowMW", u"Titulo", None))
        self.label_191.setText(QCoreApplication.translate("MainWindowMW", u"Valentia", None))
        self.label_192.setText(QCoreApplication.translate("MainWindowMW", u"Categoria", None))
        self.label_193.setText(QCoreApplication.translate("MainWindowMW", u"Dados/Horas", None))
        self.label_198.setText(QCoreApplication.translate("MainWindowMW", u"Gerencia", None))
        self.label_151.setText(QCoreApplication.translate("MainWindowMW", u"Teiser", None))
        self.label_153.setText(QCoreApplication.translate("MainWindowMW", u"KZ 200", None))
        self.label_155.setText(QCoreApplication.translate("MainWindowMW", u"Casa", None))
        self.label_174.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindowMW", u"Edit", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindowMW", u"Excluir Excluir", None))
        self.label_61.setText(QCoreApplication.translate("MainWindowMW", u"Teiser", None))
        self.label_101.setText(QCoreApplication.translate("MainWindowMW", u"KZ 200", None))
        self.label_103.setText(QCoreApplication.translate("MainWindowMW", u"Casa", None))
        self.label_111.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindowMW", u"Edit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindowMW", u"Excluir Excluir", None))
        self.label_131.setText(QCoreApplication.translate("MainWindowMW", u"Teiser", None))
        self.label_133.setText(QCoreApplication.translate("MainWindowMW", u"KZ 200", None))
        self.label_141.setText(QCoreApplication.translate("MainWindowMW", u"Casa", None))
        self.label_143.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindowMW", u"Edit", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindowMW", u"Excluir Excluir", None))
        self.label_113.setText(QCoreApplication.translate("MainWindowMW", u"Teiser", None))
        self.label_121.setText(QCoreApplication.translate("MainWindowMW", u"KZ 200", None))
        self.label_123.setText(QCoreApplication.translate("MainWindowMW", u"Casa", None))
        self.label_185.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindowMW", u"Edit", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindowMW", u"Excluir Excluir", None))
        self.label_175.setText(QCoreApplication.translate("MainWindowMW", u"Teiser", None))
        self.label_180.setText(QCoreApplication.translate("MainWindowMW", u"KZ 200", None))
        self.label_182.setText(QCoreApplication.translate("MainWindowMW", u"Casa", None))
        self.label_184.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindowMW", u"Edit", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindowMW", u"Excluir Excluir", None))
        self.label_12.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do Bitcoins", None))
        self.label_13.setText("")
        self.bitcoin_lbl.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.data_bitcoins.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_9.setText("")
        self.bitcoin_aoa_lbl.setText(QCoreApplication.translate("MainWindowMW", u"8.482.783,07 AOA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindowMW", u"1,00 BTC", None))
        self.label.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindowMW", u"19.751,20 USD", None))
        self.label_3.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindowMW", u"8.482.783,07 AOA", None))
        self.label_14.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.bitcoin_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_20.setText(QCoreApplication.translate("MainWindowMW", u"BTC", None))
        self.font.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.bitcoin_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"8.482.783,07", None))
        self.label_22.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_24.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do Dinar do Kuwait", None))
        self.label_25.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindowMW", u"\u062f.\u0643", None))
        self.dk_lbl.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.data_dk.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_18.setText("")
        self.dk_aoa_lbl.setText(QCoreApplication.translate("MainWindowMW", u"1.389,73 AOA", None))
        self.label_160.setText(QCoreApplication.translate("MainWindowMW", u"\u062f.\u0643", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowMW", u"1,00 KWD", None))
        self.label_5.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_26.setText(QCoreApplication.translate("MainWindowMW", u"3,24 USD", None))
        self.label_6.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindowMW", u"1.389,73 AOA", None))
        self.label_28.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_2.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.DK_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_30.setText(QCoreApplication.translate("MainWindowMW", u"KWD", None))
        self.font_2.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.DK_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1.389,73", None))
        self.label_32.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_33.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do Dinar do Bahrein", None))
        self.label_78.setText("")
        self.label_77.setText(QCoreApplication.translate("MainWindowMW", u"\u0628.\u062f", None))
        self.label_35.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_36.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_38.setText(QCoreApplication.translate("MainWindowMW", u"1.137,07 AOA", None))
        self.label_79.setText(QCoreApplication.translate("MainWindowMW", u"\u0628.\u062f", None))
        self.label_34.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindowMW", u"1,00 BHD", None))
        self.label_86.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_87.setText(QCoreApplication.translate("MainWindowMW", u"2,65 USD", None))
        self.label_88.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_89.setText(QCoreApplication.translate("MainWindowMW", u"1.137,07 AOA", None))
        self.label_90.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_3.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.DB_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_92.setText(QCoreApplication.translate("MainWindowMW", u"BHD", None))
        self.font_3.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.DB_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1.137,07", None))
        self.label_94.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_39.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do Rial de Om\u00e3", None))
        self.label_80.setText("")
        self.label_81.setText(QCoreApplication.translate("MainWindowMW", u"\u0631.\u0639.", None))
        self.label_41.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_42.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_44.setText(QCoreApplication.translate("MainWindowMW", u"1.113,22 AOA", None))
        self.label_37.setText("")
        self.label_82.setText(QCoreApplication.translate("MainWindowMW", u"\u0631.\u0639.", None))
        self.label_95.setText(QCoreApplication.translate("MainWindowMW", u"1,00 OMR", None))
        self.label_96.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_97.setText(QCoreApplication.translate("MainWindowMW", u"2,60 USD", None))
        self.label_98.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_99.setText(QCoreApplication.translate("MainWindowMW", u"1.113,22 AOA", None))
        self.label_100.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_5.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.RO_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_102.setText(QCoreApplication.translate("MainWindowMW", u"OMR", None))
        self.font_4.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.RO_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1.113,22", None))
        self.label_104.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_45.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do Dinar da Jord\u00e2nia", None))
        self.label_83.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindowMW", u"\u062f.\u0627", None))
        self.label_47.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_48.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_50.setText(QCoreApplication.translate("MainWindowMW", u"604,49 AOA", None))
        self.label_40.setText("")
        self.label_159.setText(QCoreApplication.translate("MainWindowMW", u"\u062f.\u0627", None))
        self.label_105.setText(QCoreApplication.translate("MainWindowMW", u"1,00 JOD", None))
        self.label_106.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_107.setText(QCoreApplication.translate("MainWindowMW", u"1,41 USD", None))
        self.label_108.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_109.setText(QCoreApplication.translate("MainWindowMW", u"604,49 AOA", None))
        self.label_110.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_6.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.DJ_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_112.setText(QCoreApplication.translate("MainWindowMW", u"JOD", None))
        self.font_5.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.DJ_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"604,49", None))
        self.label_114.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_57.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do D\u00f3lar Cayman", None))
        self.label_162.setText("")
        self.label_163.setText(QCoreApplication.translate("MainWindowMW", u"$", None))
        self.label_59.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_60.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_62.setText(QCoreApplication.translate("MainWindowMW", u"514,50 AOA", None))
        self.label_46.setText("")
        self.label_164.setText(QCoreApplication.translate("MainWindowMW", u"$", None))
        self.label_135.setText(QCoreApplication.translate("MainWindowMW", u"1,00 KYD", None))
        self.label_136.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_137.setText(QCoreApplication.translate("MainWindowMW", u"1,20 USD", None))
        self.label_138.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_139.setText(QCoreApplication.translate("MainWindowMW", u"514,50 AOA", None))
        self.label_140.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_7.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.DC_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_142.setText(QCoreApplication.translate("MainWindowMW", u"KYD", None))
        self.font_6.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.DC_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"514,50", None))
        self.label_144.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_51.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do Libra Esterlina", None))
        self.label_157.setText("")
        self.label_158.setText(QCoreApplication.translate("MainWindowMW", u"\u00a3", None))
        self.label_53.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_54.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_56.setText(QCoreApplication.translate("MainWindowMW", u"493,30 AOA", None))
        self.label_43.setText("")
        self.label_161.setText(QCoreApplication.translate("MainWindowMW", u"\u00a3", None))
        self.label_115.setText(QCoreApplication.translate("MainWindowMW", u"1,00 GBP", None))
        self.label_116.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_117.setText(QCoreApplication.translate("MainWindowMW", u"1,15 USD", None))
        self.label_118.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_119.setText(QCoreApplication.translate("MainWindowMW", u"493,30 AOA", None))
        self.label_120.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_8.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.LE_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_122.setText(QCoreApplication.translate("MainWindowMW", u"GBP", None))
        self.lfont.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.LE_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"493,30", None))
        self.label_124.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_63.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do Euro", None))
        self.label_165.setText("")
        self.label_166.setText(QCoreApplication.translate("MainWindowMW", u"\u20ac", None))
        self.label_65.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_66.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_68.setText(QCoreApplication.translate("MainWindowMW", u"426,57 AOA", None))
        self.label_49.setText("")
        self.label_167.setText(QCoreApplication.translate("MainWindowMW", u"\u20ac", None))
        self.label_125.setText(QCoreApplication.translate("MainWindowMW", u"1,00 EUR", None))
        self.label_126.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_127.setText(QCoreApplication.translate("MainWindowMW", u"1,00 USD", None))
        self.label_128.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_129.setText(QCoreApplication.translate("MainWindowMW", u"426,57 AOA", None))
        self.label_130.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_9.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.E_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_132.setText(QCoreApplication.translate("MainWindowMW", u"EUR", None))
        self.font_7.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.E_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"426,57", None))
        self.label_134.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_69.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do Franco Su\u00ed\u00e7o", None))
        self.label_168.setText(QCoreApplication.translate("MainWindowMW", u"\u20a3", None))
        self.label_169.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_72.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_74.setText(QCoreApplication.translate("MainWindowMW", u"436,79 AOA", None))
        self.label_170.setText(QCoreApplication.translate("MainWindowMW", u"\u20a3", None))
        self.label_52.setText("")
        self.label_145.setText(QCoreApplication.translate("MainWindowMW", u"1,00 CHF", None))
        self.label_146.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_147.setText(QCoreApplication.translate("MainWindowMW", u"1,02 USD", None))
        self.label_148.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_149.setText(QCoreApplication.translate("MainWindowMW", u"436,79 AOA", None))
        self.label_150.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_10.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.FS_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_152.setText(QCoreApplication.translate("MainWindowMW", u"CHF", None))
        self.font_8.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.FS_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"436,79", None))
        self.label_154.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
        self.label_70.setText(QCoreApplication.translate("MainWindowMW", u"Cota\u00e7\u00e3o do D\u00f3lar N-Americano", None))
        self.label_171.setText(QCoreApplication.translate("MainWindowMW", u"$", None))
        self.label_172.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_76.setText(QCoreApplication.translate("MainWindowMW", u"Quotation date: 01/09/2022", None))
        self.label_156.setText(QCoreApplication.translate("MainWindowMW", u"428,58 AOA", None))
        self.label_173.setText(QCoreApplication.translate("MainWindowMW", u"$", None))
        self.label_55.setText("")
        self.label_176.setText(QCoreApplication.translate("MainWindowMW", u"1,00 USD", None))
        self.label_177.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.label_178.setText(QCoreApplication.translate("MainWindowMW", u"428,58 AOA", None))
        self.label_179.setText(QCoreApplication.translate("MainWindowMW", u"disponivel", None))
        self.site_11.setText(QCoreApplication.translate("MainWindowMW", u"Site: docs.awesomeapi.com.br", None))
        self.DNA_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"1,00", None))
        self.label_181.setText(QCoreApplication.translate("MainWindowMW", u"USD", None))
        self.font_9.setText(QCoreApplication.translate("MainWindowMW", u"Fonte: AWESOMEAPI", None))
        self.DNA_aoa_LEdit.setText(QCoreApplication.translate("MainWindowMW", u"428,58", None))
        self.label_183.setText(QCoreApplication.translate("MainWindowMW", u"AOA", None))
#if QT_CONFIG(whatsthis)
        self.GoogleFinance_btl.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.GoogleFinance_btl.setText("")
#if QT_CONFIG(whatsthis)
        self.YahooFinance_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.YahooFinance_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.Investing_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Investing_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.BLHL_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.BLHL_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.Infomaney_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Infomaney_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.Dinherama_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Dinherama_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.CMEgroup_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.CMEgroup_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.Economia_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Economia_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.help_lbl.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.help_lbl.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" color:#ffffff;\">Help</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.help_btnF_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.help_btnF_2.setText("")
    # retranslateUi

