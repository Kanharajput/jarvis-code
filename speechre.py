import speech_recognition as sr
r=sr.Recognizer()
audio=sr.AudioFile('/home/kanha/Downloads/river.wav')  
with audio as source:
         audioData=r.record(source)
type(audioData)
text=r.recognize_google(audioData)
print(text)
