from Tkinter import *
import time
from PIL import ImageTk, Image
import Tkinter as tk
import os
import cam
import button2
import popup2
root = Tk()
def pop2():
    img = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/twitter/Finalfolder2/my_image.jpg"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    prompt = tk.Label(root, text="Do you want this image to be tweeted?", anchor="w")
    prompt.pack(side="top", fill="x")
    yes = tk.Button(root, text="Yes",command=on_closing)
    yes.pack(side="right")
    recap = tk.Button(root, text="Recapture the Image",command=fun)
    recap.pack(side="right")
    no = tk.Button(root, text="No, discard the image")
    no.pack(side="right")
    root.mainloop()
    
def on_closing():
    root.destroy()
    
def fun():
    time.sleep(7)
    cam.camera()
    popup2.pop2()
    root.destroy()