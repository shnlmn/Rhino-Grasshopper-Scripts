import rhinoscriptsyntax as rs

layername = rs.CurrentLayer()
viewname = rs.CurrentView()
folder = 'E:\\2015\\2015053.00\\5-Model\\ISOPLAN'
layername = layername.replace(" ", "_")
layername = layername.replace(":", "_")
layername = layername.replace("/", "-")
viewname = viewname.replace(" ", "_")

filepath = folder + '\\' + layername + "-" + viewname + ".png\" "
imagewidth = str(4000)
imageheight = str(int(4000*0.6))
rscommand = ("-ViewCaptureToFile "+ ' "' + filepath + " Width=" + imagewidth + " Height=" + imageheight + " d=yes r=no a=no enter")
print(rscommand)
rs.Command(rscommand)