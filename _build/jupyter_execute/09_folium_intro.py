import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import folium

#!pip install folium

### Maps with `folium`

Making a map: 

```python
folium.Map()
```

#make map


Typically, we want to center the map at a given latitude and longitude pair so we include the `location` argument with a specific latitude and longitude.  Often, we get this information from a dataset, so let's load in a dataset that describes some community garden locations in New York City.

#read in the data
gardens = pd.read_json('https://data.cityofnewyork.us/resource/ajxm-kzmj.json')

#note the latitude and longitude columns
gardens.info()

#take a peek


#grab first latitude, longitude pair

#create map centered at this latitude and longitude


#display the map


### Adding Markers

There are a few variations of markers that we can add to the map, but they mostly function the same way.  We say a point where we want the marker drawn, define any kind of popup, and add the marker to our map.





### Adding Many Markers

One approach to add markers for all the gardens would be to iterate over the rows of the data, grab each latitude and longitude pair, and add a marker there with any additional information we need.  We can use the `.iterrows()` function from pandas to do so.  Here, we have both the row name and the data from the rows accessible.

#.iterrows()










### Policing Map

c = pd.read_csv('data/sf_police.zip', compression = 'zip')

c.head()

#what kinds of crimes are there
c['Category'].value_counts(ascending=True)

#limit the data to a given crime
















### Heat Map

from folium.plugins import HeatMap, MarkerCluster















### Example: Earthquakes in Japan



Make a map of the earthquakes in Japan with magnitude greater than 6.5.  Include information about the earthquake in a popup marker.

japan = pd.read_csv('data/japan_earthquakes.csv')

japan.head()

japan['mag'].hist()



