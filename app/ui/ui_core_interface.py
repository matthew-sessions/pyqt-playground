# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'core_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1283, 860)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.functionalityContainer = QWidget(self.centralwidget)
        self.functionalityContainer.setObjectName(u"functionalityContainer")
        self.functionalityContainer.setGeometry(QRect(12, 112, 1231, 900))
        self.horizontalLayout = QHBoxLayout(self.functionalityContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menuContainer = QWidget(self.functionalityContainer)
        self.menuContainer.setObjectName(u"menuContainer")
        self.menuContainer.setMaximumSize(QSize(45, 16777215))
        self.menuContainer.setStyleSheet(u"background-color: rgba(18, 18, 28, 215);\n"
"border-radius: 10;")
        self.verticalLayout_3 = QVBoxLayout(self.menuContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.missionDataSwitch = QWidget(self.menuContainer)
        self.missionDataSwitch.setObjectName(u"missionDataSwitch")
        self.missionDataSwitch.setMinimumSize(QSize(0, 45))
        self.missionDataSwitch.setMaximumSize(QSize(16777215, 45))
        self.missionDataSwitch.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.missionButton = QPushButton(self.missionDataSwitch)
        self.missionButton.setObjectName(u"missionButton")
        self.missionButton.setGeometry(QRect(4, 5, 201, 32))
        font = QFont()
        font.setFamilies([u"Adelle Sans Devanagari"])
        font.setPointSize(18)
        self.missionButton.setFont(font)
        self.missionButton.setStyleSheet(u"text-align: left;\n"
"color: white;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/bird.png", QSize(), QIcon.Normal, QIcon.Off)
        self.missionButton.setIcon(icon)
        self.missionButton.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.missionDataSwitch)

        self.widget_3 = QWidget(self.menuContainer)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 45))
        self.widget_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.menuContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.menuContainer)

        self.middleContainer = QWidget(self.functionalityContainer)
        self.middleContainer.setObjectName(u"middleContainer")

        self.horizontalLayout.addWidget(self.middleContainer)

        self.funtionsContainer = QWidget(self.functionalityContainer)
        self.funtionsContainer.setObjectName(u"funtionsContainer")
        self.funtionsContainer.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout = QVBoxLayout(self.funtionsContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addWidget(self.funtionsContainer)

        self.headerContainer = QWidget(self.centralwidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setGeometry(QRect(10, 10, 1231, 101))
        self.headerContainer.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_2 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menuToggle = QWidget(self.headerContainer)
        self.menuToggle.setObjectName(u"menuToggle")
        self.menuToggle.setMinimumSize(QSize(0, 0))
        self.menuToggle.setMaximumSize(QSize(45, 45))
        self.menuToggle.setStyleSheet(u"background-color: rgba(18, 18, 28, 215);\n"
"border-radius: 10;")
        self.verticalLayout_2 = QVBoxLayout(self.menuToggle)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.menuToggle)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(0, 35))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/menu-button-of-three-horizontal-lines.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleButton.setIcon(icon1)
        self.toggleButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.toggleButton)


        self.horizontalLayout_2.addWidget(self.menuToggle)

        self.headerDisplayContainer = QWidget(self.headerContainer)
        self.headerDisplayContainer.setObjectName(u"headerDisplayContainer")

        self.horizontalLayout_2.addWidget(self.headerDisplayContainer)

        self.videoLable = QLabel(self.centralwidget)
        self.videoLable.setObjectName(u"videoLable")
        self.videoLable.setGeometry(QRect(0, -10, 1920, 1080))
        self.videoLable.setStyleSheet(u"background-color: rgb(236, 255, 18)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.videoLable.raise_()
        self.functionalityContainer.raise_()
        self.headerContainer.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.missionButton.setText("")
        self.toggleButton.setText("")
        self.videoLable.setText("")
    # retranslateUi

