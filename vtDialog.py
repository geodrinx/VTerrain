"""
/***************************************************************************
QgisSRTMDialog
A QGIS plugin
Import Nasa SRTM data to your current view
                             -------------------
begin                : 2010-01-31 
copyright            : (C) 2010 by Bluedynamics
email                : phil@bluedynamics.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui 
from Ui_vtbox import Ui_vtbox
from qgis.core import *
import sys,os

# create the dialog for zoom to point
class vtDialog(QtGui.QDialog):
  def __init__(self,parent,directory): 
    
    # Set up the user interface from Designer.
    
          QtGui.QDialog.__init__(self) 
          self.parent=parent
          self.ui = Ui_vtbox()
          self.ui.setupUi(self,directory) 
          
          canvas=self.parent.iface.mapCanvas()
          ext=canvas.extent()
          self.ui.directorydefault.setText(QtCore.QString('%s'%directory)) 
          self.ui.directorydefault.setText(QtCore.QString('%s'%directory)) 
          self.ui.label.setText(QtCore.QString('%s'%"Insert your Directory VTerrain:")) 
          self.ui.info_cancel.setText(QtCore.QString('%s'%"press CANCEL if you don't have installed VTerrain"))   
          self.ui.info_ok.setText(QtCore.QString('%s'%" press OK for save your right directory"))   
      
  def accept(self):
       directo_out = self.ui.directorydefault.displayText()
       self.done(0)
       directory = directo_out
       currentPath = os.path.dirname( __file__ )
       file = currentPath + '/version.ini'
       aggiorno=open(file,'w')
       aggiorno.write ('install;2;'+directory )
       aggiorno.close()
       
  
      
     

  
        
