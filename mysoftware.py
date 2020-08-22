import os
import pyttsx3

print("******************Welcome to my project******************")
pyttsx3.speak("Welcome to my project")
while(True):
	
	print("Enter your choice of application", end='')
	pyttsx3.speak("please enter your choice of application--- ")
	x=input()
	if ("chrome browser" in x) or ("chrome" in x):
		pyttsx3.speak("okk opening chrome for you")
		print("********************************************")
		os.system("chrome")
		
	elif ("play" in x) or ("music" in x):
		pyttsx3.speak("its time for music")
		print("********************************************")
		os.system("wmplayer")

	elif ("notepad" in x) or ("Notepad" in x):
		pyttsx3.speak("okk opening notepad foryou")
		print("********************************************")
		os.system("notepad")
	
	elif ("calculator" in x) or ("cal" in x):
		pyttsx3.speak("okk opening calculator for you")
		print("********************************************")
		os.system("calc")

	elif ("paint" in x) or ("draw" in x):
		pyttsx3.speak("okk opening paint for you")
		print("********************************************")
		os.system("start mspaint")

	elif ("cmd" in x) or ("command prompt" in x):
		pyttsx3.speak(" opening comand prompt for you")
		print("********************************************")
		os.system("start cmd")

	elif ("exit" in x) or ("bye" in x):
		pyttsx3.speak("thank you for interacting with us")
		print("********************************************")
		break

	elif ("how" in x) or ("are you" in x):
		pyttsx3.speak("I am fine thank you")

	else:
		pyttsx3.speak("please tell correct application")
	