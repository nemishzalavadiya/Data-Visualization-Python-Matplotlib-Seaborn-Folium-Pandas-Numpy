#!/usr/bin/env python
# coding: utf-8

# In[13]:


#imports
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle Charts
import pandas as pd
import numpy as np 
mpl.style.use('ggplot') # optional: for ggplot-like style

# check for latest version of Matplotlib
print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0


# In[14]:


# 1. **categories**: Unique categories or classes in dataframe.
# 2. **values**: Values corresponding to categories or classes.
# 3. **height**: Defined height of waffle chart.
# 4. **width**: Defined width of waffle chart.
# 5. **colormap**: Colormap class
# 6. **value_sign**: In order to make our function more generalizable, we will add this parameter to address signs that could be associated with a value such as %, $, and so on. **value_sign** has a default value of empty string.


# In[17]:


def create_waffle_chart(categories, values, height, width, colormap, value_sign=''):

    # compute the proportion of each category with respect to the total
    total_values = sum(values)
    category_proportions = [(float(value) / total_values) for value in values]

    # compute the total number of tiles
    total_num_tiles = width * height # total number of tiles
    print ('Total number of tiles is', total_num_tiles)
    
    # compute the number of tiles for each catagory
    tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]

    # print out number of tiles per category
    for i, tiles in enumerate(tiles_per_category):
        print (dataframe.index.values[i] + ': ' + str(tiles))
    
    # initialize the waffle chart as an empty matrix
    waffle_chart = np.zeros((height, width))

    # define indices to loop through waffle chart
    category_index = 0
    tile_index = 0

    # populate the waffle chart
    for col in range(width):
        for row in range(height):
            tile_index += 1

            # if the number of tiles populated for the current category 
            # is equal to its corresponding allocated tiles...
            if tile_index > sum(tiles_per_category[0:category_index]):
                # ...proceed to the next category
                category_index += 1       
            
            # set the class value to an integer, which increases with class
            waffle_chart[row, col] = category_index
    
    # instantiate a new figure object
    fig = plt.figure()

    # use matshow to display the waffle chart
    colormap = plt.cm.coolwarm
    plt.matshow(waffle_chart, cmap=colormap)
    plt.colorbar()

    # get the axis
    ax = plt.gca()

    # set minor ticks
    ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
    ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
    # add dridlines based on minor ticks
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

    plt.xticks([])
    plt.yticks([])

    # compute cumulative sum of individual categories to match color schemes between chart and legend
    values_cumsum = np.cumsum(values)
    total_values = values_cumsum[len(values_cumsum) - 1]

    # create legend
    legend_handles = []
    for i, category in enumerate(categories):
        if value_sign == '%':
            label_str = category + ' (' + str(values[i]) + value_sign + ')'
        else:
            label_str = category + ' (' + value_sign + str(values[i]) + ')'
            
        color_val = colormap(float(values_cumsum[i])/total_values)
        legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

    # add legend to chart
    plt.legend(
        handles=legend_handles,
        loc='lower center', 
        ncol=len(categories),
        bbox_to_anchor=(0., -0.2, 0.95, .1)
    )
    plt.show()


# In[25]:


#data form of list
Data = [['Country', 'Continent', 'Region', 'DevName', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', 'Total'], ['Denmark', 'Europe', 'Northern Europe', 'Developed regions', 272, 293, 299, 106, 93, 73, 93, 109, 129, 129, 118, 111, 158, 186, 93, 111, 70, 83, 63, 81, 93, 81, 70, 89, 89, 62, 101, 97, 108, 81, 92, 93, 94, 81, 3901], ['Norway', 'Europe', 'Northern Europe', 'Developed regions', 116, 77, 106, 51, 31, 54, 56, 80, 73, 76, 83, 103, 74, 92, 60, 65, 70, 104, 31, 36, 56, 78, 74, 77, 73, 57, 53, 73, 66, 75, 46, 49, 53, 59, 2327], ['Sweden', 'Europe', 'Northern Europe', 'Developed regions', 281, 308, 222, 176, 128, 158, 187, 198, 171, 182, 130, 167, 179, 203, 192, 176, 161, 151, 123, 170, 138, 184, 149, 161, 129, 205, 139, 193, 165, 167, 159, 134, 140, 140, 5866]]
dict_data={}
for i in range(len(Data[0])):
    dict_data[Data[0][i]]=[Data[1][i],Data[2][i],Data[3][i]]
print("Dictionary Data : ",dict_data,sep="\n\n")
dataframe = pd.DataFrame(dict_data)
dataframe.set_index("Country",inplace=True)
print("\n\n\nDataframe created from dictionary : ",dataframe,sep="\n\n")


# In[26]:


create_waffle_chart(dict_data['Country'],dict_data['Total'],10,40,plt.cm.coolwarm)


# In[ ]:




