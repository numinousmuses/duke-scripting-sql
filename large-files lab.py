#!/usr/bin/env python
# coding: utf-8

# Go through the basics of creating a Python script, and then create a Python file for the script to run it on the terminal. In this practice notebook, you'll create the building blocks for a script that finds large files on the filesytem

# ## Get the logic right 
# Start by defining some of the requirements of the script. In this case, we need to:
# - _Walk_ the filesystem looking at files, directories and sub-directories
# - Capture file information: is it a file? a directory? what size? what path?
# - Store that information in a suitable data structure
# - Report the sorted data what are the largest files by looking at the data structure

# In[3]:


# The os module is perfect for filesystem operations like "walking" throught directories and files
# Although there are many ways of achieving the same effect, a good way to loop over the filesystem is using `os.walk()`
import os
for root, directories, files in os.walk('.'):
    for _file in files:
        print(f"File found: {_file}")


# In[4]:


# Update the loop so that it shows the absolute path of a file ignoring directories which we aren't going to track
for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        print(f"File found: {full_path}")


# So now we have a few objectives completed:
# - Files are detected
# - Full paths are being collected
# 
# Next, we need to find size information. Python uses bytes by default for size, so in addition to capturing the size, we'll need to find a way to change bytes to megabytes or gigabytes to make it easier to read

# In[5]:


# Update the loop to include the file size
for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        print(f"Size: {size}b - File: {full_path}")


# In[6]:


# Persist the data into a dictionary. Since file paths are unique you can use those as dictionary keys
file_metadata = {}
for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        file_metadata[full_path] = size
print(file_metadata)


# **Exercise:** Now that the metadata is captured and stored in a suitable data structure like a dictionary, report back the results with only the four largest files. Try using other quantities to report on, like the 10 largest files instead of 4.

# In[7]:


items_shown = 0
    
for path, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
    if items_shown > 4:
        break
    print(f"Size: {size} Path: {path}")
    items_shown += 1


# There is a lot happening in the previous cell. `sorted()` is a built-in function that can sort iterables like Python dictionaries. In this case, we need to sort by the _value_. This is done using the `key` parameter which accepts a `lambda`.
# `lambda` allows to represent a function in a single line without defining it. That `lambda` expression is the same as defining a function like:
# 
# ```python
# def by_value(x):
#     return x[1]
# ```
# 
# `x` represents two items, the path and the size. The function is returning only the size because that is what we want to sort with. Try changing the `lambda` expression to use `x[0]` instead and see what happens.
# 
# **Exercise:** Try using a function instead of a `lambda` function and achieve the same result

# In[8]:


items_shown = 0
    
for path, size in sorted(file_metadata.items(), key=lambda x:x[0], reverse=True):
    if items_shown > 4:
        break
    print(f"Size: {size} Path: {path}")
    items_shown += 1

