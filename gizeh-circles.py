# Let's draw a red circle !
# modified version of example at https://pypi.org/project/gizeh/

import gizeh, random

# initialize surface
bg_white = (1,1,1)
bg_black = (0,0,0)
width  = 1280
height = 960
surface = gizeh.Surface(width, height, bg_color=bg_black) # in pixels

# Now make a shape and draw it on the surface: fill=(R,G,B)
for i in range(0, int(height/3)):
    r = random.randint(5, int(height/16))
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    red   = random.randint(0, 100)/100
    green = random.randint(0, 100)/100
    blue  = random.randint(0, 100)/100
    circle = gizeh.circle(r=r, xy= [x,y], fill=(red, green, blue))
    circle.draw(surface)

# Now export the surface
surface.get_npimage() # returns a (width x height x 3) numpy array
surface.write_to_png("circle.png")



