import requests
from bs4 import BeautifulSoup

print('Welcome to InstantWeather - an online tool to get current weather report of any city.\nEnter your city name to get its current weather report or enter "q" to quit.')

while True:

	city = input("\nEnter your city: ")
	if city == "q":
		break
		
	else:
	
		try:
			
			url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=15b5aa0c69781d1e97bff1053e67df8b&mode=html"
			data = requests.get(url)
			soup = BeautifulSoup(data.text, "html.parser")
			data1 = soup.find_all('div')
			print("Temperature: " + data1[5].string)
			print(data1[7].string)
			print(data1[8].string)
			print(data1[9].string)
			print(data1[10].string)
			
		except IndexError:
			print("Sorry, " + city + " is not a city.")
			
		except:
			print("Something went wrong, please try again.")