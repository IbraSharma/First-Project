
import json 
import requests
from random import randint
from package01 import list_utils

def main():
    # repeat this code block, until quit
    while True:
        # ask a user for input of name
        print('Enter your name: ')
        userName = input()
        print('Please enter your food choice: ')
        foodChoice = input()
        url = f'https://api.punkapi.com/v2/beers?food={foodChoice}'
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
        
        print('Can we offer a recommendation (yes/no/abv): ')
        recommendation = input()
        if recommendation == 'yes':

            x=  list_utils.recomendation_beer(beer_list)
            print(x)
            break
        elif recommendation == 'abv':

            xabv =list_utils.extract_beer(beer_list)
            print(xabv)
            break
        else:
            print('Thank you')
            break
main()