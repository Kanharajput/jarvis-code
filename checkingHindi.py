import pyttsx3
a = pyttsx3.init()
#If this doesn't work try "languages".
a.setProperty("language",'hi')
a.setProperty('rate',50)
a.say(" हाय्य दय्या")
a.setProperty('rate',80)
a.say("हम ये नहीं कर सकते पर मालिक की बात को कौन ताल सकता है|")
a.runAndWait()