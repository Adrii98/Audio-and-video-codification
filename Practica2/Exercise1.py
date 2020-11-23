import os


def compute(video_name):
    os.system("ffmpeg -i " + video_name + " 2> output.txt")


def main():
    compute("bbb.mp4")
    with open('output.txt', 'r') as file:
        for line in file:
            if (line.strip(" ").startswith("Duration") or line.strip(" ").startswith("title") or line.strip(" ").startswith("artist") or
                    line.strip(" ").startswith("comment")):
            #if line.strip(" ").startswith("title"):
                print(line)



main()
