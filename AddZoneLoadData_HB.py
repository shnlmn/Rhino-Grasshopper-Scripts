import rhinoscriptsyntax as rs
import Rhino
import random   
import json
import os
from random import randint
import Rhino.UI
import sys

import Eto.Drawing as drawing
import Eto.Forms as forms


def loadStandards():
    if not os.path.isfile("C:\\\\ladybug\\OpenStudio_Standards.json"):
        print ("You do not have OpenStudio_Standards.json in your ladybug folder. Please download and try again.")
        return -1
    else:
        filepath = "C:\\ladybug\OpenStudio_Standards.json"
        try:
            with open(filepath) as jsondata:
                openStudioStandardsLib = json.load(jsondata)
        except:
            print("Cannot Load OpenStudio_Standards.json")
            return -1
    return openStudioStandardsLib

class ZoneLoadDialog(forms.Dialog[bool]):
    
    #Dialog box Class initializer
    def __init__(self, osStandards):
        self.toggleButton = forms.ToggleButton
        self.textField = forms.TextBox
        self.objfilter = sum([16,8,32,1073741824])
        self.obj = rs.GetObject("Select Object to Apply Zone Data to:", filter=self.objfilter, preselect=True)
        self.osStandards = osStandards['space_types']['90.1-2007']['ClimateZone 1-8']
        self.bldg = ''
        self.zone = ''
        self.Standards = []
        self.Title = "Zone Load Data"
        self.Padding = drawing.Padding(10)
        self.Resizeable = False
        self.fieldsDict = {
            'bldgProgram': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'zoneProgram': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'equipmentLoadPerArea': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'infilRatePerArea_Facade': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'lightingDensityPerArea':[ forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'numOfPeoplePerArea': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'ventilationPerArea': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'ventilationPerPerson': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'recirculatedAirPerArea': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
            'isConditioned': [forms.ToggleButton(Text = 'Yes'), forms.CheckBox(Text = "Lock")],
            'maxRoofAngle': [forms.TextBox(Text = None), forms.CheckBox(Text = "Lock")],
        }
        self.GetExistingValues()
        self.bldg_dropdownlist = forms.DropDown()
        self.bldg_dropdownlist.DataStore = self.osStandards  
        self.bldg_dropdownlist.DropDownClosed += self.Bldg_DD_Close
        
        self.zone_dropdownlist = forms.DropDown()
        self.zone_dropdownlist.DropDownClosed += self.Zone_DD_Close
        
        self.ApplyStandardsButton = forms.Button(Text = "Apply")
        self.ApplyStandardsButton.Click += self.OnApplyButtonClick
        
        self.DefaultButton = forms.Button(Text = "OK")
        self.DefaultButton.Click += self.OnOKButtonClick
        
        self.AbortButton = forms.Button(Text = "Cancel")
        self.AbortButton.Click += self.OnCloseButtonClick
        
        # Add Toggle Events 
        for k,v in self.fieldsDict.items():
            if isinstance(v[0], self.toggleButton):
                v[0].Click += self.ToggleClick

        #Create Layout
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5,5)
        
        # Add Drop Down list
        layout.AddRow(self.bldg_dropdownlist, self.zone_dropdownlist)

        # Add Apply Standards
        layout.AddRow(self.ApplyStandardsButton)
        self.ApplyStandardsButton.Enabled = False
        
        # Add Fields
        for k,v in self.fieldsDict.items():
            self.m_label = forms.Label(Text = str(k))
            layout.AddRow(self.m_label, v[0], v[1])
            layout.AddRow(None)
            
        #Add Ok Close buttons
        layout.AddRow(self.DefaultButton, self.AbortButton)
        
        #Apply Layout to Form
        self.Content = layout
        
    def GetExistingValues(self):
        for k, v in self.fieldsDict.items():
            val = rs.GetUserText(self.obj, k)
            eto_field = v[0]
            try: 
                v1, v2 = val.split("::")
                if isinstance(eto_field, self.textField):
                    eto_field.Text = v1
                elif isinstance(eto_field, self.toggleButton):
                    if v1:
                        v1 = True if v1 == "True" else False
                        print("V!",v1, bool(v1))
                        eto_field.Checked = v1
                        eto_field.Text = str(v1)
                    else:
                        eto_field.Checked = True
                        eto_field.Text = 'True'
                v[1].Checked = int(v2)

            except AttributeError:
                if val:
                    v[0].Text = val
                else:
                    v[0].Text = 'default'
                v[1].Checked = False
            
             
    def _SetUserText(self):
        '''' Write the fields from the form into the Rhino Object's User Text
            Format is: Value::LockedBooleanInt
            '''
        for k,v in self.fieldsDict.items():

            eto_field = v[0]
            if isinstance(eto_field, self.textField):
                fieldVal = v[0].Text
            elif isinstance(eto_field, self.toggleButton):
                fieldVal = str(v[0].Checked)
            if fieldVal and not v[1].Checked:
                val = fieldVal+"::0"
                
            elif fieldVal and v[1].Checked:
                val = fieldVal+"::1"
                
            elif not fieldVal and v[1].Checked:
                val = "default::1"
            
            else:
                val="default::0"
                
            rs.SetUserText(self.obj, k, value=val)
            
    def Bldg_DD_Close(self, sender, e):
        self.zone_dropdownlist.DataStore = self.osStandards[self.bldg_dropdownlist.SelectedValue]
        self.bldg = self.osStandards[self.bldg_dropdownlist.SelectedValue]
        
    def Zone_DD_Close(self, sender, e):
        self.Standards = self.osStandards[self.bldg_dropdownlist.SelectedValue][self.zone_dropdownlist.SelectedValue]
        self.zone = self.osStandards[self.bldg_dropdownlist.SelectedValue][self.zone_dropdownlist.SelectedValue]
        self.ApplyStandardsButton.Enabled = True
        
    def ApplyValues(self, key, values):
        if int(self.fieldsDict[key][1].Checked) != True:
            self.fieldsDict[key][0].Text = values
        
    def OnApplyButtonClick(self, sender, e):
        self.ApplyValues('equipmentLoadPerArea', str(self.zone['elec_equip_per_area']*10.764961))
        self.ApplyValues('equipmentLoadPerArea',str(self.zone['elec_equip_per_area'] * 10.763961) ) #Per ft^2 to Per m^2
        self.ApplyValues('infilRatePerArea_Facade',str(self.zone['infiltration_per_area_ext'] * 0.00508001))
        self.ApplyValues('lightingDensityPerArea',str(self.zone['lighting_w_per_area'] * 10.763961) ) #Per ft^2 to Per m^2
        self.ApplyValues('numOfPeoplePerArea',str(self.zone[ 'occupancy_per_area'] * 10.763961 /1000 )) #Per 1000 ft^2 to Per m^2
        self.ApplyValues('ventilationPerArea',str(self.zone['ventilation_per_area'] * 0.00508001 )) #1 ft3/min.m2 = 5.08001016E-03 m3/s.m2
        self.ApplyValues('ventilationPerPerson',str(self.zone[ 'ventilation_per_person'] * 0.0004719)  ) #1 ft3/min.perosn = 4.71944743E-04 m3/s.person
        self.ApplyValues('bldgProgram',self.bldg_dropdownlist.SelectedValue)
        self.ApplyValues('zoneProgram',self.zone_dropdownlist.SelectedValue)
        
    def OnCloseButtonClick(self, sender, e):
        self.Close(False)
        
    def OnOKButtonClick(self, sender, e):
        self.Close(True)

    def ToggleClick(self, sender, e):
        print(sender.Checked)
        print(sender.Text)
        if sender.Checked == True:
            sender.Text = "True"
        else:
            sender.Text = "False"
            
def SetLoad(osStandards):
    dialog = ZoneLoadDialog(osStandards)
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    if (rc):
        pass
        dialog._SetUserText()
        print("Attributes Applied")
        
if __name__ == "__main__":
    osStandards = loadStandards()
    SetLoad(osStandards)