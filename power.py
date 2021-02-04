import speech_recognition as sr
kanha=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
    audiodata=kanha.listen(source)

text=kanha.recognize_google(audiodata)
print(text)
