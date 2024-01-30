import requests

url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"

querystring = {"lat":"16.41667N","lon":"80.25E","timezone":"auto","language":"en","units":"auto"}

headers = {
	"X-RapidAPI-Key": "0adfec26a1msh228ed72d7b5fd9ep107c77jsn04f45e6c7431",
	"X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())