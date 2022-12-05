# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SystemMWVSxyTy.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindowMW(object):
    def setupUi(self, MainWindowMW):
        if not MainWindowMW.objectName():
            MainWindowMW.setObjectName(u"MainWindowMW")
        MainWindowMW.resize(1122, 664)
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
        font = QFont()
        font.setPointSize(2)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
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
"border-radius:15px}\n"
"")
        icon = QIcon()
        icon.addFile(u"../img/logoFC.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.NameEmp = QLabel(self.barraTitulo)
        self.NameEmp.setObjectName(u"NameEmp")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.NameEmp.setFont(font1)
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
        icon1.addFile(u"../img/24x24/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimisar.setIcon(icon1)
        self.minimisar.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.minimisar)

        self.NormalMax = QToolButton(self.frame_btn_zone_3)
        self.NormalMax.setObjectName(u"NormalMax")
        self.NormalMax.setMinimumSize(QSize(0, 0))
        icon2 = QIcon()
        icon2.addFile(u"../img/24x24/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NormalMax.setIcon(icon2)
        self.NormalMax.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.NormalMax)

        self.fechar = QToolButton(self.frame_btn_zone_3)
        self.fechar.setObjectName(u"fechar")
        icon3 = QIcon()
        icon3.addFile(u"../img/24x24/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fechar.setIcon(icon3)
        self.fechar.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.fechar)


        self.horizontalLayout_9.addWidget(self.frame_btn_zone_3)


        self.verticalLayout_8.addWidget(self.barraTitulo)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame = QFrame(self.central_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(206, 0))
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
        icon4.addFile(u"../img/24x24/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home.setIcon(icon4)
        self.Home.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.Home, 0, Qt.AlignRight)

        self.web_btn_2 = QPushButton(self.xone_btn_left)
        self.web_btn_2.setObjectName(u"web_btn_2")
        self.web_btn_2.setMinimumSize(QSize(0, 35))
        self.web_btn_2.setMaximumSize(QSize(35, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"../img/web_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.web_btn_2.setIcon(icon5)
        self.web_btn_2.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.web_btn_2)

        self.settings = QPushButton(self.xone_btn_left)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 35))
        self.settings.setMaximumSize(QSize(35, 16777215))
        icon6 = QIcon()
        icon6.addFile(u"../img/24x24/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon6)
        self.settings.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.settings, 0, Qt.AlignRight)

        self.double_up = QPushButton(self.xone_btn_left)
        self.double_up.setObjectName(u"double_up")
        self.double_up.setMinimumSize(QSize(0, 35))
        self.double_up.setMaximumSize(QSize(35, 35))
        icon7 = QIcon()
        icon7.addFile(u"../img/24x24/cil-x-f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.double_up.setIcon(icon7)
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
        self.verticalLayout_141 = QVBoxLayout(self.left_menu)
        self.verticalLayout_141.setSpacing(0)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.frame_zoneQR = QFrame(self.left_menu)
        self.frame_zoneQR.setObjectName(u"frame_zoneQR")
        self.frame_zoneQR.setMinimumSize(QSize(0, 175))
        self.frame_zoneQR.setMaximumSize(QSize(0, 175))
        self.frame_zoneQR.setFrameShape(QFrame.StyledPanel)
        self.frame_zoneQR.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_zoneQR)
        self.verticalLayout_142.setSpacing(0)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_142.addItem(self.verticalSpacer_6)

        self.QRcode = QLabel(self.frame_zoneQR)
        self.QRcode.setObjectName(u"QRcode")
        self.QRcode.setMaximumSize(QSize(16777215, 184))
        self.QRcode.setPixmap(QPixmap(u"../img/qr_code_120px.png"))
        self.QRcode.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_142.addWidget(self.QRcode)

        self.data = QLabel(self.frame_zoneQR)
        self.data.setObjectName(u"data")
        self.data.setMinimumSize(QSize(100, 15))
        self.data.setMaximumSize(QSize(100, 15))
        self.data.setStyleSheet(u"")
        self.data.setAlignment(Qt.AlignCenter)

        self.verticalLayout_142.addWidget(self.data)

        self.criadoPor = QLabel(self.frame_zoneQR)
        self.criadoPor.setObjectName(u"criadoPor")
        self.criadoPor.setMinimumSize(QSize(120, 15))
        self.criadoPor.setMaximumSize(QSize(120, 21))
        self.criadoPor.setStyleSheet(u"color:#ffffff;\n"
"")
        self.criadoPor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_142.addWidget(self.criadoPor)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_142.addItem(self.verticalSpacer_5)


        self.verticalLayout_141.addWidget(self.frame_zoneQR)

        self.frame_zone_btn = QFrame(self.left_menu)
        self.frame_zone_btn.setObjectName(u"frame_zone_btn")
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
        icon8 = QIcon()
        icon8.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/help_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btn.setIcon(icon8)
        self.help_btn.setIconSize(QSize(18, 18))
        self.help_btn.setCheckable(False)

        self.verticalLayout_10.addWidget(self.help_btn)

        self.perfil_btn = QPushButton(self.frame_zone_btn)
        self.perfil_btn.setObjectName(u"perfil_btn")
        self.perfil_btn.setMinimumSize(QSize(0, 34))
        self.perfil_btn.setMaximumSize(QSize(16777215, 34))
        icon9 = QIcon()
        icon9.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfil_btn.setIcon(icon9)
        self.perfil_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.perfil_btn)

        self.web_btn = QPushButton(self.frame_zone_btn)
        self.web_btn.setObjectName(u"web_btn")
        self.web_btn.setMinimumSize(QSize(0, 34))
        self.web_btn.setMaximumSize(QSize(16777215, 34))
        icon10 = QIcon()
        icon10.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/website_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.web_btn.setIcon(icon10)
        self.web_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.web_btn)

        self.setting_btn = QPushButton(self.frame_zone_btn)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setMinimumSize(QSize(0, 34))
        self.setting_btn.setMaximumSize(QSize(16777215, 34))
        icon11 = QIcon()
        icon11.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/settings_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon11)
        self.setting_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_10.addWidget(self.setting_btn)

        self.coins_btn = QPushButton(self.frame_zone_btn)
        self.coins_btn.setObjectName(u"coins_btn")
        self.coins_btn.setMinimumSize(QSize(0, 34))
        self.coins_btn.setMaximumSize(QSize(16777215, 34))
        icon12 = QIcon()
        icon12.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/money_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coins_btn.setIcon(icon12)
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

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.verticalLayout_141.addWidget(self.frame_zone_btn)

        self.verticalSpacer_2 = QSpacerItem(5, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_141.addItem(self.verticalSpacer_2)


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
        self.frame_46 = QFrame(self.page_Home)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_46)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_222 = QFrame(self.frame_46)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setMinimumSize(QSize(400, 0))
        self.frame_222.setStyleSheet(u";\n"
"background-color: rgb(170, 85, 255);")
        self.frame_222.setFrameShape(QFrame.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Raised)
        self.verticalLayout_253 = QVBoxLayout(self.frame_222)
        self.verticalLayout_253.setObjectName(u"verticalLayout_253")
        self.verticalLayout_253.setContentsMargins(-1, 0, 0, 0)
        self.frame_364 = QFrame(self.frame_222)
        self.frame_364.setObjectName(u"frame_364")
        self.frame_364.setMinimumSize(QSize(0, 175))
        self.frame_364.setMaximumSize(QSize(16777215, 175))
        self.frame_364.setFrameShape(QFrame.StyledPanel)
        self.frame_364.setFrameShadow(QFrame.Raised)
        self.verticalLayout_254 = QVBoxLayout(self.frame_364)
        self.verticalLayout_254.setSpacing(0)
        self.verticalLayout_254.setObjectName(u"verticalLayout_254")
        self.verticalLayout_254.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.frame_364)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setMinimumSize(QSize(0, 0))
        self.scrollArea_7.setMaximumSize(QSize(16777215, 172))
        self.scrollArea_7.setStyleSheet(u"")
        self.scrollArea_7.setFrameShadow(QFrame.Sunken)
        self.scrollArea_7.setLineWidth(1)
        self.scrollArea_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_7.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1034, 172))
        self.scrollAreaWidgetContents_5.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:15px;\n"
"")
        self.horizontalLayout_109 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_109.setSpacing(8)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(5, 0, 5, 9)
        self.frame_Browsin_history_2 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_Browsin_history_2.setObjectName(u"frame_Browsin_history_2")
        self.frame_Browsin_history_2.setMinimumSize(QSize(250, 130))
        self.frame_Browsin_history_2.setMaximumSize(QSize(310, 135))
        self.frame_Browsin_history_2.setStyleSheet(u"background-color: rgb(255, 255, 255)\n"
"")
        self.frame_Browsin_history_2.setFrameShape(QFrame.StyledPanel)
        self.frame_Browsin_history_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_Browsin_history_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_205 = QFrame(self.frame_Browsin_history_2)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_205)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(96, 15, 130, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.frame_Browsin_history_btn_2 = QPushButton(self.frame_205)
        self.frame_Browsin_history_btn_2.setObjectName(u"frame_Browsin_history_btn_2")
        self.frame_Browsin_history_btn_2.setGeometry(QRect(3, 6, 88, 83))
        self.frame_Browsin_history_btn_2.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"padding:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 0px;\n"
"padding:0px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"../img/atrasado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_Browsin_history_btn_2.setIcon(icon15)
        self.frame_Browsin_history_btn_2.setIconSize(QSize(86, 101))
        self.label_186 = QLabel(self.frame_205)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(122, 34, 81, 20))
        self.label_186.setFont(font2)
        self.label_186.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.verticalLayout_16.addWidget(self.frame_205)

        self.frame_206 = QFrame(self.frame_Browsin_history_2)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setMaximumSize(QSize(16777215, 40))
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.frame_206)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.verticalLayout_177.setContentsMargins(0, 0, 10, 5)
        self.contasAreceberEmAtraso_lbl = QLabel(self.frame_206)
        self.contasAreceberEmAtraso_lbl.setObjectName(u"contasAreceberEmAtraso_lbl")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(21)
        self.contasAreceberEmAtraso_lbl.setFont(font3)
        self.contasAreceberEmAtraso_lbl.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"background-color: transparent")
        self.contasAreceberEmAtraso_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_177.addWidget(self.contasAreceberEmAtraso_lbl)


        self.verticalLayout_16.addWidget(self.frame_206)


        self.horizontalLayout_109.addWidget(self.frame_Browsin_history_2)

        self.frame_opening_history_2 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_opening_history_2.setObjectName(u"frame_opening_history_2")
        self.frame_opening_history_2.setMinimumSize(QSize(250, 130))
        self.frame_opening_history_2.setMaximumSize(QSize(310, 135))
        self.frame_opening_history_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.frame_opening_history_2.setFrameShape(QFrame.StyledPanel)
        self.frame_opening_history_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_178 = QVBoxLayout(self.frame_opening_history_2)
        self.verticalLayout_178.setSpacing(0)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.frame_207 = QFrame(self.frame_opening_history_2)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.frame_opening_history_btn_2 = QPushButton(self.frame_207)
        self.frame_opening_history_btn_2.setObjectName(u"frame_opening_history_btn_2")
        self.frame_opening_history_btn_2.setGeometry(QRect(5, 10, 90, 85))
        self.frame_opening_history_btn_2.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"padding:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 0px;\n"
"padding:0px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"../img/adiantamento-de-dinheiroV2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_opening_history_btn_2.setIcon(icon16)
        self.frame_opening_history_btn_2.setIconSize(QSize(86, 100))
        self.label_195 = QLabel(self.frame_207)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(101, 15, 157, 20))
        self.label_195.setFont(font2)
        self.label_195.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_194 = QLabel(self.frame_207)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(118, 34, 122, 20))
        self.label_194.setFont(font2)
        self.label_194.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.verticalLayout_178.addWidget(self.frame_207)

        self.frame_208 = QFrame(self.frame_opening_history_2)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMaximumSize(QSize(16777215, 37))
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.verticalLayout_179 = QVBoxLayout(self.frame_208)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.verticalLayout_179.setContentsMargins(0, 0, 10, 5)
        self.contasAreceberEmAberto_label = QLabel(self.frame_208)
        self.contasAreceberEmAberto_label.setObjectName(u"contasAreceberEmAberto_label")
        self.contasAreceberEmAberto_label.setFont(font3)
        self.contasAreceberEmAberto_label.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"background-color: transparent")
        self.contasAreceberEmAberto_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_179.addWidget(self.contasAreceberEmAberto_label)


        self.verticalLayout_178.addWidget(self.frame_208)


        self.horizontalLayout_109.addWidget(self.frame_opening_history_2)

        self.frameContasApagarEmaberto = QFrame(self.scrollAreaWidgetContents_5)
        self.frameContasApagarEmaberto.setObjectName(u"frameContasApagarEmaberto")
        self.frameContasApagarEmaberto.setMinimumSize(QSize(250, 130))
        self.frameContasApagarEmaberto.setMaximumSize(QSize(310, 135))
        self.frameContasApagarEmaberto.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frameContasApagarEmaberto.setFrameShape(QFrame.StyledPanel)
        self.frameContasApagarEmaberto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_180 = QVBoxLayout(self.frameContasApagarEmaberto)
        self.verticalLayout_180.setSpacing(0)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.verticalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.frame_user_list_3 = QFrame(self.frameContasApagarEmaberto)
        self.frame_user_list_3.setObjectName(u"frame_user_list_3")
        self.frame_user_list_3.setMinimumSize(QSize(250, 130))
        self.frame_user_list_3.setMaximumSize(QSize(310, 135))
        self.frame_user_list_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_user_list_3.setFrameShape(QFrame.StyledPanel)
        self.frame_user_list_3.setFrameShadow(QFrame.Raised)
        self.frame_user_list_btn_3 = QPushButton(self.frame_user_list_3)
        self.frame_user_list_btn_3.setObjectName(u"frame_user_list_btn_3")
        self.frame_user_list_btn_3.setGeometry(QRect(6, 6, 90, 92))
        self.frame_user_list_btn_3.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"padding:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 0px;\n"
"padding:0px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u"../img/adiantamento-de-dinheiroV.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_user_list_btn_3.setIcon(icon17)
        self.frame_user_list_btn_3.setIconSize(QSize(100, 130))
        self.label_203 = QLabel(self.frame_user_list_3)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(96, 15, 130, 20))
        self.label_203.setFont(font2)
        self.label_203.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_204 = QLabel(self.frame_user_list_3)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(120, 34, 81, 20))
        self.label_204.setFont(font2)
        self.label_204.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.verticalLayout_180.addWidget(self.frame_user_list_3)

        self.frame_211 = QFrame(self.frameContasApagarEmaberto)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setMinimumSize(QSize(0, 35))
        self.frame_211.setMaximumSize(QSize(16777215, 35))
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.verticalLayout_181 = QVBoxLayout(self.frame_211)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(0, 0, 10, 0)
        self.label_205 = QLabel(self.frame_211)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setFont(font3)
        self.label_205.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_205.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_181.addWidget(self.label_205)


        self.verticalLayout_180.addWidget(self.frame_211)


        self.horizontalLayout_109.addWidget(self.frameContasApagarEmaberto)

        self.frameContasApagarEmatraso = QFrame(self.scrollAreaWidgetContents_5)
        self.frameContasApagarEmatraso.setObjectName(u"frameContasApagarEmatraso")
        self.frameContasApagarEmatraso.setMinimumSize(QSize(250, 130))
        self.frameContasApagarEmatraso.setMaximumSize(QSize(310, 135))
        self.frameContasApagarEmatraso.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frameContasApagarEmatraso.setFrameShape(QFrame.StyledPanel)
        self.frameContasApagarEmatraso.setFrameShadow(QFrame.Raised)
        self.verticalLayout_182 = QVBoxLayout(self.frameContasApagarEmatraso)
        self.verticalLayout_182.setSpacing(0)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.verticalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.frame_210 = QFrame(self.frameContasApagarEmatraso)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self.password_faceId_btn_3 = QPushButton(self.frame_210)
        self.password_faceId_btn_3.setObjectName(u"password_faceId_btn_3")
        self.password_faceId_btn_3.setGeometry(QRect(6, 6, 90, 92))
        self.password_faceId_btn_3.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"padding:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 0px;\n"
