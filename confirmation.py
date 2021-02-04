import speech_recognition as sr
rewa=sr.Recognizer()
mic=sr.Microphone()
 
with mic as source:

    rewa.adjust_for_ambient_noise(source,duration=1)
    audio=rewa.listen(source)

text=rewa.recognize_google(audio)
print(text)


