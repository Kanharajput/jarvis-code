import speech_recognition as sr
kanha=sr.Recognizer()
mic=sr.Microphone()
print("listening...")
with mic as source:
    print("listening...")
    audio=kanha.listen(source)
    print("recognizing....")
speak=kanha.recognize_google_cloud(audio)
print("kanha I love you ")
print(speak)

