import speech_recognition as sr
import pyttsx3
import pyautogui as px
import webbrowser as w
import time as t
import subprocess
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice','english')
names = []
ages = []
op_number = 1
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    while True:
        with sr.Microphone() as source:
            try:
                speak_text("listening")
                recognizer.adjust_for_ambient_noise(source) 
                audiox = recognizer.record(source, duration = 3)
                print("finished recording")
                #audio = recognizer.listen(source)
                text = recognizer.recognize_google(audiox)
                lower1 = text.lower()
                if lower1!=None:
                    return lower1
                    break
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand your speech.")

while True:
    w.open("http://127.0.0.1:5000")
    t.sleep(3)
    px.press('tab')
    speak_text('please say your name')
    x=recognize_speech()
    px.typewrite(x)
    speak_text("your name is"+x)
    t.sleep(2)
    px.press('tab')
    speak_text('please say your age')
    x=recognize_speech()
    px.typewrite(x)
    speak_text("your age is"+x)
    t.sleep(2)
    px.press('tab') 
    speak_text('please say your Gender')    
    x=recognize_speech()
    if x in 'mail':
        x='male'
        px.typewrite(x)
    else:
         px.typewrite(x)
    speak_text("your gender is"+x)
    t.sleep(2)
    px.press('tab')
    t.sleep(2)
    px.press("enter")
    t.sleep(2)
    px.keyDown('alt')
    px.press('f4')
    px.keyUp('alt')
    x=px.confirm('Print the entry ', buttons =['Yes', 'No'])
    if x=='Yes':
        subprocess.run(["lp", "/home/liya/liya/file.txt"], capture_output=False)
    x=px.confirm('Enter another entry ', buttons =['Yes', 'No'])
    if x=='No':
        break 
    