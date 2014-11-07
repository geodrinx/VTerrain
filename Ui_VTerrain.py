# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_VTerrain.ui'
#
# Created: Thu May 17 15:07:43 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VTerrain(object):
    def setupUi(self, VTerrain):
        VTerrain.setObjectName(_fromUtf8("VTerrain"))
        VTerrain.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(VTerrain)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(VTerrain)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VTerrain.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VTerrain.reject)
        QtCore.QMetaObject.connectSlotsByName(VTerrain)

    def retranslateUi(self, VTerrain):
        VTerrain.setWindowTitle(QtGui.QApplication.translate("VTerrain", "VTerrain", None, QtGui.QApplication.UnicodeUTF8))

