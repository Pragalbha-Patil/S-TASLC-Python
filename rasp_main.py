import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import string
import wget
import paramiko
import time
from getpass import getpass
import platform

arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z',' ']
r = sr.Recognizer()

try:
    os.system("rm out.wav && clear || del out.wav && del output.wav && cls")
    ip = input("Enter the ip to recieve audio from: ")
    user_name = input("Enter username: ")
    # pass_word = input("Enter password: ")
    pass_word = getpass("Enter secure password: ")
    print("Connecting to host..")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user_name, password=pass_word)
    print("Connection succeeded..")
    time.sleep(2)
    client.exec_command('python -m http.server 8888 || python -m SimpleHTTPServer 8888')
    client.exec_command('del output.wav && del out.wav || rm out.wav')
    print("Please speak now..")
    client.exec_command('fmedia --record --dev-capture=1 -o output.wav || arecord -d 5 -f cd -t wav out.wav') # make sure fmedia is installed.
    time.sleep(6)
    client.exec_command('taskkill /IM fmedia.exe /F && ffmpeg -i output.wav out.wav') # This'll stop the recording, ONLY WINDOWS.
    time.sleep(3)
except:
    print("Something went wrong, please make sure the host is up.")
    quit()

url = 'http://192.168.0.100:8888/out.wav' # make sure you 've recorded and kept the audio 
print("Downloading...")
audio = wget.download(url)
if(audio):
	client.close()
else:
	audio = wget.download(url)
if audio.lower().endswith(('.pcm','.wav')):
    audio_file = sr.AudioFile(audio)
    with audio_file as source:
        audio_text = r.record(source)
    # print(type(audio_text))
    audio = r.recognize_google(audio_text)
    if(audio == 'goodbye'):
        print("Gotta go")
        quit()
    print("The transcribed audio is: "+audio)
    print()
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
    if(platform.system() == 'Windows'):
        os.system("python main.py")
    else:
        os.system("python3 main.py")
else:
    print("Wrong file, please record a wav file!")
