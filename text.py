import speech_recognition as sr
rewa=sr.Recognizer()
audio=sr.AudioFile("/home/kanha/Downloads/river.wav")
with audio as source:
    kanha=rewa.record(source)
laddu=rewa.recognize_google(kanha)
print("text is- ",laddu)

