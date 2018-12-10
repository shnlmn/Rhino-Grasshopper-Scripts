"""
For use with the Feasibility Study Workflow. 
See "F:\Resource\Strategic Initiatives\0702013.20 Research Initiative\Rhino Workflow"

For use with Feasibility Study Assistant Grasshopper Script.
See "F:\Resource\Strategic Initiatives\0702013.20 Research Initiative\Grasshopper\Grasshopper Toolset\Feasibility Drafting and modeling Assistant"

This script is to create a subfolder to a hatch layer that specifies it as an 
open area, as you might label as "OPEN TO BELOW" in floor plans.

Make sure the layer you want to add an OPEN layer to is the currently selected layer
before running.

"""

import rhinoscriptsyntax as rs

currentLayer = rs.CurrentLayer()
layerName = rs.LayerName(currentLayer, fullpath=False)
newLayer = rs.AddLayer(name=layerName+"_OPEN")
rs.ParentLayer(newLayer, currentLayer)


layer_c = rs.LayerColor(currentLayer)
layer_m = rs.LayerMaterialIndex(currentLayer)
if layer_m == -1:
    layer_m = rs.AddMaterialToLayer(newLayer)
rs.MaterialColor(layer_m, layer_c)
rs.LayerPrintColor(newLayer, layer_c)
rs.LayerColor(newLayer, layer_c)