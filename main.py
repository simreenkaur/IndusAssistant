import speech_recognition as sr
import pyttsx3
import pywhatkit

from translate import translator
translator = translator(to_lang="pa-IN")

listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
      engine.say(text)
      engine.runAndWait()
def take_command():

  try:
    with sr.Microphone() as source:
        print('Listening.....')
        voice = listener.listen(source)
        command = listener.recognice_google(voice)
        command = command.lower()
        #Checks if the input contains the trigger word Indus
        if 'indus' in command:
            talk('Hello ji! Do you have anything to write?')
            print(command)
        if 'write ' in command:
            print(command)
            talk('Writing...')
        if 'What is the meaning of' in command:
            command= command.replace('What is the meaning of', '')
            translation = translator.translate(command)
            #TODO: Have to check if indus can talk in punjabi
            talk(translation)

  except:
    pass
  return command

def run_indus():
    command = take_command()

    if 'Sat Sri Akal' in command:
        talk('Sat Sri Akal Ji!')

    run_indus()