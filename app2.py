import speech_recognition as sr
from time import ctime
import webbrowser


r = sr.Recognizer ()
#for hearing audio input
def record_audio(ask = False):
 with sr.Microphone() as source:
        if ask:
             print(ask)
        print('Listening...')
        audio=r.listen(source)
        voice_data = ''
        try:
             voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
             print("please Can u say it properly")
        except sr.RequestError:
             print("Sorry cant hear say it properly")
        return voice_data

def respond(voice_data):
     #for something related to  name 
     if 'what is your name' in voice_data:
         print("Hey i'm Friday")
     #for getting time .
     if 'Friday what is the time' in voice_data:
         print(ctime())
         
     if 'Friday search' in voice_data:
          search = record_audio('what do you want to search?')
          url ='https://google.com/search?q=' + search
          webbrowser.get().open(url)
          print('Here what i have found for  '+search)

     if 'Friday find location' in voice_data:
          location = record_audio('which location?')
          url ='https://google.nl/maps/place=' + location
          webbrowser.get().open(url)
          print('location found for  '+ location)     


print('Hi, How can i help you')
voice_data = record_audio()
respond(voice_data)


