import sys
import globals
from PyQt4 import QtCore, QtGui
from ui_main import *
import syntax
import json
import os
from muccafx import *
import threading

class MuccaAppyFxGui(threading.Thread):
    script = None
    ass = None
    export_path = None
    
    def __init__(self, script = None, ass = None, export_path = None):
        self.script = script
        self.ass = ass
        self.export_path = export_path

    def run(self):
        try:
            exec str(self.script)
        except Exception,e:
            print "Karaoke Script Error!","Karaoke Script Python error:\n{0}".format(str(e))
            return None
        try:
            effect = KaraokeEffect(ass)
            effect.apply()
            return True
        except:
            print "Unable to apply karaoke effect."
            return None

class MuccaFxGui(QtGui.QMainWindow):
    script_path = None
    ass_path = None
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        syntax.PythonHighlighter(self.ui.script.document())
        self.ui.script.setText("""class KaraokeEffect(MuccaFxEffect):
	def apply(self, ass):
		for line in ass.lines:
			self.dispatchEffect(line)
		pass

	def dispatchEffect(self, line):
		if line['effect'] == 'sample':
			self.sampleEffect(line)
		pass

	def sampleEffect(self, line):
		line['text'] = "{\\fad(250,250)}{0}".format(line['text'])
		pass
""")
        self.ui.actionAssColor.triggered.connect(self.actionAssColor)
        self.ui.actionExit.triggered.connect(self.actionExit)
        self.ui.actionSave.triggered.connect(self.actionSave)
        self.ui.actionSaveAs.triggered.connect(self.actionSaveAs)
        self.ui.actionOpen.triggered.connect(self.actionOpen)
        self.ui.actionSelectASS.triggered.connect(self.actionSelectASS)
        self.ui.actionPreview.triggered.connect(self.actionPreview)
        self.refreshTitle()

    def resetGui(self):
        self.script_path = None
        self.ass_path = None
        self.ui.script.setText('')
        self.refreshTitle()
    
    def refreshTitle(self):
        title = "MuccaFx v.{0}".format(globals.version)
        if self.script_path:
            title = "{0} ({1})".format(title, self.script_path)
        if self.ass_path:
            title = "{0} ({1})".format(title, self.ass_path)
        self.setWindowTitle(title)
    
    def saveScript(self, file_to_save):
        try:
            data = {}
            data['version'] = globals.version
            data['script'] = str(self.ui.script.toPlainText())
            if self.ass_path:
                data['ass_path'] = self.ass_path
            json.dump(data, open(file_to_save, 'w+'))
            return True
        except:
            QtGui.QMessageBox.warning(None,"Warning!","Unable to save the file.")
            return None

    def openScript(self, file_to_load):
        try:
            data = json.load(open(file_to_load,'rb+'))
            self.script_path = file_to_load
            if 'version' in data:
                if data['version'] < globals.version:
                    QtGui.QMessageBox.warning(None,"Warning!","The file you are trying to load was saved with version {0}!\nSome data could be missed or non-well loaded.".format(data['version']))
            try:
                self.resetGui()
                if 'script' in data:
                    self.ui.script.setText(data['script'])
                if 'ass_path' in data:
                    if os.path.isfile(data['ass_path']):
                        self.ass_path = data['ass_path']
                    else:
                        if QtGui.QMessageBox.question(None,"Warning!","Unable to find ASS script \"{0}\". Select it now?".format(data['ass_path']),QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)== QtGui.QMessageBox.Yes:
                            self.actionSelectASS()
                return True
            except:
                QtGui.QMessageBox.warning(None,"Warning!","Failed to load the given file. Too old.")
                return None
        except:
            QtGui.QMessageBox.warning(None,"Warning!","Unable to load the requested file.")
            return None
    
    def exportScript(self, file_to_export):
        if not self.ass_path:
            QtGui.QMessageBox.warning(None,"Warning!","You must select an ASS script with timed lines to export your Karaoke.")
            if not self.actionSelectASS():
                return None
        if not self.script_path:
            QtGui.QMessageBox.warning(None,"Warning!","You must save your script to have a preview.")
            if not self.actionSave():
                return None
        try:
            exec str(self.ui.script.toPlainText())
        except Exception,e:
            QtGui.QMessageBox.warning(None,"Karaoke Script Error!","Karaoke Script Python error:\n{0}".format(str(e)))
            return None

    def actionPreview(self):
        self.exportScript("preview.ass")
    
    def actionSave(self):
        if self.script_path == None:
            return self.actionSaveAs()
        else:
            return self.saveScript(self.script_path)
        

    def actionSaveAs(self):
        path = QtGui.QFileDialog.getSaveFileName(self, "Save Script", "", "MuccaFx Script (*.mfx)")
        if path:
            if self.saveScript(path):
                self.script_path = str(path)
                self.refreshTitle()
                return True
        return None
        
    def actionOpen(self):
        path = QtGui.QFileDialog.getOpenFileName(self, "Open Script", "", "MuccaFx Script (*.mfx)")
        if path:
            if self.openScript(path):
                self.script_path = str(path)
                self.refreshTitle()
                return True
        return None

    def actionSelectASS(self):
        path = QtGui.QFileDialog.getOpenFileName(self, "Open ASS Script", "", "Aegisub Subtitle Script (*.ass *.ssa)")
        if os.path.isfile(path):
            self.ass_path = str(path)
            self.refreshTitle()
            return True
        return None
        
    def actionAssColor(self):
        # QtGui.QColorDialog.setOption(QtGui.QColorDialog.ShowAlphaChannel,True) not working?
        color = QtGui.QColorDialog.getColor()
        if color.isValid():
            cursor = self.ui.script.textCursor()
            cursor.insertText(str("&H%02x%02x%02x&" % (color.blue(), color.green(), color.red())).upper())
        pass

    def actionExit(self):
        sys.exit(QtGui.qApp.quit)


if __name__ == "__main__":
    globals.app = QtGui.QApplication(sys.argv)
    globals.gui = MuccaFxGui()
    globals.gui.show()
    sys.exit(globals.app.exec_())
