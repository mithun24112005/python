import os

# if __name__=="__main__":
#     print("welcome to robo speaker by mithun")
#     x=input("what do you want me to speak: ")
#     command=f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak({x});"'
    # os.system(command)

import win32com.client as wincom

import time

def speech(text):
    speak=wincom.Dispatch("SAPI.SpVoice")
    speak.speak(text)
    time.sleep(1)

if __name__=="__main__":
    while True:
        text=input("enter the text u want to say: ")
        speech(text)

