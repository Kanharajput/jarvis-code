import speech_recognition as sr
import pyaudio
r=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
           audio=r.listen(source)
rewa=r.recognize_google(audio)
print("kanha said-")
print(rewa)

