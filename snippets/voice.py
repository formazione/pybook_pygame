from win32com.client import Dispatch

class Voice:
	speak = Dispatch("SAPI.SpVoice").Speak

Voice.speak("Ciao")


