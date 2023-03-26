import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to get the user's speech input
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except:
            print("Sorry, I didn't get that.")
            return None

# Define a function to search Wikipedia for the given query
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)
    except:
        print("Sorry, I couldn't find any information about " + query)
        speak("Sorry, I couldn't find any information about " + query)

# Define the main function
def main():
    speak("Hi, how can I help you?")
    while True:
        text = get_audio()
        if text:
            if "search for" in text:
                query = text.replace("search for", "")
                search_wikipedia(query)
            elif "exit" in text:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I don't understand. Please try again.")
