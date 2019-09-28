from tkinter.filedialog import askopenfilename
import librosa
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import string

arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z',' ']
r = sr.Recognizer()

file = askopenfilename()
print(file)
if file.lower().endswith(('.pcm','.wav')):
    audio_file = sr.AudioFile(file)
    with audio_file as source:
        audio_text = r.record(source)
    # print(type(audio_text))
    audio = r.recognize_google(audio_text)
    print("The transcribed audio is: "+audio)
    print("Now converting to Sign language...")
    for i in range(len(audio)):
                                                    #a[i]=a[i].lower()
                                                    if(audio[i] in arr):
                                                            # print(a[i])
                                                            if(audio[i] == ' '):   
                                                                ImageAddress = 'letters_asl/ .jpg'
                                                                ImageItself = Image.open(ImageAddress)
                                                                ImageNumpyFormat = np.asarray(ImageItself)
                                                                plt.imshow(ImageNumpyFormat)
                                                                plt.draw()
                                                                plt.pause(0.8) # pause how many seconds
                                                                #plt.close()
                                                            else:
                                                                ImageAddress = 'letters_asl/'+audio[i]+'.jpg'
                                                                ImageItself = Image.open(ImageAddress)
                                                                ImageNumpyFormat = np.asarray(ImageItself)
                                                                plt.imshow(ImageNumpyFormat)
                                                                plt.draw()
                                                                plt.pause(0.8) # pause how many seconds
                                                                #plt.close()
                                                    else:
                                                            continue
    plt.close()
    print("Task completed, calling main program..")
    os.system("python3 main.py")
else:
    print("Wrong file, please choose a mp3 or wav file!")
