

#------------------------------------------------------
# Name:        getLayerList  
# Purpose:     Function to return a list of layers matching pattern "L/d"
# Author:      Shane Leaman
# Created:     08/30/2017
#------------------------------------------------------

import rhinoscriptsyntax as rs
import Rhino
import re


def getLayers(include=False, exclude=False):
    
    """
    Help on function getLayers in module getLayerList:
    
        getLayers(include, exclude) 
            Get list of layers that begin with regex L/d. 
            Parameters:
                include = List of layers to linclude that do not begin with
                    regex L/d
                exclude = List of layers to exclude from children search
            Returns:
                list of layers
        
    
    """
    
    docLayers = list(filter(lambda x: not rs.IsLayerReference(x),rs.LayerNames()))
    layerSplit = [d.split("::") for d in docLayers]
    returnList = []
    nestWarning = 0
    
    # dummy patterns 
    includePattern = re.compile(r"SECTION$")
    excludePattern = re.compile(r"______________")
    
    
    if include:
        includePattern = re.compile(r"|".join(include))
    if exclude:
        excludePattern = re.compile(r"|".join(exclude))
    for entry in layerSplit:
        l_i = [i for i, item in enumerate(entry) if (re.search("^L\d", item) or re.search("^P\d", item) or includePattern.search(item))]

#       Apply exclude pattern
        exclude = 0
        for item in entry:
            if excludePattern.search(item):
                exclude = 1

        # if the position of the match is at the end of the list, then include it in the return list
        if(len(l_i) > 1) and nestWarning == 0:
            print("Nested L# layers detected. Script will only return layer highest in the heirarchy.")
            nestWarning = 1
        try:
            
            if not exclude and (l_i[0] + 1) == len(entry):
                returnList.append("::".join(entry))
        except:
            pass
    return(returnList)

if __name__ == "__main__":
    print(getLayers(exclude=[".3dm", "Make2D"]))