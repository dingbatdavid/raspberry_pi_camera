# My Camera Pi App
# Version 1.5
# Changes since version 1.1: Preview on/off option added, app now starts with preview window off and
# initial preview window starts at 640x480
# Created By David Peck
# Some of the code has been modified from various web sources
# Created Jan-2021
# App for using V1, V2 and HQ versions of raspberry Pi Camera
# File Name: camera-pi.py

from guizero import App, PushButton, Slider, Text, Combo
import colorsys
import picamera
import time
import datetime
from time import sleep

# Initialise Camera
camera = picamera.PiCamera()
win_size = (500, 40, 640, 480)
x = 0 # set zoom to zero
y = 0 # set zoom to zero
video = (1920, 1088)
photo = (2592, 1944)
framerate = 30
rotate = 0
effect_value = "none"
camera.exposure_mode = "auto"
camera.awb_mode = "auto"
camera.rotation = rotate
camera.resolution = photo
camera.zoom = (x, x, y, y)
camera.image_effect = effect_value

# Turn Preview On and update text and buttons
def preview_on():
    global window
    global win_size
    preview_ontxt.bg="lightgreen"
    preview_offtxt.bg="lightgrey"
    camera.start_preview(fullscreen=False, window = (win_size))
    current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")

# Turn Preview Off and update text and buttons
def preview_off():
    camera.stop_preview()
    preview_ontxt.bg="lightgrey"
    preview_offtxt.bg="pink"
    current_size = Text(app, text=("OFF"), width=12, color="red", grid=[6,3], align="right")

# Set selected Preview window size
def preview_size():
    global window
    global win_size
    
    if preview_set.value =="640x480":
        win_size = (500, 50, 640, 480)
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
    
    if preview_set.value =="720x576":
        win_size = (500, 40, 720, 576)
        camera.start_preview(fullscreen=False, window = (win_size))       
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
        
    if preview_set.value =="720x480":
        win_size = (490, 60, 720, 480)
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
    
    if preview_set.value =="1280x720":
        win_size = (300,40, 1280, 720)
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
    
# Set camera image rotation            
def camera_rotation():
    camera.rotation = rotation_set.value
    current_rotation = Text(app, text=str(camera.rotation), width=10, color="red",grid=[3,8], align="left")
    
# Define Zoom Settings
def zoom_set():
        
    if set_zoom.value == "Zoom-0":
        x = 0
        y = 0
        camera.zoom = (x, x, y, y)
        current_zoom = Text(app, text="Zoom-0", width=10, color="red", grid=[2,8], align="left")
    
    if set_zoom.value == "Zoom-1":
        x = 0.25
        y = 0.5
        camera.zoom = (x, x, y, y)
        current_zoom = Text(app, text="Zoom-1", width=10, color="red", grid=[2,8], align="left")
       
    if set_zoom.value == "Zoom-2":
        x = 0.5
        y = 0.25
        camera.zoom = (x, x, y, y)
        current_zoom = Text(app, text="Zoom-2", width=10, color="red", grid=[2,8], align="left")

# Set various Image effects
def set_effects():    
    global effect_value
    
    effect_value = str(effect_set.value)
    camera.image_effect = effect_value
    current_effect = Text(app, text=(camera.image_effect), width=10, color="red", grid=[4,8], align="left")

# Set Exposure mode
def set_exposure():
    exposure_value = str(exposure_set.value)
    camera.exposure_mode = exposure_value
    current_exposure = Text(app, text=(camera.exposure_mode), width=10, color="red", grid=[6,8], align="left")

# Set white balance
def set_awb():
    awb_value = str(awb_set.value)
    camera.awb_mode = awb_value
    current_awb = Text(app, text=(camera.awb_mode), width=10, color="red", grid=[7,8], align="left")

