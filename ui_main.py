# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Nov 06 13:04:31 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(975, 691)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setWindowTitle(QtGui.QApplication.translate("main", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 955, 579))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.script = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(10)
        self.script.setFont(font)
        self.script.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.script.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.script.setHtml(QtGui.QApplication.translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.script.setTabStopWidth(25)
        self.script.setAcceptRichText(False)
        self.script.setObjectName(_fromUtf8("script"))
        self.gridLayout_2.addWidget(self.script, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("main", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuKaraoke = QtGui.QMenu(self.menubar)
        self.menuKaraoke.setTitle(QtGui.QApplication.translate("main", "Karaoke", None, QtGui.QApplication.UnicodeUTF8))
        self.menuKaraoke.setObjectName(_fromUtf8("menuKaraoke"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setTitle(QtGui.QApplication.translate("main", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setTitle(QtGui.QApplication.translate("main", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(main)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("main", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(main)
        self.toolBar_2.setWindowTitle(QtGui.QApplication.translate("main", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar(main)
        self.toolBar_3.setWindowTitle(QtGui.QApplication.translate("main", "toolBar_3", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.actionSave = QtGui.QAction(main)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setText(QtGui.QApplication.translate("main", "Save", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionSave.setFont(font)
        self.actionSave.setShortcut(QtGui.QApplication.translate("main", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(main)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setText(QtGui.QApplication.translate("main", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("main", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(main)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/exclamation.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setText(QtGui.QApplication.translate("main", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPreview = QtGui.QAction(main)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/television.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreview.setIcon(icon3)
        self.actionPreview.setText(QtGui.QApplication.translate("main", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setToolTip(QtGui.QApplication.translate("main", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setShortcut(QtGui.QApplication.translate("main", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setObjectName(_fromUtf8("actionPreview"))
        self.actionSelectASS = QtGui.QAction(main)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/aegisub.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectASS.setIcon(icon4)
        self.actionSelectASS.setText(QtGui.QApplication.translate("main", "SelectASS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectASS.setObjectName(_fromUtf8("actionSelectASS"))
        self.actionExport = QtGui.QAction(main)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/script_go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon5)
        self.actionExport.setText(QtGui.QApplication.translate("main", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionAssColor = QtGui.QAction(main)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/color_wheel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAssColor.setIcon(icon6)
        self.actionAssColor.setText(QtGui.QApplication.translate("main", "AssColor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAssColor.setObjectName(_fromUtf8("actionAssColor"))
        self.actionSaveAs = QtGui.QAction(main)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/icons/disk_multiple.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon7)
        self.actionSaveAs.setText(QtGui.QApplication.translate("main", "SaveAs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("main", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuKaraoke.addAction(self.actionSelectASS)
        self.menuKaraoke.addAction(self.actionPreview)
        self.menuKaraoke.addAction(self.actionExport)
        self.menuTools.addAction(self.actionAssColor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuKaraoke.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar_2.addAction(self.actionSelectASS)
        self.toolBar_2.addAction(self.actionPreview)
        self.toolBar_2.addAction(self.actionExport)
        self.toolBar_3.addAction(self.actionAssColor)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        pass

import icons_rc
