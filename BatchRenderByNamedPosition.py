
import rhinoscriptsyntax as rs

viewList = [str(x) if x >= 10 else "0"+str(x) for x in range(16, 27)]

Outpath = r"E:\2016\2016047.00\3-Production\Model\Rhino\Structural Model_ Cadence 21st\Structural Rendering\ASSEMBLY ANIMATION"

for v in viewList:
    
    rs.Command("_-NamedPosition _Restore " + v + " _Enter", 0)
    rs.Command ("!_-Render")
    rs.Command ("_-SaveRenderWindowAs \"" + Outpath + "\\" + v + ".png\"")
    rs.Command ("_-CloseRenderWindow")
