#!/usr/bin/env python
import requests
import turtle

import sys


__author__ = 'Janelle Kuhns with help from demo'

iss_icon = 'iss.gif'
world_map_image = 'map.gif'
base_url = 'http://api.open-notify.org'

def get_astronaut_info():
    """dict of astronauts"""
    r = requests.get(base_url + "/astros.json")
    r.raise_for_status()
    return r.json()['people']
    

def get_iss_location():
    """current location of iss (lat, lon)"""
    r = requests.get(base_url + "/iss-now.json")
    r.raise_for_status()
    position = r.json()["iss.position"]
    lat = float(position("latitude"))
    lon = float(position("longitude"))
    return lat, lon

def map_iss(lat, lon):
    """Draw a world map and place ISS icon at lat, lon"""
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.bgpic(world_map_image)
    screen.setworldcoordinates(-180, -90, 180, 90)

    

def main():
    """Part A: Get astronauts in space and their crafts"""
    astronaut_dict = get_astronaut_info()
    print("\nCurrent astronauts in space: {}".format(len(astronaut_dict))

    """Part B:  Current position of ISS"""
    lat, lon = get_iss_location
    print("\nCurrent ISS coordinates: lat={:.02f} lon={:.02f}".format(lat, lon))

    #Part C: Current ISS on map
    screen = None
    try:
        screen = map_iss(lat, lon)

        #Part D: Compute next pass-over for my location
        indy_lat = 
        indy_lon = 
        location = turtle.Turtle()
        location.penup()
        location.color('yellow')
        location.goto(indy_lon, indy_lat)
        location.dot(5)
        location.hideturtle()

    except RuntimeError as e:
        print("ERROR: problem loading graphics: " + str(e))

if __name__ == '__main__':
    main()
