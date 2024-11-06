# .............AI Voice Assistant V1.5.............

#New features Added !


# Additional Libraries used --> 
#                - pyttsx3
#                - Speech Recognition
#                - datetime

# Contact { 
            #instagram : _.abh.i_.x
            #gmail : abhinavsanthosh3699@gmail.com

# ! The Code Is In Initional Stage .....
                # Future updates Soon >> :)import pyttsx3

import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing....")
        queri = r.recognize_google(audio,language = "en-in")
        print(f"You Said : {queri}")

    except Exception as e:
        return "None"
    
    return queri

current_time = datetime.datetime.now()
hour = current_time.hour
min = current_time.minute
final_time = (hour, min)
query = command().lower()

def googleSearch(query):
    
    query = query.replace("google","")
    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query,1)

        speak(result)


    except :
        speak("No speakable output found ")


if __name__ == "__main__":
    if hour>=0 and hour<12 :
        speak(f"Good morning sir, its {final_time}A,M, how can i assist you")

    elif hour>=12 and hour<16:
        speak(f"Good afternoon sir, its {final_time}P,M, how can i asist you")

    elif hour>=16 and hour<18:
        speak(f"Good evening sir, its {final_time}P,M, how can i assist you")

    else :
        speak(f"Welcome back sir, its {final_time}P,M, how can i assist you")

    while True:
        query = command().lower()
        if "how are you" in query:
            speak("i am fine sir, how are you")

        elif "i am fine" in query:
            speak("great, glad to hear that")

        elif "google" in query:
            googleSearch(query)


        elif "go to sleep" in query:
            speak("i hope it helped ")
            break

        elif "exit" in query:
            speak("i hope it helped ")
            break





