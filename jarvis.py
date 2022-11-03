import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser as wb
import os
os.system('cls')

print("Jarvis")
MASTER = "yusuf"
mendengarkan = sr.Recognizer()
engine = pyttsx3.init("sapi5")
#kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
#jenis suara [0] male [1] female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
myHobi = 'reading a book and studying about coding'


newFilm = ['Spiderman - No way Home',
            'Venom: Let There Be Carnage (2021)',
            'Shang-Chi and the Legend of the Ten Rings (2021)',
            'Squid Game (2021) - Series'
            
            ]

def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        talk("Haello... Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        talk("Haello... Good Afternoon" + MASTER)
    else:
        talk("Haello... Good Evening" + MASTER)

def take_command():
    try:
        with sr.Microphone() as source:
            print("mendengarkan")
            voice = mendengarkan.listen(source)
            command = mendengarkan.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                print(command)
                command = command.replace("jarvis", "")
                talk(command)
                
    except:
        pass

    return command


def run_jarvis():
    try:
        command = take_command()
        if 'play' in command:
            song = command.replace("play", "")
            talk("playing"+ song)
            print("playing"+ song)
            pywhatkit.playonyt(song)
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            talk("time now is "+ time)
        elif "wikipedia" in command:
            src = command.replace("wikipedia", "")
            info = wikipedia.summary(src, sentences=1)
            talk("searching wikipedia")
            print(info)
            talk(info)
        
        elif "google" in command:
            talk('opening google')
            wb.open_new_tab('http://www.google.com')

        elif command in ["open youtube","youtube","search youtube"]:
            talk('opening youtube')
            wb.open_new_tab('https://www.youtube.com')


        elif command in ['jarvis','hello jarvis','hello','helo','helo jarvis']:
            talk('hello.. i am jarvis, what is your name')
            yourName = take_command()
            print(f'Hello {yourName}')
            talk(f'Hello {yourName}')

        
        elif command in ['thank you','tengkyu','terimakasih']:
            talk('You are welcome')

        elif 'my hobby' in command:
            print(f'your hobby are {myHobi}')
            talk(f'your hobi are {myHobi}')

        elif 'course' in command:
            talk('opening your course')
            wb.open_new_tab('https://sce.iti.ac.id/my/')

        elif 'film' in command:
            talk('please select a movie')
            wb.open_new_tab('https://149.56.24.226/')

        elif 'new movie' in command:
            talk('looking for new movie')
            for i in range(len(newFilm)):
                talk(f'{i+1}. {newFilm[i]}')
                print(f'{i+1}. {newFilm[i]}')
            talk('what movie number do you want?')
            movie = take_command()
            if movie in ['one','1']:
                print(movie)
                talk(f'looking for {newFilm[0]}')
                wb.open_new_tab('https://149.56.24.226/spider-man-no-way-home-2021/')
            
            elif movie in ['two','2']:
                print(movie)
                talk(f'looking for {newFilm[1]}')
                wb.open_new_tab('https://149.56.24.226/venom-let-there-be-carnage-2021/')

            elif movie in ['three','3','tri','free']:
                print(movie)
                talk(f'looking for {newFilm[2]}')
                wb.open_new_tab('https://149.56.24.226/shang-chi-and-the-legend-of-the-ten-rings-2021/')
                    
        
            else:
                talk('not any intruction')
                print(movie)

        else:
            talk("not any intruction")
            print(command)


    except UnboundLocalError:
        pass

wishMe()

while True:   
    MASTER = "Yusuf"
    mendengarkan = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    #kecepatan baca
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    #jenis suara [0] male [1] female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    talk("I am jarvis, what do you want")
    run_jarvis()

