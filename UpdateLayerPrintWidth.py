import rhinoscriptsyntax as rs
import re
layers = rs.LayerNames()

rs.EnableRedraw(enable=False)
for layer in layers:
    if re.search("A-WALL", layer):
        rs.LayerPrintWidth(layer, 0.3)
rs.EnableRedraw(enable=True)