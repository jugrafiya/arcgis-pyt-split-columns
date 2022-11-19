# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = "Split Date columns (Columns ending with _Date) into different shp having data with the respective field not null"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        #First Parameter (Input Layer)
        param0 = arcpy.Parameter(
            displayName= "Input Featute Layer",
            name= "in_features",
            datatype ="GPFeatureLayer",
            parameterType = "Required",
            direction = "Input")


        #Second Parameter (Output Folder)
        param1 = arcpy.Parameter(
            displayName="Output Folder",
            name="out_folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input")

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        in_features = parameters[0].valueAsText
        outputFolder = parameters [1].valueAsText

        messages.addMessage('Reading File: ' + in_features)

        dateFields = []

        fields = arcpy.ListFields(in_features)

        for field in fields:
            if (field.name.endswith('_Date')):
                dateFields.append(field.name)

        
        for filename in dateFields:
            arcpy.conversion.FeatureClassToFeatureClass(in_features,outputFolder,filename.replace('_Date','')+".shp", filename +" IS NOT NULL")


        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
