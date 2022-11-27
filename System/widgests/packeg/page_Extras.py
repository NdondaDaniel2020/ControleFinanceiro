# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_ExtrascZQDRy.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_page_Extras(object):
    def setupUi(self, page_Extras):
        if not page_Extras.objectName():
            page_Extras.setObjectName(u"page_Extras")
        page_Extras.resize(400, 300)
        self.verticalLayout = QVBoxLayout(page_Extras)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_182 = QFrame(page_Extras)
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


        self.verticalLayout.addWidget(self.frame_182)


        self.retranslateUi(page_Extras)

        QMetaObject.connectSlotsByName(page_Extras)
    # setupUi

    def retranslateUi(self, page_Extras):
        page_Extras.setWindowTitle(QCoreApplication.translate("page_Extras", u"Form", None))
    # retranslateUi

