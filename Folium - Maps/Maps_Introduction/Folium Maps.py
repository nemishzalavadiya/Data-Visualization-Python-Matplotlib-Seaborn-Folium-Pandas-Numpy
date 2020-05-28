#!/usr/bin/env python
# coding: utf-8

# ### Imports

# In[1]:


import numpy as np
import pandas as pd
import folium


# In[6]:


world_data_map=folium.Map()
#print(world_data)


# In[12]:


world_data_map=folium.Map(location=[22.2587, 71.1924],zoom_start=6) # Let's zoom on Gujarat
world_data_map


# ### Now Let's change a look a little Bit by giving tiles of Stamen Toner
# #### It's gives Data about rivers and coastal zones

# In[15]:


world_map = folium.Map(location=[22.2587, 71.1924], zoom_start=6, tiles='Stamen Toner')

world_map


# ### Let's change it to natural forest colors

# In[16]:


world_map = folium.Map(location=[22.2587, 71.1924], zoom_start=6, tiles='Stamen Terrain')

world_map


# ### Now let's  create a map with Countries names

# In[21]:


world_map = folium.Map(location=[22.2587, 71.1924], tiles='Mapbox Bright')

world_map


# In[ ]:




