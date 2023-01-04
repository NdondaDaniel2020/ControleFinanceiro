# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SystemMWWuobMk.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindowMW(object):
    def setupUi(self, MainWindowMW):
        if not MainWindowMW.objectName():
            MainWindowMW.setObjectName(u"MainWindowMW")
        MainWindowMW.resize(1086, 669)
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
        self.barraTitulo_2 = QFrame(self.central_frame)
        self.barraTitulo_2.setObjectName(u"barraTitulo_2")
        self.barraTitulo_2.setMaximumSize(QSize(16777215, 40))
        self.barraTitulo_2.setFrameShape(QFrame.StyledPanel)
        self.barraTitulo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.barraTitulo_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.barraTitulo = QFrame(self.barraTitulo_2)
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


        self.verticalLayout_7.addWidget(self.barraTitulo_2)

        self.framePrincipal = QFrame(self.central_frame)
        self.framePrincipal.setObjectName(u"framePrincipal")
        self.framePrincipal.setMinimumSize(QSize(206, 0))
        self.framePrincipal.setFrameShape(QFrame.StyledPanel)
        self.framePrincipal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.framePrincipal)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 5, 0, 0)
        self.xone_btn_left = QFrame(self.framePrincipal)
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

        self.movimentacao_btn = QPushButton(self.xone_btn_left)
        self.movimentacao_btn.setObjectName(u"movimentacao_btn")
        self.movimentacao_btn.setMinimumSize(QSize(35, 35))
        self.movimentacao_btn.setMaximumSize(QSize(35, 35))
        self.movimentacao_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:17px;\n"
