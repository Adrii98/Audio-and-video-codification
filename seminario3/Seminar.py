import os

def transform():#Compute the video in different codecs
    scale = "360:240"
    os.system("ffmpeg -i bbb_cut.mp4 -vf scale=" + scale + " output_cutted_resized.mp4")
    os.system("ffmpeg -i output_cutted_resized.mp4 -c:v libvpx -b:v 1M -c:a libvorbis VP8_output.webm")
    os.system("ffmpeg -i output_cutted_resized.mp4 -c:v libvpx-vp9 -b:v 2M VP9_output.webm")
    os.system("ffmpeg -i output_cutted_resized.mp4 -c:v libx265 -crf 28 -c:a aac -b:a 128k h265_output.mp4")
    os.system("ffmpeg -i output_cutted_resized.mp4 -c:v libaom-av1 -b:v 2000k -strict experimental AV1_output.mkv")
    createvideo()

def createvideo():#Mosaic
    os.system('ffmpeg -i VP8_output.webm -i VP9_output.webm -i h265_output.mp4 -i AV1_output.mkv -filter_complex "nullsrc=size=640x480 [base]; [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" -c:v libx264 output.mkv')

def stream():#Stream
    ip = input("Write the ip where you want to transmit in the next format(127.0.0.0:port):")
    os.system("ffmpeg -i alfredo_halloween.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://" + ip)

def menu():
    inp = '5'
    while (inp != '0'):
        inp = input("This script computes different processes in the BBB video(all in 360:240)\n"
                    "Write a 1 to compute a video mae from 4 videos with different codecs\n"
                    "Write a 2 for stream Aflredo Duro Halloweens video\n"
                    "Write a 0 to finish de app\n"
                    "Option: ")
        if inp == '1':
            transform()
        elif inp == '2':
            stream()

    print("Application finished")



menu()
