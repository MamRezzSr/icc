# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainqYaIDj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1000, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        QFontDatabase.addApplicationFont("fonts/IRANSans.ttf")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)

        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_toggle.sizePolicy().hasHeightForWidth())
        self.frame_toggle.setSizePolicy(sizePolicy)
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        font = QFont()
        font.setFamily(u"IRANSans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.comboBox = QComboBox(self.page_1)
        icon = QIcon()
        icon.addFile(u"icons/flags/eu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u"icons/flags/ir.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u"icons/flags/gb.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u"icons/flags/us.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u"icons/flags/ae.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u"icons/flags/no.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u"icons/flags/se.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u"icons/flags/iq.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u"icons/flags/cn.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u"icons/flags/tr.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u"icons/flags/au.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u"icons/flags/ca.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon11, "")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(550, 40, 260, 55))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(9)
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"#comboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:1px solid #ced4da;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"#comboBox::down-arrow {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	margin-right: 15px;\n"
"}\n"
"#comboBox:on {\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"#comboBox QListView{\n"
"	font-size: 12px;\n"
"	border: 1px solid rgba(0,0,0, 10%);\n"
"	padding: 5x;\n"
"	background-color: #fff;\n"
"	outline: 0px;\n"
"}\n"
"#comboBox QListView::item{\n"
"	padding-left: 10px;\n"
"	background-color: #fff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color:rgb(189, 189, 189)\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    selection-background-color:rgb(189, 189, 189)\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 15px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
""
                        "	min-height: 5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(0, 115, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(0, 115, 255);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 5px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 5px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:"
                        "hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(8)
        self.lineEdit = QLineEdit(self.page_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(550, 140, 260, 55))
        font2 = QFont()
        font2.setPointSize(9)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(204, 204, 204);\n"
