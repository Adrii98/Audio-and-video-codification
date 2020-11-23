import os


def cutvideo():#This function cuts the video between 3:30 and 3:20
    start = "03:10"
    finish = "03:20"
    cut1 = "ffmpeg -ss " + start + " -i bbb.mp4 -to " + finish + " -c copy bbb_cut.mp4"
    cut2 = "ffmpeg -i bbb.mp4 -ss " + start + " -to " + finish + " -c copy bbb_cut.mp4"
    os.system(cut1)
    os.system(cut2)


def yuvhistogram():#This function compute the yuv histogram of the cutted video
    os.system("ffplay bbb_cut.mp4 -vf 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay'")


def resizevideo():#This function resize the video to a given resolution
    scale = input(
        "Write the resolution at which you want to resize the video. It has to be 720p,480p, 360x240 or 160x120. Write it in this format (height:weight): ")
    os.system("ffmpeg -i bbb_cut.mp4 -vf scale=" + scale + " output_resized.mp4")


def codec():#This function changes the audio codec to mp3
    os.system("ffmpeg -i bbb_cut.mp4 -ac 1 output_monoaudio.mp4")
    os.system("ffmpeg -i bbb_cut.mp4 -acodec mp3 -vcodec copy output_codec_changed.mp4")


def menu():
    inp = '5'
    while (inp != '0'):
        inp = input("This script computes different processes in the BBB video\n"
                    "Write a 1 for cutting the video\n"
                    "Write a 2 for computing the yuv histogram\n"
                    "Write a 3 for resize the video\n"
                    "Write a 4 for audiocodec change the video\n"
                    "Write a 0 to finish de app\n"
                    "Option: ")
        if inp == '1':
            cutvideo()
        elif inp == '2':
            yuvhistogram()
        elif inp == '3':
            resizevideo()
        elif inp == '4':
            codec()

    print("Application finished")


menu()
