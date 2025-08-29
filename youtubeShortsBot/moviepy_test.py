from moviepy.editor import *

# to understand how moviepy works

# Load the video
video = VideoFileClip("videos/vid1.mp4")

# Create the text clip with a white font on a transparent background
txt_clip = (TextClip("ABSOLUTE TRUTH", color='white', font='Helvetica-bold', fontsize=50)
.set_position('center')
.set_duration(video.duration))

# Create the semi-transparent colored clip for the text background
txt_width, txt_height = txt_clip.size
color_clip = (ColorClip(size=(txt_width+75, txt_height+50), color=(0,0,0))
.set_opacity(.5)
.set_duration(video.duration)
.set_position('center'))

# Create the text clip that appears in From 5 seconds
txt_clip2 = (TextClip("THE FIRST TO APOLOGIZE IS ALWAYS THE BRAVEST", color='white', font='Helvetica-bold', fontsize=50,
stroke_color='black', stroke_width=2, kerning=10, align='center', method='caption', interline=-20)
.set_position('center')
.set_duration(video.duration))

# Combine the text clip and the color clip
result = CompositeVideoClip([color_clip, txt_clip])

# Center the composition
result = result.set_position(lambda t: ('center', 120))

# Combine the original video with the text clip
final_result = CompositeVideoClip([video, result, txt_clip2])

# Save the video final
final_result.write_videofile("vid1_text.mp4", fps=video.fps)