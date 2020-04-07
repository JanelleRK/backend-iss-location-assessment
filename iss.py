#!/usr/bin/env python
import requests
import sys


__author__ = 'Janelle Kuhns with help from demo'


def main():
    astronaut_info = requests.get("http://api.open-notify.org/astros.json")
    astronaut_info.text
    print(astronaut_info)


if __name__ == '__main__':
    main()
