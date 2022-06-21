## Program  2 - Food Truck App

#### Due: 06-24-2022 (Friday @ 12:30 p.m.)

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/fast_food.png" width="500">

## Overview

Using the "Flash Chat" completed project: https://github.com/londonappbrewery/Flash-Chat-Flutter-Complete as a template, create a location based food truck app that incorporates a google map plugin which will (at a minimum) show the location of each food truck. I will provide a json file with the basic information about each food truck, and a list of possible locations that the food trucks can reside. 

I mentioned that we would use **MongoDB** as a backend for this app, but we will continue with **FireBase** so that we can get this project done by Friday. 

- **Welcom Screen**
  - Create your own "splash" screen using something other than the "Flash Chat" images, animations, and color scheme. In addition you need to create your own **app icon** for this project. 

- **Register and Login Screens**
  - Keep exactly the same layout if you like, just change the color scheme.

- **Truck Locations Screen**
  - Discussed more below in the Google Maps section

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/truck_locations.png" width="200">

## Google Maps

- Create an API key: https://developers.google.com/maps/documentation/javascript/get-api-key
- Then incorporate a maps page similar to this tutorial: https://codelabs.developers.google.com/codelabs/google-maps-in-flutter#0
- Use custom map icons: https://mapicons.mapsmarker.com/markers/restaurants-bars/take-away/food-truck/?custom_color=bf2ea2

The google maps tutorial used a file that contained a list of json object similar to: 

```json
    {
      "address": "Aabogade 15\n8200 Aarhus\nDenmark",
      "id": "aarhus",
      "image": "https://lh3.googleusercontent.com/tpBMFN5os8K-qXIHiAX5SZEmN5fCzIGrj9FdJtbZPUkC91ookSoY520NYn7fK5yqmh1L1m3F2SJA58v6Qps3JusdrxoFSwk6Ajv2K88",
      "lat": 56.172249,
      "lng": 10.187372,
      "name": "Aarhus",
      "phone": "",
      "region": "europe"
    },
```

Then added a `locations.dart` file that contained multiple classes to handle the specific json data. This is where I think most of your work will be needed to adapt each of the classes to our specific json fields.

### Discussion:


TBD


### Files in P02

- [combined_truck_data.json](combined_truck_data.json) => the location data you need for this project
- [fix_data.py](fix_data.py) => code I used to combine two json files
- [truck_data.json](truck_data.json) => food truck info
- [truck_locations.json](truck_locations.json) => possible locations for food trucks

### Deliverables


- Create a folder in your assignments folder called `P02`
- Upload all files dealing with your flutter project in this folder to github.
- Be prepared to talk about your completed project Jun 29<sup>th</sup> or Jun 30<sup>th</sup> in front of the class, while showing that your project runs correctly.


