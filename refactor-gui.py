''' ps_QMainWindow2.py
The PySide QMainWindow has layouts for menubar, toolbar, statusbar,
dock and central widgets.  You can add a QWidget instance as central 
widget for the box and grid layouts.

download PySide (LGPL-licensed version of PyQT) from:
http://qt-project.org/wiki/PySide

tested with Python27 and Python33  by  vegaseat  15jan2013
'''

from PySide.QtCore import *
from PySide.QtGui import *

from PySide import QtGui, QtWebKit, QtCore

import datetime
import sendmail

class MyDateTimeEdit(QtGui.QDateEdit):
    def __init__(self):
        super(MyDateTimeEdit, self).__init__()
        self.times = ['','9:00 AM', '9:15 AM', '9:30 AM', '9:45 AM',
        '10:00 AM', '10:15 AM', '10:30 AM', '10:45 AM',
        '11:00 AM', '11:15 AM', '11:30 AM', '11:45 AM',
        '12:00 PM', '12:15 PM', '12:30 PM', '12:45 PM',
        '1:00 PM', '1:15 PM', '1:30 PM', '1:45 PM',
        '2:00 PM', '2:15 PM', '2:30 PM', '2:45 PM',
        '3:00 PM', '3:15 PM', '3:30 PM', '3:45 PM',
        '4:00 PM', '4:15 PM', '4:30 PM', '4:45 PM',
        '5:00 PM', '5:15 PM', '5:30 PM', '5:45 PM',
        '6:00 PM', '6:15 PM', '6:30 PM', '6:45 PM',
        '7:00 PM', '7:15 PM', '7:30 PM', '7:45 PM',
        '8:00 PM', '8:15 PM', '8:30 PM', '8:45 PM',
        '9:00 PM', '9:15 PM', '9:30 PM', '9:45 PM']

        self.my_time = QtGui.QComboBox()
        self.my_time.addItems(self.times)
        self.my_time.model().item(0).setEnabled(False)

        self.start_date = datetime.date.today()
        self.end_date = self.start_date.replace(year=2017)
        self.setCalendarPopup(True)
        self.setDateRange(self.start_date, self.end_date)