# Define Camera Recording Resolution 
def record_res():
    global photo
    global video
    global window
    global winsize
    
    if res_record.value =="V1-photo":
        photo = (2592, 1944)
        camera.resolution= photo
        photores_txt = Text(app, text=str(camera.resolution),width=10, color="red", grid=[1,2], align="left") 
        camera_type_txt = Text(app, text=" V1-Camera", color="red", grid=[1,3], align="left")
        preview_ontxt.bg="lightgreen"
        preview_offtxt.bg="lightgrey"
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
    
    if res_record.value =="V2-photo":
        photo = (3280,2464)
        camera.resolution= photo
        photores_txt = Text(app, text=str(camera.resolution), width=10, color="red", grid=[1,2], align="left") 
        camera_type_txt = Text(app, text=" V2-Camera", color="red", grid=[1,3], align="left")
        preview_ontxt.bg="lightgreen"
        preview_offtxt.bg="lightgrey"
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
    
    if res_record.value == "HQ-photo":
        photo = (4056, 3040)
        camera.resolution= photo
        photores_txt = Text(app, text=str(camera.resolution), width=10, color="red", grid=[1,2], align="left") 
        camera_type_txt = Text(app, text=" HQ-Camera", color="red", grid=[1,3], align="left")
        preview_ontxt.bg="lightgreen"
        preview_offtxt.bg="lightgrey"
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
        
    if res_record.value =="1080p":
        video = (1920, 1080)
        framerate = 30
        camera.resolution = video
        vidres_txt = Text(app, text= str(camera.resolution), width=10,  color="red", grid=[2,2], align="left")
        vidframe_txt = Text(app, text=str(framerate) + " fps", width=10, color="red", grid=[2,3], align="left")
        preview_ontxt.bg="lightgreen"
        preview_offtxt.bg="lightgrey"
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
        
    
    if res_record.value =="720p":
        video = (1280, 720)
        camera.resolution = video
        framerate = 60
        vidres_txt = Text(app, text=str(camera.resolution), width=10, color="red", grid=[2,2], align="left")
        vidframe_txt = Text(app, text=str(framerate) + " fps", width=10, color="red", grid=[2,3], align="left")
        preview_ontxt.bg="lightgreen"
        preview_offtxt.bg="lightgrey"
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
        
    
    if res_record.value =="576p":
        video = (720, 576)
        camera.resolution = video
        framerate = 25
        vidres_txt = Text(app, text=str(camera.resolution), width=10, color="red", grid=[2,2], align="left")
        vidframe_txt = Text(app, text=str(framerate) + " fps", width=10, color="red", grid=[2,3], align="left")
        preview_ontxt.bg="lightgreen"
        preview_offtxt.bg="lightgrey"
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
       
    
    if res_record.value =="480p":
        video = (720, 480)
        camera.resolution = video
        framerate = 60
        vidres_txt = Text(app, text=str(camera.resolution), width=10, color="red", grid=[2,2], align="left")
        vidframe_txt = Text(app, text=str(framerate) + " fps", width=10, color="red", grid=[2,3], align="left")
        preview_ontxt.bg="lightgreen"
        preview_offtxt.bg="lightgrey"
        camera.start_preview(fullscreen=False, window = (win_size))
        current_size = Text(app, text=str(win_size[2:]), width=12, color="red", grid=[6,3], align="right")
     
    current_res = Text(app, text=str(camera.resolution), width=10, color="red", grid=[1,8], align="left") 

# Record Video
def video_record():
    global video
    camera.resolution = video
    camera.framerate = framerate
    vid_record.text="Recording   "
    vid_record.bg="pink"
    vid_record.text_color="red"
    record_stop.text_color="red"
    record_stop.text="press to Stop"
    date = datetime.datetime.now().strftime('%d-%m-%Y_%H.%M.%S')
    camera.start_recording('/home/pi/Videos/video_' + date + '.h264') 
    
# Stop Video Record    
def record_stop():
    vid_record.text="Video Record"
    vid_record.text_color="black"
    vid_record.bg="lightblue"
    record_stop.text_color="black"
    record_stop.text="Record Stop"
    camera.stop_recording()
  
# Capture Image (Take Photo)    
def image_capture():
    camera.resolution=photo
    date = datetime.datetime.now().strftime('%d-%m-%Y_%H.%M.%S')
    camera.capture('/home/pi/Pictures/image_' + date + '.jpg') 

# Exit Program    
def exit_program():
    quit()


# GUI Setings
app = App(bg ="lightgrey",  title="Raspberry Pi Camera V1.5", width=850,  height=270, layout="grid")

pad_txt = Text(app, text="      ", grid=[0,0], align="left")

options_txt = Text(app, text=" Options ", color="blue", grid=[0,1], align="left")

pic_capture = PushButton(app, command=image_capture, text="Take Photo", width=10, grid=[1,1], align="left") # capture image
pic_capture.bg="lightblue"

photores_txt = Text(app, text="  2592x1944", color="green", width=10, grid=[1,2], align="left") # displays image resolution

camera_type_txt = Text(app, text=" V1-Camera", color="green", width=10, grid=[1,3], align="left")

vid_record = PushButton(app, command=video_record, text="Video Record", width=10, grid=[2,1], align="left") # starts video recording
vid_record.text_color="black"
vid_record.bg="lightblue"

