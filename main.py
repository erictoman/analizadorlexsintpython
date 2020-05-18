from lexer import Lexer
from yacc import Yacc

tokens = (
            'NUMERO',
            'MAS',
            'MENOS',
            'MULTIPLICADOR',
            'DIVISOR',
            'CORCHIZQ',
            'CORCHDER',
            'FUNCION',
            'COMMA',
            'IDRANGO',
            'IDVALOR',
            'IGUAL',
        )

lexer = Lexer(tokens)
yacc = Yacc(tokens,lexer)


from PyQt5 import QtWidgets, uic,QtGui
from PyQt5.QtWidgets import QFileDialog
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.lexbutton = self.findChild(QtWidgets.QPushButton, 'lexbutton')
        self.sinbutton = self.findChild(QtWidgets.QPushButton, 'sinbutton')
        self.filebutton = self.findChild(QtWidgets.QPushButton, 'filebutton')
        self.plainTextEdit = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit')
        self.plainTextEdit2 = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit_2')
        self.lexbutton.clicked.connect(self.printButtonPressed)
        self.sinbutton.clicked.connect(self.setgraph)
        self.filebutton.clicked.connect(self.getFile)
        self.show()
    def printButtonPressed(self):
        self.plainTextEdit2.insertPlainText(lexer.analizar(self.plainTextEdit.toPlainText()))
    def setgraph(self):
        try:
            data=self.plainTextEdit.toPlainText()
            data=data.split("\n")
            for line in data:
                yacc.Parse(line)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Errores en el analisis sintactico')
            pass
    def getFile(self):
        self.plainTextEdit.clear()
        self.plainTextEdit2.clear()
        try:
            path = QFileDialog.getOpenFileName()[0]
            with open(path,"r") as f:
                self.plainTextEdit.insertPlainText(f.read())
        except:
            pass
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()