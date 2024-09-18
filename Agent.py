#this file excute the resprective function based on user query
import task1
from config import key
import requests #web libraries

def run_conversation(user_message):
    messages = [] # list which all messages

    system_message = """You are an AI Chat bot, that can do everything using function call. When you are asked to do something, use the function call you have available and then respond with message"""#first instruction
   
    message = { "role": "user", 
                "parts": [{"text": system_message+"\n"+user_message}] 
               }
    
    messages.append(message)

    data = {"contents": [messages],
            "tools":
                [
                    {
                      "functionDeclarations" : task1.definitions
                    }
                ]   
            }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json = data)
    
    if response.status_code != 200:
        print(response.text)

    t1 = response.json()

    if "content" not in t1.get("candidates")[0]:
        print("Error: No content in response")

    # print(t1)
    #t2= t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    #print(t2)
    print("now we are getting", t1)

if __name__ == "__main__":
    user_messages = "find the temperature of Delhi"
    run_conversation(user_messages)