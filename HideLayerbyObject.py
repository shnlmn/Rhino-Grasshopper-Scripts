import rhinoscriptsyntax as rs
theObjs = rs.GetObject("Select objects on the layer you wish to hide")
    

layerName = rs.ObjectLayer(theObjs)
print layerName
rs.LayerVisible(layerName, False)