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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(599, 280)
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit_1 = QTextEdit(self.centralwidget)
        self.textEdit_1.setObjectName(u"textEdit_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_1.sizePolicy().hasHeightForWidth())
        self.textEdit_1.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(18)
        font.setBold(True)
        self.textEdit_1.setFont(font)

        self.gridLayout.addWidget(self.textEdit_1, 0, 0, 1, 2)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(111)
        sizePolicy2.setVerticalStretch(111)
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setMinimumSize(QSize(111, 111))
        self.btn_1.setMaximumSize(QSize(333, 333))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_1.setFont(font1)
        self.btn_1.setStyleSheet(u"QPushButton{\n"
"	font: 700 22pt \"Segoe UI\";\n"
"background-color: rgb(85, 255, 0);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_1, 5, 1, 1, 1)

        self.rbtn_1 = QRadioButton(self.centralwidget)
        self.rbtn_1.setObjectName(u"rbtn_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rbtn_1.sizePolicy().hasHeightForWidth())
        self.rbtn_1.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        brush2 = QBrush(QColor(220, 162, 50, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush4 = QBrush(QColor(85, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(85, 255, 255, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.rbtn_1.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Text Semibold"])
        font2.setPointSize(18)
        font2.setWeight(QFont.DemiBold)
        font2.setItalic(False)
        self.rbtn_1.setFont(font2)
        self.rbtn_1.setStyleSheet(u"font: 600 18pt \"Segoe UI Variable Text Semibold\";\n"
"color: rgb(85, 255, 255);")

        self.gridLayout.addWidget(self.rbtn_1, 2, 0, 1, 1)

        self.rbtn_3 = QRadioButton(self.centralwidget)
        self.rbtn_3.setObjectName(u"rbtn_3")
        sizePolicy3.setHeightForWidth(self.rbtn_3.sizePolicy().hasHeightForWidth())
        self.rbtn_3.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush6 = QBrush(QColor(255, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        brush7 = QBrush(QColor(255, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.rbtn_3.setPalette(palette2)
        self.rbtn_3.setFont(font2)
        self.rbtn_3.setStyleSheet(u"font: 600 18pt \"Segoe UI Variable Text Semibold\";\n"
"color: rgb(255, 0, 0);\n"
"")

        self.gridLayout.addWidget(self.rbtn_3, 6, 0, 1, 1)

        self.rbtn_2 = QRadioButton(self.centralwidget)
        self.rbtn_2.setObjectName(u"rbtn_2")
        sizePolicy3.setHeightForWidth(self.rbtn_2.sizePolicy().hasHeightForWidth())
        self.rbtn_2.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush8 = QBrush(QColor(255, 255, 127, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        brush9 = QBrush(QColor(255, 255, 127, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.rbtn_2.setPalette(palette3)
        self.rbtn_2.setFont(font2)
        self.rbtn_2.setStyleSheet(u"font: 600 18pt \"Segoe UI Variable Text Semibold\";\n"
"color: rgb(255, 255, 127);")

        self.gridLayout.addWidget(self.rbtn_2, 5, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password_Generator", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.rbtn_1.setText(QCoreApplication.translate("MainWindow", u"Normal Password", None))
        self.rbtn_3.setText(QCoreApplication.translate("MainWindow", u"Expert Password", None))
        self.rbtn_2.setText(QCoreApplication.translate("MainWindow", u"Strong Password", None))
    # retranslateUi

