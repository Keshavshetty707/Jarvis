#pip install setuptools ,  pip install pyaudio ,  pip install SpeechRecognition
import pyaudio
import speech_recognition as sr

recognizer = sr.Recognizer()
def mic1():
    with sr.Microphone(device_index=0) as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source) #audio created
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said", text)
        return text   
#mic()

"""
index = 1
index = 0
print(sr.Microphone.list_microphone_names())

for name in sr.Microphone.list_microphone_names():
    print(index,":",name)
    #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    index= index+1
"""
