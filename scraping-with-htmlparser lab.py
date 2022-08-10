#!/usr/bin/env python
# coding: utf-8

# ## Simple parsing with HTMLParser
# 
# In this notebook you will practice one of the workflows for using `HTMLParser` effectively. As you already know, `HTMLParser` is a streaming parser, where data comes in with chunks. Each chunk of data has delimeters like tags. 
# 
# It might feel a bit complicated to have special methods to look at tags, and others to process data - this is one of the caveats of using a streaming parser.
# 
# For this exercise, you will use predefined HTML variables with raw content that can be parsed. Instead of requesting the data from the web, the content is already defined and available to be processed. The process is the same to scrape the html.

# In[1]:


content = """
<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>1992 World Junior Championships in Athletics – Men's high jump - Wikipedia</title>
"""


# Now that the data is available, import the html modules so that you can write the class next. The class has to have the `__init__()` method and set some class attributes.

# In[5]:


from html.parser import HTMLParser

class Parser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.recording = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.recording = True
        else:
            self.recording = False
            
    def handle_data(self, data):
        if self.recording:
            print(f"Found data for tag: {repr(data)}")
            


# In[6]:


p = Parser()
p.feed(content)


# Why is `handled_data()` printing twice? The second line appears to have an _empty_ data. Here is one way to find out: update the `handle_data()` method so that it displays the string with the `repr()` built-in function:
# 
# ```python
#     def handle_data(self, data):
#         if self.recording:
#             print(f"Found data for tag: {repr(data)}")
# ```
# 
# Run the cell where the class lives and re-run the Parser cell again to see if you spot the problem

# In[7]:


# repr() helps when there are hidden characters that `print()` wouldn't show. 
empty = ""
print(f"A string with an empty string var wouldn't show the variable: {empty}")
print(f"A string with an empty string var wouldn't show the variable: {repr(empty)}")


# Think about what changes could you make to prevent two lines showing in the output. There are several approaches you could take to improve the quality of the data gathering, and the previous cells showed one. But what if you are also dealing with newline characters? Or other non-visible characters? An alternative you could try is to append the data found to a list instead of printing, and when the parsing is completed, joining the data found.
# Here is how that would look with an example data.

# In[8]:


captured_data = ["1992 World Junior Championships in Athletics – Men's high jump", "\n", "\n", "Wikipedia"]
print(''.join(captured_data))


# In[ ]:




