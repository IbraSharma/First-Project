import json
import requests
from random import randint



# First step
your_name = input('please type your name: ')
food_choice = input('Please enter your food choice: ')
url = f'https://api.punkapi.com/v2/beers?food={food_choice}'
r = requests.get(url)
data = json.loads(r.text)



# List of dict 
beer_list = []
for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']
    ibu = beer['ibu']

    beer_item = {
    'name': name,
    'tagline': tagline,
    'abv': abv,
    'ibu': ibu
    }
    beer_list.append(beer_item)
print(beer_list)



#Gets a random Beer 
def recomendation_beer():
    value = randint(0,len(beer_list))
    try_this = beer_list[value]
    try_name = try_this['name']
    try_tagline = try_this['tagline']
    try_abv = try_this['abv']
    try_ibu = try_this['ibu']
    random_beer = f'You should try {try_name}, {try_tagline}, {try_abv} %, {try_ibu}'
    return random_beer
recomendation_beer()



# Collect beers within abv
def extract_beer():
    N = float(input("Enter abv number : "))
    beers_over_selected_abv = [beer["name"] for beer in beer_list if beer['abv'] >= N]
    return beers_over_selected_abv
