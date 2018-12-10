"""
Area Multi Units

This script is similar to Rhino's "Area" command, but will return a formatted
response in Inches, Feet and Meters. Useful when working in many different units.
"""


import rhinoscriptsyntax as rs

__commandname__ = "AreaMultUnits"
# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    selection = rs.GetObjects(message="Select Objects to Retrieve Area.", preselect=True)
    roundNo = rs.GetInteger("Digits to Round to.", number = 0, minimum = 0, maximum = 10)
    area = rs.Area(selection)
    aInch = rs.UnitScale(8)
    aFeet = rs.UnitScale(9)
    aMeter = rs.UnitScale(4)
    areas = [area*(a**2) for a in [aInch, aFeet, aMeter]]
    results = [int(x) if roundNo == 0 else round(x,roundNo) for x in areas]
    print("Area in Inches: {:,} in ; Area in Feet: {:,} SF ; Area in Meters: {:,} M ".format(results[0], results[1], results[2]))
#
if __name__ == "__main__":
    RunCommand(True)