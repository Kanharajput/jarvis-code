import speech_recognition as sr
import webbrowser as web
import pyaudio
r=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
           print("listning....")
           audio=r.listen(source)
           print("recognizing....")
rewa=r.recognize_google(audio)
print("user said-")
print(rewa)
url="https://www.google.com/search?q="+rewa
web.open(url)

