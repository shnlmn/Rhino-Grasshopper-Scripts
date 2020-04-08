import Rhino
import rhinoscriptsyntax as rs

details = rs.ObjectsByType(32768)
for detail in details:
    print(rs.ObjectName(detail))
    rs.DetailLock(detail, lock=True)
