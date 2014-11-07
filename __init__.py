"""
/***************************************************************************
Name			 	 : VTerrain Enviro run
Description          : VTerrain Enviro run
Date                 : 16/May/11 
copyright            : (C) 2011 by Innova
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
from PyQt4 import QtGui, QtCore
import ConfigParser
import os.path
import sys,os

#p = ConfigParser.ConfigParser()
#here = os.path.join(os.path.dirname(__file__),"config.ini")
#p.read(here)

def name():
  return "VTerrain Enviro run"
 # return p.get('general','name')

def description():
  return "VTerrain Enviro 3d viewer bt file"
 # return p.get('general','description')

def version():
  return "0.7"
 # return p.get('general','version')

def qgisMinimumVersion():
  return "1.5.0"
  #return p.get("general","qgisMinimumVersion")
  
def email():
  return "geodrinx@gmail.com"
 # return p.get('general','email')
 
def author():
  return "geodrinx"
 # return p.get('general','author')  
  
def icon():
    return 'icons/icon_VTerrain.png' 

def classFactory(iface): 
  # load VTEnviro class from file VTEnviro
  from VTerrain import VTerrain
  return VTerrain(iface)
 
 
