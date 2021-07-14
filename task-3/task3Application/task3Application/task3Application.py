
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import http.client
import json


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task-3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4


# get list of dictionaries of all countries information
def getCountriesList():
    connect = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "84ddb881f1mshe52cf4b1b8fbde2p1665f2jsnc71b246a3a81",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

    connect.request("GET", "/api/npm-covid-data/", headers=headers)

    res = connect.getresponse()
    data = res.read()

    resList = list(json.loads(data.decode("utf-8")))
    del resList[0:2]

    return resList

# get list of dictionaries of countries information that match to input country identifyer
def getCountryStat(CountryIdentifyer):

    CountriesList = getCountriesList()
    resList = []

    for i in CountriesList:
        if str(dict(i).get("Country")).lower().startswith(CountryIdentifyer.lower()):
            resList.append(dict(i))
        if str(dict(i).get("ThreeLetterSymbol")).lower() == CountryIdentifyer.lower():
            resList.append(dict(i))
        if str(dict(i).get("TwoLetterSymbol")).lower() == CountryIdentifyer.lower():
            resList.append(dict(i))

    return resList

# format string to nice look
def niceStringFormat(inputString):

    resString = inputString.split("/")
    for i in range(3 - len(resString[0])):
        resString[0] += (" ")
    for i in range(22 - len(resString[1])):
        resString[1] += (" ")
    for i in range(9 - len(resString[2])):
        resString[2] += (" ")
    for i in range(9 - len(resString[3])):
        resString[3] += (" ")
    for i in range(9 - len(resString[4])):
        resString[4] += (" ")
    return str(' '.join(resString))

# class of UI
class Ui_MainWindow(object):
    # create list of labels that contains countries information
    def createLabels(self, CountriesList):
        resoultLabelList = []

        colorFlag = False
        for i in range(len(CountriesList)):
            resoultLabelList.append(QtWidgets.QLabel(self.scrollAreaWidgetContents))
            resoultLabelList[i].setMinimumHeight(20)
            resoultLabelList[i].setObjectName("CountryLabel" + str(i))
            print()
            resoultLabelList[i].setText(niceStringFormat(str(i + 1) + "/" + dict(CountriesList[i]).get("Country") + "/" + str(dict(CountriesList[i]).get("TotalCases")) + "/" + str(dict(CountriesList[i]).get("Infection_Risk")) + "/" + str(dict(CountriesList[i]).get("TotalDeaths")) + "/" + str(dict(CountriesList[i]).get("TotalRecovered")) ))
            resoultLabelList[i].setFont(QFont('Courier New', 8))
            resoultLabelList[i].setStyleSheet("padding-left: 5px")
            if colorFlag:
                resoultLabelList[i].setStyleSheet("background-color: #dbdbdb; padding-left: 5px")
            colorFlag = not colorFlag
        return resoultLabelList

    # set all UI widgets
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Covid-19 countries status")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(219, 36, 571, 560))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 569, 122))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())

        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")

        self.headLabel = QtWidgets.QLabel(self.centralwidget)
        self.headLabel.setGeometry(QtCore.QRect(220, 10, 600, 20))
        self.headLabel.setObjectName("head label")
        #self.CountriesLabelList.append(QtWidgets.QLabel(self.scrollAreaWidgetContents))
        #self.CountriesLabelList[0].setMinimumSize(QtCore.QSize(0, 20))
        #self.CountriesLabelList[0].setObjectName("label")

        #self.verticalLayout.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(10, 50, 201, 41))
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.SearchPressed)

        self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLine.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.searchLine.setObjectName("searchLine")

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.ResetPressed)

        self.scrollArea.raise_()
        self.searchLine.raise_()
        self.resetButton.raise_()
        self.searchButton.raise_()
        self.headLabel.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # set static texts
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headLabel.setText(_translate("MainWindow", "Rate:  Name:\t\t\t         Cases:\t  infection risk:    Death:         Recovered:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.ResetPressed()
        
    # reset button event 
    def ResetPressed(self):
        #clearing vertical layout:
        for i in reversed(range(self.verticalLayout.count())): 
            self.verticalLayout.itemAt(i).widget().setParent(None)
        
        #set new widgets to layout:
        self.CountriesLabelList = self.createLabels(getCountriesList())
        for i in range(len(self.CountriesLabelList)):
                self.verticalLayout.addWidget(self.CountriesLabelList[i])

        self.searchLine.setText("")

    # search button event 
    def SearchPressed(self):
        #clearing vertical layout:
        for i in reversed(range(self.verticalLayout.count())): 
            self.verticalLayout.itemAt(i).widget().setParent(None)
        
        #set new widgets to layout:
        self.CountriesLabelList = self.createLabels(getCountryStat(self.searchLine.text()))
        for i in range(len(self.CountriesLabelList)):
            self.verticalLayout.addWidget(self.CountriesLabelList[i])

# start program
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())