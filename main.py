# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rapid\PycharmProjects\mortCalinterfaceMark2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1344, 909)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(500, 140, 221, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.calculateButton.setFont(font)
        self.calculateButton.setObjectName("calculateButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(410, 0, 451, 141))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.meleruseInput = QtWidgets.QLineEdit(self.centralwidget)
        self.meleruseInput.setGeometry(QtCore.QRect(100, 780, 113, 22))
        self.meleruseInput.setObjectName("meleruseInput")
        self.paybackInput = QtWidgets.QLineEdit(self.centralwidget)
        self.paybackInput.setGeometry(QtCore.QRect(100, 420, 113, 22))
        self.paybackInput.setObjectName("paybackInput")
        self.loanInput = QtWidgets.QLineEdit(self.centralwidget)
        self.loanInput.setGeometry(QtCore.QRect(100, 80, 113, 22))
        self.loanInput.setObjectName("loanInput")
        self.interestInput = QtWidgets.QLineEdit(self.centralwidget)
        self.interestInput.setGeometry(QtCore.QRect(100, 250, 113, 22))
        self.interestInput.setObjectName("interestInput")
        self.downpaymentInput = QtWidgets.QLineEdit(self.centralwidget)
        self.downpaymentInput.setGeometry(QtCore.QRect(100, 600, 113, 22))
        self.downpaymentInput.setObjectName("downpaymentInput")
        self.loanLabel = QtWidgets.QLabel(self.centralwidget)
        self.loanLabel.setGeometry(QtCore.QRect(50, 30, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loanLabel.setFont(font)
        self.loanLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loanLabel.setObjectName("loanLabel")
        self.interestLabel = QtWidgets.QLabel(self.centralwidget)
        self.interestLabel.setGeometry(QtCore.QRect(10, 180, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.interestLabel.setFont(font)
        self.interestLabel.setObjectName("interestLabel")
        self.paybackLabel = QtWidgets.QLabel(self.centralwidget)
        self.paybackLabel.setGeometry(QtCore.QRect(10, 370, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paybackLabel.setFont(font)
        self.paybackLabel.setObjectName("paybackLabel")
        self.downpaymentLabel = QtWidgets.QLabel(self.centralwidget)
        self.downpaymentLabel.setGeometry(QtCore.QRect(0, 540, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.downpaymentLabel.setFont(font)
        self.downpaymentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.downpaymentLabel.setObjectName("downpaymentLabel")
        self.meleruseLabel = QtWidgets.QLabel(self.centralwidget)
        self.meleruseLabel.setGeometry(QtCore.QRect(0, 720, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.meleruseLabel.setFont(font)
        self.meleruseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.meleruseLabel.setObjectName("meleruseLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 340, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(530, 410, 481, 221))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.outputLabel.setFont(font)
        self.outputLabel.setText("")
        self.outputLabel.setObjectName("outputLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1344, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.calculateButton.clicked.connect(self.output)

        self.paybackInput.editingFinished.connect(self.paybackCheck)
        self.loanInput.editingFinished.connect(self.loanCheck)
        self.interestInput.editingFinished.connect(self.interestCheck)
        self.downpaymentInput.editingFinished.connect(self.downpaymentCheck)
        self.meleruseInput.editingFinished.connect(self.meleruseCheck)

        #self.paybackInput.focusChanged.connect(self.paybackCheck())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def interestCheck(self):
        interestInput = self.interestInput.text()
        try:
            intInterestInput = int(interestInput)
            if intInterestInput <= 0 or intInterestInput >= 1:
                self.outputLabel.setText("Please input a value inbetween \n 0-1 in the interest tab")
            else:
                self.outputLabel.setText("")
        except:
            self.outputLabel.setText("Please input a number in the \n interest tab")


    def loanCheck(self):
        loanInput = self.loanInput.text()
        try:
            intLoanInput = int(loanInput)
            if intLoanInput <= 0 or intLoanInput >= 1000000000:
                self.outputLabel.setText("Please input a value inbetween \n 0-1000000000 in the loan tab")
            else:
                self.outputLabel.setText("")
        except:
            self.outputLabel.setText("Please input a number in the \n loan tab")

    def paybackCheck(self):
        paybackInput = self.paybackInput.text()
        try:
            intPaybackInput = int(paybackInput)
            if intPaybackInput <= 0 or intPaybackInput >= 100:
                self.outputLabel.setText("Please input a value inbetween \n 0-100 in the payback period tab")
            else:
                self.outputLabel.setText("")

        except:
            self.outputLabel.setText("Please input a number in the \n interest tab")



    def downpaymentCheck(self):
        downpaymentInput = self.downpaymentInput.text()
        try:
            intdownpaymentInput = int(downpaymentInput)
            if intdownpaymentInput < 0 or intdownpaymentInput >= 100:
                self.outputLabel.setText("Please input a value inbetween \n 0-100 in the downpayment period tab")
            else:
                self.outputLabel.setText("")
        except:
            self.outputLabel.setText("Please input a number in the \n downpayment tab")

    def meleruseCheck(self):
        meleruseInput = self.meleruseInput.text()
        try:
            intmeleruseInput = int(meleruseInput)
            if intmeleruseInput < 0 or intmeleruseInput >= 1000000:
                self.outputLabel.setText("Please input a value inbetween \n 0-100000 in the downpayment period tab")
            else:
                self.outputLabel.setText("")
        except:
            self.outputLabel.setText("Please input a number in the \n downpayment tab")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.title.setText(_translate("MainWindow", "Mortgage Calculator"))
        self.loanLabel.setText(_translate("MainWindow", "Input loan amount here:"))
        self.interestLabel.setText(_translate("MainWindow", "Input annual interest rate here (as a decimal):"))
        self.paybackLabel.setText(_translate("MainWindow", "Input payback period here (in years):"))
        self.downpaymentLabel.setText(_translate("MainWindow", "Input downpayment amount (as a whole number):"))
        self.meleruseLabel.setText(_translate("MainWindow", "Input monthly meleruse here (0 if none):"))
        self.label.setText(_translate("MainWindow", "Your monthly mortgage is:"))

    def output(self):
        result, value = self.calculate()
        if not result:
            self.outputLabel.setText("One of the values you put wasn't a number or was negative.")
        else:
            self.outputLabel.setText(str(value))

    def calculate(self):

        loanAmount = self.loanInput.text()
        downPayment = self.downpaymentInput.text()
        interest = self.interestInput.text()
        paybackPeriod = self.paybackInput.text()
        meleruse = self.meleruseInput.text()

        try:
            loanAmount = int(loanAmount)
            downPayment = int(downPayment)
            interest = float(interest)
            paybackPeriod = int(paybackPeriod)
            meleruse = int(meleruse)
            if loanAmount >= 0 and downPayment >= 0 and interest >= 0 and paybackPeriod >= 0 and meleruse >= 0:
                actualLoan = loanAmount - (loanAmount * (downPayment / 100))
            else:
                return False, 0
        except:
            return False, 0

        # M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1].

        firstHalf = pow((interest + 1), paybackPeriod) * interest
        secondHalf = pow((interest + 1), paybackPeriod) - 1
        mortgageCalculation = ((((actualLoan * firstHalf) / secondHalf) / 12) + meleruse) * 0.9912

        if mortgageCalculation + 0.5 >= int(mortgageCalculation) + 1:
            mortgageCalculation = int(mortgageCalculation) + 1

        else:
            mortgageCalculation = int(mortgageCalculation)

        return True, mortgageCalculation

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

