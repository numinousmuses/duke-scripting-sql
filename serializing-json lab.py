#!/usr/bin/env python
# coding: utf-8

# Work with JSON files, Python, and Python dictionaries, to load, alter, and then save data back to disk in this notebook

# ## Serialize JSON from Python
# You can serialize to and from JSON in Python using the `json` module

# In[4]:


# the JSON module can take certain Python data structures like dictionaries and convert them to JSON
import json


# From Python, convert a dictionary into a JSON string

# In[ ]:


data = {"grape": "Cabernet Franc", "species": "Vitis vinifera", "origin": "Bordeaux, France"}


# In[ ]:


# Convert Python data to JSON. The `.dumps()` method takes a data structure as input and provides a JSON string as output
# mnemonic: dumps -> DUMP to String
json.dumps(data)


# In[ ]:


# Convert a JSON string into a Python data structure
# first, define the json data with the string data
json_data = json.dumps(data)
json_data


# In[ ]:


# Now load it into Python
# mnemonic: loads -> LOAD from String
json.loads(json_data)


# In[ ]:


# Python dictionaries are not the only data structure allowed. Use lists as well
collection = [data, data]
print(collection)
# may look similar in the output, but the difference is that JSON is now a string
json.dumps(collection)


# ## JSON Formatting
# 
# The `json` module in Python allows more than just loading and parsing JSON. It can be used to format it nicely. Formatting is crucial when dealing with nested data (a dictionary within a dictionary for example). 
# 
# It is common for HTTP APIs and JSON files to present JSON as a single line. In this section, you will use formatting options in the JSON module to improve the readability of nested information in JSON.

# In[15]:


# define a nested data structure in a single line
grape_data = {"name": "Cabernet France", "regions": [{"country": "France", "sub-regions": ["Bordeaux", "Loire Valley"]},{"country": "Italy", "sub-regions": ["Apulia", "Tuscany"]}, {"country": "Argentina", "sub-regions": ["Mendoza", "Lujan de Cuyo", "Salta"]}]} 
# Serialize the Python dictionary to a JSON string, but using extra formatting options, like sorted keys
# and using 4 spaces for indentation
data_as_json = json.dumps(grape_data, sort_keys=True, indent=4)
print(data_as_json)


# In[16]:


# Try other variations like indenting 2 spaces and not sorting keys:
data_as_json = json.dumps(grape_data, sort_keys=False, indent=2)
print(data_as_json)


# ## Serialize JSON from a file
# Python can read JSON files and load them as Python data structures, which can also be saved back to the file system as a valid JSON file. In the next few cells, read a JSON file from the file system, and then use the `json` module to parse the JSON and load it into Python.
# 
# The process of reading a foreign format like JSON and loading it into Python is called serializing it.

# In[ ]:


# There are JSON files in the `sample_data/` directory. When working with paths, always ensure these paths are reachable and correct
import os
os.path.exists('sample_data/wine-ratings.json')


# In[ ]:


# read the JSON file and then parse it using the `.load()` method
# note the subtle difference, this is the `.load()` method (no 's'), not `.loads()`
with open('sample_data/wine-ratings.json') as f:
    loaded_json = json.load(f)
print(loaded_json.keys())
print(f"Number of items: {len(loaded_json['name'])}")


# ## Serialize from Python to a JSON file
# 
# Now that you've loaded JSON from a file into Python, do some data sampling, extract some interesting fields and then save the newly manipulated data to a file on disk as JSON.

# In[ ]:


# sample some items from the json file and then save it as a new file
names = loaded_json['name']
len(names)


# In[ ]:


# these names are using an index, like {"0": "Some Name and Year"}. Update the data to use a list of only the names
names_only = list(names.values())
names_only


# In[ ]:


# now use the `.dump()` JSON method (note no 's'!) to save it to a new JSON file
with open('sample_data/wine_names.json', 'w') as f:
    json.dump(names_only, f)

