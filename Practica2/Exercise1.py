import os


def compute(video_name):
    os.system("ffmpeg -i " + video_name + " 2> output.txt")


def rename():
    file = input("Write the new file you want to rename(extension needed): ")
    new_name = input("Write the new file name(extension needed): ")
    os.rename(file, new_name)


def change_codec():
    video = input("Select the video you want to change the codec: ")
    selection = input("Write 1(change video to vp9) or 0(change audio codec): ")
    if (selection):
        act = "ffmpeg -i " + video + " -c:v libvpx-vp9 -b:v 2M output_vp9_changed.webm"
    else:
        codec = input("Write the codec: ")
        act = "ffmpeg -i " + video + " -c:a " + codec + " output_audiocodec_changed.mp4"
    os.system(act)


def container_data():
    compute("bbb.mp4")
    with open('output.txt', 'r') as file:
        for line in file:
            if (line.strip(" ").startswith("Duration") or line.strip(" ").startswith("title") or line.strip(
                    " ").startswith("artist") or
                    line.strip(" ").startswith("comment")):
                print(line)


def resizevideo():  # This function resize the video to a given resolution
    file = input("Write the file you want to resize(make sure that is in the same folder than the script): ")
    scale = input(
        "Write the resolution at which you want to resize the video.Write it in this format (height:weight): ")
    outname = input("Write the name of the scaled file without the extension: ")
    os.system("ffmpeg -i " + file + " -vf scale=" + scale + " " + outname + ".mp4")


def menu():
    inp = '5'
    while (inp != '0'):
        inp = input("This script computes different processes in the BBB video\n"
                    "Write a 1 for extracting data from mp4 container\n"
                    "Write a 2 for rename the 5 quality outputs\n"
                    "Write a 3 for resize the a video\n"
                    "Write a 4 for audio or video codec change\n"
                    "Write a 0 to finish de app\n"
                    "Option: ")
        if inp == '1':
            container_data()
        elif inp == '2':
            rename()
        elif inp == '3':
            resizevideo()
        elif inp == '4':
            change_codec()

    print("Application finished")


menu()
