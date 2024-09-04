from config import key
import requests #web libraries
from mic_to_text import mic1

def chat1(chat):
    messages =[] # list which all messages
    system_message = "You are an AI Chat bot, your name is Jarvis, Created By Keshav T M ."#first instruction
    message = { "role": "user", "parts": [{"text": system_message+" "+chat}] }
    messages.append(message)
    data = {"contents": messages}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)
    
    t1 = response.json()
    # kjhprint(t1)
    t2= t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)

chat = mic1()
#chat = input("Enter your Query\n")
chat1(chat)