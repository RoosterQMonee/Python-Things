'''pip install moviepy'''

from moviepy.editor import *
import os

for f in os.listdir("data"):
    os.remove("./data/" + f)

final_clip = concatenate_videoclips([VideoFileClip("base.mp4"), VideoFileClip("base.mp4")], method="compose")
final_clip.write_videofile("./data/good-god-0.mp4")

for x in range(1, 300):
    title = f"./data/good-god-{x}.mp4"
    
    x = VideoFileClip(f"./data/good-god-{x-1}.mp4")
    y = VideoFileClip("base.mp4")

    final_clip = concatenate_videoclips([x, y], method="compose")
    final_clip.write_videofile(title)
