from moviepy.editor import *
import ffmpeg, os

clip = VideoFileClip("assets/template.mp4")

fan = input('\nAverage ... fan >> ')
enjoyer = input('\nAverage ... enjoyer >> ')

fan_txt = TextClip("average\n" + fan + "\nfan",color="black", font="Arial", kerning = 5, fontsize=75).set_position((160,10)).set_duration(clip.duration)
enjoyer_txt = TextClip("average\n" + enjoyer + "\nenjoyer",color="black", font="Arial", kerning = 5, fontsize=75).set_pos((960,10)).set_duration(clip.duration)

video = CompositeVideoClip([clip,fan_txt,enjoyer_txt])

name = "average_" + fan + "_fan_vs_average_" + enjoyer + "_enjoyer.mp4"

video.write_videofile("tmp_input.avi",fps=25,codec='mpeg4')

stream = ffmpeg.input('tmp_input.avi')
stream = ffmpeg.output(stream, name)
ffmpeg.run(stream)

os.remove("tmp_input.avi")