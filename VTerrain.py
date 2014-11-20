"""
/***************************************************************************
Name			 	 : VTerrain Enviro run
Description          : VTerrain Enviro run
Date                 : 16/May/11 
copyright            : (C) 2011 by Innova
email                : geodrinx@gmail.com : gisinnova@gmail.com
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from VTerrainDialog import VTerrainDialog
import os
import sys
import platform
from PyQt4 import QtGui, QtCore
from vtDialog import vtDialog
#currentPath = os.path.dirname( __file__ )
#sys.path.append( os.path.abspath( os.path.dirname( __file__) + '/icons' ) )

class VTerrain: 

   def __init__(self, iface):
    # Save reference to the QGIS interface
              self.iface = iface
             
   def initGui(self):  
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/VTerrain/icons/icon_VTerrain.png"),QCoreApplication.translate('VTerrain', "&VTerrain"), self.iface.mainWindow())

     # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run)

    self.iface.addPluginToMenu("VTerrain", self.action)   
    self.iface.addToolBarIcon(self.action)  
    
     #------VTerrainXYZ---------------------------------
    
    self.vterrainXYZAction=QAction(QIcon(":/VTerrain/icons/icon_VTerrainXYZ.png"), QCoreApplication.translate('VTerrain', "VTerrain_XY&Z"), self.iface.mainWindow())
    QObject.connect(self.vterrainXYZAction, SIGNAL("activated()"), self.vterrainXYZ)
         
    self.iface.addPluginToMenu("VTerrain", self.vterrainXYZAction)


     #------ABOUT---------------------------------
           
    self.aboutAction=QAction(QIcon(":/VTerrain/icons/about_icon.png"), QCoreApplication.translate('VTerrain', "&About"), self.iface.mainWindow())
    QObject.connect(self.aboutAction, SIGNAL("activated()"), self.about)
         
    self.iface.addPluginToMenu("VTerrain", self.aboutAction)


   def about(self):
        if QGis.QGIS_VERSION_INT < 10900:
           infoString = QString(QCoreApplication.translate('VTerrain', "Virtual Terrain Project Plugin<br />This plugin provides VTerrain functions.<br />Author: GeoDrinX <br />Mail: <a href=\"mailto:geodrinx@gmail.com\">geodrinx@gmail.com</a><br />Web: <a href=\"http://ExportToCanoma.blogspot.it\">ExportToCanoma.blogspot.it</a>\n"))
        else: 
           infoString = QCoreApplication.translate('VTerrain', "Virtual Terrain Project Plugin<br />This plugin provides VTerrain functions.<br />Author: GeoDrinX <br />Mail: <a href=\"mailto:geodrinx@gmail.com\">geodrinx@gmail.com</a><br />Web: <a href=\"http://ExportToCanoma.blogspot.it\">ExportToCanoma.blogspot.it</a>\n")
                      
        QMessageBox.information(self.iface.mainWindow(), "About VTerrain plugin",infoString)

   def vterrainXYZ(self):

        geomType = "Point" + '?crs=proj4:' + QgsProject.instance().readEntry("SpatialRefSys","/ProjectCRSProj4String")[0] 
        memLay = QgsVectorLayer(geomType, "VTerrain_XYZ", 'memory') 
        pr = memLay.dataProvider()

        # add fields
        pr.addAttributes( [ QgsField("X", QVariant.Double),
                            QgsField("Y", QVariant.Double),
                            QgsField("Z", QVariant.Double) ] )


        # LEGGO IL FILE "debug.txt"

        if platform.system() != "Windows":
               directory = "/usr/bin/"
               dirhome = os.environ['HOME']
               dire = dirhome + "/vtp/Data9999/"
               
        if platform.system() == "Windows":
               directory = "c:/Programmi/VTP/Apps/"  
               dire = str(directory).replace("Apps/", "Data9999/")
               dirhome = os.environ['HOME']





        
#        currentPath = os.path.dirname( __file__ )
#        file0 = currentPath + '/version.ini'
#        leggo=open(file0,'r')
#        
#        for line in leggo:
#            directory=line.split(";")
#              
#        file = directory[2] + "debug.txt"

        file = dirhome + "/debug.txt"
                
        debugTXT=open(file,'r')

#        salvalo = open("c:/gis/000report.csv",'w')
#        salvalo.write ("X,Y,Z\n")

#Click, cursor pick, epsilon 0.000103, |XY= -13.612342, 29.045197, 222.477554| nothing.
        
        while 1:
            line = debugTXT.readline()
            if not line:
                break
            trov = line.find("|XY=")
            if trov > 0:
                trov2 = line.find("|", trov+4)
                lung = len(line)
                coords = line[trov+4:trov2]
                
                trov3 = coords.find(",")
                trov4 = coords.find(",", trov3+1)
                coordX = coords[0:trov3]
                coordY = coords[trov3+1:trov4]
                coordZ = coords[trov4+1:]
                X = float(coordX) 
                Y = float(coordY)
                Z = float(coordZ)

                stringazza = ('%s,%s,%s\n') %(coordX, coordY, coordZ)
#                salvalo.write ( stringazza )                

                fet = QgsFeature()
                fet.setGeometry( QgsGeometry.fromPoint(QgsPoint(X,Y)) )
                fet.initAttributes(3)
                
                values = [(X), (Y), (Z)]                  

                fet.setAttributes(values)                        
                                                                         
                pr.addFeatures( [ fet ] )


        debugTXT.close()
#        salvalo.close()
        
        
        memLay.updateExtents()
        memLay.commitChanges()
        
        QgsMapLayerRegistry.instance().addMapLayer(memLay)            

        memLay.updateFields()
        
   
   def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("VTerrain",self.action)   
    self.iface.removeToolBarIcon(self.action)

   def run(self): 
    
    if platform.system() != "Windows":
      directory = "/usr/bin/"
      dirhome = os.environ['HOME']
      dire = dirhome + "/vtp/Data9999/"
    
    if platform.system() == "Windows":
      directory = "c:/Programmi/VTP/Apps/"      
    
    
    layer = self.iface.mapCanvas().currentLayer()
    if layer:
         name = layer.source();
                    
    # One of our tests above failed - show and error message and exit

         if platform.system() != "Windows":
               directory = "/usr/bin/"
               dirhome = os.environ['HOME']
               dire = dirhome + "/vtp/Data9999/"
               
         if platform.system() == "Windows":
               directory = "c:/Programmi/VTP/Apps/"
               
               if os.path.exists(directory):
#                  print ("Ci sta")
                  dire = str(directory).replace("Apps/", "Data9999/")
                  dirhome = os.environ['HOME']                  
               else:
#                  print ("Non ci sta !!!")
                  dirhome = os.environ['HOME']
                  directory = dirhome + "/Programmi/VTP/Apps/"                  
#                  print ("dirhome %s") %(dirhome)
                                   
               dire = str(directory).replace("Apps/", "Data9999/")
               dirhome = os.environ['HOME']
         
         try:
             os.stat(dire)
         except:
             os.makedirs(dire + "Terrains/")
             os.makedirs(dire + "BuildingData/")
             os.makedirs(dire + "BuildingModels/")
             os.makedirs(dire + "Elevation/")
             os.makedirs(dire + "GeoSpecific/")                                                    
             os.makedirs(dire + "Locations/")
             os.makedirs(dire + "PlantData/")
             os.makedirs(dire + "RoadData/")


         fileTemp=open(dire + "Terrains/tempVTP.xml",'w') 
         fileTemp.write ('<?xml version="1.0" encoding="utf-8"?>\n' )

         fileTemp.write ('<Terrain_Parameters>\n' )
         fileTemp.write ('	<Name>tempVTP</Name>\n' )

         fileTemp.write ('	<Vertical_Exag>1.000000</Vertical_Exag>\n' )
         fileTemp.write ('	<Min_Height>20.000000</Min_Height>\n' )
         fileTemp.write ('	<Nav_Style>0</Nav_Style>\n' )
         fileTemp.write ('	<Nav_Speed>100.000000</Nav_Speed>\n' )
         fileTemp.write ('	<Locations_File></Locations_File>\n' )
         fileTemp.write ('	<Init_Location></Init_Location>\n' )
         fileTemp.write ('	<Hither_Distance>5.000000</Hither_Distance>\n' )
         fileTemp.write ('	<Accel>false</Accel>\n' )
         fileTemp.write ('	<Allow_Roll>false</Allow_Roll>\n' )
         fileTemp.write ('	<LOD_Method>0</LOD_Method>\n' )
         fileTemp.write ('	<Tri_Count>10000</Tri_Count>\n' )
         fileTemp.write ('	<Tristrips>true</Tristrips>\n' )
         fileTemp.write ('	<Vert_Count>20000</Vert_Count>\n' )
         fileTemp.write ('	<Tile_Cache_Size>80</Tile_Cache_Size>\n' )
         fileTemp.write ('	<Tile_Threading>false</Tile_Threading>\n' )
         fileTemp.write ('	<Time_On>false</Time_On>\n' )
         fileTemp.write ('	<Init_Time>104 2 21 10 0 0</Init_Time>\n' )
         fileTemp.write ('	<Time_Speed>1.000000</Time_Speed>\n' )
         fileTemp.write ('	<Texture>3</Texture>\n' )
         fileTemp.write ('	<Texture_Filename></Texture_Filename>\n' )
         fileTemp.write ('	<Texture_Gradual>false</Texture_Gradual>\n' )
         fileTemp.write ('	<Texture_LOD_Factor>0.250000</Texture_LOD_Factor>\n' )
         fileTemp.write ('	<MIP_Map>false</MIP_Map>\n' )
         fileTemp.write ('	<Request_16_Bit>true</Request_16_Bit>\n' )
         fileTemp.write ('	<Pre-Light>true</Pre-Light>\n' )
         fileTemp.write ('	<PreLight_Factor>1.000000</PreLight_Factor>\n' )
         fileTemp.write ('	<Cast_Shadows>false</Cast_Shadows>\n' )
         fileTemp.write ('	<Color_Map>default_absolute.cmt</Color_Map>\n' )
         fileTemp.write ('	<Texture_Retain>true</Texture_Retain>\n' )
         fileTemp.write ('	<Detail_Texture>false</Detail_Texture>\n' )
         fileTemp.write ('	<DTexture_Name></DTexture_Name>\n' )
         fileTemp.write ('	<DTexture_Scale>1.000000</DTexture_Scale>\n' )
         fileTemp.write ('	<DTexture_Distance>1000.000000</DTexture_Distance>\n' )
         fileTemp.write ('	<Roads>false</Roads>\n' )
         fileTemp.write ('	<Road_File></Road_File>\n' )
         fileTemp.write ('	<Highway>true</Highway>\n' )
         fileTemp.write ('	<Paved>true</Paved>\n' )
         fileTemp.write ('	<Dirt>true</Dirt>\n' )
         fileTemp.write ('	<Road_Height>2.000000</Road_Height>\n' )
         fileTemp.write ('	<Road_Distance>2.000000</Road_Distance>\n' )
         fileTemp.write ('	<Road_Texture>true</Road_Texture>\n' )
         fileTemp.write ('	<Road_Culture>false</Road_Culture>\n' )
         fileTemp.write ('	<Trees>false</Trees>\n' )
         fileTemp.write ('	<Tree_File>2000</Tree_File>\n' )
         fileTemp.write ('	<Tree_Distance>5000</Tree_Distance>\n' )
         fileTemp.write ('	<Fog>false</Fog>\n' )
         fileTemp.write ('	<Fog_Distance>50.000000</Fog_Distance>\n' )
         fileTemp.write ('	<Fog_Color>-1 -1 -1</Fog_Color>\n' )
         fileTemp.write ('	<Content_File></Content_File>\n' )
         fileTemp.write ('	<Structure_Distance>1000</Structure_Distance>\n' )
         fileTemp.write ('	<Structure_Shadows>false</Structure_Shadows>\n' )
         fileTemp.write ('	<Shadow_Resolution>1024</Shadow_Resolution>\n' )
         fileTemp.write ('	<Shadow_Darkness>0.500000</Shadow_Darkness>\n' )
         fileTemp.write ('	<Shadows_Default_On>true</Shadows_Default_On>\n' )
         fileTemp.write ('	<Shadows_Every_Frame>true</Shadows_Every_Frame>\n' )
         fileTemp.write ('	<Limit_Shadow_Area>false</Limit_Shadow_Area>\n' )
         fileTemp.write ('	<Shadow_Radius>300.000000</Shadow_Radius>\n' )
         fileTemp.write ('	<PagingStructures>false</PagingStructures>\n' )
         fileTemp.write ('	<PagingStructureMax>2000</PagingStructureMax>\n' )
         fileTemp.write ('	<PagingStructureDist>2000.000000</PagingStructureDist>\n' )
         fileTemp.write ('	<Trans_Towers>false</Trans_Towers>\n' )
         fileTemp.write ('	<Tower_File></Tower_File>\n' )
         fileTemp.write ('	<Vehicles>false</Vehicles>\n' )
         fileTemp.write ('	<Vehicle_Size>1</Vehicle_Size>\n' )
         fileTemp.write ('	<Vehicle_Speed>1</Vehicle_Speed>\n' )
         fileTemp.write ('	<Sky>true</Sky>\n' )
         fileTemp.write ('	<Sky_Texture></Sky_Texture>\n' )
         fileTemp.write ('	<Ocean_Plane>false</Ocean_Plane>\n' )
         fileTemp.write ('	<Ocean_Plane_Level>-20.000000</Ocean_Plane_Level>\n' )
         fileTemp.write ('	<Depress_Ocean>false</Depress_Ocean>\n' )
         fileTemp.write ('	<Depress_Ocean_Level>-40.000000</Depress_Ocean_Level>\n' )
         fileTemp.write ('	<Horizon>false</Horizon>\n' )
         fileTemp.write ('	<Background_Color>0 0 0</Background_Color>\n' )
         fileTemp.write ('	<Route_Enable>false</Route_Enable>\n' )
         fileTemp.write ('	<Route_File></Route_File>\n' )
         fileTemp.write ('	<Distance_Tool_Height>5</Distance_Tool_Height>\n' )
         fileTemp.write ('	<HUD_Overlay>,0,0</HUD_Overlay>\n' )
         fileTemp.write ('	<Water>false</Water>\n' )
         fileTemp.write ('	<Water_File></Water_File>\n' )
         fileTemp.write ('	<HUD_Overview>false</HUD_Overview>\n' )
         fileTemp.write ('	<HUD_Compass>false</HUD_Compass>\n' )
         fileTemp.write ('	<Init_Scenario></Init_Scenario>\n' )

         for iLayer in range(self.iface.mapCanvas().layerCount()):
            layer = self.iface.mapCanvas().layer(iLayer)

            if layer.type() == layer.VectorLayer:
              
              fileTemp.write ('	<Layer>\n' )
              fileTemp.write ('		<Type>Abstract</Type>\n' )
         
              fileTemp.write ('		<Filename>')
              fileTemp.write ( str(layer.source()) )
              fileTemp.write ('</Filename>\n' )
                  
              fileTemp.write ('		<ObjectGeometry>false</ObjectGeometry>\n' )
              fileTemp.write ('		<LineGeometry>true</LineGeometry>\n' )
              fileTemp.write ('		<LineGeomColor>255 0 0</LineGeomColor>\n' )
              fileTemp.write ('		<LineGeomHeight>1.000000</LineGeomHeight>\n' )
              fileTemp.write ('		<LineWidth>1.000000</LineWidth>\n' )
              fileTemp.write ('		<Tessellate>false</Tessellate>\n' )
              fileTemp.write ('		<Labels>false</Labels>\n' )
              fileTemp.write ('	</Layer>\n' )

            elif layer.type() == layer.RasterLayer:
            
              name = layer.source();
              
              if QGis.QGIS_VERSION_INT < 10900:              
                 if name.endsWith(".bt"):            
                    fileTemp.write ('	<Surface_Type>0</Surface_Type>\n' )
              else:
                 if (name[-3:] == (".bt")):            
                    fileTemp.write ('	<Surface_Type>0</Surface_Type>\n' )              

              if QGis.QGIS_VERSION_INT < 10900: 
                 if name.endsWith(".bt.tif"):            
                    fileTemp.write ('	<Surface_Type>0</Surface_Type>\n' )
              else:
                 if (name[-7:] == (".bt.tif")):            
                    fileTemp.write ('	<Surface_Type>0</Surface_Type>\n' )                                      

              if QGis.QGIS_VERSION_INT < 10900: 
                 if name.endsWith(".itf.tif"):            
                    fileTemp.write ('	<Surface_Type>0</Surface_Type>\n' )
              else:
                 if (name[-8:] == (".itf.tif")):            
                    fileTemp.write ('	<Surface_Type>0</Surface_Type>\n' )
                        
              fileTemp.write ('	<Elevation_Filename>')

              if QGis.QGIS_VERSION_INT < 10900:              
                 if name.endsWith(".bt"):               
                    fileTemp.write ( str(layer.source()) )
              else:
                 if (name[-3:] == (".bt")):                    
                    fileTemp.write ( str(layer.source()) )

              if QGis.QGIS_VERSION_INT < 10900: 
                 if name.endsWith(".bt.tif"):            
                    name1 = str(layer.source()).replace(".bt.tif", ".bt")
                    fileTemp.write ( name1 )
              else:
                 if (name[-7:] == (".bt.tif")):            
                    name1 = str(layer.source()).replace(".bt.tif", ".bt")
                    fileTemp.write ( name1 )

              if QGis.QGIS_VERSION_INT < 10900: 
                 if name.endsWith(".itf.tif"):            
                    name1 = str(layer.source()).replace(".itf.tif", ".itf")
                    fileTemp.write ( name1 )
              else:
                 if (name[-8:] == (".itf.tif")):            
                    name1 = str(layer.source()).replace(".itf.tif", ".itf")
                    fileTemp.write ( name1 )

              if QGis.QGIS_VERSION_INT < 10900: 
                 if name.endsWith(".vtp.tif"):            
                    terrain = str(layer.name()).replace(".vtp", "")
                 else:
                    terrain = "tempVTP" 
              else:
                 if (name[-8:] == (".vtp.tif")):            
                    terrain = str(layer.name()).replace(".vtp", "")
                 else:
                    terrain = "tempVTP"                                                         

 

              fileTemp.write ('</Elevation_Filename>\n' )

#         print "name[-7:] <%s> name <%s> Terrain: <%s> " % (name[-7:], name, terrain)

         fileTemp.write ('</Terrain_Parameters> \n' )
         fileTemp.close()

         os.chdir(dirhome)
         
         print "%sEnviro -terrain=%s" % (directory , terrain)
                  
         os.spawnl(os.P_NOWAIT, directory + "Enviro", "-terrain=" + terrain)
#         QMessageBox.information(None,"VTerrain", directory + "Enviro" + " -terrain=" + terrain)         	       
#        QMessageBox.information(None,"Reader VTerrain", "Please, select a file .bt")
    return
    
#app = QtGui.QApplication(os.path.dirname(__file__)
