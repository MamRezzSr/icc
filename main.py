import sys
import platform
import logging
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QRegExp)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QRegExpValidator)
from PySide2.QtWidgets import *
# back-end
from back_end import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # convert button
        self.ui.btn_convert.clicked.connect(lambda: self.gettinglog())
        
        # ONLY NUMBER
        validator = QRegExpValidator(QRegExp(r'^\d+(\.\d{1,2})?$'))
        self.ui.lineEdit.setValidator(validator)

        # CALENDAR
        x_pos, y_pos = 550, 235
        w_pix, h_pix = 200, 45

        container = QWidget(self.ui.page_1)
        container.setContentsMargins(0, 0, 0, 0)
        container.setFixedSize(w_pix, h_pix)
        container.move(x_pos, y_pos)
        container.setStyleSheet("	background-color: rgb(231, 231, 231);\n"
"	border:1px solid #ced4da;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"	height: 50px;\n"
"}")

        hbox = QHBoxLayout(container)
        hbox.setContentsMargins(0, 0, 0, 0)
        self.dateEdit = QtWidgets.QDateEdit(calendarPopup=True)
        hbox.addWidget(self.dateEdit)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        global tarikh
        tarikh=self.dateEdit.text()
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    def onDateChanged(self, qDate):
        global tarikh
        tarikh=('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))

    def gettinglog(self):
        # logger
        logger=logging.getLogger(__name__)
        file_h = logging.FileHandler('log.log')
        file_f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_h.setFormatter(file_f)
        file_h.setLevel(logging.INFO)
        logger.addHandler(file_h)
        logger.setLevel(logging.INFO)
        arz_voroodi=self.ui.comboBox.currentText()
        arz_khoroogi=self.ui.comboBox_2.currentText()
        meghadr_arz=self.ui.lineEdit.text()
        logger.info('[+] Requesting for input_currency: %s / output_currency: %s / amount: %s / date: %s' %(arz_voroodi, arz_khoroogi, meghadr_arz, tarikh))
        
        # back-end
        try:
            output = changeTo(str(arz_voroodi), str(arz_khoroogi), str(meghadr_arz), str(tarikh))
            out = roundUp(output)
            self.ui.label.setText(out)
        except:
            logger.info("[-] Something went wrong... please try again.")
        # end of back-end

        logger.removeHandler(file_h)
        textlog=open('log.log').read()
        self.ui.label_2.setText(textlog)
        #end of logger
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
