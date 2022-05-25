import sys
import nltk
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from Source.Code import ParserTest as parser
from Source.Code import lexer as lexer


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("mainwindow.ui", self)
        self.AddCodeButton.clicked.connect(self.addCode)
        self.DFAButton.clicked.connect(self.draw_dfa)
        self.ParserButton.clicked.connect(self.draw_parseTree)
        self.ShowParseTableButton.clicked.connect(self.showParseTableImageScreen)

    def addCode(self):
        parser.p.reset_parser()
        parser.p.set_input(self.InputTextBox.toPlainText())
        print(parser.p.input)
        lexer.l.set_input(self.InputTextBox.toPlainText())

    def draw_dfa(self):
        lexer.l.lexer()
        lexer.l.draw_dfa()

    def draw_parseTree(self):
        parser.p.set_input(self.InputTextBox.toPlainText())
        parser.p.lexer()
        print(f"here {parser.p.language} ")
        parser.p.parse()
        treeS = nltk.Tree.fromstring(parser.p.s)
        if parser.p.accepted==True:
            print("here")
            parser.draw_trees(treeS)
        print("here")

    def showParseTableImageScreen(self):
        Screen2 = ParseTableScreen()
        widget.addWidget(Screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ParseTableScreen(QDialog):
    def __int__(self):
        super(ParseTableScreen, self).__init__()
        loadUi("ParseTableWindow.ui", self)
        self.backButton.clicked.connect(self.GoToScreen1)

    def GoToScreen1(self):
        screen1 = WelcomeScreen()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# main

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = WelcomeScreen()
mainwindow.setFixedSize(800, 600)
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())
