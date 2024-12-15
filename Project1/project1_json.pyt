# -*- coding: utf-8 -*-

import arcpy
from project1 import importNoTaxJSON

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
        self.label = "Import No Tax JSON to Feature Class"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        para_ws = arcpy.Parameter(
            name='workspace',
            displayName='Workspace',
            direction='Input',
            parameterType='Required',
            datatype='DEWorkspace'
        )
        para_json=arcpy.Parameter(
            name='json',
            displayName='No Tax Json',
            direction='Input',
            parameterType='Required',
            datatype='DEFile'
        )
        para_out = arcpy.Parameter(
            name='output',
            displayName='Output shpaefile',
            parameterType='Required',
            direction='Output',
            datatype='GPString'
        )
        params = [para_ws,para_json,para_out]
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
        
        workspace = parameters[0].valueAsText
        json_file = parameters[1].valueAsText
        out_fc = parameters[2].valueAsText
        importNoTaxJSON(workspace=workspace,json_file=json_file,out_fc=out_fc)
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