"padding:0px;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u"../img/adiantamento-de-dinheiroV5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.password_faceId_btn_3.setIcon(icon18)
        self.password_faceId_btn_3.setIconSize(QSize(100, 130))
        self.label_209 = QLabel(self.frame_210)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setGeometry(QRect(111, 15, 111, 22))
        self.label_209.setFont(font2)
        self.label_209.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_187 = QLabel(self.frame_210)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(130, 37, 80, 16))
        self.label_187.setFont(font2)
        self.label_187.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"padding-bottom:3px")

        self.verticalLayout_182.addWidget(self.frame_210)

        self.frame_212 = QFrame(self.frameContasApagarEmatraso)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setMinimumSize(QSize(0, 35))
        self.frame_212.setMaximumSize(QSize(16777215, 35))
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)
        self.verticalLayout_183 = QVBoxLayout(self.frame_212)
        self.verticalLayout_183.setSpacing(0)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.verticalLayout_183.setContentsMargins(0, 0, 10, 0)
        self.contasApagarEmAtraso_label = QLabel(self.frame_212)
        self.contasApagarEmAtraso_label.setObjectName(u"contasApagarEmAtraso_label")
        self.contasApagarEmAtraso_label.setFont(font3)
        self.contasApagarEmAtraso_label.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"background-color: transparent")
        self.contasApagarEmAtraso_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_183.addWidget(self.contasApagarEmAtraso_label)


        self.verticalLayout_182.addWidget(self.frame_212)


        self.horizontalLayout_109.addWidget(self.frameContasApagarEmatraso)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_254.addWidget(self.scrollArea_7)


        self.verticalLayout_253.addWidget(self.frame_364)

        self.zonadografico = QFrame(self.frame_222)
        self.zonadografico.setObjectName(u"zonadografico")
        self.zonadografico.setMinimumSize(QSize(3, 0))
        self.zonadografico.setMaximumSize(QSize(123456, 16777215))
        self.zonadografico.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.zonadografico.setFrameShape(QFrame.StyledPanel)
        self.zonadografico.setFrameShadow(QFrame.Raised)
        self.verticalLayout_graficoMain = QVBoxLayout(self.zonadografico)
        self.verticalLayout_graficoMain.setSpacing(0)
        self.verticalLayout_graficoMain.setObjectName(u"verticalLayout_graficoMain")
        self.verticalLayout_graficoMain.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_253.addWidget(self.zonadografico)

        self.frame_ulatimasTranzacao = QFrame(self.frame_222)
        self.frame_ulatimasTranzacao.setObjectName(u"frame_ulatimasTranzacao")
        self.frame_ulatimasTranzacao.setMaximumSize(QSize(16777215, 180))
        self.frame_ulatimasTranzacao.setFrameShape(QFrame.StyledPanel)
        self.frame_ulatimasTranzacao.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_ulatimasTranzacao)
        self.verticalLayout_143.setSpacing(0)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_ulatimasTranzacao)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 25))
        self.widget.setMaximumSize(QSize(16777215, 27))
        self.horizontalLayout_101 = QHBoxLayout(self.widget)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.frame_229 = QFrame(self.widget)
        self.frame_229.setObjectName(u"frame_229")
        self.frame_229.setFrameShape(QFrame.StyledPanel)
        self.frame_229.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_229)
        self.verticalLayout_147.setSpacing(0)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.label_227 = QLabel(self.frame_229)
        self.label_227.setObjectName(u"label_227")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semibold"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.label_227.setFont(font4)
        self.label_227.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_147.addWidget(self.label_227)


        self.horizontalLayout_101.addWidget(self.frame_229)

        self.frame_235 = QFrame(self.widget)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_235)
        self.verticalLayout_148.setSpacing(0)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.verticalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.label_228 = QLabel(self.frame_235)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setFont(font2)
        self.label_228.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_148.addWidget(self.label_228)


        self.horizontalLayout_101.addWidget(self.frame_235)


        self.verticalLayout_143.addWidget(self.widget)

        self.frame_49 = QFrame(self.frame_ulatimasTranzacao)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_49)
        self.verticalLayout_144.setSpacing(0)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_49)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1033, 155))
        self.horizontalLayout_46 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_47)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, -1)
        self.zonaHistoricoEntrada = QFrame(self.frame_47)
        self.zonaHistoricoEntrada.setObjectName(u"zonaHistoricoEntrada")
        self.zonaHistoricoEntrada.setMinimumSize(QSize(0, 48))
        self.zonaHistoricoEntrada.setFrameShape(QFrame.StyledPanel)
        self.zonaHistoricoEntrada.setFrameShadow(QFrame.Raised)
        self.verticalLayout_ZonaEntrada = QVBoxLayout(self.zonaHistoricoEntrada)
        self.verticalLayout_ZonaEntrada.setSpacing(3)
        self.verticalLayout_ZonaEntrada.setObjectName(u"verticalLayout_ZonaEntrada")
        self.verticalLayout_ZonaEntrada.setContentsMargins(3, 5, 3, 5)

        self.verticalLayout_22.addWidget(self.zonaHistoricoEntrada)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_7)


        self.horizontalLayout_46.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_48)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.zonaHistoricoSaida = QFrame(self.frame_48)
        self.zonaHistoricoSaida.setObjectName(u"zonaHistoricoSaida")
        self.zonaHistoricoSaida.setMinimumSize(QSize(0, 48))
        self.zonaHistoricoSaida.setFrameShape(QFrame.StyledPanel)
        self.zonaHistoricoSaida.setFrameShadow(QFrame.Raised)
        self.verticalLayout_zonaSaida = QVBoxLayout(self.zonaHistoricoSaida)
        self.verticalLayout_zonaSaida.setSpacing(3)
        self.verticalLayout_zonaSaida.setObjectName(u"verticalLayout_zonaSaida")
        self.verticalLayout_zonaSaida.setContentsMargins(3, 5, 3, 5)

        self.verticalLayout_24.addWidget(self.zonaHistoricoSaida)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_8)


        self.horizontalLayout_46.addWidget(self.frame_48)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_144.addWidget(self.scrollArea_2)


        self.verticalLayout_143.addWidget(self.frame_49)


        self.verticalLayout_253.addWidget(self.frame_ulatimasTranzacao)


        self.verticalLayout_14.addWidget(self.frame_222)


        self.verticalLayout_12.addWidget(self.frame_46)

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
        self.page_ControleDeContaAReceber = QWidget()
        self.page_ControleDeContaAReceber.setObjectName(u"page_ControleDeContaAReceber")
        self.verticalLayout_208 = QVBoxLayout(self.page_ControleDeContaAReceber)
        self.verticalLayout_208.setSpacing(0)
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.verticalLayout_208.setContentsMargins(0, 0, 0, 0)
        self.frame_213 = QFrame(self.page_ControleDeContaAReceber)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(170, 85, 255);")
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.verticalLayout_184 = QVBoxLayout(self.frame_213)
        self.verticalLayout_184.setSpacing(0)
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.verticalLayout_184.setContentsMargins(8, 0, 8, 0)
        self.frame_214 = QFrame(self.frame_213)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setMaximumSize(QSize(16777215, 250))
        self.frame_214.setStyleSheet(u"")
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.verticalLayout_185 = QVBoxLayout(self.frame_214)
        self.verticalLayout_185.setSpacing(0)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.verticalLayout_185.setContentsMargins(0, 0, 0, 0)
        self.frame_215 = QFrame(self.frame_214)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setStyleSheet(u"")
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_217 = QFrame(self.frame_215)
        self.frame_217.setObjectName(u"frame_217")
        self.frame_217.setMinimumSize(QSize(0, 250))
        font5 = QFont()
        font5.setBold(True)
        self.frame_217.setFont(font5)
        self.frame_217.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.frame_217.setFrameShape(QFrame.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Raised)
        self.verticalLayout_186 = QVBoxLayout(self.frame_217)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(0, 0, 0, 0)
        self.frame_218 = QFrame(self.frame_217)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setMinimumSize(QSize(0, 136))
        self.frame_218.setMaximumSize(QSize(16777215, 136))
        self.frame_218.setFrameShape(QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_218)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 5, 5, 0)
        self.frame_219 = QFrame(self.frame_218)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setMinimumSize(QSize(0, 131))
        self.frame_219.setMaximumSize(QSize(16777215, 131))
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_219)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(12, 10, 8, 7)
        self.frame_220 = QFrame(self.frame_219)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setMinimumSize(QSize(215, 0))
        self.frame_220.setMaximumSize(QSize(400, 16777215))
        self.frame_220.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)
        self.verticalLayout_187 = QVBoxLayout(self.frame_220)
        self.verticalLayout_187.setSpacing(0)
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.verticalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.frame_238 = QFrame(self.frame_220)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setFrameShape(QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Raised)
        self.pushButton_8 = QPushButton(self.frame_238)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(3, 15, 66, 57))
        icon19 = QIcon()
        icon19.addFile(u"../img/totalTitulos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon19)
        self.pushButton_8.setIconSize(QSize(73, 73))
        self.label_133 = QLabel(self.frame_238)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(73, 33, 160, 26))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Semibold"])
        font6.setPointSize(17)
        self.label_133.setFont(font6)
        self.label_133.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_187.addWidget(self.frame_238)

        self.frame_239 = QFrame(self.frame_220)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setMaximumSize(QSize(16777215, 35))
        self.frame_239.setFrameShape(QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Raised)
        self.verticalLayout_188 = QVBoxLayout(self.frame_239)
        self.verticalLayout_188.setSpacing(0)
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.verticalLayout_188.setContentsMargins(0, 0, 7, 7)
        self.label_141 = QLabel(self.frame_239)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMaximumSize(QSize(16777215, 35))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Semibold"])
        font7.setPointSize(16)
        font7.setBold(True)
        self.label_141.setFont(font7)
        self.label_141.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_141.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_188.addWidget(self.label_141)


        self.verticalLayout_187.addWidget(self.frame_239)


        self.horizontalLayout_61.addWidget(self.frame_220)

        self.frame_240 = QFrame(self.frame_219)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setMinimumSize(QSize(215, 0))
        self.frame_240.setMaximumSize(QSize(400, 16777215))
        self.frame_240.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_240.setFrameShape(QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Raised)
        self.verticalLayout_189 = QVBoxLayout(self.frame_240)
        self.verticalLayout_189.setSpacing(0)
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.verticalLayout_189.setContentsMargins(0, 0, 0, 0)
        self.frame_241 = QFrame(self.frame_240)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setFrameShape(QFrame.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Raised)
        self.label_143 = QLabel(self.frame_241)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(75, 33, 121, 26))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI Semibold"])
        font8.setPointSize(16)
        self.label_143.setFont(font8)
        self.label_143.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_9 = QPushButton(self.frame_241)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(4, 27, 67, 46))
        icon20 = QIcon()
        icon20.addFile(u"../img/carduse_card_payment_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon20)
        self.pushButton_9.setIconSize(QSize(64, 68))

        self.verticalLayout_189.addWidget(self.frame_241)

        self.frame_242 = QFrame(self.frame_240)
        self.frame_242.setObjectName(u"frame_242")
        self.frame_242.setMaximumSize(QSize(16777212, 35))
        self.frame_242.setFrameShape(QFrame.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Raised)
        self.verticalLayout_190 = QVBoxLayout(self.frame_242)
        self.verticalLayout_190.setSpacing(0)
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.verticalLayout_190.setContentsMargins(0, 0, 11, 7)
        self.label_151 = QLabel(self.frame_242)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font8)
        self.label_151.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_151.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_190.addWidget(self.label_151)


        self.verticalLayout_189.addWidget(self.frame_242)


        self.horizontalLayout_61.addWidget(self.frame_240)

        self.frame_246 = QFrame(self.frame_219)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setMinimumSize(QSize(215, 0))
        self.frame_246.setMaximumSize(QSize(400, 16777215))
        self.frame_246.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_246.setFrameShape(QFrame.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.frame_246)
        self.verticalLayout_191.setSpacing(0)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.verticalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.frame_255 = QFrame(self.frame_246)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setFrameShape(QFrame.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Raised)
        self.label_153 = QLabel(self.frame_255)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setGeometry(QRect(80, 33, 161, 26))
        self.label_153.setFont(font8)
        self.label_153.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_10 = QPushButton(self.frame_255)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(5, 5, 68, 60))
        icon21 = QIcon()
        icon21.addFile(u"../img/Total em Aberto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon21)
        self.pushButton_10.setIconSize(QSize(68, 73))

        self.verticalLayout_191.addWidget(self.frame_255)

        self.frame_256 = QFrame(self.frame_246)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setMaximumSize(QSize(16777212, 35))
        self.frame_256.setFrameShape(QFrame.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Raised)
        self.verticalLayout_192 = QVBoxLayout(self.frame_256)
        self.verticalLayout_192.setSpacing(0)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.verticalLayout_192.setContentsMargins(0, 0, 11, 7)
        self.label_155 = QLabel(self.frame_256)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMaximumSize(QSize(16777215, 35))
        self.label_155.setFont(font8)
        self.label_155.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_155.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_192.addWidget(self.label_155)


        self.verticalLayout_191.addWidget(self.frame_256)


        self.horizontalLayout_61.addWidget(self.frame_246)


        self.horizontalLayout_55.addWidget(self.frame_219)

        self.frame_257 = QFrame(self.frame_218)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setMinimumSize(QSize(160, 0))
        self.frame_257.setMaximumSize(QSize(175, 16777215))
        self.frame_257.setFrameShape(QFrame.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Raised)
        self.pagarConta = QPushButton(self.frame_257)
        self.pagarConta.setObjectName(u"pagarConta")
        self.pagarConta.setGeometry(QRect(0, 50, 170, 33))
        self.pagarConta.setMinimumSize(QSize(150, 33))
        self.pagarConta.setMaximumSize(QSize(12345, 33))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Semibold"])
        font9.setPointSize(10)
        font9.setBold(False)
        self.pagarConta.setFont(font9)
        self.pagarConta.setStyleSheet(u"QPushButton{\n"
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
        self.contaReceber = QPushButton(self.frame_257)
        self.contaReceber.setObjectName(u"contaReceber")
        self.contaReceber.setGeometry(QRect(0, 10, 170, 33))
        self.contaReceber.setMinimumSize(QSize(150, 33))
        self.contaReceber.setMaximumSize(QSize(12345, 33))
        self.contaReceber.setFont(font9)
        self.contaReceber.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_55.addWidget(self.frame_257)


        self.verticalLayout_186.addWidget(self.frame_218)

        self.frame_258 = QFrame(self.frame_217)
        self.frame_258.setObjectName(u"frame_258")
        self.frame_258.setMaximumSize(QSize(16777215, 117))
        self.frame_258.setStyleSheet(u"")
        self.frame_258.setFrameShape(QFrame.StyledPanel)
        self.frame_258.setFrameShadow(QFrame.Raised)
        self.frame_258.setLineWidth(1)
        self.pushButton_12 = QPushButton(self.frame_258)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(506, 77, 80, 34))
        self.pushButton_12.setMinimumSize(QSize(80, 34))
        self.pushButton_12.setMaximumSize(QSize(80, 34))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(False)
        self.pushButton_12.setFont(font10)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
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
        self.label_184 = QLabel(self.frame_258)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(261, 64, 91, 12))
        self.label_184.setMinimumSize(QSize(0, 12))
        self.label_184.setMaximumSize(QSize(16777215, 12))
        font11 = QFont()
        font11.setPointSize(11)
        self.label_184.setFont(font11)
        self.label_184.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.comboBox_4 = QComboBox(self.frame_258)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(261, 80, 241, 31))
        self.comboBox_4.setMinimumSize(QSize(0, 31))
        self.comboBox_4.setMaximumSize(QSize(16777215, 31))
        self.comboBox_4.setFont(font11)
        self.comboBox_4.setStyleSheet(u"\n"
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
        self.BuscarStatus_3 = QLineEdit(self.frame_258)
        self.BuscarStatus_3.setObjectName(u"BuscarStatus_3")
        self.BuscarStatus_3.setGeometry(QRect(15, 27, 241, 31))
        self.BuscarStatus_3.setMinimumSize(QSize(170, 31))
        self.BuscarStatus_3.setMaximumSize(QSize(300, 30))
        self.BuscarStatus_3.setFont(font11)
        self.BuscarStatus_3.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:3px;")
        self.label_190 = QLabel(self.frame_258)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(15, 0, 81, 18))
        self.label_190.setMaximumSize(QSize(16777215, 18))
        self.label_190.setFont(font11)
        self.label_190.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_191 = QLabel(self.frame_258)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(261, 0, 171, 18))
        self.label_191.setMaximumSize(QSize(16777215, 18))
        self.label_191.setFont(font11)
        self.label_191.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.comboBox_3 = QComboBox(self.frame_258)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(15, 80, 241, 31))
        self.comboBox_3.setMinimumSize(QSize(0, 31))
        self.comboBox_3.setMaximumSize(QSize(16777215, 31))
        self.comboBox_3.setFont(font11)
        self.comboBox_3.setStyleSheet(u"\n"
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
        self.label_182 = QLabel(self.frame_258)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setGeometry(QRect(15, 61, 61, 17))
        self.label_182.setMaximumSize(QSize(16777215, 18))
        self.label_182.setFont(font11)
        self.label_182.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_185 = QLabel(self.frame_258)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(506, 0, 171, 18))
        self.label_185.setMaximumSize(QSize(16777215, 18))
        self.label_185.setFont(font11)
        self.label_185.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.dateEdit_3 = QDateEdit(self.frame_258)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(375, 27, 127, 30))
        font12 = QFont()
        font12.setPointSize(12)
        font12.setBold(False)
        self.dateEdit_3.setFont(font12)
        self.dateEdit_3.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_3.setReadOnly(False)
        self.dateEdit_3.setDate(QDate(2010, 1, 1))
        self.dateEdit_4 = QDateEdit(self.frame_258)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setGeometry(QRect(261, 27, 127, 30))
        self.dateEdit_4.setFont(font12)
        self.dateEdit_4.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_4.setDate(QDate(2010, 1, 1))
        self.dateEdit_5 = QDateEdit(self.frame_258)
        self.dateEdit_5.setObjectName(u"dateEdit_5")
        self.dateEdit_5.setGeometry(QRect(619, 27, 127, 30))
        self.dateEdit_5.setFont(font12)
        self.dateEdit_5.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_5.setReadOnly(False)
        self.dateEdit_5.setDate(QDate(2010, 1, 1))
        self.dateEdit_6 = QDateEdit(self.frame_258)
        self.dateEdit_6.setObjectName(u"dateEdit_6")
        self.dateEdit_6.setGeometry(QRect(506, 27, 127, 30))
        self.dateEdit_6.setFont(font12)
        self.dateEdit_6.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_6.setDate(QDate(2010, 1, 1))

        self.verticalLayout_186.addWidget(self.frame_258)


        self.horizontalLayout_52.addWidget(self.frame_217)


        self.verticalLayout_185.addWidget(self.frame_215)


        self.verticalLayout_184.addWidget(self.frame_214)

        self.frame_259 = QFrame(self.frame_213)
        self.frame_259.setObjectName(u"frame_259")
        self.frame_259.setStyleSheet(u"")
        self.frame_259.setFrameShape(QFrame.StyledPanel)
        self.frame_259.setFrameShadow(QFrame.Raised)
        self.verticalLayout_193 = QVBoxLayout(self.frame_259)
        self.verticalLayout_193.setSpacing(0)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.verticalLayout_193.setContentsMargins(0, 0, 0, 0)
        self.frame_260 = QFrame(self.frame_259)
        self.frame_260.setObjectName(u"frame_260")
        self.frame_260.setMinimumSize(QSize(0, 45))
        self.frame_260.setFrameShape(QFrame.StyledPanel)
        self.frame_260.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_260)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.frame_263 = QFrame(self.frame_260)
        self.frame_263.setObjectName(u"frame_263")
        self.frame_263.setMinimumSize(QSize(250, 0))
        self.frame_263.setStyleSheet(u"")
        self.frame_263.setFrameShape(QFrame.StyledPanel)
        self.frame_263.setFrameShadow(QFrame.Raised)
        self.verticalLayout_194 = QVBoxLayout(self.frame_263)
        self.verticalLayout_194.setSpacing(0)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.verticalLayout_194.setContentsMargins(5, 10, 5, 0)
        self.pequenoHistoricoEntrada_7 = QFrame(self.frame_263)
        self.pequenoHistoricoEntrada_7.setObjectName(u"pequenoHistoricoEntrada_7")
        self.pequenoHistoricoEntrada_7.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_7.setStyleSheet(u"")
        self.pequenoHistoricoEntrada_7.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.pequenoHistoricoEntrada_7)
        self.horizontalLayout_132.setSpacing(3)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(12, 3, 3, 3)
        self.frame_264 = QFrame(self.pequenoHistoricoEntrada_7)
        self.frame_264.setObjectName(u"frame_264")
        self.frame_264.setMinimumSize(QSize(112, 0))
        self.frame_264.setMaximumSize(QSize(112, 16777215))
        self.frame_264.setStyleSheet(u"")
        self.frame_264.setFrameShape(QFrame.StyledPanel)
        self.frame_264.setFrameShadow(QFrame.Raised)
        self.verticalLayout_195 = QVBoxLayout(self.frame_264)
        self.verticalLayout_195.setSpacing(0)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.verticalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.label_231 = QLabel(self.frame_264)
        self.label_231.setObjectName(u"label_231")
        font13 = QFont()
        font13.setFamilies([u"Segoe UI Semibold"])
        font13.setPointSize(11)
        self.label_231.setFont(font13)
        self.label_231.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_231.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_195.addWidget(self.label_231)


        self.horizontalLayout_132.addWidget(self.frame_264)

        self.frame_265 = QFrame(self.pequenoHistoricoEntrada_7)
        self.frame_265.setObjectName(u"frame_265")
        self.frame_265.setMinimumSize(QSize(110, 0))
        self.frame_265.setMaximumSize(QSize(110, 16777215))
        self.frame_265.setStyleSheet(u"")
        self.frame_265.setFrameShape(QFrame.StyledPanel)
        self.frame_265.setFrameShadow(QFrame.Raised)
        self.verticalLayout_196 = QVBoxLayout(self.frame_265)
        self.verticalLayout_196.setSpacing(0)
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.verticalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.label_232 = QLabel(self.frame_265)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setMaximumSize(QSize(16777215, 38))
        self.label_232.setFont(font13)
        self.label_232.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_232.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_196.addWidget(self.label_232)


        self.horizontalLayout_132.addWidget(self.frame_265)

        self.frame_266 = QFrame(self.pequenoHistoricoEntrada_7)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setMinimumSize(QSize(190, 0))
        self.frame_266.setMaximumSize(QSize(190, 16777215))
        self.frame_266.setStyleSheet(u"")
        self.frame_266.setFrameShape(QFrame.StyledPanel)
        self.frame_266.setFrameShadow(QFrame.Raised)
        self.verticalLayout_197 = QVBoxLayout(self.frame_266)
        self.verticalLayout_197.setSpacing(0)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.verticalLayout_197.setContentsMargins(0, 0, 0, 0)
        self.label_233 = QLabel(self.frame_266)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setFont(font13)
        self.label_233.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_233.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_197.addWidget(self.label_233)


        self.horizontalLayout_132.addWidget(self.frame_266)

        self.frame_283 = QFrame(self.pequenoHistoricoEntrada_7)
        self.frame_283.setObjectName(u"frame_283")
        self.frame_283.setMinimumSize(QSize(125, 0))
        self.frame_283.setMaximumSize(QSize(125, 16777215))
        self.frame_283.setStyleSheet(u"")
        self.frame_283.setFrameShape(QFrame.StyledPanel)
        self.frame_283.setFrameShadow(QFrame.Raised)
        self.verticalLayout_209 = QVBoxLayout(self.frame_283)
        self.verticalLayout_209.setSpacing(0)
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.verticalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.label_246 = QLabel(self.frame_283)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setFont(font13)
        self.label_246.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_246.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_209.addWidget(self.label_246)


        self.horizontalLayout_132.addWidget(self.frame_283)

        self.frame_284 = QFrame(self.pequenoHistoricoEntrada_7)
        self.frame_284.setObjectName(u"frame_284")
        self.frame_284.setMinimumSize(QSize(110, 0))
        self.frame_284.setMaximumSize(QSize(110, 16777215))
        self.frame_284.setStyleSheet(u"")
        self.frame_284.setFrameShape(QFrame.StyledPanel)
        self.frame_284.setFrameShadow(QFrame.Raised)
        self.verticalLayout_211 = QVBoxLayout(self.frame_284)
        self.verticalLayout_211.setSpacing(0)
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.verticalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.label_248 = QLabel(self.frame_284)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setFont(font13)
        self.label_248.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_248.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_211.addWidget(self.label_248)


        self.horizontalLayout_132.addWidget(self.frame_284)

        self.frame_267 = QFrame(self.pequenoHistoricoEntrada_7)
        self.frame_267.setObjectName(u"frame_267")
        self.frame_267.setMinimumSize(QSize(97, 0))
        self.frame_267.setMaximumSize(QSize(1234605, 16777215))
        self.frame_267.setStyleSheet(u"")
        self.frame_267.setFrameShape(QFrame.StyledPanel)
        self.frame_267.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_267)
        self.horizontalLayout_133.setSpacing(0)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_234 = QLabel(self.frame_267)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setMaximumSize(QSize(233, 16777215))
        self.label_234.setFont(font13)
        self.label_234.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_234.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_133.addWidget(self.label_234)


        self.horizontalLayout_132.addWidget(self.frame_267, 0, Qt.AlignLeft)

        self.frame_269 = QFrame(self.pequenoHistoricoEntrada_7)
        self.frame_269.setObjectName(u"frame_269")
        self.frame_269.setStyleSheet(u"")
        self.frame_269.setFrameShape(QFrame.StyledPanel)
        self.frame_269.setFrameShadow(QFrame.Raised)
        self.verticalLayout_198 = QVBoxLayout(self.frame_269)
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.verticalLayout_198.setContentsMargins(0, 0, 0, 0)
        self.label_235 = QLabel(self.frame_269)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setFont(font13)
        self.label_235.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_235.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_198.addWidget(self.label_235)


        self.horizontalLayout_132.addWidget(self.frame_269)

        self.frame_285 = QFrame(self.pequenoHistoricoEntrada_7)
        self.frame_285.setObjectName(u"frame_285")
        self.frame_285.setMaximumSize(QSize(80, 16777215))
        self.frame_285.setStyleSheet(u"")
        self.frame_285.setFrameShape(QFrame.StyledPanel)
        self.frame_285.setFrameShadow(QFrame.Raised)
        self.verticalLayout_212 = QVBoxLayout(self.frame_285)
        self.verticalLayout_212.setSpacing(0)
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.verticalLayout_212.setContentsMargins(0, 0, 0, 0)
        self.label_249 = QLabel(self.frame_285)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setFont(font13)
        self.label_249.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_249.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_212.addWidget(self.label_249)


        self.horizontalLayout_132.addWidget(self.frame_285)


        self.verticalLayout_194.addWidget(self.pequenoHistoricoEntrada_7)

        self.scrollArea_8 = QScrollArea(self.frame_263)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1034, 305))
        self.verticalLayout_199 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_199.setSpacing(0)
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.verticalLayout_199.setContentsMargins(0, 0, -1, 0)
        self.frame_10 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_ZonaPagarConta = QVBoxLayout(self.frame_10)
        self.verticalLayout_ZonaPagarConta.setSpacing(3)
        self.verticalLayout_ZonaPagarConta.setObjectName(u"verticalLayout_ZonaPagarConta")
        self.verticalLayout_ZonaPagarConta.setContentsMargins(3, 5, 3, 5)
        self.pequenoHistoricoEntrada_10 = QFrame(self.frame_10)
        self.pequenoHistoricoEntrada_10.setObjectName(u"pequenoHistoricoEntrada_10")
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
        self.label_247 = QLabel(self.frame_274)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setMaximumSize(QSize(150, 16777215))
        self.label_247.setFont(font13)
        self.label_247.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_247.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_210.addWidget(self.label_247)


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
        self.label_252 = QLabel(self.frame_289)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setMaximumSize(QSize(16777215, 38))
        self.label_252.setFont(font13)
        self.label_252.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_252.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_216.addWidget(self.label_252)


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
        self.label_253 = QLabel(self.frame_290)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setFont(font13)
        self.label_253.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_253.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_217.addWidget(self.label_253)


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
        self.label_254 = QLabel(self.frame_291)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setMaximumSize(QSize(16777215, 38))
        self.label_254.setFont(font13)
        self.label_254.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_254.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_218.addWidget(self.label_254)


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
        self.label_255 = QLabel(self.frame_292)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setMaximumSize(QSize(16777215, 38))
        self.label_255.setFont(font13)
        self.label_255.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_255.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_219.addWidget(self.label_255)


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
        self.label_256 = QLabel(self.frame_293)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setFont(font13)
        self.label_256.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_256.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_141.addWidget(self.label_256)


        self.horizontalLayout_137.addWidget(self.frame_293)

        self.frame_294 = QFrame(self.pequenoHistoricoEntrada_10)
        self.frame_294.setObjectName(u"frame_294")
        self.frame_294.setStyleSheet(u"")
        self.frame_294.setFrameShape(QFrame.StyledPanel)
        self.frame_294.setFrameShadow(QFrame.Raised)
        self.verticalLayout_220 = QVBoxLayout(self.frame_294)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.verticalLayout_220.setContentsMargins(7, 0, 0, 0)
        self.label_257 = QLabel(self.frame_294)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setMinimumSize(QSize(96, 0))
        self.label_257.setFont(font13)
        self.label_257.setStyleSheet(u"color:rgb(170, 85, 255)")
        self.label_257.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_220.addWidget(self.label_257)


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
        self.pushButton_22 = QPushButton(self.frame_295)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(62, 31))
        self.pushButton_22.setMaximumSize(QSize(57, 16777215))
        font14 = QFont()
        font14.setPointSize(9)
        font14.setBold(True)
        self.pushButton_22.setFont(font14)
        self.pushButton_22.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 0, 0);")

        self.verticalLayout_221.addWidget(self.pushButton_22, 0, Qt.AlignLeft)


        self.horizontalLayout_137.addWidget(self.frame_295)


        self.verticalLayout_ZonaPagarConta.addWidget(self.pequenoHistoricoEntrada_10)

        self.pequenoHistoricoEntrada_8 = QFrame(self.frame_10)
        self.pequenoHistoricoEntrada_8.setObjectName(u"pequenoHistoricoEntrada_8")
        self.pequenoHistoricoEntrada_8.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;")
        self.pequenoHistoricoEntrada_8.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.pequenoHistoricoEntrada_8)
        self.horizontalLayout_135.setSpacing(0)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(15, 0, 0, 0)
        self.frame_270 = QFrame(self.pequenoHistoricoEntrada_8)
        self.frame_270.setObjectName(u"frame_270")
        self.frame_270.setMinimumSize(QSize(110, 0))
        self.frame_270.setMaximumSize(QSize(110, 16777215))
        self.frame_270.setStyleSheet(u"")
        self.frame_270.setFrameShape(QFrame.StyledPanel)
        self.frame_270.setFrameShadow(QFrame.Raised)
        self.verticalLayout_200 = QVBoxLayout(self.frame_270)
        self.verticalLayout_200.setSpacing(0)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.label_236 = QLabel(self.frame_270)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setMaximumSize(QSize(150, 16777215))
        self.label_236.setFont(font13)
        self.label_236.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_236.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_200.addWidget(self.label_236)


        self.horizontalLayout_135.addWidget(self.frame_270)

        self.frame_271 = QFrame(self.pequenoHistoricoEntrada_8)
        self.frame_271.setObjectName(u"frame_271")
        self.frame_271.setMinimumSize(QSize(110, 0))
        self.frame_271.setMaximumSize(QSize(110, 16777215))
        self.frame_271.setStyleSheet(u"")
        self.frame_271.setFrameShape(QFrame.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Raised)
        self.verticalLayout_201 = QVBoxLayout(self.frame_271)
        self.verticalLayout_201.setSpacing(0)
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.verticalLayout_201.setContentsMargins(0, 0, 0, 0)
        self.label_237 = QLabel(self.frame_271)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setMaximumSize(QSize(16777215, 38))
        self.label_237.setFont(font13)
        self.label_237.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_237.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_201.addWidget(self.label_237)


        self.horizontalLayout_135.addWidget(self.frame_271)

        self.frame_272 = QFrame(self.pequenoHistoricoEntrada_8)
        self.frame_272.setObjectName(u"frame_272")
        self.frame_272.setMinimumSize(QSize(190, 0))
        self.frame_272.setMaximumSize(QSize(190, 16777215))
        self.frame_272.setStyleSheet(u"")
        self.frame_272.setFrameShape(QFrame.StyledPanel)
        self.frame_272.setFrameShadow(QFrame.Raised)
        self.verticalLayout_202 = QVBoxLayout(self.frame_272)
        self.verticalLayout_202.setSpacing(0)
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.verticalLayout_202.setContentsMargins(1, 0, 0, 0)
        self.label_238 = QLabel(self.frame_272)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setFont(font13)
        self.label_238.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_238.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_202.addWidget(self.label_238)


        self.horizontalLayout_135.addWidget(self.frame_272)

        self.frame_287 = QFrame(self.pequenoHistoricoEntrada_8)
        self.frame_287.setObjectName(u"frame_287")
        self.frame_287.setMinimumSize(QSize(125, 0))
        self.frame_287.setMaximumSize(QSize(125, 16777215))
        self.frame_287.setStyleSheet(u"")
        self.frame_287.setFrameShape(QFrame.StyledPanel)
        self.frame_287.setFrameShadow(QFrame.Raised)
        self.verticalLayout_214 = QVBoxLayout(self.frame_287)
        self.verticalLayout_214.setSpacing(0)
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.verticalLayout_214.setContentsMargins(3, 0, 0, 0)
        self.label_251 = QLabel(self.frame_287)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setMaximumSize(QSize(16777215, 38))
        self.label_251.setFont(font13)
        self.label_251.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_251.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_214.addWidget(self.label_251)


        self.horizontalLayout_135.addWidget(self.frame_287)

        self.frame_286 = QFrame(self.pequenoHistoricoEntrada_8)
        self.frame_286.setObjectName(u"frame_286")
        self.frame_286.setMinimumSize(QSize(117, 0))
        self.frame_286.setMaximumSize(QSize(119, 16777215))
        self.frame_286.setStyleSheet(u"")
        self.frame_286.setFrameShape(QFrame.StyledPanel)
        self.frame_286.setFrameShadow(QFrame.Raised)
        self.verticalLayout_213 = QVBoxLayout(self.frame_286)
        self.verticalLayout_213.setSpacing(0)
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.verticalLayout_213.setContentsMargins(10, 0, 0, 0)
        self.label_250 = QLabel(self.frame_286)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setMaximumSize(QSize(16777215, 38))
        self.label_250.setFont(font13)
        self.label_250.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_250.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_213.addWidget(self.label_250)


        self.horizontalLayout_135.addWidget(self.frame_286)

        self.frame_273 = QFrame(self.pequenoHistoricoEntrada_8)
        self.frame_273.setObjectName(u"frame_273")
        self.frame_273.setMaximumSize(QSize(12345678, 16777215))
        self.frame_273.setStyleSheet(u"")
        self.frame_273.setFrameShape(QFrame.StyledPanel)
        self.frame_273.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_273)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(2, 0, 0, 0)
        self.label_239 = QLabel(self.frame_273)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setFont(font13)
        self.label_239.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_239.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_136.addWidget(self.label_239)


        self.horizontalLayout_135.addWidget(self.frame_273)

        self.frame_275 = QFrame(self.pequenoHistoricoEntrada_8)
        self.frame_275.setObjectName(u"frame_275")
        self.frame_275.setStyleSheet(u"")
        self.frame_275.setFrameShape(QFrame.StyledPanel)
        self.frame_275.setFrameShadow(QFrame.Raised)
        self.verticalLayout_203 = QVBoxLayout(self.frame_275)
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.verticalLayout_203.setContentsMargins(7, 0, 0, 0)
        self.label_240 = QLabel(self.frame_275)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setMinimumSize(QSize(96, 0))
        self.label_240.setFont(font13)
        self.label_240.setStyleSheet(u"color:rgb(170, 85, 255)")
        self.label_240.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_203.addWidget(self.label_240)


        self.horizontalLayout_135.addWidget(self.frame_275)

        self.frame_288 = QFrame(self.pequenoHistoricoEntrada_8)
        self.frame_288.setObjectName(u"frame_288")
        self.frame_288.setMinimumSize(QSize(0, 25))
        self.frame_288.setMaximumSize(QSize(79, 35))
        self.frame_288.setStyleSheet(u"")
        self.frame_288.setFrameShape(QFrame.StyledPanel)
        self.frame_288.setFrameShadow(QFrame.Raised)
        self.verticalLayout_215 = QVBoxLayout(self.frame_288)
        self.verticalLayout_215.setSpacing(0)
        self.verticalLayout_215.setObjectName(u"verticalLayout_215")
        self.verticalLayout_215.setContentsMargins(0, 0, 0, 0)
        self.pushButton_21 = QPushButton(self.frame_288)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(35, 31))
        self.pushButton_21.setMaximumSize(QSize(35, 16777215))
        self.pushButton_21.setFont(font14)
        self.pushButton_21.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_215.addWidget(self.pushButton_21, 0, Qt.AlignLeft)


        self.horizontalLayout_135.addWidget(self.frame_288)


        self.verticalLayout_ZonaPagarConta.addWidget(self.pequenoHistoricoEntrada_8)


        self.verticalLayout_199.addWidget(self.frame_10)

        self.frame_282 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_282.setObjectName(u"frame_282")
        self.frame_282.setMaximumSize(QSize(16777215, 45))
        self.frame_282.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;}")
        self.frame_282.setFrameShape(QFrame.StyledPanel)
        self.frame_282.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_282)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_199.addWidget(self.frame_282)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_199.addItem(self.verticalSpacer_11)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_194.addWidget(self.scrollArea_8)


        self.horizontalLayout_91.addWidget(self.frame_263)

        self.frame_262 = QFrame(self.frame_260)
        self.frame_262.setObjectName(u"frame_262")
        self.frame_262.setMaximumSize(QSize(16777215, 70))
        self.frame_262.setStyleSheet(u"QFrame{\n"
"background-color: rgb(,0,0,0);\n"
"border-radius:10px;}")
        self.frame_262.setFrameShape(QFrame.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_262)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_91.addWidget(self.frame_262)


        self.verticalLayout_193.addWidget(self.frame_260)


        self.verticalLayout_184.addWidget(self.frame_259)


        self.verticalLayout_208.addWidget(self.frame_213)

        self.stackedWidget.addWidget(self.page_ControleDeContaAReceber)
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
        self.verticalLayout_32 = QVBoxLayout(self.frame_25)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_268 = QFrame(self.frame_25)
        self.frame_268.setObjectName(u"frame_268")
        self.frame_268.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(170, 85, 255);")
        self.frame_268.setFrameShape(QFrame.StyledPanel)
        self.frame_268.setFrameShadow(QFrame.Raised)
        self.verticalLayout_204 = QVBoxLayout(self.frame_268)
        self.verticalLayout_204.setSpacing(0)
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.verticalLayout_204.setContentsMargins(8, 0, 8, 0)
        self.frame_276 = QFrame(self.frame_268)
        self.frame_276.setObjectName(u"frame_276")
        self.frame_276.setMaximumSize(QSize(16777215, 250))
        self.frame_276.setStyleSheet(u"")
        self.frame_276.setFrameShape(QFrame.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Raised)
        self.verticalLayout_205 = QVBoxLayout(self.frame_276)
        self.verticalLayout_205.setSpacing(0)
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.verticalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.frame_277 = QFrame(self.frame_276)
        self.frame_277.setObjectName(u"frame_277")
        self.frame_277.setStyleSheet(u"")
        self.frame_277.setFrameShape(QFrame.StyledPanel)
        self.frame_277.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_277)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_278 = QFrame(self.frame_277)
        self.frame_278.setObjectName(u"frame_278")
        self.frame_278.setMinimumSize(QSize(0, 250))
        self.frame_278.setFont(font5)
        self.frame_278.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.frame_278.setFrameShape(QFrame.StyledPanel)
        self.frame_278.setFrameShadow(QFrame.Raised)
        self.verticalLayout_206 = QVBoxLayout(self.frame_278)
        self.verticalLayout_206.setSpacing(0)
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.verticalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.frame_279 = QFrame(self.frame_278)
        self.frame_279.setObjectName(u"frame_279")
        self.frame_279.setMinimumSize(QSize(0, 136))
        self.frame_279.setMaximumSize(QSize(16777215, 136))
        self.frame_279.setFrameShape(QFrame.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_279)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 5, 5, 0)
        self.frame_280 = QFrame(self.frame_279)
        self.frame_280.setObjectName(u"frame_280")
        self.frame_280.setMinimumSize(QSize(0, 131))
        self.frame_280.setMaximumSize(QSize(16777215, 131))
        self.frame_280.setFrameShape(QFrame.StyledPanel)
        self.frame_280.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_280)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(12, 10, 8, 7)
        self.frame_281 = QFrame(self.frame_280)
        self.frame_281.setObjectName(u"frame_281")
        self.frame_281.setMinimumSize(QSize(215, 0))
        self.frame_281.setMaximumSize(QSize(400, 16777215))
        self.frame_281.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_281.setFrameShape(QFrame.StyledPanel)
        self.frame_281.setFrameShadow(QFrame.Raised)
        self.verticalLayout_207 = QVBoxLayout(self.frame_281)
        self.verticalLayout_207.setSpacing(0)
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.verticalLayout_207.setContentsMargins(0, 0, 0, 0)
        self.frame_296 = QFrame(self.frame_281)
        self.frame_296.setObjectName(u"frame_296")
        self.frame_296.setFrameShape(QFrame.StyledPanel)
        self.frame_296.setFrameShadow(QFrame.Raised)
        self.pushButton_14 = QPushButton(self.frame_296)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(3, 15, 66, 57))
        self.pushButton_14.setIcon(icon19)
        self.pushButton_14.setIconSize(QSize(73, 73))
        self.label_174 = QLabel(self.frame_296)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(73, 33, 160, 26))
        self.label_174.setFont(font6)
        self.label_174.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_207.addWidget(self.frame_296)

        self.frame_297 = QFrame(self.frame_281)
        self.frame_297.setObjectName(u"frame_297")
        self.frame_297.setMaximumSize(QSize(16777215, 35))
        self.frame_297.setFrameShape(QFrame.StyledPanel)
        self.frame_297.setFrameShadow(QFrame.Raised)
        self.verticalLayout_222 = QVBoxLayout(self.frame_297)
        self.verticalLayout_222.setSpacing(0)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.verticalLayout_222.setContentsMargins(0, 0, 7, 7)
        self.label_175 = QLabel(self.frame_297)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMaximumSize(QSize(16777215, 35))
        self.label_175.setFont(font7)
        self.label_175.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_175.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_222.addWidget(self.label_175)


        self.verticalLayout_207.addWidget(self.frame_297)


        self.horizontalLayout_65.addWidget(self.frame_281)

        self.frame_298 = QFrame(self.frame_280)
        self.frame_298.setObjectName(u"frame_298")
        self.frame_298.setMinimumSize(QSize(215, 0))
        self.frame_298.setMaximumSize(QSize(400, 16777215))
        self.frame_298.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_298.setFrameShape(QFrame.StyledPanel)
        self.frame_298.setFrameShadow(QFrame.Raised)
        self.verticalLayout_223 = QVBoxLayout(self.frame_298)
        self.verticalLayout_223.setSpacing(0)
        self.verticalLayout_223.setObjectName(u"verticalLayout_223")
        self.verticalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.frame_299 = QFrame(self.frame_298)
        self.frame_299.setObjectName(u"frame_299")
        self.frame_299.setFrameShape(QFrame.StyledPanel)
        self.frame_299.setFrameShadow(QFrame.Raised)
        self.label_180 = QLabel(self.frame_299)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setGeometry(QRect(75, 33, 121, 26))
        self.label_180.setFont(font8)
        self.label_180.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_23 = QPushButton(self.frame_299)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(4, 27, 67, 46))
        self.pushButton_23.setIcon(icon20)
        self.pushButton_23.setIconSize(QSize(64, 68))

        self.verticalLayout_223.addWidget(self.frame_299)

        self.frame_300 = QFrame(self.frame_298)
        self.frame_300.setObjectName(u"frame_300")
        self.frame_300.setMaximumSize(QSize(16777212, 35))
        self.frame_300.setFrameShape(QFrame.StyledPanel)
        self.frame_300.setFrameShadow(QFrame.Raised)
        self.verticalLayout_224 = QVBoxLayout(self.frame_300)
        self.verticalLayout_224.setSpacing(0)
        self.verticalLayout_224.setObjectName(u"verticalLayout_224")
        self.verticalLayout_224.setContentsMargins(0, 0, 11, 7)
        self.label_192 = QLabel(self.frame_300)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setFont(font8)
        self.label_192.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_192.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_224.addWidget(self.label_192)


        self.verticalLayout_223.addWidget(self.frame_300)


        self.horizontalLayout_65.addWidget(self.frame_298)

        self.frame_301 = QFrame(self.frame_280)
        self.frame_301.setObjectName(u"frame_301")
        self.frame_301.setMinimumSize(QSize(215, 0))
        self.frame_301.setMaximumSize(QSize(400, 16777215))
        self.frame_301.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_301.setFrameShape(QFrame.StyledPanel)
        self.frame_301.setFrameShadow(QFrame.Raised)
        self.verticalLayout_225 = QVBoxLayout(self.frame_301)
        self.verticalLayout_225.setSpacing(0)
        self.verticalLayout_225.setObjectName(u"verticalLayout_225")
        self.verticalLayout_225.setContentsMargins(0, 0, 0, 0)
        self.frame_302 = QFrame(self.frame_301)
        self.frame_302.setObjectName(u"frame_302")
        self.frame_302.setFrameShape(QFrame.StyledPanel)
        self.frame_302.setFrameShadow(QFrame.Raised)
        self.label_193 = QLabel(self.frame_302)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(80, 33, 161, 26))
        self.label_193.setFont(font8)
        self.label_193.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_24 = QPushButton(self.frame_302)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(5, 5, 68, 60))
        self.pushButton_24.setIcon(icon21)
        self.pushButton_24.setIconSize(QSize(68, 73))

        self.verticalLayout_225.addWidget(self.frame_302)

        self.frame_303 = QFrame(self.frame_301)
        self.frame_303.setObjectName(u"frame_303")
        self.frame_303.setMaximumSize(QSize(16777212, 35))
        self.frame_303.setFrameShape(QFrame.StyledPanel)
        self.frame_303.setFrameShadow(QFrame.Raised)
        self.verticalLayout_226 = QVBoxLayout(self.frame_303)
        self.verticalLayout_226.setSpacing(0)
        self.verticalLayout_226.setObjectName(u"verticalLayout_226")
        self.verticalLayout_226.setContentsMargins(0, 0, 11, 7)
        self.label_196 = QLabel(self.frame_303)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setMaximumSize(QSize(16777215, 35))
        self.label_196.setFont(font8)
        self.label_196.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_196.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_226.addWidget(self.label_196)


        self.verticalLayout_225.addWidget(self.frame_303)


        self.horizontalLayout_65.addWidget(self.frame_301)


        self.horizontalLayout_64.addWidget(self.frame_280)

        self.frame_304 = QFrame(self.frame_279)
        self.frame_304.setObjectName(u"frame_304")
        self.frame_304.setMinimumSize(QSize(160, 0))
        self.frame_304.setMaximumSize(QSize(175, 16777215))
        self.frame_304.setFrameShape(QFrame.StyledPanel)
        self.frame_304.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_304)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.pushButton_25 = QPushButton(self.frame_304)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(150, 33))
        self.pushButton_25.setMaximumSize(QSize(12345, 33))
        self.pushButton_25.setFont(font9)
        self.pushButton_25.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_66.addWidget(self.pushButton_25, 0, Qt.AlignTop)


        self.horizontalLayout_64.addWidget(self.frame_304)


        self.verticalLayout_206.addWidget(self.frame_279)

        self.frame_305 = QFrame(self.frame_278)
        self.frame_305.setObjectName(u"frame_305")
        self.frame_305.setMaximumSize(QSize(16777215, 117))
        self.frame_305.setStyleSheet(u"")
        self.frame_305.setFrameShape(QFrame.StyledPanel)
        self.frame_305.setFrameShadow(QFrame.Raised)
        self.frame_305.setLineWidth(1)
        self.pushButton_26 = QPushButton(self.frame_305)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(506, 77, 80, 34))
        self.pushButton_26.setMinimumSize(QSize(80, 34))
        self.pushButton_26.setMaximumSize(QSize(80, 34))
        self.pushButton_26.setFont(font10)
        self.pushButton_26.setStyleSheet(u"QPushButton{\n"
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
        self.label_197 = QLabel(self.frame_305)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(261, 64, 91, 12))
        self.label_197.setMinimumSize(QSize(0, 12))
        self.label_197.setMaximumSize(QSize(16777215, 12))
        self.label_197.setFont(font11)
        self.label_197.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.comboBox_5 = QComboBox(self.frame_305)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(261, 80, 241, 31))
        self.comboBox_5.setMinimumSize(QSize(0, 31))
        self.comboBox_5.setMaximumSize(QSize(16777215, 31))
        self.comboBox_5.setFont(font11)
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
        self.BuscarStatus_4 = QLineEdit(self.frame_305)
        self.BuscarStatus_4.setObjectName(u"BuscarStatus_4")
        self.BuscarStatus_4.setGeometry(QRect(15, 27, 241, 31))
        self.BuscarStatus_4.setMinimumSize(QSize(170, 31))
        self.BuscarStatus_4.setMaximumSize(QSize(300, 30))
        self.BuscarStatus_4.setFont(font11)
        self.BuscarStatus_4.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:3px;")
        self.label_198 = QLabel(self.frame_305)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setGeometry(QRect(15, 0, 81, 18))
        self.label_198.setMaximumSize(QSize(16777215, 18))
        self.label_198.setFont(font11)
        self.label_198.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_199 = QLabel(self.frame_305)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(261, 0, 171, 18))
        self.label_199.setMaximumSize(QSize(16777215, 18))
        self.label_199.setFont(font11)
        self.label_199.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.comboBox_6 = QComboBox(self.frame_305)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(15, 80, 241, 31))
        self.comboBox_6.setMinimumSize(QSize(0, 31))
        self.comboBox_6.setMaximumSize(QSize(16777215, 31))
        self.comboBox_6.setFont(font11)
        self.comboBox_6.setStyleSheet(u"\n"
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
        self.label_202 = QLabel(self.frame_305)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(15, 61, 61, 17))
        self.label_202.setMaximumSize(QSize(16777215, 18))
        self.label_202.setFont(font11)
        self.label_202.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_207 = QLabel(self.frame_305)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(506, 0, 171, 18))
        self.label_207.setMaximumSize(QSize(16777215, 18))
        self.label_207.setFont(font11)
        self.label_207.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.dateEdit_7 = QDateEdit(self.frame_305)
        self.dateEdit_7.setObjectName(u"dateEdit_7")
        self.dateEdit_7.setGeometry(QRect(375, 27, 127, 30))
        self.dateEdit_7.setFont(font12)
        self.dateEdit_7.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_7.setReadOnly(False)
        self.dateEdit_7.setDate(QDate(2010, 1, 1))
        self.dateEdit_8 = QDateEdit(self.frame_305)
        self.dateEdit_8.setObjectName(u"dateEdit_8")
        self.dateEdit_8.setGeometry(QRect(261, 27, 127, 30))
        self.dateEdit_8.setFont(font12)
        self.dateEdit_8.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_8.setDate(QDate(2010, 1, 1))
        self.dateEdit_9 = QDateEdit(self.frame_305)
        self.dateEdit_9.setObjectName(u"dateEdit_9")
        self.dateEdit_9.setGeometry(QRect(619, 27, 127, 30))
        self.dateEdit_9.setFont(font12)
        self.dateEdit_9.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_9.setReadOnly(False)
        self.dateEdit_9.setDate(QDate(2010, 1, 1))
        self.dateEdit_10 = QDateEdit(self.frame_305)
        self.dateEdit_10.setObjectName(u"dateEdit_10")
        self.dateEdit_10.setGeometry(QRect(506, 27, 127, 30))
        self.dateEdit_10.setFont(font12)
        self.dateEdit_10.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_10.setDate(QDate(2010, 1, 1))

        self.verticalLayout_206.addWidget(self.frame_305)


        self.horizontalLayout_63.addWidget(self.frame_278)


        self.verticalLayout_205.addWidget(self.frame_277)


        self.verticalLayout_204.addWidget(self.frame_276)

        self.frame_306 = QFrame(self.frame_268)
        self.frame_306.setObjectName(u"frame_306")
        self.frame_306.setStyleSheet(u"")
        self.frame_306.setFrameShape(QFrame.StyledPanel)
        self.frame_306.setFrameShadow(QFrame.Raised)
        self.verticalLayout_227 = QVBoxLayout(self.frame_306)
        self.verticalLayout_227.setSpacing(0)
        self.verticalLayout_227.setObjectName(u"verticalLayout_227")
        self.verticalLayout_227.setContentsMargins(0, 0, 0, 0)
        self.frame_307 = QFrame(self.frame_306)
        self.frame_307.setObjectName(u"frame_307")
        self.frame_307.setMinimumSize(QSize(0, 45))
        self.frame_307.setFrameShape(QFrame.StyledPanel)
        self.frame_307.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_307)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_308 = QFrame(self.frame_307)
        self.frame_308.setObjectName(u"frame_308")
        self.frame_308.setMinimumSize(QSize(250, 0))
        self.frame_308.setStyleSheet(u"")
        self.frame_308.setFrameShape(QFrame.StyledPanel)
        self.frame_308.setFrameShadow(QFrame.Raised)
        self.verticalLayout_228 = QVBoxLayout(self.frame_308)
        self.verticalLayout_228.setSpacing(0)
        self.verticalLayout_228.setObjectName(u"verticalLayout_228")
        self.verticalLayout_228.setContentsMargins(5, 10, 5, 0)
        self.pequenoHistoricoEntrada_9 = QFrame(self.frame_308)
        self.pequenoHistoricoEntrada_9.setObjectName(u"pequenoHistoricoEntrada_9")
        self.pequenoHistoricoEntrada_9.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_9.setStyleSheet(u"")
        self.pequenoHistoricoEntrada_9.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.pequenoHistoricoEntrada_9)
        self.horizontalLayout_134.setSpacing(3)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(12, 3, 3, 3)
        self.frame_309 = QFrame(self.pequenoHistoricoEntrada_9)
        self.frame_309.setObjectName(u"frame_309")
        self.frame_309.setMinimumSize(QSize(112, 0))
        self.frame_309.setMaximumSize(QSize(112, 16777215))
        self.frame_309.setStyleSheet(u"")
        self.frame_309.setFrameShape(QFrame.StyledPanel)
        self.frame_309.setFrameShadow(QFrame.Raised)
        self.verticalLayout_229 = QVBoxLayout(self.frame_309)
        self.verticalLayout_229.setSpacing(0)
        self.verticalLayout_229.setObjectName(u"verticalLayout_229")
        self.verticalLayout_229.setContentsMargins(0, 0, 0, 0)
        self.label_241 = QLabel(self.frame_309)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setFont(font13)
        self.label_241.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_241.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_229.addWidget(self.label_241)


        self.horizontalLayout_134.addWidget(self.frame_309)

        self.frame_310 = QFrame(self.pequenoHistoricoEntrada_9)
        self.frame_310.setObjectName(u"frame_310")
        self.frame_310.setMinimumSize(QSize(110, 0))
        self.frame_310.setMaximumSize(QSize(110, 16777215))
        self.frame_310.setStyleSheet(u"")
        self.frame_310.setFrameShape(QFrame.StyledPanel)
        self.frame_310.setFrameShadow(QFrame.Raised)
        self.verticalLayout_230 = QVBoxLayout(self.frame_310)
        self.verticalLayout_230.setSpacing(0)
        self.verticalLayout_230.setObjectName(u"verticalLayout_230")
        self.verticalLayout_230.setContentsMargins(0, 0, 0, 0)
        self.label_242 = QLabel(self.frame_310)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setMaximumSize(QSize(16777215, 38))
        self.label_242.setFont(font13)
        self.label_242.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_242.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_230.addWidget(self.label_242)


        self.horizontalLayout_134.addWidget(self.frame_310)

        self.frame_311 = QFrame(self.pequenoHistoricoEntrada_9)
        self.frame_311.setObjectName(u"frame_311")
        self.frame_311.setMinimumSize(QSize(190, 0))
        self.frame_311.setMaximumSize(QSize(190, 16777215))
        self.frame_311.setStyleSheet(u"")
        self.frame_311.setFrameShape(QFrame.StyledPanel)
        self.frame_311.setFrameShadow(QFrame.Raised)
        self.verticalLayout_231 = QVBoxLayout(self.frame_311)
        self.verticalLayout_231.setSpacing(0)
        self.verticalLayout_231.setObjectName(u"verticalLayout_231")
        self.verticalLayout_231.setContentsMargins(0, 0, 0, 0)
        self.label_243 = QLabel(self.frame_311)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setFont(font13)
        self.label_243.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_243.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_231.addWidget(self.label_243)


        self.horizontalLayout_134.addWidget(self.frame_311)

        self.frame_312 = QFrame(self.pequenoHistoricoEntrada_9)
        self.frame_312.setObjectName(u"frame_312")
        self.frame_312.setMinimumSize(QSize(125, 0))
        self.frame_312.setMaximumSize(QSize(125, 16777215))
        self.frame_312.setStyleSheet(u"")
        self.frame_312.setFrameShape(QFrame.StyledPanel)
        self.frame_312.setFrameShadow(QFrame.Raised)
        self.verticalLayout_232 = QVBoxLayout(self.frame_312)
        self.verticalLayout_232.setSpacing(0)
        self.verticalLayout_232.setObjectName(u"verticalLayout_232")
        self.verticalLayout_232.setContentsMargins(0, 0, 0, 0)
        self.label_258 = QLabel(self.frame_312)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setFont(font13)
        self.label_258.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_258.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_232.addWidget(self.label_258)


        self.horizontalLayout_134.addWidget(self.frame_312)

        self.frame_313 = QFrame(self.pequenoHistoricoEntrada_9)
        self.frame_313.setObjectName(u"frame_313")
        self.frame_313.setMinimumSize(QSize(110, 0))
        self.frame_313.setMaximumSize(QSize(110, 16777215))
        self.frame_313.setStyleSheet(u"")
        self.frame_313.setFrameShape(QFrame.StyledPanel)
        self.frame_313.setFrameShadow(QFrame.Raised)
        self.verticalLayout_233 = QVBoxLayout(self.frame_313)
        self.verticalLayout_233.setSpacing(0)
        self.verticalLayout_233.setObjectName(u"verticalLayout_233")
        self.verticalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.label_259 = QLabel(self.frame_313)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setFont(font13)
        self.label_259.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_259.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_233.addWidget(self.label_259)


        self.horizontalLayout_134.addWidget(self.frame_313)

        self.frame_314 = QFrame(self.pequenoHistoricoEntrada_9)
        self.frame_314.setObjectName(u"frame_314")
        self.frame_314.setMinimumSize(QSize(97, 0))
        self.frame_314.setMaximumSize(QSize(1234605, 16777215))
        self.frame_314.setStyleSheet(u"")
        self.frame_314.setFrameShape(QFrame.StyledPanel)
        self.frame_314.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_314)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_244 = QLabel(self.frame_314)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setMaximumSize(QSize(233, 16777215))
        self.label_244.setFont(font13)
        self.label_244.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_244.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_138.addWidget(self.label_244)


        self.horizontalLayout_134.addWidget(self.frame_314, 0, Qt.AlignLeft)

        self.frame_315 = QFrame(self.pequenoHistoricoEntrada_9)
        self.frame_315.setObjectName(u"frame_315")
        self.frame_315.setStyleSheet(u"")
        self.frame_315.setFrameShape(QFrame.StyledPanel)
        self.frame_315.setFrameShadow(QFrame.Raised)
        self.verticalLayout_234 = QVBoxLayout(self.frame_315)
        self.verticalLayout_234.setObjectName(u"verticalLayout_234")
        self.verticalLayout_234.setContentsMargins(0, 0, 0, 0)
        self.label_245 = QLabel(self.frame_315)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setFont(font13)
        self.label_245.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_245.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_234.addWidget(self.label_245)


        self.horizontalLayout_134.addWidget(self.frame_315)

        self.frame_316 = QFrame(self.pequenoHistoricoEntrada_9)
        self.frame_316.setObjectName(u"frame_316")
        self.frame_316.setMaximumSize(QSize(80, 16777215))
        self.frame_316.setStyleSheet(u"")
        self.frame_316.setFrameShape(QFrame.StyledPanel)
        self.frame_316.setFrameShadow(QFrame.Raised)
        self.verticalLayout_235 = QVBoxLayout(self.frame_316)
        self.verticalLayout_235.setSpacing(0)
        self.verticalLayout_235.setObjectName(u"verticalLayout_235")
        self.verticalLayout_235.setContentsMargins(0, 0, 0, 0)
        self.label_260 = QLabel(self.frame_316)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setFont(font13)
        self.label_260.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_260.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_235.addWidget(self.label_260)


        self.horizontalLayout_134.addWidget(self.frame_316)


        self.verticalLayout_228.addWidget(self.pequenoHistoricoEntrada_9)

        self.scrollArea_9 = QScrollArea(self.frame_308)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1034, 305))
        self.verticalLayout_236 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_236.setSpacing(3)
        self.verticalLayout_236.setObjectName(u"verticalLayout_236")
        self.verticalLayout_236.setContentsMargins(-1, 0, -1, -1)
        self.pequenoHistoricoEntrada_11 = QFrame(self.scrollAreaWidgetContents_7)
        self.pequenoHistoricoEntrada_11.setObjectName(u"pequenoHistoricoEntrada_11")
        self.pequenoHistoricoEntrada_11.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;")
        self.pequenoHistoricoEntrada_11.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.pequenoHistoricoEntrada_11)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(15, 0, 0, 0)
        self.frame_317 = QFrame(self.pequenoHistoricoEntrada_11)
        self.frame_317.setObjectName(u"frame_317")
        self.frame_317.setMinimumSize(QSize(110, 0))
        self.frame_317.setMaximumSize(QSize(110, 16777215))
        self.frame_317.setStyleSheet(u"")
        self.frame_317.setFrameShape(QFrame.StyledPanel)
        self.frame_317.setFrameShadow(QFrame.Raised)
        self.verticalLayout_237 = QVBoxLayout(self.frame_317)
        self.verticalLayout_237.setSpacing(0)
        self.verticalLayout_237.setObjectName(u"verticalLayout_237")
        self.verticalLayout_237.setContentsMargins(0, 0, 0, 0)
        self.label_261 = QLabel(self.frame_317)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setMaximumSize(QSize(150, 16777215))
        self.label_261.setFont(font13)
        self.label_261.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_261.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_237.addWidget(self.label_261)


        self.horizontalLayout_139.addWidget(self.frame_317)

        self.frame_318 = QFrame(self.pequenoHistoricoEntrada_11)
        self.frame_318.setObjectName(u"frame_318")
        self.frame_318.setMinimumSize(QSize(110, 0))
        self.frame_318.setMaximumSize(QSize(110, 16777215))
        self.frame_318.setStyleSheet(u"")
        self.frame_318.setFrameShape(QFrame.StyledPanel)
        self.frame_318.setFrameShadow(QFrame.Raised)
        self.verticalLayout_238 = QVBoxLayout(self.frame_318)
        self.verticalLayout_238.setSpacing(0)
        self.verticalLayout_238.setObjectName(u"verticalLayout_238")
        self.verticalLayout_238.setContentsMargins(0, 0, 0, 0)
        self.label_262 = QLabel(self.frame_318)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setMaximumSize(QSize(16777215, 38))
        self.label_262.setFont(font13)
        self.label_262.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_262.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_238.addWidget(self.label_262)


        self.horizontalLayout_139.addWidget(self.frame_318)

        self.frame_319 = QFrame(self.pequenoHistoricoEntrada_11)
        self.frame_319.setObjectName(u"frame_319")
        self.frame_319.setMinimumSize(QSize(190, 0))
        self.frame_319.setMaximumSize(QSize(190, 16777215))
        self.frame_319.setStyleSheet(u"")
        self.frame_319.setFrameShape(QFrame.StyledPanel)
        self.frame_319.setFrameShadow(QFrame.Raised)
        self.verticalLayout_239 = QVBoxLayout(self.frame_319)
        self.verticalLayout_239.setSpacing(0)
        self.verticalLayout_239.setObjectName(u"verticalLayout_239")
        self.verticalLayout_239.setContentsMargins(1, 0, 0, 0)
        self.label_263 = QLabel(self.frame_319)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setFont(font13)
        self.label_263.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_263.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_239.addWidget(self.label_263)


        self.horizontalLayout_139.addWidget(self.frame_319)

        self.frame_320 = QFrame(self.pequenoHistoricoEntrada_11)
        self.frame_320.setObjectName(u"frame_320")
        self.frame_320.setMinimumSize(QSize(125, 0))
        self.frame_320.setMaximumSize(QSize(125, 16777215))
        self.frame_320.setStyleSheet(u"")
        self.frame_320.setFrameShape(QFrame.StyledPanel)
        self.frame_320.setFrameShadow(QFrame.Raised)
        self.verticalLayout_240 = QVBoxLayout(self.frame_320)
        self.verticalLayout_240.setSpacing(0)
        self.verticalLayout_240.setObjectName(u"verticalLayout_240")
        self.verticalLayout_240.setContentsMargins(3, 0, 0, 0)
        self.label_264 = QLabel(self.frame_320)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setMaximumSize(QSize(16777215, 38))
        self.label_264.setFont(font13)
        self.label_264.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_264.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_240.addWidget(self.label_264)


        self.horizontalLayout_139.addWidget(self.frame_320)

        self.frame_321 = QFrame(self.pequenoHistoricoEntrada_11)
        self.frame_321.setObjectName(u"frame_321")
        self.frame_321.setMinimumSize(QSize(117, 0))
        self.frame_321.setMaximumSize(QSize(119, 16777215))
        self.frame_321.setStyleSheet(u"")
        self.frame_321.setFrameShape(QFrame.StyledPanel)
        self.frame_321.setFrameShadow(QFrame.Raised)
        self.verticalLayout_241 = QVBoxLayout(self.frame_321)
        self.verticalLayout_241.setSpacing(0)
        self.verticalLayout_241.setObjectName(u"verticalLayout_241")
        self.verticalLayout_241.setContentsMargins(10, 0, 0, 0)
        self.label_265 = QLabel(self.frame_321)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setMaximumSize(QSize(16777215, 38))
        self.label_265.setFont(font13)
        self.label_265.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_265.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_241.addWidget(self.label_265)


        self.horizontalLayout_139.addWidget(self.frame_321)

        self.frame_322 = QFrame(self.pequenoHistoricoEntrada_11)
        self.frame_322.setObjectName(u"frame_322")
        self.frame_322.setMaximumSize(QSize(12345678, 16777215))
        self.frame_322.setStyleSheet(u"")
        self.frame_322.setFrameShape(QFrame.StyledPanel)
        self.frame_322.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.frame_322)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(2, 0, 0, 0)
        self.label_266 = QLabel(self.frame_322)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setFont(font13)
        self.label_266.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_266.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_140.addWidget(self.label_266)


        self.horizontalLayout_139.addWidget(self.frame_322)

        self.frame_323 = QFrame(self.pequenoHistoricoEntrada_11)
        self.frame_323.setObjectName(u"frame_323")
        self.frame_323.setStyleSheet(u"")
        self.frame_323.setFrameShape(QFrame.StyledPanel)
        self.frame_323.setFrameShadow(QFrame.Raised)
        self.verticalLayout_242 = QVBoxLayout(self.frame_323)
        self.verticalLayout_242.setObjectName(u"verticalLayout_242")
        self.verticalLayout_242.setContentsMargins(7, 0, 0, 0)
        self.label_267 = QLabel(self.frame_323)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setMinimumSize(QSize(96, 0))
        self.label_267.setFont(font13)
        self.label_267.setStyleSheet(u"color:rgb(170, 85, 255)")
        self.label_267.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_242.addWidget(self.label_267)


        self.horizontalLayout_139.addWidget(self.frame_323)

        self.frame_324 = QFrame(self.pequenoHistoricoEntrada_11)
        self.frame_324.setObjectName(u"frame_324")
        self.frame_324.setMinimumSize(QSize(0, 25))
        self.frame_324.setMaximumSize(QSize(79, 35))
        self.frame_324.setStyleSheet(u"")
        self.frame_324.setFrameShape(QFrame.StyledPanel)
        self.frame_324.setFrameShadow(QFrame.Raised)
        self.verticalLayout_243 = QVBoxLayout(self.frame_324)
        self.verticalLayout_243.setSpacing(0)
        self.verticalLayout_243.setObjectName(u"verticalLayout_243")
        self.verticalLayout_243.setContentsMargins(0, 0, 0, 0)
        self.pushButton_27 = QPushButton(self.frame_324)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(35, 31))
        self.pushButton_27.setMaximumSize(QSize(35, 16777215))
        font15 = QFont()
        font15.setPointSize(8)
        font15.setBold(False)
        self.pushButton_27.setFont(font15)
        self.pushButton_27.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_243.addWidget(self.pushButton_27, 0, Qt.AlignLeft)


        self.horizontalLayout_139.addWidget(self.frame_324)


        self.verticalLayout_236.addWidget(self.pequenoHistoricoEntrada_11)

        self.pequenoHistoricoEntrada_12 = QFrame(self.scrollAreaWidgetContents_7)
        self.pequenoHistoricoEntrada_12.setObjectName(u"pequenoHistoricoEntrada_12")
        self.pequenoHistoricoEntrada_12.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:4px;")
        self.pequenoHistoricoEntrada_12.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.pequenoHistoricoEntrada_12)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(15, 0, 0, 0)
        self.frame_325 = QFrame(self.pequenoHistoricoEntrada_12)
        self.frame_325.setObjectName(u"frame_325")
        self.frame_325.setMinimumSize(QSize(110, 0))
        self.frame_325.setMaximumSize(QSize(110, 16777215))
        self.frame_325.setStyleSheet(u"")
        self.frame_325.setFrameShape(QFrame.StyledPanel)
        self.frame_325.setFrameShadow(QFrame.Raised)
        self.verticalLayout_244 = QVBoxLayout(self.frame_325)
        self.verticalLayout_244.setSpacing(0)
        self.verticalLayout_244.setObjectName(u"verticalLayout_244")
        self.verticalLayout_244.setContentsMargins(0, 0, 0, 0)
        self.label_268 = QLabel(self.frame_325)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setMaximumSize(QSize(150, 16777215))
        self.label_268.setFont(font13)
        self.label_268.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_268.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_244.addWidget(self.label_268)


        self.horizontalLayout_142.addWidget(self.frame_325)

        self.frame_326 = QFrame(self.pequenoHistoricoEntrada_12)
        self.frame_326.setObjectName(u"frame_326")
        self.frame_326.setMinimumSize(QSize(110, 0))
        self.frame_326.setMaximumSize(QSize(110, 16777215))
        self.frame_326.setStyleSheet(u"")
        self.frame_326.setFrameShape(QFrame.StyledPanel)
        self.frame_326.setFrameShadow(QFrame.Raised)
        self.verticalLayout_245 = QVBoxLayout(self.frame_326)
        self.verticalLayout_245.setSpacing(0)
        self.verticalLayout_245.setObjectName(u"verticalLayout_245")
        self.verticalLayout_245.setContentsMargins(0, 0, 0, 0)
        self.label_269 = QLabel(self.frame_326)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setMaximumSize(QSize(16777215, 38))
        self.label_269.setFont(font13)
        self.label_269.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_269.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_245.addWidget(self.label_269)


        self.horizontalLayout_142.addWidget(self.frame_326)

        self.frame_327 = QFrame(self.pequenoHistoricoEntrada_12)
        self.frame_327.setObjectName(u"frame_327")
        self.frame_327.setMinimumSize(QSize(190, 0))
        self.frame_327.setMaximumSize(QSize(190, 16777215))
        self.frame_327.setStyleSheet(u"")
        self.frame_327.setFrameShape(QFrame.StyledPanel)
        self.frame_327.setFrameShadow(QFrame.Raised)
        self.verticalLayout_246 = QVBoxLayout(self.frame_327)
        self.verticalLayout_246.setSpacing(0)
        self.verticalLayout_246.setObjectName(u"verticalLayout_246")
        self.verticalLayout_246.setContentsMargins(1, 0, 0, 0)
        self.label_270 = QLabel(self.frame_327)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setFont(font13)
        self.label_270.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_270.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_246.addWidget(self.label_270)


        self.horizontalLayout_142.addWidget(self.frame_327)

        self.frame_328 = QFrame(self.pequenoHistoricoEntrada_12)
        self.frame_328.setObjectName(u"frame_328")
        self.frame_328.setMinimumSize(QSize(125, 0))
        self.frame_328.setMaximumSize(QSize(125, 16777215))
        self.frame_328.setStyleSheet(u"")
        self.frame_328.setFrameShape(QFrame.StyledPanel)
        self.frame_328.setFrameShadow(QFrame.Raised)
        self.verticalLayout_247 = QVBoxLayout(self.frame_328)
        self.verticalLayout_247.setSpacing(0)
        self.verticalLayout_247.setObjectName(u"verticalLayout_247")
        self.verticalLayout_247.setContentsMargins(3, 0, 0, 0)
        self.label_271 = QLabel(self.frame_328)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setMaximumSize(QSize(16777215, 38))
        self.label_271.setFont(font13)
        self.label_271.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_271.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_247.addWidget(self.label_271)


        self.horizontalLayout_142.addWidget(self.frame_328)

        self.frame_329 = QFrame(self.pequenoHistoricoEntrada_12)
        self.frame_329.setObjectName(u"frame_329")
        self.frame_329.setMinimumSize(QSize(117, 0))
        self.frame_329.setMaximumSize(QSize(119, 16777215))
        self.frame_329.setStyleSheet(u"")
        self.frame_329.setFrameShape(QFrame.StyledPanel)
        self.frame_329.setFrameShadow(QFrame.Raised)
        self.verticalLayout_248 = QVBoxLayout(self.frame_329)
        self.verticalLayout_248.setSpacing(0)
        self.verticalLayout_248.setObjectName(u"verticalLayout_248")
        self.verticalLayout_248.setContentsMargins(10, 0, 0, 0)
        self.label_272 = QLabel(self.frame_329)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setMaximumSize(QSize(16777215, 38))
        self.label_272.setFont(font13)
        self.label_272.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_272.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_248.addWidget(self.label_272)


        self.horizontalLayout_142.addWidget(self.frame_329)

        self.frame_330 = QFrame(self.pequenoHistoricoEntrada_12)
        self.frame_330.setObjectName(u"frame_330")
        self.frame_330.setMaximumSize(QSize(12345678, 16777215))
        self.frame_330.setStyleSheet(u"")
        self.frame_330.setFrameShape(QFrame.StyledPanel)
        self.frame_330.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_330)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(2, 0, 0, 0)
        self.label_273 = QLabel(self.frame_330)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setFont(font13)
        self.label_273.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_273.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_143.addWidget(self.label_273)


        self.horizontalLayout_142.addWidget(self.frame_330)

        self.frame_331 = QFrame(self.pequenoHistoricoEntrada_12)
        self.frame_331.setObjectName(u"frame_331")
        self.frame_331.setStyleSheet(u"")
        self.frame_331.setFrameShape(QFrame.StyledPanel)
        self.frame_331.setFrameShadow(QFrame.Raised)
        self.verticalLayout_249 = QVBoxLayout(self.frame_331)
        self.verticalLayout_249.setObjectName(u"verticalLayout_249")
        self.verticalLayout_249.setContentsMargins(7, 0, 0, 0)
        self.label_274 = QLabel(self.frame_331)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setMinimumSize(QSize(96, 0))
        self.label_274.setFont(font13)
        self.label_274.setStyleSheet(u"color:rgb(170, 85, 255)")
        self.label_274.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_249.addWidget(self.label_274)


        self.horizontalLayout_142.addWidget(self.frame_331)

        self.frame_332 = QFrame(self.pequenoHistoricoEntrada_12)
        self.frame_332.setObjectName(u"frame_332")
        self.frame_332.setMinimumSize(QSize(0, 25))
        self.frame_332.setMaximumSize(QSize(79, 35))
        self.frame_332.setStyleSheet(u"")
        self.frame_332.setFrameShape(QFrame.StyledPanel)
        self.frame_332.setFrameShadow(QFrame.Raised)
        self.verticalLayout_250 = QVBoxLayout(self.frame_332)
        self.verticalLayout_250.setSpacing(0)
        self.verticalLayout_250.setObjectName(u"verticalLayout_250")
        self.verticalLayout_250.setContentsMargins(0, 0, 0, 0)
        self.pushButton_28 = QPushButton(self.frame_332)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(62, 31))
        self.pushButton_28.setMaximumSize(QSize(57, 16777215))
        self.pushButton_28.setFont(font15)
        self.pushButton_28.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"border-radius:5px;\n"
