#!/usr/local/bin/python3

import os
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.filenames = []

    def init_ui(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        new_action = QAction('New File', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('Create new file')
        new_action.triggered.connect(self.new_file)

        open_action = QAction('Open...', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open a file')
        open_action.triggered.connect(self.open_file)

        save_action = QAction('Save File', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save current file')
        save_action.triggered.connect(self.save_file)

        new_save_action = QAction('Save File As...', self)
        new_save_action.setShortcut('Shift+Ctrl+S')
        new_save_action.setStatusTip('Save current file')
        new_save_action.triggered.connect(self.save_file_as)

        close_action = QAction('Close File', self)
        close_action.setShortcut('Ctrl+Q')
        close_action.setStatusTip('Close Notepad')
        close_action.triggered.connect(self.close)

        undo_action = QAction('Undo', self)
        undo_action.setShortcut('Ctrl+Z')

        copy_action = QAction('Copy', self)
        copy_action.setShortcut('Ctrl+C')

        cut_action = QAction('Cut', self)
        cut_action.setShortcut('Ctrl+X')

        paste_action = QAction('Paste', self)
        paste_action.setShortcut('Ctrl+V')

        minimize_action = QAction('Minimize', self)
        minimize_action.setShortcut('Ctrl+M')

        view_action = QAction('Show', self)
        view_action.setShortcut('Ctrl+/')

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        edit_menu = menubar.addMenu('&Edit')
        view_menu = menubar.addMenu('&View')
        window_menu = menubar.addMenu('&Window')

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(new_save_action)
        file_menu.addAction(close_action)

        edit_menu.addAction(undo_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(cut_action)
        edit_menu.addAction(paste_action)

        view_menu.addAction(view_action)

        window_menu.addAction(minimize_action)

        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)
        self.setGeometry(300, 300, 1324, 1068)
        self.setWindowTitle('Notepad')
        self.setStyleSheet('font-size: 14pt; font-family: Courier;')

        self.show()

    def new_file(self):
        self.text.clear()

    def save_file(self):
        if len(self.filenames) > 0:
            filename = self.filenames[0]
            f = open(filename, 'w')
            filedata = self.text.toPlainText()
            f.write(filedata)
            f.close()
        else:
            self.save_file_as()

    def save_file_as(self):
        filename = QFileDialog.getSaveFileName(
            self, 'Save File', os.getenv('HOME'))[0]
        print(filename)
        if filename != ('', ''):
            f = open(filename, 'w')
            filedata = self.text.toPlainText()
            f.write(filedata)
            f.close()

    def open_file(self):
        filename = QFileDialog.getOpenFileName(
            self, 'Open File', os.getenv('HOME'))[0]
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()
        self.setWindowTitle(filename)
        self.filenames.append(filename)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
