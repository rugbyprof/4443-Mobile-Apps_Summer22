import json
from rich import print
from random import shuffle
import pymongo
import sys
import certifi

mongoUser = 'admin'
mongoPass = 'XxD4nIYVU94mo6e1'

# client = pymongo.MongoClient(
#     f"mongodb+srv://@cluster0.g7iqr.mongodb.net/?retryWrites=true&w=majority",
#     tlsCAFile=certifi.where())

client = pymongo.MongoClient(
    f"mongodb+srv://{mongoUser}:{mongoPass}@mobileapps.g7iqr.mongodb.net/?retryWrites=true&w=majority",
    tlsCAFile=certifi.where())

print(client)

db = client['restaurants']
collection1 = db['food_trucks_geo']
collection2 = db['food_trucks']

extremes = {
    'maxLon': -98.60366821289061,
    'maxLat': 33.81509581951251,
    'minLon': -98.44985961914062,
    'maxLon': 34.033314554166736
}

food_categories = [
    'American', 'Breakfast', 'BBQ', 'Bistro', 'Cajun'
    'Chinese', 'Italian', 'Japanese', 'Korean BBQ', 'Mexican', 'Pizza',
    'SeaFood', 'Sushi'
]

names = [("Speedy Eats", 'American'), ("Jumping Jack's Burgers", 'American'),
         ("The Lunch Truck", 'American'),
         ("The Lumberjack Mobile Smokehouse", 'BBQ'),
         ("The Crunchy Taco", 'Mexican'), ("Chicky Chimichanga", 'Mexican'),
         ("Highway Heartburn", 'Korean BBQ'), ("The Tasty Taquito", 'Mexican'),
         ("The Bun Bus", 'Breakfast'), ("Bullseye Burritos", 'Mexican'),
         ("Burger Bus", 'American'), ("Big Bob's Burritos", 'Mexican'),
         ("Rex Fries", 'American'),
         ("Fanny's Fried and Ready", "Dream Doughnuts", 'Breakfast'),
         ("The Clamshell", 'Bistro'), ("Chicka Chicken Boom Boom", 'BBQ'),
         ("Boxtruck Takeout", 'American'), ("Taste of Chicago", 'Pizza'),
         ("Hot Potatoes", 'American'), ("Cruisin' Cuisine", 'Sushi'),
         ("Gulf Coast Seafood", 'SeaFood'), ("The Gourmet Machine", 'Bistro'),
         ("The Rock Lobster", 'SeaFood'),
         ("Hungry Henry's Burger Bus", 'American'),
         ("Rocky Mountain Pizza", 'Pizza'), ("Fuel Up Fast Food", 'American'),
         ("The Mouthful", 'BBQ'), ("The Pasta Parade", 'Italian'),
         ("The Food Dude", 'BBQ'), ("Cheddar Chariot", 'Bistro'),
         ("Smiles 4 Miles Fried Foods", 'American'),
         ("Pete's Pizza Mobile", 'Pizza'), ("Sir Burger", 'American'),
         ("Taco Trailer", 'Mexican'), ("Bacon Buggy", 'Breakfast'),
         ("Alligatah", 'Cajun')]

if __name__ == '__main__':
    with open("truck_data.json") as f:
        data = json.load(f)

    with open("truck_locations.geojson") as f:
        locs = json.load(f)

    locs = locs['features']

    shuffle(locs)

    for i in range(len(data)):
        # randomize names to assign for our fake trucks
        shuffle(names)
        print(i)
        # assign name and food type to our dictionary
        data[i]['food_truck_name'] = names[0][0]
        data[i]['food_type'] = names[0][1]

        # pull out the locations from 'truck_locations.geojson' that we read in
        data[i]['latitude'] = locs[i]["geometry"]["coordinates"][1]
        data[i]['longitude'] = locs[i]["geometry"]["coordinates"][0]
        #collection2.insert_one(data[i])

        #print(data[i])

        data[i]['location'] = locs[i]
        del data[i]['latitude']
        del data[i]['longitude']

        collection1.insert_one(data[i])
        print("*" * 80)
        print(data[i])
