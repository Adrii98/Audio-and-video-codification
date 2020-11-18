import os

time1 = "03:10"
time2 = "03:20"
cut1 = "ffmpeg -ss " + time1 + " -i bbb.mp4 -to " + time2 + " -c copy bbb_cut.mp4"
cut2 = "ffmpeg -i bbb.mp4 -ss "  + time1 + " -to " + time2 + " -c copy bbb_cut.mp4"
os.system(cut1)
os.system(cut2)
