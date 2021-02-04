import speech_recognition as kanha
rewa=kanha.Recognizer()
mic=kanha.Microphone()
while True:

     with mic as source:
        rewa.adjust_for_ambient_noise(source,duration=1)
        audio=rewa.listen(source)
        laddu=rewa.recognize_google(audio)
        print("kanha said",laddu)
