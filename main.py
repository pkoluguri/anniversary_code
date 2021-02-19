from os import system
try: 
 from gtts import gTTS
except ModuleNotFoundError:
   system("pip3 install gtts")
   from gtts import gTTS
try:
 from googletrans import Translator
except ModuleNotFoundError:
   system("pip3 install googletrans==3.1.0a0")
   from googletrans import Translator
try:
 import pyttsx3
except:
 system("pip3 install pyttsx3")
 import pyttsx3

engine = pyttsx3.init()
i=0
system('clear')
print("\t\t\t        Congratulations     ")
engine.say("Congratulations")
engine.runAndWait()
print("\t\t\t            on              ")
engine.say("on")
engine.runAndWait()
print("\t\t\t            26              ")
engine.say("twenty six")
engine.runAndWait()
print("\t\t\t           years             ")
engine.say("years")
engine.runAndWait()
print("\t\t\t            of               ")
engine.say("of")
engine.runAndWait()
print("\t\t\t         togetherness ;)            ")
engine.say("togetherness")
engine.runAndWait()

languages = ['feliz aniversario','記念日おめでとう','frohes Jubiläum','இனிய திருமண நாள் வாழ்த்துக்கள்','వార్షికోత్సవ శుభాకాంక్షలు','χαρούμενη επέτειος','ವಾರ್ಷಿಕೋತ್ಸವದ ಶುಭಾಷಯಗಳು','joyeux anniversaire','शादी की सालगिरह मुबारक','Happy anniversary']
for lang in languages:
    print("\t\t\t\t",lang) 
    go = gTTS(lang)
    t = str(i)+'.mp3'
    go.save(t)
    system(f"afplay {t}")
    i+=1
