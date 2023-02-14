import json
import requests
from random import randint




#Gets a random Beer 
def recomendation_beer(beer_list):
    value = randint(0,len(beer_list))
    try_this = beer_list[value]
    try_name = try_this['name']
    try_tagline = try_this['tagline']
    try_abv = try_this['abv']
    try_ibu = try_this['ibu']
    random_beer = f'You should try {try_name}, {try_tagline}, {try_abv} %, {try_ibu}'
    return random_beer




# Collect beers within abv
def extract_beer(beer_list):
    print('Enter abv number to collect beers (float x.0): ')
    N = float(input("Enter abv number : "))
    beers_over_selected_abv = [beer["name"] for beer in beer_list if beer['abv'] >= N]
    return beers_over_selected_abv

