# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(454, 590)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(242, 178, 55, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(25, 42, 50, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.textEdit_1 = QTextEdit(self.centralwidget)
        self.textEdit_1.setObjectName(u"textEdit_1")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(True)
        self.textEdit_1.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.textEdit_1)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.textEdit_2.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.textEdit_2)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(111)
        sizePolicy1.setVerticalStretch(111)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setMinimumSize(QSize(111, 111))
        self.btn_1.setMaximumSize(QSize(333, 333))
        font2 = QFont()
        font2.setFamilies([u"Segoe Script"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_1.setFont(font2)
        self.btn_1.setStyleSheet(u"QPushButton{\n"
"	font: 700 16pt \"Segoe Script\";\n"
"	background-color: rgb(170, 0, 255);\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.btn_1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setMinimumSize(QSize(111, 111))
        self.btn_2.setMaximumSize(QSize(333, 333))
        self.btn_2.setFont(font2)
        self.btn_2.setStyleSheet(u"QPushButton{\n"
"	font: 700 16pt \"Segoe Script\";\n"
"	background-color: rgb(85, 255, 0);\n"
"}")
        self.btn_2.setIconSize(QSize(16, 16))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.btn_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Line Break Removal", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"New Text", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"Line Break Removal", None))
    # retranslateUi