"	color: rgb(255, 255, 255);\n"
"    text-align: left;	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 83, 248);\n"
"	border-radius:17px;\n"
"	color: rgb(255, 255, 255);\n"
"   text-align: justify;	\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(170, 85, 255);\n"
"	border-radius:17px;\n"
"	color: rgb(255, 255, 255);\n"
"    text-align: justify;	\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../img/ControleFinanceiro1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.movimentacao_btn.setIcon(icon5)
        self.movimentacao_btn.setIconSize(QSize(28, 31))

        self.verticalLayout_9.addWidget(self.movimentacao_btn)

        self.settings = QPushButton(self.xone_btn_left)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 35))
        self.settings.setMaximumSize(QSize(35, 16777215))
        icon6 = QIcon()
        icon6.addFile(u"../img/24x24/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon6)
        self.settings.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.settings, 0, Qt.AlignRight)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.xone_btn_left)

        self.left_menu = QFrame(self.framePrincipal)
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
        self.frame_zone_btn.setMinimumSize(QSize(190, 300))
        self.frame_zone_btn.setMaximumSize(QSize(192, 300))
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
        self.perfil_btn = QPushButton(self.frame_zone_btn)
        self.perfil_btn.setObjectName(u"perfil_btn")
        self.perfil_btn.setMinimumSize(QSize(0, 34))
        self.perfil_btn.setMaximumSize(QSize(16777215, 34))
        self.perfil_btn.setStyleSheet(u"padding-left:22px;")
        icon7 = QIcon()
        icon7.addFile(u"../img/24x24/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfil_btn.setIcon(icon7)
        self.perfil_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_10.addWidget(self.perfil_btn)

        self.movimentacao_btn3 = QPushButton(self.frame_zone_btn)
        self.movimentacao_btn3.setObjectName(u"movimentacao_btn3")
        self.movimentacao_btn3.setMinimumSize(QSize(0, 34))
        self.movimentacao_btn3.setMaximumSize(QSize(16777215, 34))
        self.movimentacao_btn3.setStyleSheet(u"padding-left:19px;")
        icon8 = QIcon()
        icon8.addFile(u"../img/ControleFinanceiro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.movimentacao_btn3.setIcon(icon8)
        self.movimentacao_btn3.setIconSize(QSize(27, 29))

        self.verticalLayout_10.addWidget(self.movimentacao_btn3)

        self.fluxodecaixa = QPushButton(self.frame_zone_btn)
        self.fluxodecaixa.setObjectName(u"fluxodecaixa")
        self.fluxodecaixa.setMinimumSize(QSize(0, 34))
        self.fluxodecaixa.setMaximumSize(QSize(16777215, 34))
        icon9 = QIcon()
        icon9.addFile(u"../img/controle de fluxo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fluxodecaixa.setIcon(icon9)
        self.fluxodecaixa.setIconSize(QSize(27, 33))

        self.verticalLayout_10.addWidget(self.fluxodecaixa)

        self.exit = QPushButton(self.frame_zone_btn)
        self.exit.setObjectName(u"exit")
        self.exit.setMinimumSize(QSize(0, 34))
        self.exit.setMaximumSize(QSize(16777215, 34))
        self.exit.setStyleSheet(u"padding-left:23px;")
        icon10 = QIcon()
        icon10.addFile(u"../img/24x24/cil-exit-to-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit.setIcon(icon10)
        self.exit.setIconSize(QSize(19, 22))

        self.verticalLayout_10.addWidget(self.exit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.verticalLayout_141.addWidget(self.frame_zone_btn)

        self.verticalSpacer_2 = QSpacerItem(5, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_141.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.stackedWidget = QStackedWidget(self.framePrincipal)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_Home = QWidget()
        self.page_Home.setObjectName(u"page_Home")
        self.verticalLayout_4 = QVBoxLayout(self.page_Home)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_Home = QFrame(self.page_Home)
        self.frame_Home.setObjectName(u"frame_Home")
        self.frame_Home.setFrameShape(QFrame.StyledPanel)
        self.frame_Home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_Home)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_222 = QFrame(self.frame_Home)
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
        self.scrollArea_Home = QScrollArea(self.frame_364)
        self.scrollArea_Home.setObjectName(u"scrollArea_Home")
        self.scrollArea_Home.setMinimumSize(QSize(0, 0))
        self.scrollArea_Home.setMaximumSize(QSize(16777215, 172))
        self.scrollArea_Home.setStyleSheet(u"")
        self.scrollArea_Home.setFrameShadow(QFrame.Sunken)
        self.scrollArea_Home.setLineWidth(1)
        self.scrollArea_Home.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_Home.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_Home.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_Home.setWidgetResizable(True)
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
        self.frame_movimentacao = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_movimentacao.setObjectName(u"frame_movimentacao")
        self.frame_movimentacao.setMinimumSize(QSize(250, 130))
        self.frame_movimentacao.setMaximumSize(QSize(310, 135))
        self.frame_movimentacao.setStyleSheet(u"background-color: rgb(255, 255, 255)\n"
"")
        self.frame_movimentacao.setFrameShape(QFrame.StyledPanel)
        self.frame_movimentacao.setFrameShadow(QFrame.Raised)
        self.label_186 = QLabel(self.frame_movimentacao)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(133, 54, 110, 17))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        self.label_186.setFont(font2)
        self.label_186.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_31 = QLabel(self.frame_movimentacao)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(132, 30, 80, 21))
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.movimentacao_btn2 = QPushButton(self.frame_movimentacao)
        self.movimentacao_btn2.setObjectName(u"movimentacao_btn2")
        self.movimentacao_btn2.setGeometry(QRect(7, 10, 115, 115))
        self.movimentacao_btn2.setStyleSheet(u"QPushButton{\n"
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
        icon11 = QIcon()
        icon11.addFile(u"../img/navamovimentacao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.movimentacao_btn2.setIcon(icon11)
        self.movimentacao_btn2.setIconSize(QSize(115, 115))
        self.label_199 = QLabel(self.frame_movimentacao)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(130, 74, 80, 20))
        self.label_199.setFont(font2)
        self.label_199.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.horizontalLayout_109.addWidget(self.frame_movimentacao)

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
        icon12 = QIcon()
        icon12.addFile(u"../img/adiantamento-de-dinheiroV2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_opening_history_btn_2.setIcon(icon12)
        self.frame_opening_history_btn_2.setIconSize(QSize(86, 100))
        self.label_195 = QLabel(self.frame_207)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(100, 15, 157, 20))
        self.label_195.setFont(font2)
        self.label_195.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_194 = QLabel(self.frame_207)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(100, 34, 117, 20))
        self.label_194.setFont(font2)
        self.label_194.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_196 = QLabel(self.frame_207)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(96, 55, 80, 20))
        self.label_196.setFont(font2)
        self.label_196.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.verticalLayout_178.addWidget(self.frame_207)

        self.frame_208 = QFrame(self.frame_opening_history_2)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMaximumSize(QSize(16777215, 37))
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.verticalLayout_179 = QVBoxLayout(self.frame_208)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.verticalLayout_179.setContentsMargins(0, 0, 10, 0)
        self.homeValorTotal = QLabel(self.frame_208)
        self.homeValorTotal.setObjectName(u"homeValorTotal")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(21)
        self.homeValorTotal.setFont(font3)
        self.homeValorTotal.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"background-color: transparent")
        self.homeValorTotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_179.addWidget(self.homeValorTotal)


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
        self.frame_user_list_btn_3.setGeometry(QRect(6, 6, 92, 92))
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
        icon13 = QIcon()
        icon13.addFile(u"../img/adiantamento-de-dinheiroV.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_user_list_btn_3.setIcon(icon13)
        self.frame_user_list_btn_3.setIconSize(QSize(100, 130))
        self.label_203 = QLabel(self.frame_user_list_3)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(103, 15, 130, 20))
        self.label_203.setFont(font2)
        self.label_203.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_204 = QLabel(self.frame_user_list_3)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(105, 34, 130, 20))
        self.label_204.setFont(font2)
        self.label_204.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_197 = QLabel(self.frame_user_list_3)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(102, 55, 80, 20))
        self.label_197.setFont(font2)
        self.label_197.setStyleSheet(u"color: rgb(170, 85, 255);")

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
        self.homeTotalEntrada = QLabel(self.frame_211)
        self.homeTotalEntrada.setObjectName(u"homeTotalEntrada")
        self.homeTotalEntrada.setFont(font3)
        self.homeTotalEntrada.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.homeTotalEntrada.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_181.addWidget(self.homeTotalEntrada)


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
        icon14 = QIcon()
        icon14.addFile(u"../img/adiantamento-de-dinheiroV5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.password_faceId_btn_3.setIcon(icon14)
        self.password_faceId_btn_3.setIconSize(QSize(100, 130))
        self.label_206 = QLabel(self.frame_210)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(105, 34, 130, 20))
        self.label_206.setFont(font2)
        self.label_206.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_207 = QLabel(self.frame_210)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(103, 15, 130, 20))
        self.label_207.setFont(font2)
        self.label_207.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_198 = QLabel(self.frame_210)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setGeometry(QRect(102, 55, 80, 20))
        self.label_198.setFont(font2)
        self.label_198.setStyleSheet(u"color: rgb(170, 85, 255);")

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
        self.homeTotalSaidas = QLabel(self.frame_212)
        self.homeTotalSaidas.setObjectName(u"homeTotalSaidas")
        self.homeTotalSaidas.setFont(font3)
        self.homeTotalSaidas.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"background-color: transparent")
        self.homeTotalSaidas.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_183.addWidget(self.homeTotalSaidas)


        self.verticalLayout_182.addWidget(self.frame_212)


        self.horizontalLayout_109.addWidget(self.frameContasApagarEmatraso)

        self.scrollArea_Home.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_254.addWidget(self.scrollArea_Home)


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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 997, 155))
        self.horizontalLayout_46 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_ZonaEntrada = QVBoxLayout(self.frame_47)
        self.verticalLayout_ZonaEntrada.setSpacing(2)
        self.verticalLayout_ZonaEntrada.setObjectName(u"verticalLayout_ZonaEntrada")
        self.verticalLayout_ZonaEntrada.setContentsMargins(0, 0, 2, -1)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_ZonaEntrada.addItem(self.verticalSpacer_7)


        self.horizontalLayout_46.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_zonaSaida = QVBoxLayout(self.frame_48)
        self.verticalLayout_zonaSaida.setSpacing(2)
        self.verticalLayout_zonaSaida.setObjectName(u"verticalLayout_zonaSaida")
        self.verticalLayout_zonaSaida.setContentsMargins(2, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_zonaSaida.addItem(self.verticalSpacer_8)


        self.horizontalLayout_46.addWidget(self.frame_48)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_144.addWidget(self.scrollArea_2)


        self.verticalLayout_143.addWidget(self.frame_49)


        self.verticalLayout_253.addWidget(self.frame_ulatimasTranzacao)


        self.verticalLayout_14.addWidget(self.frame_222)


        self.verticalLayout_4.addWidget(self.frame_Home)

        self.stackedWidget.addWidget(self.page_Home)
        self.page_perfil = QWidget()
        self.page_perfil.setObjectName(u"page_perfil")
        self.verticalLayout_12 = QVBoxLayout(self.page_perfil)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_perfil = QFrame(self.page_perfil)
        self.frame_perfil.setObjectName(u"frame_perfil")
        self.frame_perfil.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_perfil.setFrameShape(QFrame.StyledPanel)
        self.frame_perfil.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_perfil)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_101 = QFrame(self.frame_perfil)
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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1037, 145))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:15px;\n"
"")
        self.horizontalLayout_108 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_108.setSpacing(9)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(5, 0, 5, 0)
        self.frame_CategoriaBtn = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_CategoriaBtn.setObjectName(u"frame_CategoriaBtn")
        self.frame_CategoriaBtn.setMinimumSize(QSize(250, 145))
        self.frame_CategoriaBtn.setMaximumSize(QSize(310, 145))
        self.frame_CategoriaBtn.setStyleSheet(u"background-color: rgb(255, 255, 255)\n"
"")
        self.frame_CategoriaBtn.setFrameShape(QFrame.StyledPanel)
        self.frame_CategoriaBtn.setFrameShadow(QFrame.Raised)
        self.frame_Browsin_history_lbl = QLabel(self.frame_CategoriaBtn)
        self.frame_Browsin_history_lbl.setObjectName(u"frame_Browsin_history_lbl")
        self.frame_Browsin_history_lbl.setGeometry(QRect(16, 100, 190, 30))
        font5 = QFont()
        font5.setPointSize(17)
        self.frame_Browsin_history_lbl.setFont(font5)
        self.frame_Browsin_history_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.categoria_btn = QPushButton(self.frame_CategoriaBtn)
        self.categoria_btn.setObjectName(u"categoria_btn")
        self.categoria_btn.setGeometry(QRect(13, 13, 90, 71))
        icon15 = QIcon()
        icon15.addFile(u"../img/web_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.categoria_btn.setIcon(icon15)
        self.categoria_btn.setIconSize(QSize(100, 100))

        self.horizontalLayout_108.addWidget(self.frame_CategoriaBtn)

        self.frame_opening_history = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_opening_history.setObjectName(u"frame_opening_history")
        self.frame_opening_history.setMinimumSize(QSize(250, 145))
        self.frame_opening_history.setMaximumSize(QSize(310, 145))
        self.frame_opening_history.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.frame_opening_history.setFrameShape(QFrame.StyledPanel)
        self.frame_opening_history.setFrameShadow(QFrame.Raised)
        self.frame_opening_history_btn = QPushButton(self.frame_opening_history)
        self.frame_opening_history_btn.setObjectName(u"frame_opening_history_btn")
        self.frame_opening_history_btn.setGeometry(QRect(13, 13, 90, 71))
        icon16 = QIcon()
        icon16.addFile(u"../img/close_pane_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_opening_history_btn.setIcon(icon16)
        self.frame_opening_history_btn.setIconSize(QSize(100, 100))
        self.frame_opening_history_lbl = QLabel(self.frame_opening_history)
        self.frame_opening_history_lbl.setObjectName(u"frame_opening_history_lbl")
        self.frame_opening_history_lbl.setGeometry(QRect(16, 100, 210, 30))
        font6 = QFont()
        font6.setPointSize(12)
        self.frame_opening_history_lbl.setFont(font6)
        self.frame_opening_history_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_108.addWidget(self.frame_opening_history)

        self.frame_user_perfil = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_user_perfil.setObjectName(u"frame_user_perfil")
        self.frame_user_perfil.setMinimumSize(QSize(250, 145))
        self.frame_user_perfil.setMaximumSize(QSize(310, 145))
        self.frame_user_perfil.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_user_perfil.setFrameShape(QFrame.StyledPanel)
        self.frame_user_perfil.setFrameShadow(QFrame.Raised)
        self.frame_user_list_btn = QPushButton(self.frame_user_perfil)
        self.frame_user_list_btn.setObjectName(u"frame_user_list_btn")
        self.frame_user_list_btn.setGeometry(QRect(10, 17, 91, 71))
        icon17 = QIcon()
        icon17.addFile(u"../img/user_menu_female_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_user_list_btn.setIcon(icon17)
        self.frame_user_list_btn.setIconSize(QSize(115, 115))
        self.frame_user_list_lbl = QLabel(self.frame_user_perfil)
        self.frame_user_list_lbl.setObjectName(u"frame_user_list_lbl")
        self.frame_user_list_lbl.setGeometry(QRect(10, 100, 171, 30))
        self.frame_user_list_lbl.setFont(font5)
        self.frame_user_list_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_108.addWidget(self.frame_user_perfil)

        self.frame_password_faceId = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_password_faceId.setObjectName(u"frame_password_faceId")
        self.frame_password_faceId.setMinimumSize(QSize(250, 145))
        self.frame_password_faceId.setMaximumSize(QSize(310, 145))
        self.frame_password_faceId.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame_password_faceId.setFrameShape(QFrame.StyledPanel)
        self.frame_password_faceId.setFrameShadow(QFrame.Raised)
        self.password_faceId_btn_2 = QPushButton(self.frame_password_faceId)
        self.password_faceId_btn_2.setObjectName(u"password_faceId_btn_2")
        self.password_faceId_btn_2.setGeometry(QRect(13, 10, 90, 90))
        icon18 = QIcon()
        icon18.addFile(u"../img/instagram_logo_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.password_faceId_btn_2.setIcon(icon18)
        self.password_faceId_btn_2.setIconSize(QSize(110, 130))
        self.lineEdit_2 = QLineEdit(self.frame_password_faceId)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(59, 53, 106, 32))
        font7 = QFont()
        font7.setPointSize(15)
        self.lineEdit_2.setFont(font7)
        self.lineEdit_2.setStyleSheet(u"border-radius:7px;\n"
"color:rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px solid rgb(170, 85, 255)")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.password_faceId_lbl_6 = QLabel(self.frame_password_faceId)
        self.password_faceId_lbl_6.setObjectName(u"password_faceId_lbl_6")
        self.password_faceId_lbl_6.setGeometry(QRect(18, 101, 186, 30))
        self.password_faceId_lbl_6.setFont(font6)
        self.password_faceId_lbl_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_29 = QLabel(self.frame_password_faceId)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(60, 47, 114, 37))
        self.label_29.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_108.addWidget(self.frame_password_faceId)

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
        font8 = QFont()
        font8.setPointSize(25)
        self.frame_Browsin_history_lbl_2.setFont(font8)
        self.frame_Browsin_history_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_12 = QFrame(self.frame_232)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 60, 120, 80))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

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
        self.editFotho = QPushButton(self.frame_234)
        self.editFotho.setObjectName(u"editFotho")
        self.editFotho.setGeometry(QRect(60, 200, 110, 35))
        self.editFotho.setFont(font6)
        self.editFotho.setStyleSheet(u"QPushButton{\n"
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
        self.perfifEdit = QPushButton(self.frame_223)
        self.perfifEdit.setObjectName(u"perfifEdit")
        self.perfifEdit.setStyleSheet(u"QPushButton{\n"
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
        icon19 = QIcon()
        icon19.addFile(u"../img/daniel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.perfifEdit.setIcon(icon19)
        self.perfifEdit.setIconSize(QSize(144, 154))

        self.verticalLayout_150.addWidget(self.perfifEdit)


        self.verticalLayout_155.addWidget(self.frame_234)

        self.frame_236 = QFrame(self.frame_231)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)

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
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Semibold"])
        font9.setPointSize(11)
        self.label_189.setFont(font9)
        self.label_189.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.horizontalLayout_104.addWidget(self.label_189)

        self.label_201 = QLabel(self.frame_lineEditPerfil)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setMinimumSize(QSize(0, 30))
        self.label_201.setMaximumSize(QSize(16777215, 30))
        self.label_201.setFont(font9)
        self.label_201.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.horizontalLayout_104.addWidget(self.label_201)


        self.verticalLayout_151.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setSpacing(40)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.mudaNome = QLineEdit(self.frame_lineEditPerfil)
        self.mudaNome.setObjectName(u"mudaNome")
        self.mudaNome.setMinimumSize(QSize(0, 40))
        self.mudaNome.setMaximumSize(QSize(16777215, 40))
        self.mudaNome.setFont(font6)
        self.mudaNome.setStyleSheet(u"QLineEdit{\n"
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

        self.horizontalLayout_103.addWidget(self.mudaNome)

        self.mudaSenha = QLineEdit(self.frame_lineEditPerfil)
        self.mudaSenha.setObjectName(u"mudaSenha")
        self.mudaSenha.setMinimumSize(QSize(0, 40))
        self.mudaSenha.setMaximumSize(QSize(16777215, 40))
        self.mudaSenha.setFont(font6)
        self.mudaSenha.setStyleSheet(u"QLineEdit{\n"
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

        self.horizontalLayout_103.addWidget(self.mudaSenha)


        self.verticalLayout_151.addLayout(self.horizontalLayout_103)

        self.label_200 = QLabel(self.frame_lineEditPerfil)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setMinimumSize(QSize(0, 30))
        self.label_200.setMaximumSize(QSize(16777215, 30))
        self.label_200.setFont(font9)
        self.label_200.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.verticalLayout_151.addWidget(self.label_200)

        self.lineEdit_4 = QLineEdit(self.frame_lineEditPerfil)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_4.setFont(font6)
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
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frameButonnsPerfil)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_10)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(321, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.salvarAlteracao = QPushButton(self.frame_11)
        self.salvarAlteracao.setObjectName(u"salvarAlteracao")
        self.salvarAlteracao.setMinimumSize(QSize(110, 35))
        self.salvarAlteracao.setMaximumSize(QSize(110, 16777215))
        self.salvarAlteracao.setFont(font6)
        self.salvarAlteracao.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_5.addWidget(self.salvarAlteracao)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_21.addWidget(self.frame_13)


        self.horizontalLayout_105.addWidget(self.frame_10)


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
        self.pushButton_20.setFont(font6)
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
        self.pushButton_19.setFont(font6)
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
        self.page_webCam = QWidget()
        self.page_webCam.setObjectName(u"page_webCam")
        self.verticalLayout_20 = QVBoxLayout(self.page_webCam)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.faceId = QLabel(self.page_webCam)
        self.faceId.setObjectName(u"faceId")

        self.verticalLayout_20.addWidget(self.faceId)

        self.stackedWidget_2.addWidget(self.page_webCam)
        self.page_Categoria = QWidget()
        self.page_Categoria.setObjectName(u"page_Categoria")
        self.verticalLayout_25 = QVBoxLayout(self.page_Categoria)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.page_Categoria)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 63))
        self.label_2.setMaximumSize(QSize(16777215, 81))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(27)
        font10.setBold(False)
        self.label_2.setFont(font10)
        self.label_2.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"padding-left:3px")

        self.verticalLayout_25.addWidget(self.label_2)

        self.frame_14 = QFrame(self.page_Categoria)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_21 = QFrame(self.frame_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(245, 0))
        self.frame_21.setMaximumSize(QSize(360, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_21)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_21)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_22.setSpacing(3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 2, 0, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 49, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_13)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_19.addWidget(self.scrollArea)


        self.horizontalLayout_13.addWidget(self.frame_21)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QSize(525, 0))
        self.frame_15.setMaximumSize(QSize(700, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_15)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 40))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mudaNome_2 = QLineEdit(self.frame_18)
        self.mudaNome_2.setObjectName(u"mudaNome_2")
        self.mudaNome_2.setMinimumSize(QSize(0, 35))
        self.mudaNome_2.setMaximumSize(QSize(123456, 35))
        self.mudaNome_2.setFont(font6)
        self.mudaNome_2.setStyleSheet(u"QLineEdit{\n"
"color: rgb(170, 85, 255);\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(170, 85, 255);		\n"
"border-radius:4px;\n"
"padding-left:5px}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(247, 248, 248);\n"
"border: 2px solid rgb(170, 85, 255);		\n"
"border-radius:4px}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(247, 248, 248);\n"
"border: 2px solid rgb(170, 85, 255);		\n"
"border-radius:4px}")

        self.horizontalLayout_6.addWidget(self.mudaNome_2)

        self.salvarAlteracao_2 = QPushButton(self.frame_18)
        self.salvarAlteracao_2.setObjectName(u"salvarAlteracao_2")
        self.salvarAlteracao_2.setMinimumSize(QSize(80, 35))
        self.salvarAlteracao_2.setMaximumSize(QSize(80, 16777215))
        self.salvarAlteracao_2.setFont(font6)
        self.salvarAlteracao_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 4px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(165, 82, 247);\n"
