#!/usr/bin/env python
# coding: utf-8

# # Word Cloud Chart Using Andreas Mueller Library WordCloud

# In[17]:


# imports
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle Charts
import pandas as pd
import numpy as np 
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
mpl.style.use('ggplot') # optional: for ggplot-like style

# check for latest version of Matplotlib
print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0


# ## Load Data

# In[18]:


alice_novel = open('WordCloud/Data_Source.txt', 'r').read()    
print ('File downloaded and saved!')


# ### Create Unique Stopwords

# In[19]:


stopwords = set(STOPWORDS)
str(stopwords)


# ### create WordCloud Object

# In[20]:


alice_wc = WordCloud(
    background_color='white',
    max_words=200000,
    stopwords=stopwords
)

# generate the word cloud with 2000 word to save time
alice_wc.generate(alice_novel)


# ### Plot The Word Cloud

# In[21]:


plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# ### let's create size of plot bigger so we can able to small frq. word also

# In[22]:


fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

# display the cloud
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# ### Now Let's Create Word Cloud With masking

# In[23]:


alice_mask = np.array(Image.open('WordCloud/alice_mask.png'))
    
print('Image downloaded and saved!')


# In[24]:


fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[26]:


alice_wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, stopwords=stopwords)

# generate the word cloud
alice_wc.generate(alice_novel)

# display the word cloud
fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.title("WordCloud Looks Amazing isn't it??")
plt.show()

