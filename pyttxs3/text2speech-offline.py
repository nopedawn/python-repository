# pip install pyttsx3 / pyttsx3 library
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 100)
engine.say("hello world")

engine.runAndWait()
