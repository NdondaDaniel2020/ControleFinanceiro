# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SystemMWuKzhXy.ui'
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
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

from packeg.slideStackedWidgets import SlidingStackedWidget
from packeg.page_perfil import Ui_page_perfil
from packeg.page_Home import Ui_page_Home
from packeg.page_edit import Ui_page_edit
from packeg.page_web import Ui_page_web
from packeg.page_Extras import Ui_page_Extras
from packeg.page_ControlFinace import Ui_page_ControlFinace
from packeg.page_CoinsQuote import Ui_page_CoinsQuote


class Ui_MainWindowMW(object):
    def setupUi(self, MainWindowMW):
        if not MainWindowMW.objectName():
            MainWindowMW.setObjectName(u"MainWindowMW")
        MainWindowMW.resize(703, 580)
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

        self.frame_stacked = QFrame(self.frame)
        self.frame_stacked.setObjectName(u"frame_stacked")
        self.frame_stacked.setFrameShape(QFrame.StyledPanel)
        self.frame_stacked.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_stacked)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_stacked)


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
        icon16 = QIcon()
        icon16.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/fina.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GoogleFinance_btl.setIcon(icon16)
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
        icon17 = QIcon()
        icon17.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/yahoo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.YahooFinance_btn.setIcon(icon17)
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
        icon18 = QIcon()
        icon18.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/investing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Investing_btn.setIcon(icon18)
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
        icon19 = QIcon()
        icon19.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/BLHL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BLHL_btn.setIcon(icon19)
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
        icon20 = QIcon()
        icon20.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/infomaney.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Infomaney_btn.setIcon(icon20)
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
        icon21 = QIcon()
        icon21.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/dinherama.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dinherama_btn.setIcon(icon21)
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
        icon22 = QIcon()
        icon22.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/cme.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CMEgroup_btn.setIcon(icon22)
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
        icon23 = QIcon()
        icon23.addFile(u"../img/uol economia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Economia_btn.setIcon(icon23)
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
        font2 = QFont()
        font2.setPointSize(12)
        self.help_lbl.setFont(font2)
        self.help_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.help_btnF_2 = QPushButton(self.frame_Helpe)
        self.help_btnF_2.setObjectName(u"help_btnF_2")
        self.help_btnF_2.setGeometry(QRect(10, 10, 40, 40))
        icon24 = QIcon()
        icon24.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/help_70px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btnF_2.setIcon(icon24)
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

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.i = Ui_MainWindowMW()
        self.i.setupUi(self)

        self.SlidingStacked = SlidingStackedWidget()

        page_perfil = Ui_page_perfil()
        page_Home = Ui_page_Home()
        page_edit = Ui_page_edit()
        page_web = Ui_page_web()__init__
        page_Extras = Ui_page_Extras().__init__()
        page_ControlFinace = Ui_page_ControlFinace().__init__()
        page_CoinsQuote = Ui_page_CoinsQuote().__init__()

        self.SlidingStacked.addWidget(page_perfil)
        self.SlidingStacked.addWidget(page_Home)
        self.SlidingStacked.addWidget(page_edit)
        self.SlidingStacked.addWidget(page_web)
        self.SlidingStacked.addWidget(page_Extras)
        self.SlidingStacked.addWidget(page_ControlFinace)
        self.SlidingStacked.addWidget(page_CoinsQuote)

        self.i.horizontalLayout_11.addWidget(self.SlidingStacked)


if __name__ == "__main__":
        import sys

        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = MainWindow()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec())