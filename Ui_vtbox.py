# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_vtbox.ui'
#
# Created: Sat Sep 11 02:43:52 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_vtbox(object):
    def setupUi(self, vtbox,directory):
        vtbox.setObjectName("vTerrain box")
        vtbox.resize(550, 120)
        self.buttonBox = QtGui.QDialogButtonBox(vtbox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        #self.buttonBox.setObjectName("buttonBox")
        
        self.location = QtGui.QFileDialog(vtbox)
        self.location.setGeometry(QtCore.QRect(10, 40, 171, 37))
        self.location.setObjectName("directory")
        
        self.label = QtGui.QLabel(vtbox)
        self.label.setGeometry(QtCore.QRect(5, 30, 160, 28))
        self.label.setObjectName("directory:")
        
        self.directorydefault = QtGui.QLineEdit(vtbox)
        self.directorydefault.setGeometry(QtCore.QRect(190, 30, 333, 27))
        self.directorydefault.setObjectName("directory")
        
        
        self.info_cancel = QtGui.QLabel(vtbox)
        self.info_cancel.setGeometry(QtCore.QRect(5, 70, 491, 28))
        self.info_cancel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";color:red;")
        self.info_cancel .setObjectName("info_cancel")
        
        self.info_ok = QtGui.QLabel(vtbox)
        self.info_ok.setGeometry(QtCore.QRect(1, 90, 391, 28))
        self.info_ok.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color:red;")
        self.info_ok .setObjectName("info_ok")
        
       
        

        self.retranslateUi(vtbox)
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), vtbox.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), vtbox.reject)
        QtCore.QMetaObject.connectSlotsByName(vtbox)

    def retranslateUi(self, vtbox):
        vtbox.setWindowTitle(QtGui.QApplication.translate("vtbox", "VTerrain Dialogs", None, QtGui.QApplication.UnicodeUTF8))
        #self.location.setLabelText(QtGui.QApplication.translate("vtbox", "directory",  None ,QtGui.QApplication.UnicodeUTF8))
   

