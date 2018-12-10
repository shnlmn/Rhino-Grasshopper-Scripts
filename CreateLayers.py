import rhinoscriptsyntax as rs
import re
from System.Drawing import Color
import Rhino
layerDict = {}


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
layerDict["A-HATCH-AMENITY"] = {"LayerColor" : -36904, "LayerPrintColor" : -1335850, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-BOH"] = {"LayerColor" : -9868951, "LayerPrintColor" : -9868951, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-CORE"] = {"LayerColor" : -9723720, "LayerPrintColor" : -9723720, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-CORRIDOR"] = {"LayerColor" : -1644826, "LayerPrintColor" : -1644826, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-LIVEWORK"] = {"LayerColor" : -6365441, "LayerPrintColor" : -6365441, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-LOBBY"] = {"LayerColor" : -545672, "LayerPrintColor" : -545672, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-OUTDRAMEN"] = {"LayerColor" : -16777216, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-PARKING"] = {"LayerColor" : -4276546, "LayerPrintColor" : -4276546, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-RESIDENTIAL"] = {"LayerColor" : -2245022, "LayerPrintColor" : -2245022, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-RETAIL"] = {"LayerColor" : -1331795, "LayerPrintColor" : -1331795, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-HATCH-ROOFDECK"] = {"LayerColor" : -6501269, "LayerPrintColor" : -6501269, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-PLNT"] = {"LayerColor" : -16711936, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-PROP"] = {"LayerColor" : -1, "LayerPrintColor" : -16777216, "LayerLinetype" : "PROPERTY", "LayerPrintWidth" : 0.3}
layerDict["A-SITE"] = {"LayerColor" : -3080448, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-TOPO"] = {"LayerColor" : -65281, "LayerPrintColor" : -16777216, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.0}
layerDict["A-WALL"] = {"LayerColor" : -1, "LayerPrintColor" : -1, "LayerLinetype" : "Continuous", "LayerPrintWidth" : 0.6}

currentLayer = rs.CurrentLayer()
print(currentLayer)

for entry in layerDict:
    cLayerName = currentLayer + "::" + entry
    print(cLayerName)
    if cLayerName not in rs.LayerNames():
        rs.AddLayer(entry, Color.FromArgb(layerDict[entry]['LayerColor']), parent=currentLayer)
        rs.LayerLinetype(cLayerName, layerDict[entry]['LayerLinetype'])
        rs.LayerPrintWidth(cLayerName, layerDict[entry]['LayerPrintWidth'])
    elif rs.LayerLinetype(cLayerName) is not (layerDict[entry]['LayerLinetype']):
        print(cLayerName, rs.LayerLinetype(cLayerName))
        print(entry, layerDict[entry]['LayerLinetype'])
        rs.LayerLinetype(cLayerName, layerDict[entry]['LayerLinetype'])
    if re.search("-HATCH-", cLayerName):
        layer_c = rs.LayerColor(cLayerName)
        layer_m = rs.LayerMaterialIndex(cLayerName)
        if layer_m == -1:
            layer_m = rs.AddMaterialToLayer(cLayerName)
        rs.MaterialColor(layer_m, layer_c)
        rs.LayerPrintColor(cLayerName, layer_c)