import rhinoscriptsyntax as rs

hatches = rs.ObjectsByType(65536)
lock = True
for hatch in hatches:
    if rs.IsObjectLocked(hatch):
        lock = False
        
if lock:
    rs.LockObjects(hatches)
else:
    rs.UnlockObjects(selblockhatches)