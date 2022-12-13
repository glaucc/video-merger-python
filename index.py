from moviepy.editor import *

clip1 = VideoFileClip("file1.mp4").subclip(5,15)
clip2 = VideoFileClip("file2.mp4").subclip(10,20)

clip2 = clip2.set_position((45,150))

final = concatenate_videoclips([clip1,clip2])
final_video.write_videofile("final.mp4")