"border-radius: 4px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 4px;\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.salvarAlteracao_2)


        self.verticalLayout_23.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_GraficoCategoria = QVBoxLayout(self.frame_17)
        self.verticalLayout_GraficoCategoria.setSpacing(0)
        self.verticalLayout_GraficoCategoria.setObjectName(u"verticalLayout_GraficoCategoria")
        self.verticalLayout_GraficoCategoria.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_23.addWidget(self.frame_17)


        self.horizontalLayout_13.addWidget(self.frame_15)


        self.verticalLayout_25.addWidget(self.frame_14)

        self.stackedWidget_2.addWidget(self.page_Categoria)

        self.verticalLayout_66.addWidget(self.stackedWidget_2)


        self.verticalLayout_252.addWidget(self.frame_167)


        self.horizontalLayout_3.addWidget(self.frame_101)

        self.frame_173 = QFrame(self.frame_perfil)
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
        self.descricao = QLabel(self.frame_175)
        self.descricao.setObjectName(u"descricao")
        self.descricao.setGeometry(QRect(30, 137, 150, 30))
        font11 = QFont()
        font11.setPointSize(14)
        self.descricao.setFont(font11)
        self.descricao.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.descricao.setAlignment(Qt.AlignCenter)
        self.userName = QLabel(self.frame_175)
        self.userName.setObjectName(u"userName")
        self.userName.setGeometry(QRect(50, 120, 110, 20))
        self.userName.setFont(font6)
        self.userName.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.userName.setAlignment(Qt.AlignCenter)
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
        self.fotoPerfil = QPushButton(self.frame_176)
        self.fotoPerfil.setObjectName(u"fotoPerfil")
        self.fotoPerfil.setStyleSheet(u"QPushButton{\n"
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
        icon20 = QIcon()
        icon20.addFile(u"../img/asd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fotoPerfil.setIcon(icon20)
        self.fotoPerfil.setIconSize(QSize(107, 118))

        self.verticalLayout_36.addWidget(self.fotoPerfil)


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
        self.label_67.setFont(font6)
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
        self.label_23.setFont(font6)
        self.label_23.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_23)

        self.horizontalSpacer_42 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_42)

        self.label_11 = QLabel(self.frame_181)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 0))
        self.label_11.setMaximumSize(QSize(60, 16777215))
        font12 = QFont()
        font12.setPointSize(10)
        self.label_11.setFont(font12)
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
        self.label_91.setFont(font6)
        self.label_91.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_91.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_91)

        self.horizontalSpacer_44 = QSpacerItem(23, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_44)

        self.TotalUser = QLabel(self.frame_365)
        self.TotalUser.setObjectName(u"TotalUser")
        self.TotalUser.setMinimumSize(QSize(50, 0))
        self.TotalUser.setMaximumSize(QSize(50, 16777215))
        self.TotalUser.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.TotalUser.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.TotalUser)


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
        self.label_58.setFont(font6)
        self.label_58.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_58)

        self.horizontalSpacer_43 = QSpacerItem(42, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_43)

        self.label_21 = QLabel(self.frame_366)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 0))
        self.label_21.setMaximumSize(QSize(50, 16777215))
        self.label_21.setFont(font12)
        self.label_21.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_21)


        self.verticalLayout_37.addWidget(self.frame_366)


        self.verticalLayout_65.addWidget(self.frame_179)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_4)

        self.dataPerfil = QLabel(self.frame_177)
        self.dataPerfil.setObjectName(u"dataPerfil")
        self.dataPerfil.setFont(font12)
        self.dataPerfil.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.dataPerfil.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_65.addWidget(self.dataPerfil)


        self.verticalLayout_35.addWidget(self.frame_177)


        self.verticalLayout_34.addWidget(self.frame_174)


        self.horizontalLayout_3.addWidget(self.frame_173)


        self.verticalLayout_12.addWidget(self.frame_perfil)

        self.stackedWidget.addWidget(self.page_perfil)
        self.page_FluxodeCaixa = QWidget()
        self.page_FluxodeCaixa.setObjectName(u"page_FluxodeCaixa")
        self.verticalLayout_13 = QVBoxLayout(self.page_FluxodeCaixa)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_FluxodeCaixa = QFrame(self.page_FluxodeCaixa)
        self.frame_FluxodeCaixa.setObjectName(u"frame_FluxodeCaixa")
        self.frame_FluxodeCaixa.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_FluxodeCaixa.setFrameShape(QFrame.StyledPanel)
        self.frame_FluxodeCaixa.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_FluxodeCaixa)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_FluxodeCaixa)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 610))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_ControleFinanceiro_2 = QFrame(self.frame)
        self.frame_ControleFinanceiro_2.setObjectName(u"frame_ControleFinanceiro_2")
        self.frame_ControleFinanceiro_2.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(170, 85, 255);")
        self.frame_ControleFinanceiro_2.setFrameShape(QFrame.StyledPanel)
        self.frame_ControleFinanceiro_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_ControleFinanceiro_2)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_ControleFinanceiro_2)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 305))
        self.frame_67.setMaximumSize(QSize(16777215, 300))
        font13 = QFont()
        font13.setBold(True)
        self.frame_67.setFont(font13)
        self.frame_67.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_GraficoDados = QVBoxLayout(self.frame_67)
        self.verticalLayout_GraficoDados.setSpacing(0)
        self.verticalLayout_GraficoDados.setObjectName(u"verticalLayout_GraficoDados")
        self.verticalLayout_GraficoDados.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_72.addWidget(self.frame_67)

        self.frame_7 = QFrame(self.frame_ControleFinanceiro_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 28)
        self.frame_224 = QFrame(self.frame_7)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setMinimumSize(QSize(250, 0))
        self.frame_224.setStyleSheet(u"")
        self.frame_224.setFrameShape(QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Raised)
        self.verticalLayout_184 = QVBoxLayout(self.frame_224)
        self.verticalLayout_184.setSpacing(0)
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.verticalLayout_184.setContentsMargins(5, 10, 5, 0)
        self.pequenoHistoricoEntrada_6 = QFrame(self.frame_224)
        self.pequenoHistoricoEntrada_6.setObjectName(u"pequenoHistoricoEntrada_6")
        self.pequenoHistoricoEntrada_6.setMinimumSize(QSize(0, 40))
        self.pequenoHistoricoEntrada_6.setStyleSheet(u"")
        self.pequenoHistoricoEntrada_6.setFrameShape(QFrame.StyledPanel)
        self.pequenoHistoricoEntrada_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.pequenoHistoricoEntrada_6)
        self.horizontalLayout_126.setSpacing(3)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(12, 3, 3, 3)
        self.frame_227 = QFrame(self.pequenoHistoricoEntrada_6)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setMaximumSize(QSize(158, 16777215))
        self.frame_227.setStyleSheet(u"")
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.verticalLayout_185 = QVBoxLayout(self.frame_227)
        self.verticalLayout_185.setSpacing(0)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.verticalLayout_185.setContentsMargins(0, 0, 0, 0)
        self.label_218 = QLabel(self.frame_227)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setFont(font9)
        self.label_218.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_218.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_185.addWidget(self.label_218)


        self.horizontalLayout_126.addWidget(self.frame_227)

        self.frame_228 = QFrame(self.pequenoHistoricoEntrada_6)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setStyleSheet(u"")
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.verticalLayout_324 = QVBoxLayout(self.frame_228)
        self.verticalLayout_324.setSpacing(0)
        self.verticalLayout_324.setObjectName(u"verticalLayout_324")
        self.verticalLayout_324.setContentsMargins(0, 0, 0, 0)
        self.label_220 = QLabel(self.frame_228)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setMaximumSize(QSize(16777215, 38))
        self.label_220.setFont(font9)
        self.label_220.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_220.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_324.addWidget(self.label_220)


        self.horizontalLayout_126.addWidget(self.frame_228)

        self.frame_250 = QFrame(self.pequenoHistoricoEntrada_6)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setStyleSheet(u"")
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Raised)
        self.verticalLayout_325 = QVBoxLayout(self.frame_250)
        self.verticalLayout_325.setSpacing(0)
        self.verticalLayout_325.setObjectName(u"verticalLayout_325")
        self.verticalLayout_325.setContentsMargins(0, 0, 0, 0)
        self.categoria_38 = QLabel(self.frame_250)
        self.categoria_38.setObjectName(u"categoria_38")
        self.categoria_38.setFont(font9)
        self.categoria_38.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.categoria_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_325.addWidget(self.categoria_38)


        self.horizontalLayout_126.addWidget(self.frame_250)

        self.frame_448 = QFrame(self.pequenoHistoricoEntrada_6)
        self.frame_448.setObjectName(u"frame_448")
        self.frame_448.setStyleSheet(u"")
        self.frame_448.setFrameShape(QFrame.StyledPanel)
        self.frame_448.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_233 = QHBoxLayout(self.frame_448)
        self.horizontalLayout_233.setSpacing(0)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(0, 0, 0, 0)
        self.frame_449 = QFrame(self.frame_448)
        self.frame_449.setObjectName(u"frame_449")
        self.frame_449.setStyleSheet(u"")
        self.frame_449.setFrameShape(QFrame.StyledPanel)
        self.frame_449.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_234 = QHBoxLayout(self.frame_449)
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.horizontalLayout_234.setContentsMargins(0, 0, 0, 0)
        self.label_221 = QLabel(self.frame_449)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setFont(font9)
        self.label_221.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_221.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_234.addWidget(self.label_221)


        self.horizontalLayout_233.addWidget(self.frame_449)


        self.horizontalLayout_126.addWidget(self.frame_448)

        self.frame_251 = QFrame(self.pequenoHistoricoEntrada_6)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setStyleSheet(u"")
        self.frame_251.setFrameShape(QFrame.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Raised)
        self.verticalLayout_326 = QVBoxLayout(self.frame_251)
        self.verticalLayout_326.setObjectName(u"verticalLayout_326")
        self.verticalLayout_326.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_251)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font9)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_326.addWidget(self.label_25)


        self.horizontalLayout_126.addWidget(self.frame_251)


        self.verticalLayout_184.addWidget(self.pequenoHistoricoEntrada_6)


        self.verticalLayout_18.addWidget(self.frame_224)

        self.scrollArea_8 = QScrollArea(self.frame_7)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setStyleSheet(u"")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 769, 223))
        self.verticalLayout_fluxo = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_fluxo.setSpacing(3)
        self.verticalLayout_fluxo.setObjectName(u"verticalLayout_fluxo")
        self.verticalLayout_fluxo.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_fluxo.addItem(self.verticalSpacer_12)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_18.addWidget(self.scrollArea_8)


        self.verticalLayout_72.addWidget(self.frame_7)

        self.frame_7.raise_()
        self.frame_67.raise_()

        self.verticalLayout_17.addWidget(self.frame_ControleFinanceiro_2)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_182 = QFrame(self.frame_FluxodeCaixa)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setMinimumSize(QSize(255, 0))
        self.frame_182.setMaximumSize(QSize(275, 16777215))
        self.frame_182.setStyleSheet(u"QFrame{\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius:0px;\n"
"}\n"
"")
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_182)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(8, 0, 8, 8)
        self.frame_196 = QFrame(self.frame_182)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMinimumSize(QSize(210, 0))
        self.frame_196.setMaximumSize(QSize(1234567, 16777215))
        self.frame_196.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_196)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_197 = QFrame(self.frame_196)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setMinimumSize(QSize(0, 200))
        self.frame_197.setMaximumSize(QSize(16777215, 200))
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_197)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 0)
        self.frame_2 = QFrame(self.frame_197)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 210, 16))
        font14 = QFont()
        font14.setPointSize(13)
        self.label.setFont(font14)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalEntradaFluxo = QLabel(self.frame_2)
        self.totalEntradaFluxo.setObjectName(u"totalEntradaFluxo")
        self.totalEntradaFluxo.setGeometry(QRect(10, 32, 220, 31))
        font15 = QFont()
        font15.setFamilies([u"Segoe UI Semibold"])
        font15.setPointSize(15)
        font15.setBold(False)
        self.totalEntradaFluxo.setFont(font15)
        self.totalEntradaFluxo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.percentualEntrada = QLabel(self.frame_2)
        self.percentualEntrada.setObjectName(u"percentualEntrada")
        self.percentualEntrada.setGeometry(QRect(14, 70, 80, 16))
        self.percentualEntrada.setFont(font12)
        self.percentualEntrada.setStyleSheet(u"color: rgb(85, 255, 127);")

        self.verticalLayout_15.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_197)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 140, 16))
        self.label_4.setFont(font14)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalSaidaFluxo = QLabel(self.frame_3)
        self.totalSaidaFluxo.setObjectName(u"totalSaidaFluxo")
        self.totalSaidaFluxo.setGeometry(QRect(10, 32, 220, 31))
        self.totalSaidaFluxo.setFont(font15)
        self.totalSaidaFluxo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.percentualSaida = QLabel(self.frame_3)
        self.percentualSaida.setObjectName(u"percentualSaida")
        self.percentualSaida.setGeometry(QRect(14, 70, 80, 16))
        self.percentualSaida.setFont(font12)
        self.percentualSaida.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_15.addWidget(self.frame_3)


        self.verticalLayout_40.addWidget(self.frame_197)

        self.frame_199 = QFrame(self.frame_196)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_199)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(3, 0, 3, 3)
        self.frame_200 = QFrame(self.frame_199)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setMinimumSize(QSize(0, 123))
        self.frame_200.setMaximumSize(QSize(16777215, 111))
        self.frame_200.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_200)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(5, 16, 91, 91))
        self.frame_4.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(170, 0, 255, 255), stop:0.183946 rgba(170, 0, 255, 255), stop:0.187291 rgba(255, 0, 0, 255), stop:0.389632 rgba(255, 0, 0, 255), stop:0.393352 rgba(255, 255, 127, 255), stop:0.568562 rgba(255, 255, 127, 255), stop:0.571906 rgba(85, 255, 255, 255), stop:0.737458 rgba(85, 255, 255, 255), stop:0.740803 rgba(85, 170, 127, 255), stop:0.854515 rgba(85, 170, 127, 255), stop:0.856187 rgba(255, 0, 127, 255), stop:1 rgba(255, 0, 127, 255));\n"
