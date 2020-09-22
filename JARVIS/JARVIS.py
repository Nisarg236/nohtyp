import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb

engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    elif hour>=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir")
    speak("I am jarvis")
    #speak("The current time is")
    #time()
    #speak("The current date is")
    #date()
    
    speak("How may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1#wait for one second
#pause for 1 second
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en.in')
        print(query)
    except Exception as e:
        print(e)
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login('19k054@nirmauni.ac.in','NPanchal')
    server.sendmail('19k054@nirmauni.ac.in',to,content)

if __name__=="__main__":
    wishme()
    while(True):
        query=takeCommand().lower()
        if 'time' in query:
            speak("the current time is")
            time()
        elif 'date' in query:
            speak("todays date is")
            date()
        elif 'quit' in query:
            quit()
        elif 'what is' in query:
            query=query.replace('what is','')
            result=wikipedia.summary(query,sentences=4)
            print(result)
            speak('result')
        elif 'tell me about' in query:
            query=query.replace('tell me about','')
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'shut up' in query:
            speak('you shut up!')
        elif 'send mail' in query:
            speak("Please tell me the password to proceed")
            pwd=takeCommand()
            if "tubelight" in pwd:
                try:
                    speak("Please enter the reciever address")
                    to=input("Enter the reciever Address :")
                    speak("What message shall i say")
                    content=takeCommand()
                    print(content)
                    speak("Connected to the server")
                    speak("Sending Mail")
                    sendEmail(to,content)
                    speak('E-mail sent sucsessfully')
                except Exception as e:
                    print(e)
                    speak("Unable to send Mail")
            else:
                speak("incorrect password")
                speak("action terminated")


        elif 'offline' in query:
            quit()
            
while(True):
    wishme()
    takeCommand()
    
    

