# for any wikipedia
import wikipedia
# for voice data as input
import speech_recognition as sr
#time and date
from time import ctime
# for any web searches
import webbrowser
# for Holding the Voice assistant
import time
# for voice
import playsound
# fro removing voice
import os
# for random string value
import random
# actual google text to speech functon
from gtts import gTTS


r = sr.Recognizer()
# for hearing audio input


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        print('Listening...')
        audio = r.listen(source)
        voice_data = ''
        try:
            print('Recognizing...')
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            friday("please Can u say it properly")
        except sr.RequestError:
            friday("Sorry cant hear say it properly")
        return voice_data


def friday(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def respond(voice_data):
    # for something related to  name
    if 'what is your name' in voice_data or 'what are you' in voice_data:
        friday("Hey i'm Friday")

    # for getting time .
    if 'Friday what is the time' in voice_data or 'tell me time' in voice_data:
        friday(ctime())

    # for websearch
    if 'Friday search' in voice_data or 'can you search'in voice_data:
        friday('what do you want to search?')
        search = record_audio('')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        friday('Here what i have found for  '+search)

    # for searching location9
    if 'Friday find location' in voice_data or 'location' in voice_data or 'search location' in voice_data:
        friday('which location you want to search?')
        location = record_audio('')
        url = 'https://www.google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        friday('location found for  ' + location)
        
    # for any wiki
    if 'Friday wikipedia' in voice_data or 'wikipedia' in voice_data or 'find wiki' in voice_data:
        wiki = record_audio('')
        friday('searching wikipedia')
        vd = wiki.replace('wikipedia', '')
        re = wikipedia.summary(vd, sentences=2)
        friday('According to wikipedia')
        friday(re)

    # for quiting the program
        if 'friday exit' in voice_data or 'bye friday' in voice_data or 'stop' in voice_data:
            exit(0)


time.sleep(1)
friday('Hi, How can i help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)
