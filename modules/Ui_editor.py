# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\HTML Editor\UI\editor_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget
import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QColor, QSyntaxHighlighter, QTextCharFormat, QIcon


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)  # type: ignore
        self._mapping = {}

    def add_mapping(self, pattern, pattern_format):
        self._mapping[pattern] = pattern_format

    def highlightBlock(self, text_block):
        for pattern, fmt in self._mapping.items():
            for match in re.finditer(pattern, text_block):
                start, end = match.span()
                self.setFormat(start, end-start, fmt)


class HTMLEditor(QPlainTextEdit):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.highlighter = Highlighter()

        self.setUpEditor()

    def setUpEditor(self):
        # pattern #1: ATTRIBUTE format
        class_format = QTextCharFormat()
        class_format.setForeground(QtGui.QColor('#0c98f5'))
        class_format.setFontWeight(QFont.Bold)
        pattern = r"(\w+|\w+-\w+)\s*(=)\s*((\"([^']*)\")|(\'([^']*)\')|((\w+(0-9)*)))"
        self.highlighter.add_mapping(pattern, class_format)

        # pattern #2: TAG format
        function_format = QTextCharFormat()
        function_format.setForeground(QtGui.QColor('#f7be00'))
        function_format.setFontWeight(QFont.Bold)
        pattern = r'(<(\w+))|(>)|(</(\w+)>)'
        self.highlighter.add_mapping(pattern, function_format)

        # pattern 3: COMMENT format
        comment_format = QTextCharFormat()
        comment_format.setForeground(QtGui.QColor('#7a7a7a'))
        comment_format.setFontItalic(True)
        pattern = r'<!--(.*?)-->'  # just the text
        self.highlighter.add_mapping(pattern, comment_format)

        # pattern 3: QUOTES format
        quotation_format = QTextCharFormat()
        quotation_format.setForeground(QtGui.QColor('#d9834d'))
        quotation_format.setFontItalic(False)
        quotation_format.setFontWeight(QFont.Bold)
        pattern = r'\"(.*?)\"'  # just the text
        self.highlighter.add_mapping(pattern, quotation_format)
        
        # pattern 3: DOCUMENT format
        quotation_format = QTextCharFormat()
        quotation_format.setForeground(QtGui.QColor('#9002d1'))
        quotation_format.setFontItalic(True)
        quotation_format.setFontWeight(QFont.Bold)
        pattern = r'<!DOCTYPE html>'  # just the text
        self.highlighter.add_mapping(pattern, quotation_format)
        
        # pattern 3: TAG-PARANTHESES format
        quotation_format = QTextCharFormat()
        quotation_format.setForeground(QtGui.QColor('#fce69a'))
        quotation_format.setFontItalic(False)
        quotation_format.setFontWeight(QFont.Bold)
        pattern = r'<|>'  # just the text
        self.highlighter.add_mapping(pattern, quotation_format)
        
        
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.setFont(font)

        self.highlighter.setDocument(self.document())




class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(619, 459)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)  # type: ignore
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.textEdit = HTMLEditor(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.webView = QWebEngineView(self.splitter)
        self.webView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.webView.setObjectName("frame")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter.setSizes([310,310])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
