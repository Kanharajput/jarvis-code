import subprocess
def rewa(text,lang="en"):
       subprocess.call("espeak-ven{0}{1}".format(lang,text),shell=True)






rewa("hello")
