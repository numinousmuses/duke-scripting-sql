#!/usr/bin/env python
# coding: utf-8

# Use all the new skills you've learned for iterating over data structures like dictionaries and lists to practice in this notebook.

# # Data structures
# The trick is that it is all about state!

# ## Lists
# Lists are easy to encounter and easy to abuse. Lists hold individual items, keeping a specific order. To access them, treat the order like an index. The index starts at `0,` and it continues incrementally every time a new item gets added. A loop (sometimes referred to as *"for loop"*) is the most common operation you can encounter.

# In[2]:


directories = ['Documents', 'Music', 'Desktop', 'Downloads', 'Pictures', 'Movies']
for directory in directories:
  print(directory)


# In[3]:


import os
for item in os.listdir('sample_data'):
  if os.path.isdir(item):
    print("This is a directory {0}".format(item))
  else:
    print("This is a file: {0}".format(item))


# In[4]:


# Looping is easy, but what about state? 
# here state is captured in a new variable called `important_directories`
important_directories = []
for item in os.listdir('.'):
  if os.path.isdir(item):
    important_directories.append(item)
print(important_directories)


# In[11]:


os.listdir('.')


# In[6]:


important_directories = []
for item in os.listdir('.'):
  if item.startswith('.'):
    continue # flow control!
  if os.path.isdir(item):
    important_directories.append(item)
print(important_directories)


# In[7]:


items = ['first', 'second', 'third', 'foo']
#items[-1]
url = "https://colab.research.com/drive/asdfjhasdf/alfredo/oreilly"

parts = url.split('/')
#print(parts)
# Everything except the first three items
#print(parts[3:])
#protocol, _, fqdn = parts[:3]
#print("protocol is: %s" % protocol)
#print(fqdn)
#company = parts[-1]
#print(company)

#print("The first item is: {0}".format(items[0]))

#items[1]

# you can also 'ask' for a given item:
items.index('foo')
# watchout for `ValueError` though!
#items.index('fifth')


# ## Tuples
# Should be treated as "read only" lists, the differences are subtle!

# In[8]:


ro_items = ('first', 'second', 'third')
print("first item in the tuple is: %s" % ro_items.index('first'))
print(ro_items[-1])
for item in ro_items:
    print(item)


# In[9]:


# expect an error here, just like a list!
ro_items[9]


# In[ ]:


# same with indexes
ro_items.index('fifth')


# In[12]:


# find out what methods are available in a tuple
for method in dir(tuple()):
  if method.startswith('__'):
    continue
  print(method)


# In[14]:


# tuples are inmmutable
ro_items.append('a')


# ## List Comprehensions
# So easy to abuse!

# In[ ]:


items = ['a', '1', '23', 'b', '4', 'c', 'd']
numeric = []
for item in items:
  if item.isnumeric():
    numeric.append(item)
print(numeric)


# In[ ]:


# notice the `if` condition at the end, is this more readable? or less?
inlined_numeric = [item for item in items if item.isnumeric()]
inlined_numeric


# In[ ]:


# doubly nested items are usually targetted for list comprehensions
items = ['a', '1', '23', 'b', '4', 'c', 'd']
nested_items = [items, items]
nested_items


# In[ ]:


numeric = []
for parent in nested_items:
    for item in parent:
      if item.isnumeric():
        numeric.append(item)
numeric


# In[ ]:


# and now with list comprehensions
numeric = [item for item in parent for parent in nested_items if item.isnumeric()]
numeric


# In[ ]:


# this can improve readability
numeric = [
    item for item in parent
        for parent in nested_items
            if item.isnumeric()
]
numeric


# ## The awesome dictionary
# One of my favorite data structures in Python, learning it can yield inmense benefits.

# In[ ]:


# dictionaries are mappings, usually referred to as key/value mappings
contacts = {
    'alfredo': '+3 678-677-0000',
    'noah': '+3 707-777-9191'
}
contacts


# In[ ]:


contacts['noah']


# In[ ]:


# you can get keys as list-like objects
contacts.keys()


# In[ ]:


# or you can get the values as well
contacts.values()


# In[ ]:


# looping over dictionaries default to `.keys()` and you can loop over both keys and values
for key in contacts:
  print(key)
for name, phone in contacts.items():
  print("Key: {0}, Value: {1}".format(name, phone))


# In[ ]:


# you should treat dictionaries like a small database, with cheap (and fast!) access
contacts['alfredo']
contacts['John']


# In[ ]:


# super nice way to "fallback" when things do not exist
print(contacts.get('John', "Peter"))
try:
  contacts['John']
except KeyError:
  print("Peter")


# ## Walking the filesystem, inspecting files
# Python has built-in utilities to walk the filesystem. It is a bit clunky, and creating something useful requires stitching things together to produce good output
# 

# In[ ]:


import os

# yields the 'current' dir, then the directories, and then any files it finds
# for each level it traverses
for path_info in os.walk('.'):
    print(path_info)
    break


# In[ ]:


import os
from os.path import abspath, join

# producing absolute paths, instead of a tuple of three items
for top_dir, directories, files in os.walk('.'):
    for directory in directories:
        print(abspath(join(top_dir, directory)))
    for _file in files:
        print(abspath(join(top_dir, _file)))
    break


# In[ ]:


# Now that absolute paths are shown, we can inspect them for file metadata

import os
from os.path import abspath, join, getsize

sizes = {}

for top_dir, directories, files in os.walk('.'):
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size
        #break

sorted_results = sorted(sizes, key=sizes.get, reverse=True)

for path in sorted_results[:10]:
    print("Path: {0}, size: {1}".format(path, sizes[path]))

