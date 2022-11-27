# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_webkpcAiM.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_page_web(object):
    def setupUi(self, page_web):
        if not page_web.objectName():
            page_web.setObjectName(u"page_web")
        page_web.resize(400, 300)
        self.verticalLayout = QVBoxLayout(page_web)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(page_web)
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
        icon = QIcon()
        icon.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/search_30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pesquisar_btn.setIcon(icon)
        self.pesquisar_btn.setIconSize(QSize(23, 23))

        self.horizontalLayout_7.addWidget(self.pesquisar_btn)

        self.update = QPushButton(self.frame_9)
        self.update.setObjectName(u"update")
        self.update.setMinimumSize(QSize(34, 34))
        self.update.setMaximumSize(QSize(34, 34))
        self.update.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update.setIcon(icon1)
        self.update.setIconSize(QSize(23, 23))

        self.horizontalLayout_7.addWidget(self.update)

        self.LineUrl = QLineEdit(self.frame_9)
        self.LineUrl.setObjectName(u"LineUrl")
        self.LineUrl.setMinimumSize(QSize(0, 36))
        self.LineUrl.setMaximumSize(QSize(16777215, 36))
        font = QFont()
        font.setPointSize(13)
        self.LineUrl.setFont(font)
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
        icon2 = QIcon()
        icon2.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/microphone_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.voz_btn.setIcon(icon2)
        self.voz_btn.setIconSize(QSize(23, 23))

        self.horizontalLayout_7.addWidget(self.voz_btn)

        self.arrow_left = QPushButton(self.frame_9)
        self.arrow_left.setObjectName(u"arrow_left")
        self.arrow_left.setMinimumSize(QSize(34, 34))
        self.arrow_left.setMaximumSize(QSize(34, 34))
        self.arrow_left.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrow_left.setIcon(icon3)
        self.arrow_left.setIconSize(QSize(22, 22))

        self.horizontalLayout_7.addWidget(self.arrow_left)

        self.arrow_right = QPushButton(self.frame_9)
        self.arrow_right.setObjectName(u"arrow_right")
        self.arrow_right.setMinimumSize(QSize(34, 34))
        self.arrow_right.setMaximumSize(QSize(34, 34))
        self.arrow_right.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../../../../3D Objects/ControleFinanceiro/System/img/24x24/cil-arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrow_right.setIcon(icon4)
        self.arrow_right.setIconSize(QSize(22, 22))

        self.horizontalLayout_7.addWidget(self.arrow_right)


        self.horizontalLayout_8.addWidget(self.frame_9, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_16 = QFrame(page_web)
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


        self.verticalLayout.addWidget(self.frame_16)


        self.retranslateUi(page_web)

        QMetaObject.connectSlotsByName(page_web)
    # setupUi

    def retranslateUi(self, page_web):
        page_web.setWindowTitle(QCoreApplication.translate("page_web", u"Form", None))
        self.pesquisar_btn.setText("")
        self.update.setText("")
        self.LineUrl.setInputMask("")
        self.LineUrl.setPlaceholderText(QCoreApplication.translate("page_web", u"Procurar no Google ou Introduza uma URL", None))
        self.voz_btn.setText("")
        self.arrow_left.setText("")
        self.arrow_right.setText("")
    # retranslateUi

