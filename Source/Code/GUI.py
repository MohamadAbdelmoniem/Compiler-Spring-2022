import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi
from Source.Code import ParserLexer as PL
from Source.Code import Parser as P
from Source.Code import ParsingTable as PT


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("mainwindow.ui", self)
        self.AddCodeButton.clicked.connect(self.addCode)
        '''self.ShowParseTableButton.clicked.connect(self.showParseTableImage)'''

    def addCode(self):
        PL.lexer(self.InputTextBox.currentText())
        P.input_code=self.InputTextBox.currentText()







