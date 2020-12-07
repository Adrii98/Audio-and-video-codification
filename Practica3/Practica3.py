import os
import subprocess

class container:
    def __init__(self):
        self.videofile = "bbb.mp4"
        self.cuttedfile = "bbb_cut.mp4"
        self.cont = "container.mp4"
        self.monoaudio = "cutted_monoaudio.aac"
        self.lowbitrate = "cutted_lowbitrate.ac3"

    def cut_video(self):
        start = "00:00"
        finish = "01:00"
        cut1 = "ffmpeg -ss " + start + " -i " + self.videofile + " -to " + finish + " -c " + self.cuttedfile
        cut2 = "ffmpeg -i " + self.videofile + " -ss " + start + " -to " + finish + " -c " + self.cuttedfile
        os.system(cut1)
        os.system(cut2)

    def get_mono_lowbitrate_audios(self):
        #This method creates a monoaudio and decreases de bitrate
        os.system("ffmpeg -i " + self.cuttedfile + " -vn -ac 1 " + self.monoaudio)
        os.system("ffmpeg -i " + self.cuttedfile + " -vn -c:a copy -ab 80k " + self.lowbitrate)

    def create_container(self):
        # Create container using the previous streams
        os.system("ffmpeg -i " + self.cuttedfile + " -i " + self.monoaudio + " -i " + self.lowbitrate + " -map 0:v:0 -map 1:a:0 -map 2:a:0 -c:v copy -c:a copy " + self.cont)

    def track_reading(self):
        #This method takes a container and indicates with what  broadcasting standars is compatible
        videocodec = os.popen("ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 " + self.cont).read()
        videocodec = videocodec[:len(videocodec)-1]
        audiocodec = os.popen("ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 " + self.cont).read()
        audiocodec = audiocodec[:len(audiocodec) - 1]
        comp = " "
        if str(videocodec) in ["mpeg2", "h264", "avs", "avs+"]:
            if str(audiocodec) in ["aac", "ac3", "mp3", "dra", "mp2", "mp3"]:
                comp = "DTMB"
                if str(audiocodec) in ["aac", "ac3", "mp3"]:
                    comp += " , DVB"
                if str(audiocodec) == "aac":
                    comp += " , ISDB"
                if str(audiocodec) == "ac3":
                    comp += " , ATSC"
            print("The container introduced is compatible with this broadcasting standards: " + comp)
        else:
            print("ERROR:Container not compatible with any broadcasting standard")

def testing():
    cont1 = container()
    cont1.cut_video()
    cont1.get_mono_lowbitrate_audios()
    cont1.create_container()
    cont1.track_reading()


testing()



