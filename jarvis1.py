from subprocess import call
from pygame import *
import speech_recognition as sr
import datetime
import webbrowser as web
import wikipedia
import wolframalpha
import smtplib
import random

def wish():
    time=datetime.datetime.now().time()
    hour=time.hour

    if hour>=12 and hour<18:
         print("good afternoon sir")
         call(["espeak","-s140 -ven+18 -z","good afternoon sir"])
    elif hour>=6 and hour<12:
         print("good morning sir")
         call(["espeak","-s140 -ven+18 -z","good morning"])
    else:
        print("good night sir")
        call(["espeak","-s140 -ven+18 -z","good night sir"])


def special_command():
    global reply
    recog=sr.Recognizer()
    mic1=sr.Microphone()

    with mic1 as source:
        print("listning....")
        recog.adjust_for_ambient_noise(source,duration=1)
        audio=recog.listen(source)

    try:
        call(["espeak","-s140 -ven+18 -z","reconizing."])
        print("recognizing...")
        REPLY=recog.recognize_google(audio,language="en-IN")
        reply=REPLY.lower()
        print("you said:",reply)

    except Exception as e:
        return()

def command():
    global text
    rec=sr.Recognizer()
    mic=sr.Microphone()
    
    with mic as source:
        print("listening...")
        rec.adjust_for_ambient_noise(source,duration=1)
        audio=rec.listen(source)

    try:
        print("recognizing....")
        call(["espeak","-s140 -ven+18 -z","recognizing"])
        TEXT=rec.recognize_google(audio,language="en-IN")
        text=TEXT.lower()
        print("you said:",text)
        

    except Exception as e:
        print("sir please say that again.")
        call(["espeak","-s140 -ven+18 -z","sir please say that again"])
        return()
        

wish()
call(["espeak","-s140 -ven+18 -z","i am your jarvis sir,how can i help you"])
while True:
    command()

    if "open youtube" in text:
        text=""
        web.open("https://www.youtube.com")
        call(["espeak","-s140 -ven+18 -z","opening youtube,sir"])
        call(["espeak","-s140 -ven+18 -z","next command,sir"])


    elif "search" in text:
        text=""
        call(["espeak","-s140 -ven+18 -z","what i have to search sir"])
        special_command()
        site="https://www.google.com/search?source=hp&ei=0bAJXaG9O4W8rQG1mZxA&q="+reply
        web.open(site)
        reply=""
        call(["espeak","-s140 -ven+18 -z","here is it,sir"])
        call(["espeak","-s140 -ven+18 -z","now what my next task,sir"])


    elif "open facebook" in text:
        text=""
        web.open("https://www.facebook.com")
        call(["espeak","-s140 -ven+18 -z","opening facebook,sir"])
        call(["espeak","-s140 -ven+18 -z","next command,sir"])


    elif "open whatsapp" in text:
        text=""
        web.open("https://web.whatsapp.com")
        call(["espeak","-s140 -ven+18 -z","opening whatsapp,sir"])
        call(["espeak","-s140 -ven+18 -z","next command,sir"])


    elif "wikipedia" in text:
        text=""
        call(["espeak","-s140 -ven+18 -z","sir please say,what i have to search"])
        special_command()
        call(["espeak","-s140 -ven+18 -z","searching"])
        wiki=wikipedia.summary(reply,sentences=2)
        print("According to Wikipedia:",wiki)
        call(["espeak","-s140 -ven+18 -z","sir,wikipedia says that,"])
        call(["espeak","-s140 -ven+18 -z",wiki])
        reply=""
        call(["espeak","-s140 -ven+18 -z","next command,sir"])


    elif "tell me" in text:
        call(["espeak","-s140 -ven+18 -z","yes sir,what i have to search"])
        command()
        client=wolframalpha.Client("JXW3A3-EK792GWGXL")
        res=client.query(text)
        output=next(res.results).text
        print(output)
        call(["espeak","-s140 -ven -z",output])
        text=""
        call(["espeak","-s140 -ven+18 -z","next command,sir"])


    elif "email" in text:
        text=""
        while True:
            call(["espeak","-s140 -ven+18 -z","whom you want to send the mail?sir"])
            special_command()
            if "boss"==reply:
                reply=""
                call(["espeak","-s140 -ven+18 -z","what should i say"])
                special_command()
                content=reply
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.ehlo()
                server.starttls()
                server.login("kanharajput91@gmail.com","9926495946")
                server.sendmail("kanharajput91@gmail.com","kanharajput91@gmail.com",content)
                server.close()
                reply=""
                call(["espeak","-s140 -ven+18 -z","mubarak! email sent successfull"])
                call(["espeak","-s140 -ven+18 -z","next command,sir"])


            elif "no one"==reply:
                 call(["espeak","-s140 -ven+18 -z","what can i do for you sir other then sending a mail"])
                 reply=""
                 break


            else:
                reply=""
                call(["espeak","-s140 -ven+18 -z","please type the email adress ,sir"])
                email=str(input("email:")) 

                if email=="exit":
                    call(["espeak","-s140 -ven+18 -z","what can i do for you sir other then sending a mail"])
                    break

                else:
                    call(["espeak","-s140 -ven+18 -z","what should i say?sir"])
                    special_command()
                    content=reply
                    server=smtplib.SMTP("smtp.gmail.com",587)
                    server.ehlo()
                    server.starttls()
                    server.login("kanharajput91@gmail.com","9926495946")
                    server.sendmail("kanharajp[ut91@gmail.com",email,content)
                    server.close()
                    call(["espeak","-s140 -vven+18 -z","mubarak,email sent successfully!"])
                    reply=""



    elif "open gmail" in text:
        text=""
        call(["espeak","-s140 -ven+18 -z","opening gmail,sir"])
        web.open("https://www.gmail.com")
        call(["espeak","-s140 -ven+18 -z","next command,sir"])



    elif "play song" in text:
        text=""
        songs=["kanha.wav","pehli.wav","jogi.wav"]
        file=(random.choice(songs))
        mixer.init()
        mixer.music.load(file)
        call(["espeak","-s140 -ven+18 -z","okay sir,here is your music,enjoy!"])
        mixer.music.play()
        while mixer.music.get_busy:
            time.Clock().tick(10)


    elif  "stop" in text:
        call(["espeak","-s140 -ven+18 -z","okay sir, as you wish,bye-bye"])
        break


    elif "flow" in text: #to open stackoverflow site
        text=""
        call(["espeak","-s140 -ven18 -z","opening the stackoverflow site,sir"])
        web.open("https://stackoverflow.com")
        call(["espeak","-s140 -ven+18 -z","next command,sir"])





        









         