"color: rgb(170, 85, 255);")

        self.verticalLayout_250.addWidget(self.pushButton_28, 0, Qt.AlignLeft)


        self.horizontalLayout_142.addWidget(self.frame_332)


        self.verticalLayout_236.addWidget(self.pequenoHistoricoEntrada_12)

        self.frame_333 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_333.setObjectName(u"frame_333")
        self.frame_333.setMaximumSize(QSize(16777215, 45))
        self.frame_333.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;}")
        self.frame_333.setFrameShape(QFrame.StyledPanel)
        self.frame_333.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_333)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_236.addWidget(self.frame_333)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_236.addItem(self.verticalSpacer_12)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_228.addWidget(self.scrollArea_9)


        self.horizontalLayout_93.addWidget(self.frame_308)

        self.frame_334 = QFrame(self.frame_307)
        self.frame_334.setObjectName(u"frame_334")
        self.frame_334.setMaximumSize(QSize(16777215, 70))
        self.frame_334.setStyleSheet(u"QFrame{\n"
"background-color: rgb(,0,0,0);\n"
"border-radius:10px;}")
        self.frame_334.setFrameShape(QFrame.StyledPanel)
        self.frame_334.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_334)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_93.addWidget(self.frame_334)


        self.verticalLayout_227.addWidget(self.frame_307)


        self.verticalLayout_204.addWidget(self.frame_306)


        self.verticalLayout_32.addWidget(self.frame_268)


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
        font16 = QFont()
        font16.setPointSize(17)
        self.frame_Browsin_history_lbl.setFont(font16)
        self.frame_Browsin_history_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_Browsin_history_btn = QPushButton(self.frame_Browsin_history)
        self.frame_Browsin_history_btn.setObjectName(u"frame_Browsin_history_btn")
        self.frame_Browsin_history_btn.setGeometry(QRect(13, 13, 90, 71))
        icon22 = QIcon()
        icon22.addFile(u"../img/web_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_Browsin_history_btn.setIcon(icon22)
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
        icon23 = QIcon()
        icon23.addFile(u"../img/close_pane_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_opening_history_btn.setIcon(icon23)
        self.frame_opening_history_btn.setIconSize(QSize(100, 100))
        self.frame_opening_history_lbl = QLabel(self.frame_opening_history)
        self.frame_opening_history_lbl.setObjectName(u"frame_opening_history_lbl")
        self.frame_opening_history_lbl.setGeometry(QRect(16, 100, 171, 30))
        font17 = QFont()
        font17.setPointSize(12)
        self.frame_opening_history_lbl.setFont(font17)
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
        icon24 = QIcon()
        icon24.addFile(u"../img/user_menu_female_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_user_list_btn.setIcon(icon24)
        self.frame_user_list_btn.setIconSize(QSize(115, 115))
        self.frame_user_list_lbl = QLabel(self.frame_user_list)
        self.frame_user_list_lbl.setObjectName(u"frame_user_list_lbl")
        self.frame_user_list_lbl.setGeometry(QRect(10, 100, 171, 30))
        self.frame_user_list_lbl.setFont(font16)
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
        icon25 = QIcon()
        icon25.addFile(u"../img/instagram_logo_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.password_faceId_btn_2.setIcon(icon25)
        self.password_faceId_btn_2.setIconSize(QSize(110, 130))
        self.lineEdit_2 = QLineEdit(self.frame_password_faceId)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(59, 53, 106, 32))
        font18 = QFont()
        font18.setPointSize(15)
        self.lineEdit_2.setFont(font18)
        self.lineEdit_2.setStyleSheet(u"border-radius:7px;\n"
"color:rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px solid rgb(170, 85, 255)")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.password_faceId_lbl_6 = QLabel(self.frame_password_faceId)
        self.password_faceId_lbl_6.setObjectName(u"password_faceId_lbl_6")
        self.password_faceId_lbl_6.setGeometry(QRect(18, 101, 186, 30))
        self.password_faceId_lbl_6.setFont(font17)
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
        self.ios_lbl_2.setFont(font17)
        self.ios_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ios_btn_2 = QPushButton(self.frame_IOs_2)
        self.ios_btn_2.setObjectName(u"ios_btn_2")
        self.ios_btn_2.setGeometry(QRect(7, 7, 50, 50))
        icon26 = QIcon()
        icon26.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/mac_client_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ios_btn_2.setIcon(icon26)
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
        self.ibm_lbl_2.setFont(font17)
        self.ibm_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ibm_btn_2 = QPushButton(self.frame_IBM_2)
        self.ibm_btn_2.setObjectName(u"ibm_btn_2")
        self.ibm_btn_2.setGeometry(QRect(10, 15, 50, 30))
        icon27 = QIcon()
        icon27.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/ibm_70px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ibm_btn_2.setIcon(icon27)
        self.ibm_btn_2.setIconSize(QSize(50, 50))

        self.horizontalLayout_108.addWidget(self.frame_IBM_2)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_251.addWidget(self.scrollArea_6, 0, Qt.AlignBottom)


        self.verticalLayout_252.addWidget(self.frame_363)

        self.line_3 = QFrame(self.frame_101)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_252.addWidget(self.line_3)

        self.frame_167 = QFrame(self.frame_101)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setMinimumSize(QSize(3, 0))
        self.frame_167.setMaximumSize(QSize(123456, 16777215))
        self.frame_167.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(170, 85, 255);\n"
"	width: 18px;\n"
"	height: 18px;\n"
"	border-radius: 12px;\n"
"    background: rgb(41, 42, 65);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(165, 83, 248);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(170, 85, 255);\n"
"	border: 3px solid rgb(41, 42, 65)\n"
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
        self.page_perfilUsuario = QWidget()
        self.page_perfilUsuario.setObjectName(u"page_perfilUsuario")
        self.verticalLayout_149 = QVBoxLayout(self.page_perfilUsuario)
        self.verticalLayout_149.setSpacing(0)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.frame_232 = QFrame(self.page_perfilUsuario)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setMinimumSize(QSize(0, 63))
        self.frame_232.setMaximumSize(QSize(16777215, 81))
        self.frame_232.setFrameShape(QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Raised)
        self.frame_Browsin_history_lbl_2 = QLabel(self.frame_232)
        self.frame_Browsin_history_lbl_2.setObjectName(u"frame_Browsin_history_lbl_2")
        self.frame_Browsin_history_lbl_2.setGeometry(QRect(10, 16, 251, 41))
        self.frame_Browsin_history_lbl_2.setMaximumSize(QSize(366, 59))
        font19 = QFont()
        font19.setPointSize(25)
        self.frame_Browsin_history_lbl_2.setFont(font19)
        self.frame_Browsin_history_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_149.addWidget(self.frame_232)

        self.frame_226 = QFrame(self.page_perfilUsuario)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setFrameShape(QFrame.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_226)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.frame_231 = QFrame(self.frame_226)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setMinimumSize(QSize(270, 0))
        self.frame_231.setMaximumSize(QSize(270, 16777206))
        self.frame_231.setFrameShape(QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_231)
        self.verticalLayout_155.setSpacing(0)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.frame_234 = QFrame(self.frame_231)
        self.frame_234.setObjectName(u"frame_234")
        self.frame_234.setMinimumSize(QSize(0, 250))
        self.frame_234.setMaximumSize(QSize(16777215, 250))
        self.frame_234.setFrameShape(QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_234)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 200, 110, 35))
        self.pushButton.setFont(font17)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_223 = QFrame(self.frame_234)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setGeometry(QRect(40, 10, 161, 171))
        self.frame_223.setStyleSheet(u"QFrame{\n"
"border: 1px solid rgb(170, 85, 255);\n"
"border-radius: 20px;\n"
"}")
        self.frame_223.setFrameShape(QFrame.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_223)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_223)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon28 = QIcon()
        icon28.addFile(u"../img/daniel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon28)
        self.pushButton_13.setIconSize(QSize(147, 154))

        self.verticalLayout_150.addWidget(self.pushButton_13)


        self.verticalLayout_155.addWidget(self.frame_234)

        self.frame_236 = QFrame(self.frame_231)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_236)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, 18, 0, 0)

        self.verticalLayout_155.addWidget(self.frame_236)


        self.horizontalLayout_97.addWidget(self.frame_231)

        self.frame_225 = QFrame(self.frame_226)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setFrameShape(QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.frame_225)
        self.verticalLayout_152.setSpacing(0)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.verticalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.frame_lineEditPerfil = QFrame(self.frame_225)
        self.frame_lineEditPerfil.setObjectName(u"frame_lineEditPerfil")
        self.frame_lineEditPerfil.setFrameShape(QFrame.StyledPanel)
        self.frame_lineEditPerfil.setFrameShadow(QFrame.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.frame_lineEditPerfil)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(0, 0, 12, 10)
        self.verticalLayout_151 = QVBoxLayout()
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setSpacing(42)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.label_189 = QLabel(self.frame_lineEditPerfil)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setMinimumSize(QSize(0, 30))
        self.label_189.setMaximumSize(QSize(16777215, 30))
        self.label_189.setFont(font13)
        self.label_189.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.horizontalLayout_104.addWidget(self.label_189)

        self.label_201 = QLabel(self.frame_lineEditPerfil)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setMinimumSize(QSize(0, 30))
        self.label_201.setMaximumSize(QSize(16777215, 30))
        self.label_201.setFont(font13)
        self.label_201.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.horizontalLayout_104.addWidget(self.label_201)


        self.verticalLayout_151.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setSpacing(40)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.lineEdit = QLineEdit(self.frame_lineEditPerfil)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 40))
        self.lineEdit.setFont(font17)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(170, 85, 255);\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(170, 85, 255);		\n"