"	border-radius: 5px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(204, 204, 204);\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(177, 177, 177);\n"
"	border: 2px solid rgb(177, 177, 177);\n"
"}\n"
"QLineEdit:focus{\n"
"	background-color: rgb(177, 177, 177);\n"
"	border: 2px solid rgb(177, 177, 177);\n"
"}\n"
"")
        self.comboBox_2 = QComboBox(self.page_1)
        self.comboBox_2.addItem(icon1, "")
        self.comboBox_2.addItem(icon, "")
        self.comboBox_2.addItem(icon2, "")
        self.comboBox_2.addItem(icon3, "")
        self.comboBox_2.addItem(icon4, "")
        self.comboBox_2.addItem(icon5, "")
        self.comboBox_2.addItem(icon6, "")
        self.comboBox_2.addItem(icon7, "")
        self.comboBox_2.addItem(icon8, "")
        self.comboBox_2.addItem(icon9, "")
        self.comboBox_2.addItem(icon10, "")
        self.comboBox_2.addItem(icon11, "")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(240, 40, 260, 55))
        self.comboBox_2.setFont(font2)
        self.comboBox_2.setStyleSheet(u"#comboBox_2{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:1px solid #ced4da;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"#comboBox_2::down-arrow {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	margin-right: 15px;\n"
"}\n"
"#comboBox_2:on {\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"#comboBox_2 QListView{\n"
"	font-size: 12px;\n"
"	border: 1px solid rgba(0,0,0, 10%);\n"
"	padding: 5x;\n"
"	background-color: #fff;\n"
"	outline: 0px;\n"
"}\n"
"#comboBox_2 QListView::item{\n"
"	padding-left: 10px;\n"
"	background-color: #fff;\n"
"}\n"
"#comboBox_2 QListView::item:hover{\n"
"	background-color: #1e90ff;\n"
"}\n"
"#comboBox_2 QListView::item:selected{\n"
"	background-color: #1e90ff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color:rgb(189, 189, 189)\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    selection-background-color:rgb(189, 189, 189)\n"
"}\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 15px;\n"
"    margin: "
                        "15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(0, 115, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(0, 115, 255);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 5px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 5px;\n"
"	border-bottom"
                        "-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(8)
        self.label_date = QLabel(self.page_1)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(750, 240, 61, 31))
        font3 = QFont()
        font3.setFamily(u"IRANSans")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_date.setFont(font3)
        self.label_date.setLayoutDirection(Qt.RightToLeft)
        self.label_date.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_date.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 140, 260, 55))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel{\n"
"	border: 2px solid rgb(204, 204, 204);\n"
"	border-radius: 5px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(204, 204, 204);\n"
"}\n"
"QLabel:hover{\n"
"	background-color: rgb(177, 177, 177);\n"
"	border: 2px solid rgb(177, 177, 177);\n"
"}\n"
"QLabel:focus{\n"
"	background-color: rgb(177, 177, 177);\n"
"	border: 2px solid rgb(177, 177, 177);\n"
"}\n"
"")
        self.btn_convert = QPushButton(self.page_1)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setGeometry(QRect(90, 45, 93, 41))
        self.btn_convert.setFont(font)
        self.btn_convert.setStyleSheet(u"#btn_convert{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;;\n"
"	border-radius: 5px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"#btn_convert:hover{\n"
"	background-color: rgb(0, 115, 255);\n"
"}\n"
"#btn_convert:pressed{\n"
"	background-color: rgb(0, 0, 255)\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(0, 115, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(0, 115, 255);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBa"
                        "r::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizo"
                        "ntal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_1 = QWidget()
        self.scrollAreaWidgetContents_1.setObjectName(u"scrollAreaWidgetContents_1")
        self.scrollAreaWidgetContents_1.setGeometry(QRect(0, 0, 926, 556))
        self.scrollAreaWidgetContents_1.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.scrollAreaWidgetContents_1)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(11)
        self.label_2.setFont(font4)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"COLOR: #FFF;")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(25)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_1)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setFamily(u"IRANSans")
        font5.setPointSize(11)
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"COLOR: #FFF;")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(20)

        self.verticalLayout_6.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        font6 = QFont()
        font6.setFamily(u"IRANSans")
        font6.setPointSize(8)
        font6.setBold(False)
        font6.setWeight(50)
        self.btn_page_1.setFont(font6)
        self.btn_page_1.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(0, 115, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        font7 = QFont()
        font7.setFamily(u"IRANSans")
        font7.setPointSize(8)
        self.btn_page_2.setFont(font7)
        self.btn_page_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(0, 115, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setFont(font7)
        self.btn_page_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(0, 115, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("intelligent currency converter", u"intelligent currency converter", None))
        MainWindow.setWindowIcon(QIcon("icons/titleicon.png"))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646\u0648", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Euro", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Iranian Rial", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Great British Pound", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"US Dollar", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Utd. Arab Emir. Dirham", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Norwegian Kroner", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Swedish Krona", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Iraqi Dinar", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Chinese Yuan Renminbi", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Turkish Lira", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Australian Dollar", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Canadian Dollar", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Iranian Rial", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Euro", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Great British Pound", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"US Dollar", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Utd. Arab Emir. Dirham", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Norwegian Kroner", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Swedish Krona", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Iraqi Dinar", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Chinese Yuan Renminbi", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Turkish Lira", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Australian Dollar", None))
        self.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Canadian Dollar", None))

        self.label_date.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e", None))
        self.label.setText("")
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0628\u062f\u06cc\u0644", None))
        textlog=open('log.log').read()
        self.label_2.setText(textlog)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627 \u0646\u0631\u0645 \u0627\u0641\u0632\u0627\u0631 \u062a\u0628\u062f\u06cc\u0644 \u0627\u0631\u0632 \u0647\u0648\u0634\u0645\u0646\u062f \u0634\u0645\u0627 \u0645\u06cc\u062a\u0648\u0627\u0646\u06cc\u062f \u0628\u0647 \u0633\u0627\u062f\u06af\u06cc \u0627\u0631\u0632\u0647\u0627\u06cc \u0645\u0648\u0631\u062f\u0646\u0638\u0631 \u062e\u0648\u062f \u0631\u0627 \u0628\u0647 \u0635\u0648\u0631\u062a \u0622\u0646\u0644\u0627\u06cc\u0646 \u062a\u0628\u062f\u06cc\u0644 \u06a9\u0646\u06cc\u062f. \u0628\u0627 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u0627\u0632 \u0627\u06cc\u0646 \u0628\u0631\u0646\u0627\u0645\u0647 \u0634\u0645\u0627 \u0645\u06cc\u062a\u0648\u0627\u0646\u06cc\u062f \u0644\u0627\u06af \u0647\u0627\u06cc \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0647\u0627\u06cc \u0642\u0628\u0644\u06cc \u062e\u0648\u062f \u0631\u0627 \u0628\u0628\u06cc\u0646\u06cc\u062f.  \u0627\u06cc\u0646 \u0628\u0631\u0646\u0627\u0645\u0647 \u0627\u0632 \u062f\u06cc\u062a\u0627 \u0633\u0627\u06cc\u062a tgju.org \u0627"
                        "\u0633\u062a\u0641\u0627\u062f\u0647 \u0645\u06cc\u06a9\u0646\u062f \u0648 \u0628\u0627 \u0632\u0628\u0627\u0646 \u067e\u0627\u06cc\u062a\u0648\u0646 \u0648 \u0628\u0627 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u0627\u0632 PySide2 \u062a\u0648\u0633\u0637 \u0645\u062d\u0645\u062f\u0631\u0636\u0627 \u0635\u0627\u0628\u0631\u06cc \u0648 \u0627\u0645\u06cc\u0631\u0631\u0636\u0627 \u0627\u0645\u06cc\u0631\u06cc \u0646\u0648\u0634\u062a\u0647 \u0634\u062f\u0647 \u0627\u0633\u062a. \u0628\u0627 \u062a\u0634\u06a9\u0631 \u0627\u0632 \u0627\u0633\u062a\u0627\u062f \u0645\u0647\u0631\u062f\u0627\u062f \u0642\u062f\u0633\u06cc \u0627\u062d\u0633\u0627\u0646 \u0622\u0628\u0627\u062f \u06a9\u0647 \u062f\u0631 \u0633\u0627\u062e\u062a \u0627\u06cc\u0646 \u0628\u0631\u0646\u0627\u0645\u0647 \u0645\u0627 \u0631\u0627 \u06cc\u0627\u0631\u06cc \u06a9\u0631\u062f\u0646\u062f. \u0628\u0631\u0627\u06cc \u0627\u0631\u062a\u0628\u0627\u0637 \u0628\u0627 \u0645\u0627 \u0648 \u0641\u0631\u0633\u062a\u0627\u062f\u0646 \u0646\u0638\u0631"
                        " \u062e\u0648\u062f \u0645\u06cc\u062a\u0648\u0627\u0646\u06cc\u062f \u0627\u0632 \u0627\u06cc\u0645\u06cc\u0644 \u0632\u06cc\u0631 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u06a9\u0646\u06cc\u062f. \u0627\u06cc\u0645\u06cc\u0644: iamirreza13@gmail.com", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0628\u062f\u06cc\u0644 \u0645\u0628\u0646\u0627", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e\u0686\u0647", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0628\u0627\u0631\u0647 \u0645\u0627", None))
    # retranslateUi

