import sys
import nltk
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
import ParserTest as parser
import lexer as lexer


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("mainwindow.ui", self)
        self.AddCodeButton.clicked.connect(self.addCode)
        self.DFAButton.clicked.connect(self.draw_dfa)
        self.ParserButton.clicked.connect(self.draw_parseTree)
        self.ShowParseTableButton.clicked.connect(self.showParseTableImageScreen)

    def addCode(self):
        lexer.l.set_input(self.InputTextBox.toPlainText())
        parser.p.set_input(self.InputTextBox.toPlainText())


    def draw_dfa(self):
        lexer.l.lexer()
        lexer.l.draw_dfa()

    def draw_parseTree(self):
        parser.p.lexer()
        parser.p.parse()

        if parser.p.accepted:
            treeS = nltk.Tree.fromstring(parser.p.s)
            parser.draw_trees(treeS)
        else:
            treeS=nltk.Tree.fromstring("( String not accepted )")
            parser.draw_trees(treeS)

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