"border-radius: 45px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_5)

        self.label_9 = QLabel(self.frame_200)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(98, 8, 230, 27))
        self.label_9.setFont(font14)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.valorTotalFluxo = QLabel(self.frame_200)
        self.valorTotalFluxo.setObjectName(u"valorTotalFluxo")
        self.valorTotalFluxo.setGeometry(QRect(101, 30, 180, 31))
        self.valorTotalFluxo.setFont(font4)
        self.valorTotalFluxo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.frame_200)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(113, 68, 10, 10))
        self.label_13.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"border-radius:5px")
        self.label_14 = QLabel(self.frame_200)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(113, 87, 10, 10))
        self.label_14.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius:5px")
        self.label_15 = QLabel(self.frame_200)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(113, 106, 10, 10))
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius:5px")
        self.label_18 = QLabel(self.frame_200)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 106, 10, 10))
        self.label_18.setStyleSheet(u"background-color: rgb(255, 0, 127);\n"
"border-radius:5px")
        self.label_20 = QLabel(self.frame_200)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(170, 87, 10, 10))
        self.label_20.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"border-radius:5px")
        self.label_26 = QLabel(self.frame_200)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(170, 68, 10, 10))
        self.label_26.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-radius:5px")
        self.label_27 = QLabel(self.frame_200)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(130, 67, 20, 10))
        self.label_27.setStyleSheet(u"color: rgb(102, 0, 153);")
        self.label_28 = QLabel(self.frame_200)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(130, 86, 20, 10))
        self.label_28.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_30 = QLabel(self.frame_200)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(130, 105, 20, 10))
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 127)")
        self.label_32 = QLabel(self.frame_200)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(187, 105, 20, 10))
        self.label_32.setStyleSheet(u"color:rgb(182, 0, 91)")
        self.label_33 = QLabel(self.frame_200)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(187, 87, 20, 10))
        self.label_33.setStyleSheet(u"color: rgb(59, 118, 87)")
        self.label_34 = QLabel(self.frame_200)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(187, 66, 20, 10))
        self.label_34.setStyleSheet(u"color: rgb(85, 255, 255);")

        self.verticalLayout_70.addWidget(self.frame_200)

        self.frame_201 = QFrame(self.frame_199)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setMinimumSize(QSize(0, 181))
        self.frame_201.setMaximumSize(QSize(16777215, 185))
        self.frame_201.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.label_102 = QLabel(self.frame_201)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(7, 3, 130, 25))
        font16 = QFont()
        font16.setPointSize(11)
        self.label_102.setFont(font16)
        self.label_102.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.planoContasBuscaFluxo = QComboBox(self.frame_201)
        self.planoContasBuscaFluxo.setObjectName(u"planoContasBuscaFluxo")
        self.planoContasBuscaFluxo.setGeometry(QRect(5, 30, 223, 31))
        self.planoContasBuscaFluxo.setMinimumSize(QSize(0, 31))
        self.planoContasBuscaFluxo.setMaximumSize(QSize(16777215, 31))
        self.planoContasBuscaFluxo.setFont(font16)
        self.planoContasBuscaFluxo.setStyleSheet(u"\n"
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
        self.totalCategoria_lbl = QLabel(self.frame_201)
        self.totalCategoria_lbl.setObjectName(u"totalCategoria_lbl")
        self.totalCategoria_lbl.setGeometry(QRect(10, 80, 50, 25))
        font17 = QFont()
        font17.setFamilies([u"Segoe UI Semibold"])
        font17.setPointSize(14)
        font17.setBold(False)
        self.totalCategoria_lbl.setFont(font17)
        self.totalCategoria_lbl.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.totalCategoria = QLabel(self.frame_201)
        self.totalCategoria.setObjectName(u"totalCategoria")
        self.totalCategoria.setGeometry(QRect(58, 80, 170, 25))
        self.totalCategoria.setFont(font17)
        self.totalCategoria.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.verticalLayout_70.addWidget(self.frame_201)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_70.addItem(self.verticalSpacer_11)

        self.frame_6 = QFrame(self.frame_199)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_70.addWidget(self.frame_6)


        self.verticalLayout_40.addWidget(self.frame_199)


        self.verticalLayout_38.addWidget(self.frame_196)


        self.horizontalLayout.addWidget(self.frame_182)


        self.verticalLayout_13.addWidget(self.frame_FluxodeCaixa)

        self.stackedWidget.addWidget(self.page_FluxodeCaixa)
        self.page_ControleFinanceiro = QWidget()
        self.page_ControleFinanceiro.setObjectName(u"page_ControleFinanceiro")
        self.verticalLayout_11 = QVBoxLayout(self.page_ControleFinanceiro)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_ControleFinanceiro = QFrame(self.page_ControleFinanceiro)
        self.frame_ControleFinanceiro.setObjectName(u"frame_ControleFinanceiro")
        self.frame_ControleFinanceiro.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(170, 85, 255);")
        self.frame_ControleFinanceiro.setFrameShape(QFrame.StyledPanel)
        self.frame_ControleFinanceiro.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_ControleFinanceiro)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(8, 0, 8, 0)
        self.frame_44 = QFrame(self.frame_ControleFinanceiro)
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
        self.frame_66.setFont(font13)
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
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
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
        icon21 = QIcon()
        icon21.addFile(u"../img/fluxoEntrada.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon21)
        self.pushButton_7.setIconSize(QSize(73, 76))
        self.label_121 = QLabel(self.frame_187)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(90, 47, 80, 26))
        font18 = QFont()
        font18.setFamilies([u"Segoe UI Semibold"])
        font18.setPointSize(16)
        self.label_121.setFont(font18)
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
        font19 = QFont()
        font19.setFamilies([u"Segoe UI Semibold"])
        font19.setPointSize(16)
        font19.setBold(True)
        self.totalEntrada.setFont(font19)
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
        self.label_111.setFont(font18)
        self.label_111.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_6 = QPushButton(self.frame_189)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(5, 5, 80, 71))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
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
        icon22 = QIcon()
        icon22.addFile(u"../img/fluxoSaida.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon22)
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
        self.totalSaida.setFont(font18)
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
        self.label_113.setFont(font18)
        self.label_113.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.frame_191)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(5, 5, 81, 71))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
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
        icon23 = QIcon()
        icon23.addFile(u"../img/fluxoTotal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon23)
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
        self.valorTotal.setFont(font18)
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
        font20 = QFont()
        font20.setFamilies([u"Segoe UI Semibold"])
        font20.setPointSize(10)
        font20.setBold(False)
        self.novaMovimentacao.setFont(font20)
        self.novaMovimentacao.setStyleSheet(u"QPushButton{\n"
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
        self.label_61.setFont(font16)
        self.label_61.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.buscar = QPushButton(self.frame_185)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setGeometry(QRect(609, 29, 81, 32))
        font21 = QFont()
        font21.setPointSize(10)
        font21.setBold(False)
        self.buscar.setFont(font21)
        self.buscar.setStyleSheet(u"QPushButton{\n"
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
        self.label_8 = QLabel(self.frame_185)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(15, 0, 170, 25))
        self.label_8.setFont(font16)
        self.label_8.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.codigoBusca = QLineEdit(self.frame_185)
        self.codigoBusca.setObjectName(u"codigoBusca")
        self.codigoBusca.setGeometry(QRect(15, 30, 170, 30))
        self.codigoBusca.setFont(font12)
        self.codigoBusca.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left:3px;")
        self.label_101 = QLabel(self.frame_185)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(437, 0, 130, 25))
        self.label_101.setFont(font16)
        self.label_101.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.dataMovimentacaoInicio = QDateEdit(self.frame_185)
        self.dataMovimentacaoInicio.setObjectName(u"dataMovimentacaoInicio")
        self.dataMovimentacaoInicio.setGeometry(QRect(190, 30, 127, 30))
        font22 = QFont()
        font22.setPointSize(12)
        font22.setBold(False)
        self.dataMovimentacaoInicio.setFont(font22)
        self.dataMovimentacaoInicio.setStyleSheet(u"QDateEdit{\n"
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
        self.dataMovimentacaoInicio.setDate(QDate(2010, 1, 1))
        self.dataMovimentacaofim = QDateEdit(self.frame_185)
        self.dataMovimentacaofim.setObjectName(u"dataMovimentacaofim")
        self.dataMovimentacaofim.setGeometry(QRect(305, 30, 127, 30))
        self.dataMovimentacaofim.setFont(font22)
        self.dataMovimentacaofim.setStyleSheet(u"QDateEdit{\n"
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
        self.dataMovimentacaofim.setReadOnly(False)
        self.dataMovimentacaofim.setDate(QDate(2010, 1, 1))
        self.planoContasBusca = QComboBox(self.frame_185)
        self.planoContasBusca.setObjectName(u"planoContasBusca")
        self.planoContasBusca.setGeometry(QRect(436, 30, 170, 31))
        self.planoContasBusca.setMinimumSize(QSize(0, 31))
        self.planoContasBusca.setMaximumSize(QSize(16777215, 31))
        self.planoContasBusca.setFont(font16)
        self.planoContasBusca.setStyleSheet(u"\n"
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
        self.dataMovimentacaofim.raise_()
        self.label_61.raise_()
        self.buscar.raise_()
        self.label_8.raise_()
        self.codigoBusca.raise_()
        self.label_101.raise_()
        self.dataMovimentacaoInicio.raise_()
        self.planoContasBusca.raise_()

        self.verticalLayout_39.addWidget(self.frame_185)


        self.horizontalLayout_49.addWidget(self.frame_66)


        self.verticalLayout_67.addWidget(self.frame_50)


        self.verticalLayout_68.addWidget(self.frame_44)

        self.frame_43 = QFrame(self.frame_ControleFinanceiro)
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
        self.label_214.setFont(font9)
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
        self.label_215.setFont(font9)
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
        self.categoria.setFont(font9)
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
        self.label_217.setFont(font9)
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
        self.label_22.setFont(font9)
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 990, 332))
        self.verticalLayout_ScrolNovaTranzacao = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_ScrolNovaTranzacao.setSpacing(3)
        self.verticalLayout_ScrolNovaTranzacao.setObjectName(u"verticalLayout_ScrolNovaTranzacao")
        self.verticalLayout_ScrolNovaTranzacao.setContentsMargins(-1, 0, -1, 23)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_ScrolNovaTranzacao.addItem(self.verticalSpacer_10)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_69.addWidget(self.scrollArea_5)


        self.verticalLayout_68.addWidget(self.frame_43)


        self.verticalLayout_11.addWidget(self.frame_ControleFinanceiro)

        self.stackedWidget.addWidget(self.page_ControleFinanceiro)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_7.addWidget(self.framePrincipal)


        self.verticalLayout_6.addWidget(self.central_frame)


        self.verticalLayout_5.addWidget(self.frame_centaralCentral)


        self.verticalLayout_3.addWidget(self.frame_central)


        self.verticalLayout_2.addWidget(self.linha)


        self.verticalLayout.addWidget(self.primeiro_container)

        MainWindowMW.setCentralWidget(self.centralwidget_styleSheet)

        self.retranslateUi(MainWindowMW)

        self.stackedWidget.setCurrentIndex(0)
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
        self.movimentacao_btn.setText("")
        self.settings.setText("")
        self.QRcode.setText("")
#if QT_CONFIG(whatsthis)
        self.data.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.data.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" color:#dcbbff;\">date: </span><span style=\" color:#ffffff;\">28/06/2022</span></p></body></html>", None))
        self.criadoPor.setText(QCoreApplication.translate("MainWindowMW", u"created by: NdDaniel", None))
        self.perfil_btn.setText(QCoreApplication.translate("MainWindowMW", u"    Perfil", None))
        self.movimentacao_btn3.setText(QCoreApplication.translate("MainWindowMW", u"  Movimenta\u00e7\u00e3o", None))
        self.fluxodecaixa.setText(QCoreApplication.translate("MainWindowMW", u"  Fluxo de caixa", None))
        self.exit.setText(QCoreApplication.translate("MainWindowMW", u"   Exit", None))
        self.label_186.setText(QCoreApplication.translate("MainWindowMW", u"Movimenta\u00e7\u00e3o", None))
        self.label_31.setText(QCoreApplication.translate("MainWindowMW", u"Fazer nova ", None))
#if QT_CONFIG(whatsthis)
        self.movimentacao_btn2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.movimentacao_btn2.setText("")
        self.label_199.setText(QCoreApplication.translate("MainWindowMW", u" Finaceira", None))
#if QT_CONFIG(whatsthis)
        self.frame_opening_history_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_opening_history_btn_2.setText("")
        self.label_195.setText(QCoreApplication.translate("MainWindowMW", u"Valor total das", None))
        self.label_194.setText(QCoreApplication.translate("MainWindowMW", u"movimenta\u00e7\u00f5es", None))
        self.label_196.setText(QCoreApplication.translate("MainWindowMW", u" finaceiras", None))
        self.homeValorTotal.setText(QCoreApplication.translate("MainWindowMW", u"Kz  2.200,00", None))
#if QT_CONFIG(whatsthis)
        self.frame_user_list_btn_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_user_list_btn_3.setText("")
        self.label_203.setText(QCoreApplication.translate("MainWindowMW", u"Valor total de ", None))
        self.label_204.setText(QCoreApplication.translate("MainWindowMW", u"todas as entradas", None))
        self.label_197.setText(QCoreApplication.translate("MainWindowMW", u" finaceiras", None))
        self.homeTotalEntrada.setText(QCoreApplication.translate("MainWindowMW", u"Kz  0,00", None))
