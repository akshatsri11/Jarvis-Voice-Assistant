import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    engine.setProperty('rate', 170)     # setting up new voice rate
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('listening...')
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source)
        audio =r.listen(source, 10, 6)

    try:
        print('recognizing...')
        eel.DisplayMessage('recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}")
        
    
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommand():

    query = takeCommand()

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    
    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        print("not run")

    eel.ShowHood()