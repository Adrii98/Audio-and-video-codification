import os


class container:
    pass

def create_container():
    start = "00:00"
    finish = "01:00"
    cut1 = "ffmpeg -ss " + start + " -i bbb.mp4 -to " + finish + " -c copy bbb_cut.mp4"
    cut2 = "ffmpeg -i bbb.mp4 -ss " + start + " -to " + finish + " -c copy bbb_cut.mp4"
    os.system(cut1)
    os.system(cut2)
    os.system("ffmpeg -i bbb_cut.mp4 -vn -ac 1 cutted_monoaudio.mp3")
    os.system("ffmpeg -i bbb_cut.mp4 -vn -ac copy -b:a 80k cutted_lowbitrate.mp3")
    os.system("ffmpeg -i cutted_monoaudio.mp3 -i bb_cut.mp4 -i cutted_lowbitrate.mp3 -c:v copy -c:a copy container.mp4 ")




create_container()

