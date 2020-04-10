# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City():
  def __init__(self, city, lat, lon):
    self.name = city
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f'{self.name} {self.lat} {self.lon}'

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []
import csv

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open('cities.csv', newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      # print(row)
      if(row[0] != 'city'):

        zip_codes = row[-1].split(' ')
        parameter_list = [*row[:len(row) - 1], *zip_codes]
        # print(parameter_list)
        cities.append(City(city=parameter_list[0],
                          lat=float(parameter_list[3]),
                          lon=float(parameter_list[4])))
        # print(row[0].split(','))
        # print(', '.join(row))
        # print()
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def is_in(city, lat1, lon1, lat2, lon2):
  
  # print(type(city.lat) is float and type(city.lon) is float)

  if(not(type(city.lat) is float and type(city.lon) is float)):
    return False
  # print(city, '|',lat1, lon1, lat2, lon2)
  # lat1 lat2
  # 45 <= 42.333
  max_lat = lat2
  min_lat = lat1
  if(lat1 > lat2):
    max_lat = lat1
    min_lat = lat2

  pass_lat = float(min_lat) <= city.lat <= float(max_lat)
  # print(pass_lat)
  # lon1 lon2
  max_lon = lon2
  min_lon = lon1
  if(lon1 > lon2):
    max_lon = lon1
    min_lon = lon2
  pass_lon = float(min_lon) <= city.lon <= float(max_lon)
  return pass_lat and pass_lon

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):

  # if(not(type(lat1) == 'float' and type(lon1) == 'float' and type(lat2) == 'float' and type(lon2) == 'float')):
  #   return cities
    # print(cities)

  # within will hold the cities that fall within the specified region
  within = [city for city in cities if is_in(city, lat1, lon1, lat2, lon2)]

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within