#if QT_CONFIG(whatsthis)
        self.password_faceId_btn_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.password_faceId_btn_3.setText("")
        self.label_206.setText(QCoreApplication.translate("MainWindowMW", u"todas as saidas", None))
        self.label_207.setText(QCoreApplication.translate("MainWindowMW", u"Valor total de ", None))
        self.label_198.setText(QCoreApplication.translate("MainWindowMW", u" finaceiras", None))
        self.homeTotalSaidas.setText(QCoreApplication.translate("MainWindowMW", u"Kz  0,00", None))
        self.label_227.setText(QCoreApplication.translate("MainWindowMW", u"   Entradas ", None))
        self.label_228.setText(QCoreApplication.translate("MainWindowMW", u"    Saidas", None))
#if QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; color:#aa55ff;\">Castrar Categoria</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.categoria_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.categoria_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.frame_opening_history_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_opening_history_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.frame_opening_history_lbl.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_opening_history_lbl.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; font-size:18pt; color:#aa55ff;\">Ligar WebCam</span></p></body></html>", None))
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
        self.frame_Browsin_history_lbl_2.setWhatsThis(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl_2.setText(QCoreApplication.translate("MainWindowMW", u"<html><head/><body><p><span style=\" font-family:'inherit'; color:#aa55ff;\">   Perfil do Usuario</span></p></body></html>", None))
        self.editFotho.setText(QCoreApplication.translate("MainWindowMW", u"Edit photo", None))
        self.perfifEdit.setText("")
        self.label_189.setText(QCoreApplication.translate("MainWindowMW", u"Nome", None))
        self.label_201.setText(QCoreApplication.translate("MainWindowMW", u"Senha", None))
        self.mudaNome.setPlaceholderText("")
        self.mudaSenha.setPlaceholderText("")
        self.label_200.setText(QCoreApplication.translate("MainWindowMW", u"Descri\u00e7\u00e3o", None))
        self.lineEdit_4.setPlaceholderText("")
        self.salvarAlteracao.setText(QCoreApplication.translate("MainWindowMW", u"Salvar", None))
        self.configFaceId.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("MainWindowMW", u"Config Id", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindowMW", u"Test", None))
        self.faceId.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindowMW", u"Categoria ", None))
        self.mudaNome_2.setPlaceholderText("")
        self.salvarAlteracao_2.setText(QCoreApplication.translate("MainWindowMW", u"ADD", None))
        self.descricao.setText(QCoreApplication.translate("MainWindowMW", u"Deskop Eginer", None))
        self.userName.setText(QCoreApplication.translate("MainWindowMW", u"User Name", None))
        self.fotoPerfil.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindowMW", u"Internet", None))
        self.label_64.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindowMW", u"Fast Internet", None))
        self.label_11.setText(QCoreApplication.translate("MainWindowMW", u"2.6 Mbps", None))
        self.label_91.setText(QCoreApplication.translate("MainWindowMW", u"Total Users", None))
        self.TotalUser.setText(QCoreApplication.translate("MainWindowMW", u"1", None))
        self.label_58.setText(QCoreApplication.translate("MainWindowMW", u" Version", None))
        self.label_21.setText(QCoreApplication.translate("MainWindowMW", u"0.8.9", None))
        self.dataPerfil.setText(QCoreApplication.translate("MainWindowMW", u"07/09/2022", None))
        self.label_218.setText(QCoreApplication.translate("MainWindowMW", u"C\u00f3digo", None))
        self.label_220.setText(QCoreApplication.translate("MainWindowMW", u"Data de \n"
"Movimenta\u00e7\u00e3o", None))
        self.categoria_38.setText(QCoreApplication.translate("MainWindowMW", u"Planos de Contas", None))
        self.label_221.setText(QCoreApplication.translate("MainWindowMW", u"Complemento", None))
        self.label_25.setText(QCoreApplication.translate("MainWindowMW", u"Valor", None))
        self.label.setText(QCoreApplication.translate("MainWindowMW", u"Total de entradas", None))
        self.totalEntradaFluxo.setText(QCoreApplication.translate("MainWindowMW", u"Kz 0,00", None))
        self.percentualEntrada.setText(QCoreApplication.translate("MainWindowMW", u"0%", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowMW", u"Total de saidas ", None))
        self.totalSaidaFluxo.setText(QCoreApplication.translate("MainWindowMW", u"Kz 0,00", None))
        self.percentualSaida.setText(QCoreApplication.translate("MainWindowMW", u"0%", None))
        self.label_9.setText(QCoreApplication.translate("MainWindowMW", u"Total de Valores", None))
        self.valorTotalFluxo.setText(QCoreApplication.translate("MainWindowMW", u"Kz 0,00", None))
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_18.setText("")
        self.label_20.setText("")
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindowMW", u"0%", None))
        self.label_28.setText(QCoreApplication.translate("MainWindowMW", u"0%", None))
        self.label_30.setText(QCoreApplication.translate("MainWindowMW", u"0%", None))
        self.label_32.setText(QCoreApplication.translate("MainWindowMW", u"0%", None))
        self.label_33.setText(QCoreApplication.translate("MainWindowMW", u"0%", None))
        self.label_34.setText(QCoreApplication.translate("MainWindowMW", u"0%", None))
        self.label_102.setText(QCoreApplication.translate("MainWindowMW", u"Valor por Categoria", None))
        self.planoContasBuscaFluxo.setPlaceholderText(QCoreApplication.translate("MainWindowMW", u"Planos de contas", None))
        self.totalCategoria_lbl.setText(QCoreApplication.translate("MainWindowMW", u"Total:", None))
        self.totalCategoria.setText(QCoreApplication.translate("MainWindowMW", u"Kz 0,00", None))
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
        self.buscar.setText(QCoreApplication.translate("MainWindowMW", u"Buscar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindowMW", u"C\u00f3digo", None))
        self.codigoBusca.setPlaceholderText(QCoreApplication.translate("MainWindowMW", u"C\u00f3digo", None))
        self.label_101.setText(QCoreApplication.translate("MainWindowMW", u"Planos de contas", None))
        self.dataMovimentacaoInicio.setDisplayFormat(QCoreApplication.translate("MainWindowMW", u"dd/MM/yyyy", None))
        self.planoContasBusca.setPlaceholderText(QCoreApplication.translate("MainWindowMW", u"Planos de contas", None))
        self.label_214.setText(QCoreApplication.translate("MainWindowMW", u"C\u00f3digo", None))
        self.label_215.setText(QCoreApplication.translate("MainWindowMW", u"Data de \n"
"Movimenta\u00e7\u00e3o", None))
        self.categoria.setText(QCoreApplication.translate("MainWindowMW", u"Planos de Contas", None))
        self.label_217.setText(QCoreApplication.translate("MainWindowMW", u"Complemento", None))
        self.label_22.setText(QCoreApplication.translate("MainWindowMW", u"Valor", None))
    # retranslateUi

