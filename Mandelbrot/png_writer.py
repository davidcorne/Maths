#!/usr/bin/env python
# Written by: DGC

import png

colours = []
for i in range(16):
    colour = int(255 * (16 - i))
    colours.append("#%02d%02d%02d" % (colour, colour, colour))
pic = png.from_array(colours)

pic.save("file.png")
