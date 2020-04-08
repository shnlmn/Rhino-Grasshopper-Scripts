import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

def ExportSTLWithSettings(objs):
    rs.SelectObjects(objs)
    
    strCurrDP = rs.DocumentPath()
    strCurrDN = rs.DocumentName()
    filt = "STL Files (*.stl)|*stl||"
    
    if strCurrDN:
        strSaveDN = strCurrDN[:-3] + "stl"
        strFileName = rs.SaveFileName("Export STL", filt, strCurrDP, strSaveDN)
    else:
        strFileName = rs.SaveFileName("Export STL", filt)
 
    strSett = STLSettings()
    
    if not strSett:
        print("Unable to get export settings")
    
    print("exporting"+strFileName)
    rs.Command("-_Export" + " \"" + strFileName + "\"" + " " + strSett, True)
    
def STLSettings():
    str1 = "_ExportFileAs=_Binary "
    str2 = "_ExportUnfinishedObjects=_Yes "
    str3 = "_UseSimpleDialog=_No "
    str4 = "_UseSimpleParameters=_No "
    str5 = "_Enter _DetailedOptions "
    str6 = "_JaggedSeams=_No "
    str7 = "_PackTextures=_No "
    str8 = "_Refine=_Yes "
    str9 = "_SimplePlane=_No "
    str10 = "_Weld=_No "
    str11 = "_AdvancedOptions "
    str12 = "_Angle=15 "
    str13 = "_AspectRatio=0 "
    str14 = "_Distance=0.01 "
    str15 = "_Grid=16 "
    str16 = "_MaxEdgeLength=0 "
    str17 = "_MinEdgeLength=0.0001 "
    str18 = "_Enter _Enter"

    strComb = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10
    strComb = strComb + str11 + str12 + str13 + str14 + str15 + str16 + str17 + str18

    return(strComb)
    

### Get objects to export ###
orig_obj = rs.GetObjects(message="Select objects to scale and export.", filter=16)
obj_scale = rs.GetReal(message="Scale to export (____\" to 1')")
obj_scale = obj_scale*1/12

current_UnitSystem = rs.UnitSystem()
rs.UnitSystem(2, True)

scaled_obj = rs.ScaleObjects(rs.CopyObjects(orig_obj), (0,0,0), [obj_scale,obj_scale,obj_scale])

ExportSTLWithSettings(scaled_obj)

rs.DeleteObjects(scaled_obj)

rs.UnitSystem(current_UnitSystem, True)