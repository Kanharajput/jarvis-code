import speech_recognition as sr
good=sr.Recognizer()
mic=sr.Microphone()
 
with mic as source:

    rewa.adjust_for_ambient_noise(source,duration=1)
    audio=good.listen(source)

text=good.recognize_google(audio)
print(text)


