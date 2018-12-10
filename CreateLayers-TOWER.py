import rhinoscriptsyntax as rs
import re
import Rhino
layerDict = {}

rs.EnableRedraw(enable=False)

layerDict["A-ANNO-LEGN"] = {"LayerColor" : -16711681, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-ANNO-NOTE"] = {"LayerColor" : -16711681, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-ANNO-SYMB"] = {"LayerColor" : -16711681, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-AREA"] = {"LayerColor" : -65536, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-AREA-BOUNDARY"] = {"LayerColor" : -65536, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : -1.0}
layerDict["A-BLDG-OTLN"] = {"LayerColor" : -165536, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-BLDG-SHAFT"] = {"LayerColor" : -165536, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-BLDG-OTLN-ABOV"] = {"LayerColor" : -65536, "LayerPrintColor" : -16777216, "LayerLinetype" : "HIDDEN2", "LayerPrintWidth" : 0.0}
layerDict["A-BLDG-OTLN-BLOW"] = {"LayerColor" : -65536, "LayerPrintColor" : -16777216, "LayerLinetype" : "Dashed", "LayerPrintWidth" : 0.0}
layerDict["A-ESMT"] = {"LayerColor" : -3080448, "LayerPrintColor" : -16777216, "LayerLinetype" : "Dashed", "LayerPrintWidth" : 0.0}
layerDict["A-FLOR"] = {"LayerColor" : -3080448, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-FLOR-DIMS"] = {"LayerColor" : -3080448, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-FLOR-PATT"] = {"LayerColor" : -8355712, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-FLOR-STRS"] = {"LayerColor" : -3080448, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-FURN"] = {"LayerColor" : -65281, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-PLNT"] = {"LayerColor" : -16711936, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-PROP"] = {"LayerColor" : -1, "LayerPrintColor" : -16777216, "LayerLinetype" : "PROPERTY", "LayerPrintWidth" : 0.3}
layerDict["A-SITE"] = {"LayerColor" : -3080448, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-TOPO"] = {"LayerColor" : -65281, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-WALL"] = {"LayerColor" : -1, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.6}
layerDict["S-COL"] = {"LayerColor" : -3080448, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.6}
layerDict["A-WALL-INTR"] = {"LayerColor" : -1, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.3}
layerDict["I-WALL"] = {"LayerColor" : -1644826, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.3}
layerDict["A-GLAZ"] = {"LayerColor" : -16711681, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}

layerDict["A-HATCH-BOH"] = {"LayerColor" : (150, 150, 150), "LayerPrintColor" : (150, 150, 150), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-CORE"] = {"LayerColor" : -9723720, "LayerPrintColor" : -9723720, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-AMENITY"] = {"LayerColor" : (242, 218, 241), "LayerPrintColor" : (242, 218, 241), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-CORRIDOR"] = {"LayerColor" : -1644826, "LayerPrintColor" : -1644826, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-PARKING"] = {"LayerColor" : (220,220,220), "LayerPrintColor" : (220,220,220), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-RES_LOBBY"] = {"LayerColor" : (171, 223, 243), "LayerPrintColor" : (171, 223, 243), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-RESIDENTIAL"] = {"LayerColor" : (180, 223, 240), "LayerPrintColor" : (180, 223, 240), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-RES_BOH"] = {"LayerColor" : (178, 210, 222), "LayerPrintColor" : (178, 210, 222), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-RETAIL_LOBBY"] = {"LayerColor" : (254, 248, 226), "LayerPrintColor" : (254, 248, 226), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-RETAIL"] = {"LayerColor" : (247, 234, 193), "LayerPrintColor" : (247, 234, 193), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-RETAIL_BOH"] = {"LayerColor" : (222, 213, 178), "LayerPrintColor" : (222, 213, 178), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-HOTEL_LOBBY"] = {"LayerColor" : (230, 243, 197), "LayerPrintColor" :(230, 243, 197), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-HOTEL"] = {"LayerColor" : (214, 232, 168), "LayerPrintColor" : (214, 232, 168), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-HOTEL_BOH"] = {"LayerColor" : (209, 222, 178), "LayerPrintColor" : (209, 222, 178), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-OFFICE_LOBBY"] = {"LayerColor" : (251, 235, 229), "LayerPrintColor" : (251, 235, 229), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-OFFICE"] = {"LayerColor" : (241, 211, 199), "LayerPrintColor" : (241, 211, 199), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-OFFICE_BOH"] = {"LayerColor" : (222, 191, 178), "LayerPrintColor" : (222, 191, 178), "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}


currentLayer = rs.CurrentLayer()


for entry in layerDict:
    
    cLayerName = currentLayer + "::" + entry
    
    if cLayerName not in rs.LayerNames():
        rs.AddLayer(entry, rs.coercecolor(layerDict[entry]['LayerColor']), parent=currentLayer)
    elif rs.LayerLinetype(cLayerName) is not (layerDict[entry]['LayerLinetype']):
        rs.LayerLinetype(cLayerName, layerDict[entry]['LayerLinetype'])
        
    rs.LayerColor(cLayerName, rs.coercecolor(layerDict[entry]['LayerColor']))
    rs.LayerLinetype(cLayerName, layerDict[entry]['LayerLinetype'])
    rs.LayerPrintWidth(cLayerName, layerDict[entry]['LayerPrintWidth'])
    rs.LayerPrintColor(cLayerName, rs.coercecolor(layerDict[entry]['LayerPrintColor']))
        
    if re.search("-HATCH-", cLayerName):
        layer_c = rs.coercecolor(rs.LayerColor(cLayerName))
        layer_m = rs.LayerMaterialIndex(cLayerName)
        if layer_m == -1:
            layer_m = rs.AddMaterialToLayer(cLayerName)
        rs.MaterialColor(layer_m, layer_c)
        rs.LayerPrintColor(cLayerName, layer_c)
        
rs.EnableRedraw(enable=True)
