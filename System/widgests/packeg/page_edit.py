# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYAUfhh.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_page_edit(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(607, 520)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame_25 = QFrame(Form)
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
        font = QFont()
        font.setPointSize(15)
        self.plainTextEdit.setFont(font)
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
        font1 = QFont()
        font1.setPointSize(11)
        self.open.setFont(font1)

        self.horizontalLayout_34.addWidget(self.open)

        self.save = QPushButton(self.frame_98)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(75, 30))
        self.save.setMaximumSize(QSize(75, 30))
        self.save.setFont(font1)

        self.horizontalLayout_34.addWidget(self.save)


        self.verticalLayout_32.addWidget(self.frame_98)


        self.horizontalLayout_31.addWidget(self.frame_99)


        self.verticalLayout.addWidget(self.frame_25)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.plainTextEdit.setPlainText("")
        self.open.setText(QCoreApplication.translate("Form", u"Open", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

