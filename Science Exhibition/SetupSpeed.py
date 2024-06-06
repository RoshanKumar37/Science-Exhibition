#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3 as pt
import speech_recognition as sr
import requests
import time as time
from datetime import datetime, timedelta


# In[2]:


# Common responses
# -------------------------------------------------------------------------------------------------------------------------------













# In[3]:


# Speak function initialization
def speak(text, voice_id):
    engine = pt.init()
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()


# In[4]:


# pause function
import time
def delay(seconds):
    time.sleep(seconds)


# In[5]:


# Voice Functions

def get_voice_id(gender):
    engine = pt.init()
    voices = engine.getProperty('voices')
    
    # print("Available voices:")
    # for voice in voices:
    #     print(f"ID: {voice.id}, Name: {voice.name}")
    
    for voice in voices:
        if gender == 'male' and 'david' in voice.name.lower():
            return voice.id
        elif gender == 'female' and 'zira' in voice.name.lower():
            return voice.id
    return None
    


# In[6]:


# Setting up Voice 'Male/Female'

responseVoiceSelection = input("Select voice: Enter 1 for male or 2 for female: ")

if responseVoiceSelection == '1':
    voice_id = get_voice_id('male')
    if voice_id:
        speak("You have selected the male voice.", voice_id)
    else:
        print("Male voice not found.")
elif responseVoiceSelection == '2':
    voice_id = get_voice_id('female')
    if voice_id:
        speak("You have selected the female voice.", voice_id)
    else:
        print("Female voice not found.")
else:
    print("Invalid selection. Please enter 1 or 2.")


# In[7]:


def speak(something):
    engine = pt.init()
    engine.setProperty('voice', voice_id)
    engine.say(something)
    engine.runAndWait()


# In[8]:


# set up
speak(f"Hello Sir")
speak("This is the setup of my program")
delay(2)
speak("You must answer everything correctly in order to finish setup")
speak("So, let us get started")


# In[9]:


# Setting up Speech Recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_sphinx(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble accessing your request")
        return ""


# In[10]:


# Setting up username

nameList = []



speak("Please tell your name")
print("Enter your name: ")
userName = input()
responseName = f"{userName}, seems a nice name."
speak(responseName)

speak("How would you like me to call you?")
print("For eg: 'sir', 'bro', or anything of your choice...")
userCall = input()

speak(f"Great {userName}{userCall}")
print(f"I would be calling you {userName} {userCall} from now on...")


# In[11]:


# News Functions

def get_news(topic):
    api_key = '361c686e684a4b4395024882ff62a898'
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:  # Ensure the request was successful
        news_data = response.json()
        if 'articles' in news_data:
            return news_data['articles']
        else:
            print("No articles found in the response.")
            return []
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return []

def read_news(articles):
    for i, article in enumerate(articles[:5], 1):  # limiting to first 5 articles
        news_text = f"News {i}: {article['title']}. {article['description']}"
        print(news_text)
        speak(news_text)
        


# In[11]:


# Setting up interests for morning news
# online only
speak(f"{userCall}, do you want to stay updated for what's going on around the world.")
print("'y' for yes and 'n' for no")
responseNews = input()

if responseNews.lower() == 'n' or responseNews.lower() == 'no':
    speak("Alright! then I will proceed next.")

elif responseNews.lower() == 'y' or responseNews.lower() == 'yes':
    speak("What topics of news are you interested in?")
    print("""
    Options are:
    1. National
    2. International
    3. Entertainment
    4. Education
    5. Health
    6. Sports
    7. Business and Stocks
    and much more...
    """)
    
    responseNewsInput = input()

    speak("I will provide with you with the headlines in the morning")
    
    def wait_until(target_hour):
        now = datetime.now()
        target_time = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    
        if target_time < now:
            target_time += timedelta(days=1)

        time_to_wait = (target_time - now).total_seconds()
        print(f"Waiting for {int(time_to_wait)} seconds until {target_time.strftime('%I:%M %p')}")

        time.sleep(time_to_wait)
        next_program()

    def next_program():
        def read_news_in_morning():
            if responseNewsInput:
                articles = get_news(responseNewsInput)
                if articles:
                    read_news(articles)
                else:
                    speak("Sorry, I couldn't find any news on that topic.")
            else:
                speak("Sorry, I didn't understand the topic.")
        read_news_in_morning()

    def main():
        while True:
            try:
                response_time = int(input("Enter the time (an integer between 6 and 12): "))
                if 6 <= response_time <= 12:
                    break
                else:
                    print("Please enter a valid time between 6 and 12.")
            except ValueError:
                print("Invalid input. Please enter an integer between 6 and 12.")

        print(f"Time set to {response_time} AM")
        wait_until(response_time)

    if __name__ == "__main__":
        main()
    

    
    
    
else:
    speak("Sorry! I couldn't get that")

speak


# In[12]:


delay(1.5)
speak("Great! Setup Finished")
print("Feel free to ask anything!")


# In[ ]:





# In[ ]:





# In[ ]:




