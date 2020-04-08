import rhinoscriptsyntax as rs
import Rhino
import random
from random import randint
from System.Drawing import Color

dirs = dir(Color)
colors = list(filter(lambda x: Color.ToArgb((Color.FromName(x))) != 0, dirs))
layers = rs.LayerNames()
colors = random.sample(colors, len(layers))

for i, layer in enumerate(layers):
    rs.LayerColor(layer, color = Color.FromName(colors[i]))
