import os


def compute(video_name):
    os.system("ffmpeg -i " + video_name + " 2> output.txt")


def rename(file):
    new_name = 'BBB_renamed.mp4'
    os.rename(file, new_name)


def change_codec(video):
    act = "ffmpeg -i " + video + "-acodec mp3 -vcodec copy output_codec_changed.mp4"
    os.system(act)


def main():
    compute("bbb.mp4")
    with open('output.txt', 'r') as file:
        for line in file:
            if (line.strip(" ").startswith("Duration") or line.strip(" ").startswith("title") or line.strip(
                    " ").startswith("artist") or
                    line.strip(" ").startswith("comment")):
                print(line)


main()
