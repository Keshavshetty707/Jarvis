import requests
from mic_to_text import mic1

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":"sunnyvale","format":"json","u":"f"}

    headers = {
	"x-rapidapi-key": "b13f83939dmshe7badec8d082479p17c309jsnf2d1f054c2f3",
	"x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    d1= response.json()
    d1 = d1.get("current_observation")
    humidity = d1.get('atmosphere').get("humidity")
    temp = d1.get('condition').get("temperature")
    temp = round((temp-32)*5/9,2)
    print(f"Humidity: {humidity}, Temp in Celcious:{temp}")

if __name__ == "__main__":
    print(temp_city("karnataka"))