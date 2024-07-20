import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to recognize speech and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None
    return query.lower()

# Function to respond to greetings
def respond_to_greetings():
    speak("Hello! How can I assist you today?")

# Function to tell the time
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

# Function to tell the date
def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

# Function to search the web
def search_web(query):
    speak("Searching the web for you...")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Main function to run the voice assistant
def main():
    while True:
        query = listen()
        if query is None:
            continue

        if "hello" in query:
            respond_to_greetings()
        elif "time" in query:
            tell_time()
        elif "date" in query:
            tell_date()
        elif "search for" in query:
            search_term = query.split("search for")[-1].strip()
            search_web(search_term)
        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I can't help with that.")

if __name__ == "__main__":
    main()