"border-radius:9px;\n"
"padding-left:5px}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(247, 248, 248);\n"
"border: 2px solid rgb(170, 85, 255);		\n"
"border-radius:8px}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(247, 248, 248);\n"
"border: 2px solid rgb(170, 85, 255);		\n"
"border-radius:8px}")

        self.horizontalLayout_103.addWidget(self.lineEdit)

        self.lineEdit_3 = QLineEdit(self.frame_lineEditPerfil)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_3.setFont(font17)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"color: rgb(170, 85, 255);\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(170, 85, 255);		\n"
"border-radius:8px;\n"
"padding-left:5px}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(247, 248, 248);\n"
"border: 2px solid rgb(170, 85, 255);		\n"
"border-radius:8px}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(247, 248, 248);\n"
"border: 2px solid rgb(170, 85, 255);		\n"
"border-radius:8px}")

        self.horizontalLayout_103.addWidget(self.lineEdit_3)


        self.verticalLayout_151.addLayout(self.horizontalLayout_103)

        self.label_200 = QLabel(self.frame_lineEditPerfil)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setMinimumSize(QSize(0, 30))
        self.label_200.setMaximumSize(QSize(16777215, 30))
        self.label_200.setFont(font13)
        self.label_200.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.verticalLayout_151.addWidget(self.label_200)

        self.lineEdit_4 = QLineEdit(self.frame_lineEditPerfil)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_4.setFont(font17)
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"color: rgb(170, 85, 255);\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(170, 85, 255);		\n"
"border-radius:5px;\n"
"padding-left:5px}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(247, 248, 248);\n"
"border: 2px solid rgb(170, 85, 255);		\n"
"border-radius:5px}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(247, 248, 248);\n"
"border: 2px solid rgb(170, 85, 255);		\n"
"border-radius:5px}")

        self.verticalLayout_151.addWidget(self.lineEdit_4)


        self.verticalLayout_153.addLayout(self.verticalLayout_151)


        self.verticalLayout_152.addWidget(self.frame_lineEditPerfil)

        self.frameButonnsPerfil = QFrame(self.frame_225)
        self.frameButonnsPerfil.setObjectName(u"frameButonnsPerfil")
        self.frameButonnsPerfil.setFrameShape(QFrame.StyledPanel)
        self.frameButonnsPerfil.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frameButonnsPerfil)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalSpacer_45 = QSpacerItem(261, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_45)

        self.frame_237 = QFrame(self.frameButonnsPerfil)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setMinimumSize(QSize(260, 101))
        self.frame_237.setMaximumSize(QSize(260, 101))
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.pushButton_17 = QPushButton(self.frame_237)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(140, 20, 110, 35))
        self.pushButton_17.setMinimumSize(QSize(110, 35))
        self.pushButton_17.setMaximumSize(QSize(110, 16777215))
        self.pushButton_17.setFont(font17)
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_18 = QPushButton(self.frame_237)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(10, 20, 110, 35))
        self.pushButton_18.setMinimumSize(QSize(110, 35))
        self.pushButton_18.setMaximumSize(QSize(110, 16777215))
        self.pushButton_18.setFont(font17)
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(170, 85, 255);\n"
"color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(170, 85, 255);\n"
"color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"}")

        self.horizontalLayout_105.addWidget(self.frame_237, 0, Qt.AlignTop)

        self.frame_233 = QFrame(self.frameButonnsPerfil)
        self.frame_233.setObjectName(u"frame_233")
        self.frame_233.setMaximumSize(QSize(16777215, 81))
        self.frame_233.setFrameShape(QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.frame_233)
        self.verticalLayout_158.setSpacing(0)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_105.addWidget(self.frame_233)


        self.verticalLayout_152.addWidget(self.frameButonnsPerfil)

        self.frameTestFaceId = QFrame(self.frame_225)
        self.frameTestFaceId.setObjectName(u"frameTestFaceId")
        self.frameTestFaceId.setMinimumSize(QSize(0, 0))
        self.frameTestFaceId.setMaximumSize(QSize(16777215, 0))
        self.frameTestFaceId.setFrameShape(QFrame.StyledPanel)
        self.frameTestFaceId.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frameTestFaceId)
        self.horizontalLayout_124.setSpacing(0)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.configFaceId = QLabel(self.frameTestFaceId)
        self.configFaceId.setObjectName(u"configFaceId")
        self.configFaceId.setStyleSheet(u"")

        self.horizontalLayout_124.addWidget(self.configFaceId)

        self.frame_252 = QFrame(self.frameTestFaceId)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setMaximumSize(QSize(123, 16777215))
        self.frame_252.setFrameShape(QFrame.StyledPanel)
        self.frame_252.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_252)
        self.verticalLayout_157.setSpacing(3)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_157.addItem(self.verticalSpacer_9)

        self.pushButton_20 = QPushButton(self.frame_252)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(110, 35))
        self.pushButton_20.setMaximumSize(QSize(110, 16777215))
        self.pushButton_20.setFont(font17)
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_157.addWidget(self.pushButton_20, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_19 = QPushButton(self.frame_252)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(110, 35))
        self.pushButton_19.setMaximumSize(QSize(110, 16777215))
        self.pushButton_19.setFont(font17)
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_157.addWidget(self.pushButton_19, 0, Qt.AlignHCenter)


        self.horizontalLayout_124.addWidget(self.frame_252, 0, Qt.AlignRight)


        self.verticalLayout_152.addWidget(self.frameTestFaceId)


        self.horizontalLayout_97.addWidget(self.frame_225)


        self.verticalLayout_149.addWidget(self.frame_226)

        self.stackedWidget_2.addWidget(self.page_perfilUsuario)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_66.addWidget(self.stackedWidget_2)


        self.verticalLayout_252.addWidget(self.frame_167)


        self.horizontalLayout_3.addWidget(self.frame_101)

        self.frame_173 = QFrame(self.frame_100)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setMinimumSize(QSize(220, 0))
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
        self.frame_174.setMinimumSize(QSize(210, 0))
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
        font20 = QFont()
        font20.setPointSize(14)
        self.label_17.setFont(font20)
        self.label_17.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.frame_175)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 120, 110, 20))
        self.label_16.setFont(font17)
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
        self.label_7.setPixmap(QPixmap(u"../img/asd.png"))
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
        self.label_67.setFont(font17)
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
        self.label_23.setFont(font17)
        self.label_23.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_23)

        self.horizontalSpacer_42 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_42)

        self.label_11 = QLabel(self.frame_181)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 0))
        self.label_11.setMaximumSize(QSize(60, 16777215))
        font21 = QFont()
        font21.setPointSize(10)
        self.label_11.setFont(font21)
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
        self.label_91.setFont(font17)
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
        self.label_58.setFont(font17)
        self.label_58.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_58)

        self.horizontalSpacer_43 = QSpacerItem(42, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_43)

        self.label_21 = QLabel(self.frame_366)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 0))
        self.label_21.setMaximumSize(QSize(50, 16777215))
        self.label_21.setFont(font21)
        self.label_21.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_21)


        self.verticalLayout_37.addWidget(self.frame_366)


        self.verticalLayout_65.addWidget(self.frame_179)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_4)

        self.label_19 = QLabel(self.frame_177)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font21)
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
        self.frame_42.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(170, 85, 255);")
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
        self.frame_50 = QFrame(self.frame_44)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_50)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 206))
        self.frame_66.setFont(font5)
        self.frame_66.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_66)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_186 = QFrame(self.frame_66)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_186)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 5, 5, 0)
        self.frame_8 = QFrame(self.frame_186)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(12, 10, 8, 7)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(215, 0))
        self.frame_9.setMaximumSize(QSize(400, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_9)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.frame_187 = QFrame(self.frame_9)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.pushButton_7 = QPushButton(self.frame_187)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(5, 5, 80, 70))
        icon29 = QIcon()
        icon29.addFile(u"../img/fluxoEntrada.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon29)
        self.pushButton_7.setIconSize(QSize(73, 76))
        self.label_121 = QLabel(self.frame_187)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(90, 47, 80, 26))
        self.label_121.setFont(font8)
        self.label_121.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_154.addWidget(self.frame_187)

        self.frame_188 = QFrame(self.frame_9)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setMaximumSize(QSize(16777215, 35))
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_188)
        self.verticalLayout_159.setSpacing(0)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.verticalLayout_159.setContentsMargins(0, 0, 7, 7)
        self.totalEntrada = QLabel(self.frame_188)
        self.totalEntrada.setObjectName(u"totalEntrada")
        self.totalEntrada.setMaximumSize(QSize(16777215, 35))
        self.totalEntrada.setFont(font7)
        self.totalEntrada.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalEntrada.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_159.addWidget(self.totalEntrada)


        self.verticalLayout_154.addWidget(self.frame_188)


        self.horizontalLayout_35.addWidget(self.frame_9)

        self.frame_45 = QFrame(self.frame_8)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(215, 0))
        self.frame_45.setMaximumSize(QSize(400, 16777215))
        self.frame_45.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_45)
        self.verticalLayout_160.setSpacing(0)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.frame_189 = QFrame(self.frame_45)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.label_111 = QLabel(self.frame_189)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(90, 47, 54, 26))
        self.label_111.setFont(font8)
        self.label_111.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_6 = QPushButton(self.frame_189)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(5, 5, 80, 71))
        icon30 = QIcon()
        icon30.addFile(u"../img/fluxoSaida.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon30)
        self.pushButton_6.setIconSize(QSize(73, 73))

        self.verticalLayout_160.addWidget(self.frame_189)

        self.frame_190 = QFrame(self.frame_45)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setMaximumSize(QSize(16777212, 35))
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_190)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 11, 7)
        self.totalSaida = QLabel(self.frame_190)
        self.totalSaida.setObjectName(u"totalSaida")
        self.totalSaida.setFont(font8)
        self.totalSaida.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalSaida.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_161.addWidget(self.totalSaida)


        self.verticalLayout_160.addWidget(self.frame_190)


        self.horizontalLayout_35.addWidget(self.frame_45)

        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(215, 0))
        self.frame_16.setMaximumSize(QSize(400, 16777215))
        self.frame_16.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_16)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(0, 0, 0, 0)
        self.frame_191 = QFrame(self.frame_16)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.label_113 = QLabel(self.frame_191)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(90, 47, 61, 26))
        self.label_113.setFont(font8)
        self.label_113.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.frame_191)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(5, 5, 81, 71))
        icon31 = QIcon()
        icon31.addFile(u"../img/fluxoTotal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon31)
        self.pushButton_3.setIconSize(QSize(73, 73))

        self.verticalLayout_162.addWidget(self.frame_191)

        self.frame_204 = QFrame(self.frame_16)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setMaximumSize(QSize(16777212, 35))
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.frame_204)
        self.verticalLayout_176.setSpacing(0)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.verticalLayout_176.setContentsMargins(0, 0, 11, 7)
        self.valorTotal = QLabel(self.frame_204)
        self.valorTotal.setObjectName(u"valorTotal")
        self.valorTotal.setMaximumSize(QSize(16777215, 35))
        self.valorTotal.setFont(font8)
        self.valorTotal.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.valorTotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_176.addWidget(self.valorTotal)


        self.verticalLayout_162.addWidget(self.frame_204)


        self.horizontalLayout_35.addWidget(self.frame_16)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.frame_183 = QFrame(self.frame_186)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setMinimumSize(QSize(160, 0))
        self.frame_183.setMaximumSize(QSize(175, 16777215))
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_183)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.novaMovimentacao = QPushButton(self.frame_183)
        self.novaMovimentacao.setObjectName(u"novaMovimentacao")
        self.novaMovimentacao.setMinimumSize(QSize(150, 33))
        self.novaMovimentacao.setMaximumSize(QSize(12345, 33))
        self.novaMovimentacao.setFont(font9)
        self.novaMovimentacao.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.novaMovimentacao, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.frame_183)


        self.verticalLayout_39.addWidget(self.frame_186)

        self.frame_185 = QFrame(self.frame_66)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setMaximumSize(QSize(16777215, 70))
        self.frame_185.setStyleSheet(u"")
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.label_61 = QLabel(self.frame_185)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(190, 0, 171, 25))
        self.label_61.setFont(font11)
        self.label_61.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.lineEdit_7 = QLineEdit(self.frame_185)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(437, 30, 170, 30))
        self.lineEdit_7.setFont(font11)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:3px;")
        self.pushButton_2 = QPushButton(self.frame_185)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(609, 29, 81, 32))
        self.pushButton_2.setFont(font10)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame_185)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(15, 0, 170, 25))
        self.label_8.setFont(font11)
        self.label_8.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.lineEdit_5 = QLineEdit(self.frame_185)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(15, 30, 170, 30))
        self.lineEdit_5.setFont(font21)
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:3px;")
        self.label_101 = QLabel(self.frame_185)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(437, 0, 130, 25))
        self.label_101.setFont(font11)
        self.label_101.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.dateEdit = QDateEdit(self.frame_185)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(190, 30, 127, 30))
        self.dateEdit.setFont(font12)
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit.setDate(QDate(2010, 1, 1))
        self.dateEdit_2 = QDateEdit(self.frame_185)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(305, 30, 127, 30))
        self.dateEdit_2.setFont(font12)
        self.dateEdit_2.setStyleSheet(u"QDateEdit{\n"
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
        self.dateEdit_2.setReadOnly(False)
        self.dateEdit_2.setDate(QDate(2010, 1, 1))
        self.dateEdit_2.raise_()
        self.label_61.raise_()
        self.lineEdit_7.raise_()
        self.pushButton_2.raise_()
        self.label_8.raise_()
        self.lineEdit_5.raise_()
        self.label_101.raise_()
        self.dateEdit.raise_()

        self.verticalLayout_39.addWidget(self.frame_185)


        self.horizontalLayout_49.addWidget(self.frame_66)


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
        self.frame_221 = QFrame(self.frame_216)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setMinimumSize(QSize(250, 0))
        self.frame_221.setStyleSheet(u"")
        self.frame_221.setFrameShape(QFrame.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_221)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(5, 10, 5, 0)
        self.pequenoHistoricoEntrada_4 = QFrame(self.frame_221)
        self.pequenoHistoricoEntrada_4.setObjectName(u"pequenoHistoricoEntrada_4")
        self.pequenoHistoricoEntrada_4.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_4.setStyleSheet(u"")
        self.pequenoHistoricoEntrada_4.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.pequenoHistoricoEntrada_4)
        self.horizontalLayout_121.setSpacing(3)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(12, 3, 3, 3)
        self.frame_192 = QFrame(self.pequenoHistoricoEntrada_4)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setMaximumSize(QSize(158, 16777215))
        self.frame_192.setStyleSheet(u"")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_192)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.label_214 = QLabel(self.frame_192)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setFont(font13)
        self.label_214.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_214.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_163.addWidget(self.label_214)


        self.horizontalLayout_121.addWidget(self.frame_192)

        self.frame_193 = QFrame(self.pequenoHistoricoEntrada_4)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setStyleSheet(u"")
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_193)
        self.verticalLayout_164.setSpacing(0)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.label_215 = QLabel(self.frame_193)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setMaximumSize(QSize(16777215, 38))
        self.label_215.setFont(font13)
        self.label_215.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_215.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_164.addWidget(self.label_215)


        self.horizontalLayout_121.addWidget(self.frame_193)

        self.frame_194 = QFrame(self.pequenoHistoricoEntrada_4)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setStyleSheet(u"")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.verticalLayout_165 = QVBoxLayout(self.frame_194)
        self.verticalLayout_165.setSpacing(0)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.verticalLayout_165.setContentsMargins(0, 0, 0, 0)
        self.categoria = QLabel(self.frame_194)
        self.categoria.setObjectName(u"categoria")
        self.categoria.setFont(font13)
        self.categoria.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.categoria.setAlignment(Qt.AlignCenter)

        self.verticalLayout_165.addWidget(self.categoria)


        self.horizontalLayout_121.addWidget(self.frame_194)

        self.frame_248 = QFrame(self.pequenoHistoricoEntrada_4)
        self.frame_248.setObjectName(u"frame_248")
        self.frame_248.setStyleSheet(u"")
        self.frame_248.setFrameShape(QFrame.StyledPanel)
        self.frame_248.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_248)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.frame_249 = QFrame(self.frame_248)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setStyleSheet(u"")
        self.frame_249.setFrameShape(QFrame.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_249)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_217 = QLabel(self.frame_249)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setFont(font13)
        self.label_217.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_217.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_125.addWidget(self.label_217)


        self.horizontalLayout_123.addWidget(self.frame_249)


        self.horizontalLayout_121.addWidget(self.frame_248)

        self.frame_195 = QFrame(self.pequenoHistoricoEntrada_4)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setStyleSheet(u"")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_195)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_195)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font13)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_166.addWidget(self.label_22)


        self.horizontalLayout_121.addWidget(self.frame_195)


        self.verticalLayout_168.addWidget(self.pequenoHistoricoEntrada_4)


        self.horizontalLayout_90.addWidget(self.frame_221)


        self.horizontalLayout_89.addWidget(self.frame_216)


        self.verticalLayout_69.addWidget(self.frame_184)

        self.scrollArea_5 = QScrollArea(self.frame_43)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1044, 345))
        self.verticalLayout_71 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_71.setSpacing(3)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(-1, 0, -1, -1)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 45))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_ScrolNovaTranzacao = QVBoxLayout(self.frame_7)
        self.verticalLayout_ScrolNovaTranzacao.setSpacing(4)
        self.verticalLayout_ScrolNovaTranzacao.setObjectName(u"verticalLayout_ScrolNovaTranzacao")
        self.verticalLayout_ScrolNovaTranzacao.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_71.addWidget(self.frame_7)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_71.addItem(self.verticalSpacer_10)

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
        self.frame_3 = QFrame(self.page_CoinsQuote)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 150))
        self.frame_4.setMaximumSize(QSize(16777215, 150))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_29 = QPushButton(self.frame_4)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(285, 108, 80, 34))
        self.pushButton_29.setMinimumSize(QSize(80, 34))
        self.pushButton_29.setMaximumSize(QSize(80, 34))
        self.pushButton_29.setFont(font10)
        self.pushButton_29.setStyleSheet(u"QPushButton{\n"
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
        icon32 = QIcon()
        icon32.addFile(u"../img/search_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_29.setIcon(icon32)
        self.pushButton_29.setIconSize(QSize(19, 16))
        self.BuscarStatus_5 = QLineEdit(self.frame_4)
        self.BuscarStatus_5.setObjectName(u"BuscarStatus_5")
        self.BuscarStatus_5.setGeometry(QRect(40, 110, 241, 31))
        self.BuscarStatus_5.setMinimumSize(QSize(170, 31))
        self.BuscarStatus_5.setMaximumSize(QSize(300, 30))
        self.BuscarStatus_5.setFont(font11)
        self.BuscarStatus_5.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:3px;")
        self.pushButton_30 = QPushButton(self.frame_4)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(830, 110, 80, 34))
        self.pushButton_30.setMinimumSize(QSize(80, 34))
        self.pushButton_30.setMaximumSize(QSize(80, 34))
        self.pushButton_30.setFont(font10)
        self.pushButton_30.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_30.setIconSize(QSize(19, 16))

        self.verticalLayout_18.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_20.addWidget(self.tableWidget)


        self.verticalLayout_19.addWidget(self.frame_6)


        self.verticalLayout_18.addWidget(self.frame_5)


        self.verticalLayout_15.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_CoinsQuote)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.central_frame)

        self.frame_MarcaTech = QFrame(self.frame_centaralCentral)
        self.frame_MarcaTech.setObjectName(u"frame_MarcaTech")
        self.frame_MarcaTech.setMinimumSize(QSize(0, 0))
        self.frame_MarcaTech.setMaximumSize(QSize(16777215, 0))
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
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1490, 120))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(159, 80, 239);\n"
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
        icon33 = QIcon()
        icon33.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/fina.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GoogleFinance_btl.setIcon(icon33)
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
        icon34 = QIcon()
        icon34.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/yahoo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.YahooFinance_btn.setIcon(icon34)
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
        icon35 = QIcon()
        icon35.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/investing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Investing_btn.setIcon(icon35)
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
        icon36 = QIcon()
        icon36.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/BLHL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BLHL_btn.setIcon(icon36)
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
        icon37 = QIcon()
        icon37.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/infomaney.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Infomaney_btn.setIcon(icon37)
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
        icon38 = QIcon()
        icon38.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/dinherama.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dinherama_btn.setIcon(icon38)
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
        icon39 = QIcon()
        icon39.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/cme.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CMEgroup_btn.setIcon(icon39)
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
        icon40 = QIcon()
        icon40.addFile(u"../img/uol economia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Economia_btn.setIcon(icon40)
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
        self.help_lbl.setFont(font17)
        self.help_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.help_btnF_2 = QPushButton(self.frame_Helpe)
        self.help_btnF_2.setObjectName(u"help_btnF_2")
        self.help_btnF_2.setGeometry(QRect(10, 10, 40, 40))
        icon41 = QIcon()
        icon41.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/help_70px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btnF_2.setIcon(icon41)
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

        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(1)


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
        self.setting_user_btn.setText(QCoreApplication.translate("MainWindowMW", u"     Fluxo Diario", None))
        self.editTest.setText(QCoreApplication.translate("MainWindowMW", u"     Fluxo Mensal", None))
        self.label_31.setText(QCoreApplication.translate("MainWindowMW", u"Contas a receber", None))
#if QT_CONFIG(whatsthis)
        self.frame_Browsin_history_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_Browsin_history_btn_2.setText("")
        self.label_186.setText(QCoreApplication.translate("MainWindowMW", u"em atraso", None))
        self.contasAreceberEmAtraso_lbl.setText(QCoreApplication.translate("MainWindowMW", u"Kz  0,00", None))
#if QT_CONFIG(whatsthis)
        self.frame_opening_history_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_opening_history_btn_2.setText("")
        self.label_195.setText(QCoreApplication.translate("MainWindowMW", u"Contas a receber em", None))
        self.label_194.setText(QCoreApplication.translate("MainWindowMW", u"aberto este m\u00eas", None))
        self.contasAreceberEmAberto_label.setText(QCoreApplication.translate("MainWindowMW", u"Kz  2.200,00", None))
#if QT_CONFIG(whatsthis)
        self.frame_user_list_btn_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_user_list_btn_3.setText("")
        self.label_203.setText(QCoreApplication.translate("MainWindowMW", u"Contas a receber", None))
        self.label_204.setText(QCoreApplication.translate("MainWindowMW", u"em atraso", None))
        self.label_205.setText(QCoreApplication.translate("MainWindowMW", u"Kz  0,00", None))
#if QT_CONFIG(whatsthis)
        self.password_faceId_btn_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.password_faceId_btn_3.setText("")
        self.label_209.setText(QCoreApplication.translate("MainWindowMW", u"Contas a pagar", None))
        self.label_187.setText(QCoreApplication.translate("MainWindowMW", u"em atraso", None))
        self.contasApagarEmAtraso_label.setText(QCoreApplication.translate("MainWindowMW", u"Kz  0,00", None))
        self.label_227.setText(QCoreApplication.translate("MainWindowMW", u"   Entradas ", None))
        self.label_228.setText(QCoreApplication.translate("MainWindowMW", u"    Saidas", None))
        self.pushButton_8.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindowMW", u"Total de Titulos", None))
        self.label_141.setText(QCoreApplication.translate("MainWindowMW", u"Kz 700.000,00", None))
        self.label_143.setText(QCoreApplication.translate("MainWindowMW", u"Total Pago", None))
        self.pushButton_9.setText("")
        self.label_151.setText(QCoreApplication.translate("MainWindowMW", u"Kz 100,00", None))
        self.label_153.setText(QCoreApplication.translate("MainWindowMW", u"Total em Aberto", None))
        self.pushButton_10.setText("")
        self.label_155.setText(QCoreApplication.translate("MainWindowMW", u"Kz 600.900,00", None))
        self.pagarConta.setText(QCoreApplication.translate("MainWindowMW", u"Pagar Conta", None))
        self.contaReceber.setText(QCoreApplication.translate("MainWindowMW", u"Adicionar conta a receber", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindowMW", u"Buscar", None))
        self.label_184.setText(QCoreApplication.translate("MainWindowMW", u"Cliente", None))
        self.comboBox_4.setItemText(0, "")

        self.label_190.setText(QCoreApplication.translate("MainWindowMW", u"N\u00famero", None))
        self.label_191.setText(QCoreApplication.translate("MainWindowMW", u"Data de Emiss\u00e3o", None))
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindowMW", u"Pago", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindowMW", u"Aberto", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindowMW", u"Parcelado", None))

        self.label_182.setText(QCoreApplication.translate("MainWindowMW", u"Status", None))
        self.label_185.setText(QCoreApplication.translate("MainWindowMW", u"Data de Vencimento", None))
        self.label_231.setText(QCoreApplication.translate("MainWindowMW", u"N\u00famero", None))
        self.label_232.setText(QCoreApplication.translate("MainWindowMW", u"Emiss\u00e3o", None))
        self.label_233.setText(QCoreApplication.translate("MainWindowMW", u"Planos de Contas", None))
        self.label_246.setText(QCoreApplication.translate("MainWindowMW", u"Cliente", None))
        self.label_248.setText(QCoreApplication.translate("MainWindowMW", u"Vencimento", None))
        self.label_234.setText(QCoreApplication.translate("MainWindowMW", u"Valor Total", None))
        self.label_235.setText(QCoreApplication.translate("MainWindowMW", u"Valor Pago", None))
        self.label_249.setText(QCoreApplication.translate("MainWindowMW", u"Status", None))
        self.label_247.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_252.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.label_253.setText(QCoreApplication.translate("MainWindowMW", u"2-presta\u00e7\u00e3o de servi\u00e7o", None))
        self.label_254.setText(QCoreApplication.translate("MainWindowMW", u"2-Beltrano", None))
        self.label_255.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.label_256.setText(QCoreApplication.translate("MainWindowMW", u"20.000", None))
        self.label_257.setText(QCoreApplication.translate("MainWindowMW", u"100,00", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindowMW", u"Abertio", None))
        self.label_236.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_237.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.label_238.setText(QCoreApplication.translate("MainWindowMW", u"2-presta\u00e7\u00e3o de servi\u00e7o", None))
        self.label_251.setText(QCoreApplication.translate("MainWindowMW", u"2-Beltrano", None))
        self.label_250.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.label_239.setText(QCoreApplication.translate("MainWindowMW", u"20.000", None))
        self.label_240.setText(QCoreApplication.translate("MainWindowMW", u"100,00", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindowMW", u"Pago", None))
        self.pushButton_14.setText("")
        self.label_174.setText(QCoreApplication.translate("MainWindowMW", u"Total de Titulos", None))
        self.label_175.setText(QCoreApplication.translate("MainWindowMW", u"Kz 700.000,00", None))
        self.label_180.setText(QCoreApplication.translate("MainWindowMW", u"Total Pago", None))
        self.pushButton_23.setText("")
        self.label_192.setText(QCoreApplication.translate("MainWindowMW", u"Kz 100,00", None))
        self.label_193.setText(QCoreApplication.translate("MainWindowMW", u"Total em Aberto", None))
        self.pushButton_24.setText("")
        self.label_196.setText(QCoreApplication.translate("MainWindowMW", u"Kz 600.900,00", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindowMW", u"Adicionar contas a pagar", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindowMW", u"Buscar", None))
        self.label_197.setText(QCoreApplication.translate("MainWindowMW", u"Fornecedor", None))
        self.comboBox_5.setItemText(0, "")

        self.label_198.setText(QCoreApplication.translate("MainWindowMW", u"N\u00famero", None))
        self.label_199.setText(QCoreApplication.translate("MainWindowMW", u"Data de Emiss\u00e3o", None))
        self.comboBox_6.setItemText(0, "")
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindowMW", u"Pago", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindowMW", u"Aberto", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindowMW", u"Parcelado", None))

        self.label_202.setText(QCoreApplication.translate("MainWindowMW", u"Status", None))
        self.label_207.setText(QCoreApplication.translate("MainWindowMW", u"Data de Vencimento", None))
        self.label_241.setText(QCoreApplication.translate("MainWindowMW", u"N\u00famero", None))
        self.label_242.setText(QCoreApplication.translate("MainWindowMW", u"Emiss\u00e3o", None))
        self.label_243.setText(QCoreApplication.translate("MainWindowMW", u"Planos de Contas", None))
        self.label_258.setText(QCoreApplication.translate("MainWindowMW", u"Fornecedor", None))
        self.label_259.setText(QCoreApplication.translate("MainWindowMW", u"Vencimento", None))
        self.label_244.setText(QCoreApplication.translate("MainWindowMW", u"Valor", None))
        self.label_245.setText(QCoreApplication.translate("MainWindowMW", u"Valor Pago", None))
        self.label_260.setText(QCoreApplication.translate("MainWindowMW", u"Status", None))
        self.label_261.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_262.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.label_263.setText(QCoreApplication.translate("MainWindowMW", u"2-presta\u00e7\u00e3o de servi\u00e7o", None))
        self.label_264.setText(QCoreApplication.translate("MainWindowMW", u"Beltrano", None))
        self.label_265.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.label_266.setText(QCoreApplication.translate("MainWindowMW", u"20.000", None))
        self.label_267.setText(QCoreApplication.translate("MainWindowMW", u"100,00", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindowMW", u"Pago", None))
        self.label_268.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_269.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.label_270.setText(QCoreApplication.translate("MainWindowMW", u"2-presta\u00e7\u00e3o de servi\u00e7o", None))
        self.label_271.setText(QCoreApplication.translate("MainWindowMW", u"Beltrano", None))
        self.label_272.setText(QCoreApplication.translate("MainWindowMW", u"12/04/2022", None))
        self.label_273.setText(QCoreApplication.translate("MainWindowMW", u"20.000", None))
        self.label_274.setText(QCoreApplication.translate("MainWindowMW", u"100,00", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindowMW", u"Apagar", None))
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
        self.frame_user_list_lbl.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; color:#aa55ff;\">Perfil do Usuario</span></p></body></html>", None))
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
#if QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl_2.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl_2.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; color:#aa55ff;\">   Perfil do Usuario</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindowMW", u"Edit photo", None))
        self.pushButton_13.setText("")
        self.label_189.setText(QCoreApplication.translate("MainWindowMW", u"Nome", None))
        self.label_201.setText(QCoreApplication.translate("MainWindowMW", u"Senha", None))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit_3.setPlaceholderText("")
        self.label_200.setText(QCoreApplication.translate("MainWindowMW", u"Email", None))
        self.lineEdit_4.setPlaceholderText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindowMW", u"Salvar", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindowMW", u"Config face Id", None))
        self.configFaceId.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("MainWindowMW", u"Config Id", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindowMW", u"Test", None))
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
        self.pushButton_7.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindowMW", u"Entrada", None))
        self.totalEntrada.setText(QCoreApplication.translate("MainWindowMW", u"Kz 0,00", None))
        self.label_111.setText(QCoreApplication.translate("MainWindowMW", u"Saida", None))
        self.pushButton_6.setText("")
        self.totalSaida.setText(QCoreApplication.translate("MainWindowMW", u"Kz 0,00", None))
        self.label_113.setText(QCoreApplication.translate("MainWindowMW", u"Total", None))
        self.pushButton_3.setText("")
        self.valorTotal.setText(QCoreApplication.translate("MainWindowMW", u"Kz 0,00", None))
        self.novaMovimentacao.setText(QCoreApplication.translate("MainWindowMW", u"Nova Movimenta\u00e7\u00e3o", None))
        self.label_61.setText(QCoreApplication.translate("MainWindowMW", u"Data de Movimenta\u00e7\u00e3o", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindowMW", u"Buscar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindowMW", u"C\u00f3digo", None))
        self.label_101.setText(QCoreApplication.translate("MainWindowMW", u"Planos de contas", None))
        self.label_214.setText(QCoreApplication.translate("MainWindowMW", u"C\u00f3digo", None))
        self.label_215.setText(QCoreApplication.translate("MainWindowMW", u"Data de \n"
"Movimenta\u00e7\u00e3o", None))
        self.categoria.setText(QCoreApplication.translate("MainWindowMW", u"Planos de Contas", None))
        self.label_217.setText(QCoreApplication.translate("MainWindowMW", u"Complemento", None))
        self.label_22.setText(QCoreApplication.translate("MainWindowMW", u"Valor", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindowMW", u"Buscar", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindowMW", u"Exportar PDF", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindowMW", u"Dia", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindowMW", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindowMW", u"Entradas", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindowMW", u"Saldo do Dia", None));
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

