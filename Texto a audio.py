
import pyttsx3 

labels = ["A", "B", "C","Eres demasiado bueno"]
engine= pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+200)
engine.setProperty("rate",100)
engine.say("Estas letras son:",labels)
engine.runAndWait()


