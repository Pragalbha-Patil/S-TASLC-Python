from threading import Thread
# import pygame
# import speake3
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
import platform

def play_music():
    os.system("gnome-terminal -e 'play bg.mp3'")


#import selecting for recorded voice

# obtain audio from the microphone
def func():
        r = sr.Recognizer()
        taslc_gif=['','']
        
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z',' ']
        with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source) 
                i=0
                # thread = Thread(target = play_music)
                # thread.start()
                # thread.join()
                while True:
                        print('Listening...')
                        audio = r.listen(source)

                                                        # recognize speech using Sphinx
                        try:
                                a=r.recognize_google(audio)
                                # mixer.init()
                                # mixer.music.load("bg.mp3")
                                # mixer.music.play()
                                print("You said:  " + a.lower())
                                
                                for c in string.punctuation:
                                    a = a.replace(c,"")
                                    
                                if(a.lower()=='goodbye'):
                                        print("Good bye!")
                                        break
                                
                                elif(a.lower() in taslc_gif):
                                    
                                    class ImageLabel(tk.Label):
                                            """a label that displays images, and plays them if they are gifs"""
                                            def load(self, im):
                                                if isinstance(im, str):
                                                    im = Image.open(im)
                                                self.loc = 0
                                                self.frames = []

                                                try:
                                                    for i in count(1):
                                                        self.frames.append(ImageTk.PhotoImage(im.copy()))
                                                        im.seek(i)
                                                except EOFError:
                                                    pass

                                                try:
                                                    self.delay = im.info['duration']
                                                except:
                                                    self.delay = 100

                                                if len(self.frames) == 1:
                                                    self.config(image=self.frames[0])
                                                else:
                                                    self.next_frame()

                                            def unload(self):
                                                self.config(image=None)
                                                self.frames = None

                                            def next_frame(self):
                                                if self.frames:
                                                    self.loc += 1
                                                    self.loc %= len(self.frames)
                                                    self.config(image=self.frames[self.loc])
                                                    self.after(self.delay, self.next_frame)

                                    root = tk.Tk()
                                    lbl = ImageLabel(root)
                                    lbl.pack()
                                    lbl.load(r'/home/psp/Desktop/projects/TASLC/TASLC_Gifs/{0}.gif'.format(a.lower()))
                                    root.mainloop()
                                else:
                                    # os.system("espeak "+a)
                                    # print(a)
                                    # print(len(a))
                                    # break
                                    for i in range(len(a)):
                                                    #a[i]=a[i].lower()
                                                    if(a[i] in arr):
                                                            # print(a[i])
                                                            if(a[i] == ' '):   
                                                                ImageAddress = 'letters_asl/ .jpg'
                                                                ImageItself = Image.open(ImageAddress)
                                                                ImageNumpyFormat = np.asarray(ImageItself)
                                                                plt.imshow(ImageNumpyFormat)
                                                                plt.draw()
                                                                plt.pause(0.8) # pause how many seconds
                                                                #plt.close()
                                                            else:
                                                                ImageAddress = 'letters_asl/'+a[i]+'.jpg'
                                                                ImageItself = Image.open(ImageAddress)
                                                                ImageNumpyFormat = np.asarray(ImageItself)
                                                                plt.imshow(ImageNumpyFormat)
                                                                plt.draw()
                                                                plt.pause(0.8) # pause how many seconds
                                                                #plt.close()
                                                    else:
                                                            continue

                        except:
                               print("Could not listen probably audio is too low to listen")
                        plt.close()
#func()
while 1:
  image   = "logo.jpg"
  msg="S - TASLC - Speech to American Sign Language Converter"
  choices = ["Live Conversation mode","Close","Convert Recorded Voice", "Raspberry pi mode"]
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
  if reply==choices[2]:
        if(platform.system() == 'Windows'):
            os.system("python recorded.py")
        else:
            os.system("python3 recorded.py")
        break
  if reply==choices[3]:
      if(platform.system() == 'Windows'):  
        os.system("python rasp_main.py")
      else:
          os.system("python3 rasp_main.py")
      quit()