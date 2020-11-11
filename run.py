import os
from PIL import Image
from moviepy.editor import ImageClip
from moviepy.editor import * 
import moviepy.video.io.ImageSequenceClip
from PIL import ImageFont
from PIL import ImageDraw 
import moviepy.editor as mp

image_folder ="img/"
output_folder = "output/"

def videoProgress():
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")] #get all images if have .jpg extension

    for i in images:
        image = Image.open(image_folder+i)                                     #image_folder is path which has input folder and i has image name
        draw = ImageDraw.Draw(image)                                           
        font = ImageFont.truetype("Roboto-Regular.ttf", 72)
        draw.text((50, 600),"Hello World",(255,255,255),font=font)          #x y position - 0000 000 00 00 is text, 255 255 255 rgb color
        print(i)                                                               #just check from the console
        new_image = image.resize((1920, 1080))                                 # concatenate_videoclips need to same image sizes
        new_image.save(output_folder+i)

    output = [img for img in os.listdir(output_folder) if img.endswith(".jpg")] #get all output from output folder
    clips = [ImageClip(output_folder+m).set_duration(2)                         #add duration all of them
        for m in output]

    concat_clip = concatenate_videoclips(clips, method="compose")               
    concat_clip.write_videofile("test.mp4", fps=24)                             

videoProgress()                                                                 #call method.

def addLogo():
    video = mp.VideoFileClip("test.mp4")                                        #videoprogress output "test.mp4". 

    logo = (mp.ImageClip("logo.png")                                            #logo name in the folder
            .set_duration(video.duration)
            .resize(height=400)                                                 # if you need to resize...              
            .margin(right=8, top=8, opacity=0)                                  # (optional) logo-border padding
            .set_pos(("right","top")))                                          #position

    final = mp.CompositeVideoClip([video, logo])            
    final.write_videofile("test1.mp4")

addLogo()