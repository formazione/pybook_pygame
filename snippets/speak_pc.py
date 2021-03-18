# This make you use the synthetic voice of windows
from win32com.client import Dispatch

def speak(x):
    "x = something to say"
    print(x)
    return Dispatch("SAPI.SpVoice").Speak(x)

speak("Ciao a tutti")







