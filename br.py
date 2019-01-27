from gtts import gTTS
import speech_recognition as sr
#import SpeechRecognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import engineio
#from weather import Weather
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
def talkToMe(audio):
    "speaks audio passed as argument"
    
    for line in audio.splitlines():
        #os.system("say " + audio)
        #engine.say(audio)
        #engine.runAndWait()
        speak.Speak(audio)
        print(audio)
    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    "if statements for executing commands"
    if 'hello' in command:
        talkToMe('hello')
        print("working")

    elif 'barry search for' in command:
        reg_ex = re.search('barry search for (.*)', command)
        query = reg_ex.group(1)
        talkToMe("searched google for " + query + "")
        talkToMe("oh ooh oh")

        url = 'https://www.google.com/search?q='+ query +'&rlz=1C1CHBF_enUS797US797&oq='+ query +'&aqs=chrome..69i64j0l5.4624j0j1&sourceid=chrome&ie=UTF-8'
        webbrowser.open(url)
    elif 'barry open r /' in command:
        reg_ex = re.search('barry open r / (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit.replace(" ", "")
        webbrowser.open(url)
        talkToMe("Opening r/" + " " + subreddit + " owo")
        print('Done!')
        talkToMe("oh ooh oh")

    
    elif 'barry what\'s up' in command:
        talkToMe('lmao screw off pleb')
    elif 'barry tell me a joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

talkToMe('Hello! Im berry! and I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
