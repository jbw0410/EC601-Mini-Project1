import os,sys,ffmpeg

os.system("ffmpeg -r 1 -f image2 -i %d.jpg  Boston.mp4")