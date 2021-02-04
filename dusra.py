from subprocess import call
text="we are doing good,sir"
call(["espeak","-s140 -ven+18 -z",text])

