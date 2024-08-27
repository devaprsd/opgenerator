import speech_recognition as sr
import tkinter as tk
from tkinter import PhotoImage
import serial 
import pyttsx3 
import time as t
import csv 
import concurrent.futures 
import pyautogui as px
global count
count=0
global final_entry
global name_entry
global age_entry
global gender_entry
name_entry=None
age_entry=None
gender_entry=None
final_entry=None
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice','english')
line=None
#communi = serial.Serial("/dev/ttyUSB0", 9600, timeout = 1.0)
t.sleep(3)
def gui():
    def speak_text(text):
        engine.say(text)
        engine.runAndWait()
    def collect_data():
        print("Serial OK")
        line=None
        try:
            communi = serial.Serial("/dev/ttyUSB0", 9600, timeout = 1.0)
            t.sleep(3)
            line = communi.readline().decode("utf-8")
            px.alert(line)
            final_entry.delete(1.0, tk.END) 
            final_entry.insert(tk.END,line)
            communi.reset_output_buffer()
        except KeyboardInterrupt:
            print("closing serial communication")
            communi.close()
    def recognize_speech():
        with sr.Microphone() as source:
            # Clear the Text widget
            while True:
                try:
                    speak_text("listening")
                    audio = recognizer.record(source,duration=4)
                    speak_text("Finished Recording")  # Clear the "Listening..." message
                    recognized_text = recognizer.recognize_google(audio)
                    if recognized_text != None:
                        break
                except sr.UnknownValueError:
                    return "Values not found"
                    speak_text("Google Web Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    return "Values not found"
                    speak_text("Could not request results from Google Web Speech Recognition service")

    def submit_form():
        name = name_entry.get("1.0", "end-1c")  # Get the text from the Text widget
        age = age_entry.get("1.0", "end-1c")
        gender = gender_entry.get("1.0", "end-1c")
        fina=final_entry.get("1.0","end-1c")
        global count
        try:
            with open('data.csv', 'r', newline='') as input_file:
                reader = csv.reader(input_file)
                for row in reader:
                    last_row = row[0]
                print(last_row)
            count=int(last_row)
        except FileNotFoundError:
            count=0
        count=count+1
        with open("data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([count,name,age,gender,fina])
        
        with open("file.txt",'w') as f:
            f.write("\n\n\n\n\n\n\n\n\nOP NO:"+str(count)+"\n"+"Name :"+str(name)+"\n"+"Age :"+str(age)+"\n"+"Gender :"+str(gender)+"\n"+"Recorded Data"+str(fina))
            # You can perform actions with the form data here
        print("Name:", name)
        print("Age:", age)
        print("Gender:", gender)
        print("The values taken by liya:",fina)
        name_entry.delete(1.0, tk.END)
        age_entry.delete(1.0, tk.END)
        gender_entry.delete(1.0, tk.END)
        final_entry.delete(1.0, pulstk.END)
        #root.destroy()
        # Create the main application window
    def liyadrive():
        x="try"
        t.sleep(1)
        speak_text('please say your name')
        x=recognize_speech()
        name_entry.delete(1.0, tk.END)
        name_entry.insert(tk.END, x)
        speak_text("your name is"+x)
        t.sleep(1)
        speak_text('please say your age')
        x=recognize_speech()
        age_entry.delete(1.0, tk.END)
        age_entry.insert(tk.END, x)
        speak_text("your age is"+x)
        t.sleep(1)
        speak_text('please say your Gender')    
        x=recognize_speech()
        if  x in 'mail':
                x="male"
                
        else:
            x=x
        gender_entry.delete(1.0, tk.END)
        gender_entry.insert(tk.END, x)
        speak_text("your gender is"+x)
    root = tk.Tk()
    root.title("Sample Form")
    # Maximize the window (works on Linux)
    root.attributes('-zoomed', True)

    # Load and display a custom background image
    background_image = PhotoImage(file="background.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Create and display form elements
    name_label = tk.Label(root, text="Name:", font=("Arial", 20))
    name_label.pack(padx=10, pady=10)
    name_entry = tk.Text(root, height=1, width=40,font=("Arial", 15))
    name_entry.pack(padx=10, pady=10)

    age_label = tk.Label(root, text="Age:", font=("Arial", 20))
    age_label.pack(padx=10, pady=10)

    age_entry = tk.Text(root, height=1, width=40,font=("Arial", 15))
    age_entry.pack(padx=10, pady=10)

    gender_label = tk.Label(root, text="Gender:", font=("Arial", 20))
    gender_label.pack(padx=10, pady=10)

    gender_entry = tk.Text(root, height=1, width=40,font=("Arial",15))
    gender_entry.pack(padx=10, pady=10)

    final_label = tk.Label(root, text="Final result are", font=("Arial", 20))
    final_label.pack(padx=10, pady=10)

    final_entry = tk.Text(root, height=1, width=40,font=("Arial", 15))
    final_entry.pack(padx=10, pady=10)
    rec_button = tk.Button(root, text="Start Registration", command=lambda: liyadrive(), font=("Arial", 30))
    rec_button.pack(padx=40, pady=40)

    collect_data_button = tk.Button(root, text="Generate Result", command=lambda: collect_data() ,font=("Arial", 30))
    collect_data_button.pack(padx=40,pady=40)

    submit_button = tk.Button(root, text="Submit", command=lambda: submit_form(), font=("Arial", 30))
    submit_button.pack(padx=40, pady=40)

    #exit_button =tk.Button(root, text="X", command=root.destroy, font=("Arial", 25))
    #exit_button.pack(padx=30, pady=30)
    # Start the main event loop
    root.mainloop()
gui()
