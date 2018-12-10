import rhinoscriptsyntax as rs

def main():
    rs.EnableRedraw(False)
    selected = rs.SelectedObjects()
    theObjs = rs.GetObject("Select objects on the layer you wish to select")

    layer = rs.ObjectLayer(theObjs)
    
    layerObjs= rs.ObjectsByLayer(layer)
    layerObjs.extend(selected)
    print(layerObjs)
    rs.SelectObjects(layerObjs)
    
    rs.EnableRedraw(True)

if __name__=="__main__":
    main()