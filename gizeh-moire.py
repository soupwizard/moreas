# Let's draw a red circle !
# modified version of example at https://pypi.org/project/gizeh/

import gizeh, random

# initialize surface
bg_white = (1,1,1)
bg_black = (0,0,0)
width  = 1280 
height = 960
surface = gizeh.Surface(width, height, bg_color=bg_black) # in pixels


center_x = int(width/2)
center_y = int(height/2)
center = (center_x, center_y)

def make_line(x,y):
    red   = random.randint(0, 100)/100
    green = random.randint(0, 100)/100
    blue  = random.randint(0, 100)/100
    line = gizeh.polyline(points=[center, (x,y)], stroke_width=1, 
                          stroke=(red,green,blue))
    return line

# Now make a shape and draw it on the surface: fill=(R,G,B)

# draw from center to across top
y = 0
for x in range(0, width-1):
    line = make_line(x,y)
    line.draw(surface)

# draw from center to along right side 
x = width-1
for y in range(0, height-1):
    line = make_line(x,y)
    line.draw(surface)

# draw from center to across bottom
y = height-1
for x in range(0, width-1):
    line = make_line(x,y)
    line.draw(surface)

# draw from center to along left side 
x = 0
for y in range(0, height-1):
    line = make_line(x,y)
    line.draw(surface)

# Now export the surface
#surface.get_npimage() # returns a (width x height x 3) numpy array
surface.write_to_png("moire.png")



