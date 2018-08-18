from gtts import gtts
import speech_recognition as sr
import os
import webbrowser
import smtplib

def Talktome(audio):
	print(audio)
	tts = gTTS(text = audio , lang = 'en')
	tts.save('audio.mp3')
	os.system('mpg123 audio.mp3')

	#listens for commands
def myCommand():

	r= sr.Recognizer()

	with sr.Microphone() as source:
		print('I am ready for your next command')
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source , duration = 1)
		audio = r.listen(source)

		try:
			command = r.recognize_google(audio)
			print('You said '+ command + '/n')

		#Loop back to continue to listen for commands

	except sr.UnknownValueError:
		assistant(myCommand())

	return command

#if statement for executing command

def asssistant(command):

	if 'open reddit python' in command:
		chrome_path = '/usr/bin/google-chrome'
		url = 'https://www.reddit.com/r/python'
		webbrowser.get(chrome_path).open(url)

	if ' What \'s up' in command:
		Talktome('Chillin bro')

	if 'email' in command:
		Talktome('Who is the recipient')
		recipient = myCommand()

		if 'Jaynil' in recipient:
			Talktome('What should I say')
			content = myCommand()

			#init gmail SMTP
			mail = smtplib.SMTP('smtp.gmail.com',587)

			#identify to server
			mail.elho()

			#encrypt session
			mail.starttls()

			#login
			mail.login('username' , 'password')

			#send message
			mail.sendmail('PERSON NAME','jaynibvb@gmail.com',content)

			#close connection
			mail.close()

			Talktome('EMAIL Sent')

Talktome('I am ready for your command')

while True:
	assistant(myCommand())

	
