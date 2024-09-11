#!/usr/bin/env python3

"""
A console application that shows the current weather forecast for a given location. 
It accepts as arguments:
    - latitude (--lat) (required)
    - longitude (--lon) (required)
    - a flag indicated whether to print the temperatures predicted for the whole day instead (-d)

Example usage:

$ python3 app.py --lat 42 --lon 23
$ python3 app.py --lat 42 --lon 23 -d
$ python3 app.py --help
"""

import requests  # you need to install it via `pip install requests`
import argparse  # built-in, no installation needed
import dotenv    # you need to install it via `pip install python-dotenv`

import sys
import os

dotenv.load_dotenv()  # exports contents of a `.env` file in the curr dir as environmental variables
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    error_msg = """
Please supply a valid API key using either
`export API_KEY=...` before running the command
or
creating a file named `.env` in the current directory and putting API_KEY=... inside.
"""

    # When writing a console app
    # it is better to write error messages to STDERR instead of STDOUT 
    # (the `print` function will write them to STDOUT)
    sys.stderr.write(error_msg)
    exit(1)

parser = argparse.ArgumentParser(description="Get the weather for a given location")
parser.add_argument("--lat", type=float, required=True, help="latitude of the location")
parser.add_argument("--lon", type=float, required=True, help="longitude of the location")
parser.add_argument("-d", "--day", action="store_true", help="whether to print the temperatures predicted for the whole day instead")
args = parser.parse_args()

lat = args.lat
lon = args.lon
is_requesting_whole_day = args.day

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params={
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
    }
)

if not response:
    sys.stderr.write(f"Error fetching data ({response.status_code=}). Please try again later.\n")
    exit(1)

forecasts = response.json()["list"]
forecasts.sort(key=lambda x: -x["dt"])  # biggest (most recent) datetime first

if not is_requesting_whole_day:
    temperature = forecasts[0]["main"]["temp"]
    print(temperature)
else:
    temps = "\n".join(
        str(forecast["main"]["temp"])
        for forecast in forecasts[:8]
    )
    print(temps)
