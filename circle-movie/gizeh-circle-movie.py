# Let's draw a red circle !
# modified version of example at https://pypi.org/project/gizeh/

import moviepy.editor as mpy
import gizeh, random

# initialize surface
bg_white = (1,1,1)
bg_black = (0,0,0)
width  = 1280
height = 960
surface = gizeh.Surface(width, height, bg_color=bg_black) # in pixels

def make_frame(t):
    # t is time, from 0.0 to N.0, where N is duration of movie
    # every t, draw a new bubble

    # figure out radius of circle
    std_radius = int(height/20) # pick circle size relative to image size
    if t <= half_duration:
        # first half of video, circles get progressively bigger
        percent = t/half_duration
    else:
        # second half of video, circles get progressively smaller
        percent = 1 - (t-half_duration)/half_duration
    r = random.randint(0, round(std_radius*percent))
   
    # pick random placment and color for circle, draw it
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    red   = random.randint(0, 100)/100
    green = random.randint(0, 100)/100
    blue  = random.randint(0, 100)/100
    circle = gizeh.circle(r=r, xy= [x,y], fill=(red, green, blue))
    circle.draw(surface)

    # return image bitmap with color depth for making video frame
    return surface.get_npimage()

# make video animation
fps = 60
duration = 40
half_duration = int(duration / 2)
videoclip = mpy.VideoClip(make_frame, duration=duration)

# make audio clip and attach to video clip
audioclip = mpy.AudioFileClip("emperors-army-jeremy-blake-40sec.mp3")
new_audioclip = mpy.CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip

# write to video file
videoclip.write_videofile('circle_movie.mp4', fps=fps)

