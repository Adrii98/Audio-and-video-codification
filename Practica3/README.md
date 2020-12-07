## SCAV-Video-P3
This script is made for de Lab3 of the Audio and Video codification Systems subject of the Audiovisual Systems Engineering in Pompeu Fabra University

## Script
In the script there is a class container where all methods needed for the execution of the lab are.  
In the container class there are the following methods:    
-cut_video(): In this method the bbb video is cutted into one minute video.    
-get_mono_lowbitrate_audios(): Rename a given file.    
-create_container(): This function changes the audio codec and video codec of a video provided by the user.    
-track_reading(): This method given a container indicates what the broadcasting standard supports it. To do this, both the audio codec and the video codec from the container are extracted and it is verified that the standards support those codecs.  
Outside the class there is the testing method(). This method is done for test the correct operation of the functions.  

## Requisites
To execute this code it is necessary to have a version of ffmpeg and python 3. On the other hand, 
it is also necessary to have the BBB (Big Buck Bunny) video in mp4 format.
