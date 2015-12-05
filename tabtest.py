#!/usr/local/bin/python3

import os
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self, filename):
        super().__init__()

        self.setGeometry(20, 20, 1324, 1068)
        self.setWindowTitle('qt-Notepad')
        self.setStyleSheet('font-size: 14pt; font-family: Courier;')

        self.show()
        self.init_ui()
        centralWidget = QWidget()
        self.tabs = QTabWidget(centralWidget)
        self.setCentralWidget(self.tabs)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.closeTab)
        if filename:
            f = open(filename, 'r')
            filedata = f.read()
            f.close()
            newfile = QTextEdit()
            newfile.setText(filedata)
            i = self.tabs.addTab(newfile, filename)
            self.tabs.setCurrentIndex(i)
        else:
            self.open_file()

    def init_ui(self):

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
        close_action.setShortcut('Ctrl+W')
        close_action.setStatusTip('Close file and exit tab')
        close_action.triggered.connect(self.close_file)

        exit_action = QAction('Exit qt-Notepad', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Close Notepad')
        exit_action.triggered.connect(self.close)

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
        file_menu.addAction(exit_action)

        edit_menu.addAction(undo_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(cut_action)
        edit_menu.addAction(paste_action)

        view_menu.addAction(view_action)

        window_menu.addAction(minimize_action)

    def closeTab(self, currentIndex):
        currentQWidget = self.tabs.currentWidget()
        currentQWidget.deleteLater()
        self.tabs.removeTab(currentIndex)

    def new_file(self):
        newfile = QTextEdit()
        i = self.tabs.addTab(newfile, 'New Document')
        self.tabs.setCurrentIndex(i)

    def save_file(self):
        editor = self.tabs.currentWidget()
        filename = self.tabs.tabText(self.tabs.currentIndex())
        if filename != 'New Document':
            f = open(filename, 'w')
            filedata = editor.toPlainText()
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
        f.close()
        newfile = QTextEdit()
        newfile.setText(filedata)
        i = self.tabs.addTab(newfile, filename)
        self.tabs.setCurrentIndex(i)

    def close_file(self):
        self.save_file()
        currentIndex = self.tabs.currentIndex()
        self.tabs.removeTab(currentIndex)


def main(argv):
    app = QApplication(argv)
    title = ''
    if len(argv) > 1:
        title = sys.argv[1]

    window = MainWindow(title)

    window.show()

    return app.exec()


if __name__ == "__main__":
    main(sys.argv)
