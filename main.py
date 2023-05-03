import ephem
import datetime
from geopy.geocoders import Nominatim

# Define a list of cities
cities = ['Berlin', 'London', 'New York', 'Sydney', 'Vienna', 'Paris']

# Initialize a geocoder object
geolocator = Nominatim(user_agent='full_moon_bot')

# Set the current date and time
now = datetime.datetime.utcnow()

# Create a list to store the names of cities where a full moon is visible
visible_cities = []

# Loop over each city and calculate the location of the next full moon visible from that city
for city in cities:
    # Geocode the city name to get its latitude and longitude
    location = geolocator.geocode(city)
    if location is None:
        continue
    lat, lon = location.latitude, location.longitude

    obs = ephem.Observer()
    obs.lat = str(lat)
    obs.lon = str(lon)
    obs.date = now

    # Check if there is a full moon visible from this location
    next_full_moon = ephem.next_full_moon(now)
    obs.date = next_full_moon
    moon = ephem.Moon()
    moon.compute(obs)
    if moon.alt > 0:
        # If a full moon is visible, save the city in an array
        visible_cities.append((city, next_full_moon.datetime()))

# Check if there are any cities with full moon visible, if true -> print out
if len(visible_cities) > 0:
    print('Full moon visible from following cities: ')
    for city, full_moon_time in visible_cities:
        print('{} on {}'.format(city, full_moon_time))
else:
    print('No full moon in this city. *sad awoooo* ')
