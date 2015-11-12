#! /Users/lewisde/anaconda/bin/python3

import sys
import os
from PySide import QtGui


class Notepad(QtGui.QMainWindow):

    def __init__(self):
        super(Notepad, self).__init__()
        self.init_ui()
        self.filenames = []

    def init_ui(self):

        new_action = QtGui.QAction('New File', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('Create new file')
        new_action.triggered.connect(self.new_file)

        open_action = QtGui.QAction('Open...', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open a file')
        open_action.triggered.connect(self.open_file)

        save_action = QtGui.QAction('Save File', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save current file')
        save_action.triggered.connect(self.save_file)

        new_save_action = QtGui.QAction('Save File As...', self)
        new_save_action.setShortcut('Shift+Ctrl+S')
        new_save_action.setStatusTip('Save current file')
        new_save_action.triggered.connect(self.save_file_as)

        close_action = QtGui.QAction('Close File', self)
        close_action.setShortcut('Ctrl+Q')
        close_action.setStatusTip('Close Notepad')
        close_action.triggered.connect(self.close)

        undo_action = QtGui.QAction('Undo', self)
        undo_action.setShortcut('Ctrl+Z')

        copy_action = QtGui.QAction('Copy', self)
        copy_action.setShortcut('Ctrl+C')

        cut_action = QtGui.QAction('Cut', self)
        cut_action.setShortcut('Ctrl+X')

        paste_action = QtGui.QAction('Paste', self)
        paste_action.setShortcut('Ctrl+V')

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

        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)
        self.setGeometry(300, 300, 1324, 1068)
        self.setWindowTitle('Notepad')
        self.setStyleSheet(
            'font-size: 18pt; font-family: Courier;')

        self.show()

    def new_file(self):
        self.text.clear()

    def save_file(self):
        filename = self.filenames[0]
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()

    def save_file_as(self):
        filename = QtGui.QFileDialog.getSaveFileName(
            self, 'Save File', os.getenv('HOME'))
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()

    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(
            self, 'Open File', os.getenv('HOME'))
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()
        self.filenames.append(filename)
        self.setWindowTitle(filename)


def main():
    app = QtGui.QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
