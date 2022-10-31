from dataclasses import dataclass
import requests
import time

url = "https://spotify23.p.rapidapi.com/artist_singles/"

querystring = {"id":"2w9zwq3AktTeYYMuhMjju8","offset":"0","limit":"20"}

headers = {
	"X-RapidAPI-Key": "8222bd61f1mshad1ad1dfca1b2bcp1aa093jsnd4c03fb4a7ae",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

rj = response.json()

# print(rj)
x = range(10)

one = rj['data']['artist']['discography']['singles']['items'][int(0)]['releases']['items'][int(0)]['name']
two = rj['data']['artist']['discography']['singles']['items'][int(1)]['releases']['items'][int(0)]['name']
three = rj['data']['artist']['discography']['singles']['items'][int(2)]['releases']['items'][int(0)]['name']
four = rj['data']['artist']['discography']['singles']['items'][int(3)]['releases']['items'][int(0)]['name']
five = rj['data']['artist']['discography']['singles']['items'][int(4)]['releases']['items'][int(0)]['name']
six = rj['data']['artist']['discography']['singles']['items'][int(5)]['releases']['items'][int(0)]['name']
seven = rj['data']['artist']['discography']['singles']['items'][int(6)]['releases']['items'][int(0)]['name']
eight = rj['data']['artist']['discography']['singles']['items'][int(7)]['releases']['items'][int(0)]['name']
nine = rj['data']['artist']['discography']['singles']['items'][int(8)]['releases']['items'][int(0)]['name']
ten = rj['data']['artist']['discography']['singles']['items'][int(9)]['releases']['items'][int(0)]['name']

print(one, two, three, four, five, six, seven, eight, nine, ten)
