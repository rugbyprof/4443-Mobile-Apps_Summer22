import json
from rich import print
from random import shuffle
from random import randint


def phoneNumber():
    areacode = '940'
    prefixes = ['631', '632', '636', '882', '235']
    shuffle(prefixes)

    num = str(randint(1000, 9999))

    return f"({areacode}) {prefixes[0]}-{num}"


def makeUrl(name):
    name = name.replace(' ', '-').lower()
    name = name.replace("'", "")
    exts = ['com', 'biz', 'food', 'us', 'net']
    shuffle(exts)

    return f"https://{name}.{exts[0]}"


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

    with open("truck_locations.json") as f:
        locs = json.load(f)

    locs = locs['features']

    shuffle(locs)

    simple = {}
    nestedVersion = {}

    simpleList = []
    nestedList = []

    # "city": "Wichita Falls",
    # "email": "areyburn0@shutterfly.com",
    # "first_name": "Aura",
    # "food_truck_name": null,
    # "food_type": "American",
    # "id": 1,
    # "last_name": "Reyburn",
    # "lat": 33.964683,
    # "lng": -98.51316,
    # "phone": "(940) 882-8321",
    # "state": "TX",
    # "truck_color": "Pink",
    # "truck_name": "Sir Burger",
    # "url": "https://sir-burger.food"

    #

    for i in range(len(data)):
        simple = {}
        nested = {}
        # randomize names to assign for our fake trucks
        shuffle(names)
        print(i)
        # assign name and food type to our dictionary
        simple['truck_name'] = names[0][0]
        simple['food_type'] = names[0][1]

        # pull out the locations from 'truck_locations.geojson' that we read in
        simple['lat'] = round(locs[i]["geometry"]["coordinates"][1], 6)
        simple['lng'] = round(locs[i]["geometry"]["coordinates"][0], 6)

        simple['phone'] = phoneNumber()
        simple['url'] = makeUrl(names[0][0])
        simple['city'] = 'Wichita Falls'

        simple['id'] = data[i]['id']
        simple['email'] = data[i]['email']
        simple['first_name'] = data[i]['first_name']
        simple['last_name'] = data[i]['last_name']
        simple['state'] = data[i]['state']
        simple['truck_color'] = data[i]['truck_color']

        #data[i]['location'] = locs[i]
        del data[i]['latitude']
        del data[i]['longitude']

        simpleList.append(simple)

        nested.update(simple)

        nested['location'] = {'lat': simple['lat'], 'lng': simple['lng']}

        del nested['lat']
        del nested['lng']

        nested['address'] = {'city': simple['city'], 'state': simple['state']}

        del nested['city']
        del nested['state']

        nestedList.append(nested)

    with open("truck_data_combined_simple.json", "w") as f:
        json.dump(simpleList, f, indent=2, sort_keys=True)

    with open("truck_data_combined_nested.json", "w") as f:
        json.dump(nestedList, f, indent=2, sort_keys=True)