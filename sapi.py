from matplotlib import artist
import requests

url = "https://spotify81.p.rapidapi.com/artist_singles"

querystring = {"id":"2w9zwq3AktTeYYMuhMjju8"}

headers = {
	"X-RapidAPI-Key": "8222bd61f1mshad1ad1dfca1b2bcp1aa093jsnd4c03fb4a7ae",
	"X-RapidAPI-Host": "spotify81.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())