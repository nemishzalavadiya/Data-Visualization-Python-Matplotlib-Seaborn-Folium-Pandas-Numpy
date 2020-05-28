#!/usr/bin/env python
# coding: utf-8

# ### Imports

# In[2]:


import numpy as np
import pandas as pd
import folium


# ### Load Data Of Police Incidents

# In[3]:


df_incidents = pd.read_csv('Folium/PoliceDepartment_incidents_2016/Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset Loaded')


# ### it's has colums,
# #### IncidntNum: Incident Number
# #### Category: Category of crime or incident
# #### Descript: Description of the crime or incident
# #### DayOfWeek: The day of week on which the incident occurred
# #### Date: The Date on which the incident occurred
# #### Time: The time of day on which the incident occurred
# #### PdDistrict: The police department district
# #### Resolution: The resolution of the crime in terms whether the perpetrator was arrested or not
# #### Address: The closest address to where the incident took place
# #### X: The longitude value of the crime location
# #### Y: The latitude value of the crime location
# #### Location: A tuple of the latitude and the longitude values
# #### PdId: The police department ID

# In[4]:


df_incidents.head()


# In[5]:


limit = 100
df_incidents = df_incidents.iloc[0:limit, :]


# In[6]:


# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42


# In[7]:


# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
sanfran_map


# In[9]:


# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
sanfran_map.add_child(incidents)


# In[11]:


# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add pop-up text to each marker on the map
latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)    
    
# add incidents to map
sanfran_map.add_child(incidents)


# ##### Make this Notebook Trusted to load map: File -> Trust Notebook
# ##### The other proper remedy is to group the markers into different clusters. Each cluster is then represented by the number of crimes in each neighborhood. These clusters can be thought of as pockets of San Francisco which you can then analyze separately.
# 
# ##### To implement this, we start off by instantiating a MarkerCluster object and adding all the data points in the dataframe to this object.

# In[12]:


from folium import plugins

# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(sanfran_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

# display map
sanfran_map

