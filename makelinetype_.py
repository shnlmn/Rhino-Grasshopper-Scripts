import Rhino
import scriptcontext as sc
print(sc.doc.Linetypes.ReferenceEquals.DeclaringType)
#line = sc.doc.Linetypes.Add("test")
for t in sc.doc.Linetypes:
    print(t.Name)
    
