# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 02:11:23 2024

@author: Anıl
"""

import requests
import json

response = requests.get('https://api.nobelprize.org/2.1/nobelPrizes?_ga=2.96356767.2000896419.1706655639-527502705.1706655639')

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data,  indent = 2))
else:
    # Print an error message
    print('Error fetching data')
    
    
#to print all basic information of the prizes per year.

for item in range (len(data['nobelPrizes'])):
    
    print("Year: " + data['nobelPrizes'][item].get('awardYear'))
    print("Category: " + data['nobelPrizes'][item].get('category').get('en'))
    
    if data['nobelPrizes'][item].get('dateAwarded') != None:
        print("Date Awarded: " + data['nobelPrizes'][item].get('dateAwarded'))
    
    if data['nobelPrizes'][item].get('laureates')[0].get('knownName') != None:
        print("Name: " + data['nobelPrizes'][item].get('laureates')[0].get('knownName').get('en'))
        
    print("Reason of the prize: " + data['nobelPrizes'][item].get('laureates')[0].get('motivation').get('en'))
    
    print()


#to search for a specific year or category

search_year = input("Enter the Year you want to search for within 1901-1904: ")

flag_for_category = input("Do you want to search for a specific category? (Yes/No): ").lower()

if flag_for_category == 'yes':
    
    search_category = input("Enter the category you want to search for: ")

for item in range (len(data['nobelPrizes'])):
    
    if (data['nobelPrizes'][item].get('awardYear') == search_year) & (flag_for_category == 'yes'):
        
                
        if data['nobelPrizes'][item].get('category').get('en') == search_category:
                print()
                print("Year: " + data['nobelPrizes'][item].get('awardYear'))
                print("Category: " + data['nobelPrizes'][item].get('category').get('en'))
                print("Date Awarded: " + data['nobelPrizes'][item].get('dateAwarded'))
                print("Name: " + data['nobelPrizes'][item].get('laureates')[0].get('knownName').get('en'))

    elif (data['nobelPrizes'][item].get('awardYear') == search_year) & (flag_for_category == 'no'): 
        print()
        print("Year: " + data['nobelPrizes'][item].get('awardYear'))
        print("Category: " + data['nobelPrizes'][item].get('category').get('en'))
        print("Date Awarded: " + data['nobelPrizes'][item].get('dateAwarded'))
        print("Name: " + data['nobelPrizes'][item].get('laureates')[0].get('knownName').get('en'))
        


