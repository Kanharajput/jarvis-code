from subprocess import call
import speech_recognition as sr
import datetime
import webbrowser as web


time=datetime.datetime.now().time()
hour=time.hour
if hour>=12 and hour<18:
    print("good afternoon sir")
    call(["espeak","-s140 -ven+18 -z","good afternoon sir"])

if hour>=18 and hour<6:
    print("good night sir")
    call(["espeak","-s140 -ven+18 -z","good night sir"])

if hour>=6 and hour<12:
    print("good morning sir")
    call(["espeak","-s140 -ven+18 -z","good morning"])

call(["espeak","-s140 -ven+18 -z"," here is jarvis , how can i help you."])


rec=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
    print("listening....")
    rec.pause_threshold=1 
    rec.energy_thresold=500
    audio=rec.listen(source)
try:
    print("recognizing....")
    TEXT=rec.recognize_google(audio)
    text=TEXT.lower()
    print("you said:",text)
except Exception as e:
    print("say that again please...")
     

 if text=="open youtube":
     call(["espeak","-s104 -ven+18 -z","opening sir"])
     url="https://www.youtube.com/"
     web.open(url)
     call(["espeak","-s140 -ven+18 -z","youtube home, enjoy sir "])
      
if text=="search":
     call(["espeak","-s140 -ven+18 -z","what i have to search,sir"])
     url="https://www.google.com/search?q="+text
     web.open(url)
     call(["espeak","-s140 -ven+18 -z","nice,choice sir"])

        
        
