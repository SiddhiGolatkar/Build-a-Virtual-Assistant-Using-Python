
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) 

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command(): 
    global command  
    try:
        with sr.Microphone() as source:
            print('I am listening, Say something...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print('Me:', command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        print('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%m %p')
        print(time)
        talk('Current time is ' + time)

    elif 'tell me about' in command:
        ask = command.replace('tell me about', '')
        info = wikipedia.summary(ask, 2)
        print(info)
        talk(info)

    elif 'how are you' in command:
        talk('I am fine. Thank You! How about you?')

    elif 'what are you doing' in command:
        talk('hmmm.. I am damn busy')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'thank you' in command:
        talk('Your welcome. Anything else you want me to do ?')

    elif 'good bye' in command:
        talk('GoodBye Smarty. See you later, Alligator.')

    else:
        talk('Sorry, i dint get you. Please come again.')


while True:     
    run_alexa()
    
    
