import rhinoscriptsyntax as rs
import Rhino
import clr

path = "\"C:\Users\sleaman\Desktop\Rainier Batch Renders\\"
print(path)
plugin = rs.GetPlugInObject("Rhino Bonus Tools")
if plugin is not None:
    states = plugin.LayerStateNames()

for state in states:
    plugin.RestoreLayerState(state)
    rs.Command("!_Render", echo=False)
    rs.Command("-_SaveRenderWindowAs " + path + state + "\"")
    
print("Finished Renders")