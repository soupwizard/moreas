# Let's draw a red circle !
# modified version of example at https://pypi.org/project/gizeh/

import moviepy.editor as mpy
import gizeh, random

# initialize surface
bg_white = (1,1,1)
bg_black = (0,0,0)
width  = 1920
height = 1080
surface = gizeh.Surface(width, height, bg_color=bg_black) # in pixels

count = 0
std_radius = int(height/18) # pick circle size relative to image size

def make_frame(t):
    # t is frame number
    # number of frames is fps*duration
    # so for a 10 second duration movie at 30fps, this is called 300 times
    # every t, draw a new circle

    # figure out radius of circle as percent of std_radius
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
half_duration = round(duration / 2)
videoclip = mpy.VideoClip(make_frame, duration=duration)

# make audio clip and attach to video clip
audioclip = mpy.AudioFileClip("emperors-army-jeremy-blake-41sec.mp3")
new_audioclip = mpy.CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip

# audio has trailing 1 sec of silence to cover make_frame doing 1 frame too many
# so clip back down to duration
videoclip = videoclip.subclip(0.0, duration)

# write to video file
videoclip.write_videofile('circle_movie.mp4', fps=fps)