class InputForm(QtGui.QDialog):
   
    def __init__(self):
        super(InputForm, self).__init__()

        self.information = []
        self.date_container = []

        self.createParentInfo()
        self.createStudentInfo()
        self.createDateTimes()

        self.createAdditionalInfo()

        btn = QtGui.QPushButton("Launch HTML")
        btn.clicked.connect(self.show_html_page)


        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
       
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.studentInfo)
        mainLayout.addWidget(self.availability)
        mainLayout.addWidget(self.add_info)
        mainLayout.addWidget(btn)
    
        mainLayout.addWidget(buttonBox)

  
        self.setLayout(mainLayout)

        self.setWindowTitle("Recital App")
        self.show()

        

    def createDateTimes(self):
        self.availability = QtGui.QGroupBox("Availability")
        layout = QtGui.QGridLayout()  

        self.container = []  

        for n in range(5):
            self.container.append(MyDateTimeEdit())

        for magic, n in zip(self.container, range(5)):
            layout.addWidget(magic, n, 0)
            layout.addWidget(magic.my_time, n, 1)

        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 2)
        self.availability.setLayout(layout)

    def accept(self):
       
        # password Bool
        password, flag = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter your password:')
        if flag:
            print "sending email"
            with open('email_for_piano_prospective.html', 'r') as f:
            	my_message = f.read()
                
            to_send_to = self.email_name.text()
            sbj_student_name = self.student_name.text()
            sendmail.send_email(my_message, to_send_to, sbj_student_name, password)


    
    def show_html_page(self):
        self.information.append(self.suffix.currentText())   
        self.information.append(self.first_name.text())      
        self.information.append(self.last_name.text())      
        self.information.append(self.email_name.text())
        self.information.append(self.instrument.currentText())
        self.information.append(self.student_name.text())       
        self.information.append(self.age.value())  
        self.information.append(self.infobox.toPlainText())  

        '''Get dates for only the fields that have times completed'''
        for dt in self.container:
            if dt.my_time.currentText() != '':
                self.date_container.append((dt.text(),dt.my_time.currentText()))
            

        for info in self.information:
            print info

        from createhtml import create_html_for_derek
        create_html_for_derek(self.information, self.date_container)
        

        self.m = InternetPopUp(self.information, self.date_container)
        self.m.show()

        self.information = []
        self.date_container = []

    def createStudentInfo(self):
        self.studentInfo = QtGui.QGroupBox("Student Info")
        layout = QtGui.QGridLayout()

        self.student_name = QtGui.QLineEdit('StudentFirst')
        label = QtGui.QLabel("First")
        layout.addWidget(label,0,0)
        layout.addWidget(self.student_name,0,1)

        self.age = QtGui.QSpinBox()
        label = QtGui.QLabel("Age")
        layout.addWidget(label,0,3)
        layout.addWidget(self.age,0,3)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 2)
        self.studentInfo.setLayout(layout)

    def createAdditionalInfo(self):
        self.add_info = QtGui.QGroupBox("Additional Info")
        layout = QtGui.QGridLayout()

        self.infobox = QtGui.QTextEdit()
  
        layout.addWidget(self.infobox,0,0)


        # layout.setColumnStretch(1, 10)
        # layout.setColumnStretch(1, 2)
        self.add_info.setLayout(layout)

           

    def createParentInfo(self):
        self.gridGroupBox = QtGui.QGroupBox("Parent Info")
        layout = QtGui.QGridLayout()

        suffixes = ['','Ms.', 'Mr.', 'Mrs.']
        
        self.suffix = QtGui.QComboBox()
        self.suffix.addItems(suffixes)
        self.suffix.model().item(0).setEnabled(False)
        
        instruments = ['','None', 'Has Piano', 'Has Keyboard']
        
        self.instrument = QtGui.QComboBox()
        self.instrument.addItems(instruments)
        self.instrument.model().item(0).setEnabled(False)
        

        layout.addWidget(self.instrument,1,2)

        layout.addWidget(self.suffix,0,2)

        self.first_name = QtGui.QLineEdit('ParentFirst')
        label = QtGui.QLabel("First")
        layout.addWidget(label,0,0)
        layout.addWidget(self.first_name,0,1)

        self.last_name = QtGui.QLineEdit('ParentLast')
        label = QtGui.QLabel("Last")
        layout.addWidget(label,1,0)
        layout.addWidget(self.last_name,1,1)

        self.email_name = QtGui.QLineEdit('email@gmail.com')
        label = QtGui.QLabel("Email")
        layout.addWidget(label,2,0)
        layout.addWidget(self.email_name,2,1)


  
        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 2)
        self.gridGroupBox.setLayout(layout)



class InternetPopUp(QtGui.QWidget):
    def __init__(self, form_info, date_info):
        super(InternetPopUp, self).__init__()


        # Setup the size and title of the main window
        self.setWindowTitle('Preview')

        # Create the web widget and set it as the central widget.
        self.web = QtWebKit.QWebView(self)
        self.web.resize(1000,1000)
        self.web.load(QtCore.QUrl('email_for_piano_prospective.html'))

        # print "------"
        # for info in form_info:
        #     print info
        # for info in date_info:
        #     print info[0], info[1]
        
 

class InputDateTime(QtGui.QWidget):
    def __init__(self):
        super(InputDateTime, self).__init__()

        self.show()
    



class MyWindow(QMainWindow):
    '''
    QMainWinodw does not allow box/grid layout, but you can
    make a QWidget instance the central widget to do so
    '''
    def __init__(self):
        # if you want a menubar or statusbar, you have to use
        # QMainWindow since QWidget does not have those
        QMainWindow.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        # upper left corner coordinates (x_pos, y_pos)
        self.setGeometry(300, 100, 270, 100)
        self.resize(500,1000)
        self.setWindowTitle('Exploring QMainWindow')

        # exit option for the menu bar File menu
        self.exit = QAction('Exit', self)
        # message for the status bar if mouse is over Exit
        self.exit.setStatusTip('Exit program')
        # newer connect style (PySide/PyQT 4.5 and higher)
        self.exit.triggered.connect(app.quit)

        # create the menu bar
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        # now add self.exit
        file.addAction(self.exit)

        # Creating login select
        login = menubar.addMenu('&Login')

        # create the status bar
        self.statusBar()

        # QWidget or its instance needed for box layout

        # Work around to make central widget a layout to put widgets in with .addWidget
        self.setCentralWidget(QtGui.QWidget(self))
        self.hbox = QtGui.QVBoxLayout()
        self.centralWidget().setLayout(self.hbox)


        self.hbox.addWidget(InputForm())
        # self.hbox.addWidget(Calendar())

if __name__ == '__main__':

    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()


