# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_perfilFkKNBB.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_page_perfil(object):
    def setupUi(self, page_perfil):
        if not page_perfil.objectName():
            page_perfil.setObjectName(u"page_perfil")
        page_perfil.resize(405, 539)
        self.verticalLayout = QVBoxLayout(page_perfil)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(page_perfil)
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
        font = QFont()
        font.setPointSize(17)
        self.frame_Browsin_history_lbl.setFont(font)
        self.frame_Browsin_history_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_Browsin_history_btn = QPushButton(self.frame_Browsin_history)
        self.frame_Browsin_history_btn.setObjectName(u"frame_Browsin_history_btn")
        self.frame_Browsin_history_btn.setGeometry(QRect(13, 13, 90, 71))
        icon = QIcon()
        icon.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/web_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_Browsin_history_btn.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/close_pane_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_opening_history_btn.setIcon(icon1)
        self.frame_opening_history_btn.setIconSize(QSize(100, 100))
        self.frame_opening_history_lbl = QLabel(self.frame_opening_history)
        self.frame_opening_history_lbl.setObjectName(u"frame_opening_history_lbl")
        self.frame_opening_history_lbl.setGeometry(QRect(16, 100, 171, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.frame_opening_history_lbl.setFont(font1)
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
        icon2 = QIcon()
        icon2.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/user_menu_female_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_user_list_btn.setIcon(icon2)
        self.frame_user_list_btn.setIconSize(QSize(115, 115))
        self.frame_user_list_lbl = QLabel(self.frame_user_list)
        self.frame_user_list_lbl.setObjectName(u"frame_user_list_lbl")
        self.frame_user_list_lbl.setGeometry(QRect(16, 100, 100, 30))
        self.frame_user_list_lbl.setFont(font1)
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
        icon3 = QIcon()
        icon3.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/instagram_logo_120px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.password_faceId_btn_2.setIcon(icon3)
        self.password_faceId_btn_2.setIconSize(QSize(110, 130))
        self.lineEdit_2 = QLineEdit(self.frame_password_faceId)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(59, 53, 106, 32))
        font2 = QFont()
        font2.setPointSize(15)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"border-radius:7px;\n"
"color:rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px solid rgb(170, 85, 255)")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.password_faceId_lbl_6 = QLabel(self.frame_password_faceId)
        self.password_faceId_lbl_6.setObjectName(u"password_faceId_lbl_6")
        self.password_faceId_lbl_6.setGeometry(QRect(18, 101, 186, 30))
        self.password_faceId_lbl_6.setFont(font1)
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
        self.ios_lbl_2.setFont(font1)
        self.ios_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ios_btn_2 = QPushButton(self.frame_IOs_2)
        self.ios_btn_2.setObjectName(u"ios_btn_2")
        self.ios_btn_2.setGeometry(QRect(7, 7, 50, 50))
        icon4 = QIcon()
        icon4.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/mac_client_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ios_btn_2.setIcon(icon4)
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
        self.ibm_lbl_2.setFont(font1)
        self.ibm_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ibm_btn_2 = QPushButton(self.frame_IBM_2)
        self.ibm_btn_2.setObjectName(u"ibm_btn_2")
        self.ibm_btn_2.setGeometry(QRect(10, 15, 50, 30))
        icon5 = QIcon()
        icon5.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/ibm_70px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ibm_btn_2.setIcon(icon5)
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
        font3 = QFont()
        font3.setPointSize(14)
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.frame_175)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 120, 110, 20))
        self.label_16.setFont(font1)
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
        self.label_67.setFont(font1)
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
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_23)

        self.horizontalSpacer_42 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_42)

        self.label_11 = QLabel(self.frame_181)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 0))
        self.label_11.setMaximumSize(QSize(60, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        self.label_11.setFont(font4)
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
        self.label_91.setFont(font1)
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
        self.label_58.setFont(font1)
        self.label_58.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_58)

        self.horizontalSpacer_43 = QSpacerItem(42, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_43)

        self.label_21 = QLabel(self.frame_366)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 0))
        self.label_21.setMaximumSize(QSize(50, 16777215))
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_21)


        self.verticalLayout_37.addWidget(self.frame_366)


        self.verticalLayout_65.addWidget(self.frame_179)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_4)

        self.label_19 = QLabel(self.frame_177)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_65.addWidget(self.label_19)


        self.verticalLayout_35.addWidget(self.frame_177)


        self.verticalLayout_34.addWidget(self.frame_174)


        self.horizontalLayout_3.addWidget(self.frame_173)


        self.verticalLayout.addWidget(self.frame_100)


        self.retranslateUi(page_perfil)

        QMetaObject.connectSlotsByName(page_perfil)
    # setupUi

    def retranslateUi(self, page_perfil):
        page_perfil.setWindowTitle(QCoreApplication.translate("page_perfil", u"Form", None))
#if QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl.setWhatsThis(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_Browsin_history_lbl.setText(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><span style=\" font-family:'inherit'; color:#aa55ff;\">Browsing history</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.frame_Browsin_history_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_Browsin_history_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.frame_opening_history_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_opening_history_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.frame_opening_history_lbl.setWhatsThis(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_opening_history_lbl.setText(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><span style=\" font-family:'inherit'; font-size:18pt; color:#aa55ff;\">Opening history</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.frame_user_list_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.frame_user_list_btn.setText("")
#if QT_CONFIG(whatsthis)
        self.frame_user_list_lbl.setWhatsThis(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.frame_user_list_lbl.setText(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><span style=\" font-family:'inherit'; font-size:18pt; color:#aa55ff;\">User list</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.password_faceId_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.password_faceId_btn_2.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("page_perfil", u"123456789", None))
#if QT_CONFIG(whatsthis)
        self.password_faceId_lbl_6.setWhatsThis(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.password_faceId_lbl_6.setText(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><span style=\" font-family:'inherit'; font-size:18pt; color:#aa55ff;\">Password face id </span></p></body></html>", None))
        self.label_29.setText("")
#if QT_CONFIG(whatsthis)
        self.ios_lbl_2.setWhatsThis(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ios_lbl_2.setText(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><span style=\" color:#ffffff;\">IOS</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.ios_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ios_btn_2.setText("")
        self.iconWindow_4.setText("")
#if QT_CONFIG(whatsthis)
        self.ibm_lbl_2.setWhatsThis(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><br/></p><p><span style=\" color:#ffffff;\">Unity</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ibm_lbl_2.setText(QCoreApplication.translate("page_perfil", u"<html><head/><body><p><span style=\" color:#ffffff;\">IBM</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.ibm_btn_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ibm_btn_2.setText("")
        self.label_17.setText(QCoreApplication.translate("page_perfil", u"Deskop Eginer", None))
        self.label_16.setText(QCoreApplication.translate("page_perfil", u"User Name", None))
        self.label_7.setText("")
        self.label_67.setText(QCoreApplication.translate("page_perfil", u"Internet", None))
        self.label_64.setText("")
        self.label_23.setText(QCoreApplication.translate("page_perfil", u"Fast Internet", None))
        self.label_11.setText(QCoreApplication.translate("page_perfil", u"2.6 Mbps", None))
        self.label_91.setText(QCoreApplication.translate("page_perfil", u"Total Users", None))
        self.label_93.setText(QCoreApplication.translate("page_perfil", u"1", None))
        self.label_58.setText(QCoreApplication.translate("page_perfil", u" Version", None))
        self.label_21.setText(QCoreApplication.translate("page_perfil", u"0.8.9", None))
        self.label_19.setText(QCoreApplication.translate("page_perfil", u"07/09/2022", None))
    # retranslateUi

