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
        MainWindow.resize(1274, 860)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.functionalityContainer = QWidget(self.centralwidget)
        self.functionalityContainer.setObjectName(u"functionalityContainer")
        self.functionalityContainer.setGeometry(QRect(12, 112, 1900, 700))
        self.functionalityContainer.setMinimumSize(QSize(1900, 0))
        self.functionalityContainer.setMaximumSize(QSize(1000, 700))
        self.horizontalLayout = QHBoxLayout(self.functionalityContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menuContainer = QWidget(self.functionalityContainer)
        self.menuContainer.setObjectName(u"menuContainer")
        self.menuContainer.setMaximumSize(QSize(45, 16777215))
        self.menuContainer.setStyleSheet(u"background-color: rgba(0, 0, 0, 189);\n"
"border-radius: 10;")
        self.verticalLayout_3 = QVBoxLayout(self.menuContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.missionDataSwitch = QWidget(self.menuContainer)
        self.missionDataSwitch.setObjectName(u"missionDataSwitch")
        self.missionDataSwitch.setMinimumSize(QSize(0, 40))
        self.missionDataSwitch.setMaximumSize(QSize(45, 45))
        self.missionDataSwitch.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.missionButton = QPushButton(self.missionDataSwitch)
        self.missionButton.setObjectName(u"missionButton")
        self.missionButton.setGeometry(QRect(4, 5, 201, 32))
        font = QFont()
        font.setFamilies([u"Noto Sans New Tai Lue"])
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
        self.horizontalLayout_3 = QHBoxLayout(self.middleContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.middleContainer)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_5 = QWidget(self.middleContainer)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(500, 0))
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 220, 271, 91))

        self.horizontalLayout_3.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.middleContainer)
        self.widget_4.setObjectName(u"widget_4")

        self.horizontalLayout_3.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.middleContainer)

        self.funtionsContainer = QWidget(self.functionalityContainer)
        self.funtionsContainer.setObjectName(u"funtionsContainer")
        self.funtionsContainer.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout = QVBoxLayout(self.funtionsContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addWidget(self.funtionsContainer)

        self.headerContainer = QWidget(self.centralwidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setGeometry(QRect(10, 20, 1900, 75))
        self.headerContainer.setMinimumSize(QSize(1900, 75))
        self.headerContainer.setMaximumSize(QSize(1900, 75))
        self.horizontalLayout_2 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 1, 12, 1)
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
        self.headerDisplayContainer.setMinimumSize(QSize(0, 75))
        self.horizontalLayout_4 = QHBoxLayout(self.headerDisplayContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.widget_9 = QWidget(self.headerDisplayContainer)
        self.widget_9.setObjectName(u"widget_9")

        self.horizontalLayout_4.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.headerDisplayContainer)
        self.widget_8.setObjectName(u"widget_8")

        self.horizontalLayout_4.addWidget(self.widget_8)

        self.widget_6 = QWidget(self.headerDisplayContainer)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(50, 0))
        self.widget_10.setMaximumSize(QSize(200, 16777215))
        self.widget_10.setStyleSheet(u"background-color: rgba(0, 0, 0, 189);\n"
"border-radius: 10;")
        self.verticalLayout_5 = QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.widget_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_5.addWidget(self.widget_10)


        self.horizontalLayout_4.addWidget(self.widget_6)

        self.heightContainer = QWidget(self.headerDisplayContainer)
        self.heightContainer.setObjectName(u"heightContainer")
        self.heightContainer.setMinimumSize(QSize(50, 0))
        self.heightContainer.setMaximumSize(QSize(100, 16777215))
        self.heightContainer.setStyleSheet(u"background-color: rgba(0, 0, 0, 189);\n"
"border-radius: 10;")
        self.verticalLayout_4 = QVBoxLayout(self.heightContainer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.feetText = QLabel(self.heightContainer)
        self.feetText.setObjectName(u"feetText")
        font1 = QFont()
        font1.setPointSize(25)
        self.feetText.setFont(font1)
        self.feetText.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.feetText.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.feetText)

        self.feetLabelText = QLabel(self.heightContainer)
        self.feetLabelText.setObjectName(u"feetLabelText")
        self.feetLabelText.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.feetLabelText.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.feetLabelText)


        self.horizontalLayout_4.addWidget(self.heightContainer)


        self.horizontalLayout_2.addWidget(self.headerDisplayContainer)

        self.videoLable = QLabel(self.centralwidget)
        self.videoLable.setObjectName(u"videoLable")
        self.videoLable.setGeometry(QRect(0, -10, 1920, 1080))
        self.videoLable.setMinimumSize(QSize(1920, 1080))
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
        self.missionButton.setText(QCoreApplication.translate("MainWindow", u"tests de", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Stream", None))
        self.toggleButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.feetText.setText(QCoreApplication.translate("MainWindow", u"100ft", None))
        self.feetLabelText.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.videoLable.setText("")
    # retranslateUi

