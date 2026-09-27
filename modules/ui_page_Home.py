# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_HomesPijoO.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_page_Home(object):
    def setupUi(self, page_Home):
        if not page_Home.objectName():
            page_Home.setObjectName(u"page_Home")
        page_Home.resize(684, 558)
        self.verticalLayout = QVBoxLayout(page_Home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_principal_Contaner = QFrame(page_Home)
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
        font = QFont()
        font.setFamilies([u"Bauhaus 93"])
        font.setPointSize(64)
        self.logo_principal_2.setFont(font)
        self.logo_principal_2.setStyleSheet(u"color: rgb(219, 218, 218);\n"
"padding-bottom:0px;\n"
"\n"
"")
        self.logo_principal_2.setPixmap(QPixmap(u"../../../../3D Objects/ControleFinanceiro/System/img/SystemMW.png"))
        self.logo_principal_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.logo_principal_2)


        self.verticalLayout.addWidget(self.logo_principal_Contaner)


        self.retranslateUi(page_Home)

        QMetaObject.connectSlotsByName(page_Home)
    # setupUi

    def retranslateUi(self, page_Home):
        page_Home.setWindowTitle(QCoreApplication.translate("page_Home", u"Form", None))
        self.logo_principal_2.setText("")
    # retranslateUi