vidres_txt = Text(app, text="   1920x1080", width=10, color="green", grid=[2,2], align="left")
vidframe_txt = Text(app, text="      " + str(framerate) + " fps", width=10, color="green", grid=[2,3], align="left")

record_stop = PushButton(app, command=record_stop, text="Record Stop", width=10, grid=[3,1], align="left") # stop video recording
record_stop.bg="lightblue"

recordstop_txt = Text(app, text="                ", width=10, grid=[3,7], align="left")

preview_txt = Text(app, text="Preview On/Off", color="blue", grid=[4,1], align="bottom")
preview_ontxt = PushButton(app, command=preview_on, width=4, text="On", grid=[4,2], align="right")
preview_ontxt = PushButton(app, command=preview_on, width=4, text="On", grid=[4,2], align="right")
preview_ontxt.text_color="blue"

preview_offtxt = PushButton(app, command=preview_off, width=4, text="Off", grid=[4,2], align="left")
preview_offtxt.text_color="blue"
preview_offtxt.bg="pink"

pad_txt = Text(app, text="       ", grid=[0,5], align="left")

preview_txt = Text(app, text="Preview", width=10, color="blue", grid=[1,6], align="left")

res_record= Combo(app, command=record_res, options=["V1-photo", "V2-photo", "HQ-photo", "1080p", "720p", "576p", "480p"], width=6, grid=[1,7], align="left") # sets video resolution
res_record.text_color="blue"
current_res = Text(app, text="2592x1944", width=10, color="green", grid=[1,8], align="left")

zoom_txt = Text(app, text="Zoom", width=10, color="blue", grid=[2,6], align="left")
set_zoom = Combo(app, command=zoom_set, options=["Zoom-0", "Zoom-1", "Zoom-2"], width=6, grid=[2,7], align="left") # sets zoom level
set_zoom.text_color="blue"
current_zoom = Text(app, text="Zoom-0", color="green", width=10, grid=[2,8], align="left")

rotate_txt = Text(app, text="Rotation  ", color="blue", width=10, grid=[3,6], align="left")
rotation_set = Combo(app, command=camera_rotation, options=["0", "90", "180"], width=6, grid=[3,7], align="left")
rotation_set.text_color="blue"
current_rotation = Text(app, text=str(camera.rotation), width=10, color="green",grid=[3,8], align="left")

effects_txt = Text(app, text="Effects", width=12, color="blue", grid=[4,6], align="left")
effect_set = Combo(app, command=set_effects, options=["none", "negative", "solarize", "sketch", "denoise", "emboss", "oilpaint", "hatch", "gpen", "pastel", "watercolor", "film", "blur", "saturation", "colorswap", "washedout", "posterise", "colorpoint", "cartoon", "deinterlace1", "deinterlace2"], width=10, grid=[4,7], align="left")
effect_set.text_color="blue"
current_effect = Text(app, text=str(camera.image_effect), width=10, color="green", grid=[4,8], align="left")

exposure_txt = Text(app, text="Exposure",  width=10, grid=[6,6], align="left")
exposure_txt.text_color="blue"
exposure_set = Combo(app, command=set_exposure, options=["auto", "off", "night", "nightpreview", "backlight", "spotlight", "sports", "snow", "beach", "verylong", "fixedfps", "antishake", "fireworks"], width=10, grid=[6,7], align="left")
exposure_set.text_color="blue"
current_exposure = Text(app, text=str(camera.exposure_mode), width=10, color="green", grid=[6,8], align="left")
                        
awb_txt = Text(app, text="AWB", width=10, grid=[7,6], align="left")
awb_txt.text_color="blue"
awb_set = Combo(app, command=set_awb, options=["auto", "off", "sunlight", "cloudy", "shade", "tungsten", "fluorescent", "incandescent", "flash", "horizon"], width=10, grid=[7,7], align="left")
awb_set.text_color="blue"
current_awb = Text(app, text=(camera.awb_mode), width=10, color="green", grid=[7,8], align="left")

Preview_wintxt = Text(app, text="  Preview Size", width=12, color="blue", grid=[6,1], align="bottom")
preview_set = Combo(app, command=preview_size, options=["640x480", "720x480", "720x576", "1280x720"], width=8, grid=[6,2], align="right")
preview_set.text_color="blue"
current_size = Text(app, text=("OFF"), width=12, color="green", grid=[6,3], align="right")

exit_prog = PushButton(app, command=exit_program, text="Quit Program", width=10, grid=[7,1], align="left")
exit_prog.text_color="blue"
exit_prog.bg="pink"


app.display()