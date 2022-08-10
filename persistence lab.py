#!/usr/bin/env python
# coding: utf-8

# # Persistence and Efficency
# You now might be aware of some of the problems with parsing several pages and how that can quicly get out of hand. While parsing, you might chose to persist the collected data, so that it can be analyzed and cleaned later. 
# Parsing, retrieving, saving, and cleaning data are all separate actions, and you shouldn't try to work with data while collecting. In this notebook you'll practice further parsing techniques along with persistency, both for JSON and CSV formats as well as using SQL and a database.
# 
# Start by loading one of the available HTML files into the `scrapy` library

# In[1]:


# If you haven't already created an activated a virtual environment for this notebook, run this cell
get_ipython().system('python3 -m venv venv')
get_ipython().system('source venv/bin/activate')
get_ipython().system('pip install -r requirements.txt')


# In[4]:


import scrapy
import os
current_dir = os.path.abspath('')
url = os.path.join(current_dir, "html/1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump")
with open(url) as _f:
    url_data = _f.read()

response = scrapy.http.TextResponse(url, body=url_data, encoding='utf-8')


# In[5]:


# Make sure that the interesting data is available 
table = response.xpath('//table')[1].xpath('tbody')
for tr in table.xpath('tr'):
    print(tr.xpath('td/b/text()').extract()[0],
          tr.xpath('td/a/text()').extract()[0]
    )


# This interaction with `scrapy` in a Jupyter Notebook is useful because you don't need to run the special shell and you also don't need to run the whole spider. Once you learn what you need to do here, you can adapat the spider to persist data.
# First, start by persisting data as JSON. To do this, you will need to keep the information in a Python data structure like a dictionary, and then load it as a JSON object, and finally, save it to a file.

# In[6]:


scrapped_data = {}
for tr in table.xpath('tr'):
    medal = tr.xpath('td/b/text()').extract()[0]
    athlete = tr.xpath('td/a/text()').extract()[0]
    scrapped_data[medal] = athlete

scrapped_data


# In[7]:


import json

# You can convert Python into JSON first, but there is no need if you use `json.dump()`
# as shown next
json_data = json.dumps(scrapped_data)

# Persist it in a file:
with open("1992_results.json", "w") as _f:
    # use dump() with the Python dictionary directly. 
    # the conversion is done on the fly
    json.dump(scrapped_data, _f)


# Now that you can persist the scrapped data as JSON, you can also use CSV. This is specially useful if you want to to some data science operations. Although you can use an advanced library like Pandas for this, you can use the standard library CSV module from Python.

# In[8]:


# construct the data first

column_names = ["Medal", "Athlete"]
rows = []

for tr in table.xpath('tr'):
    medal = tr.xpath('td/b/text()').extract()[0]
    athlete = tr.xpath('td/a/text()').extract()[0]
    rows.append([medal, athlete])


# In[9]:


# Now persist it to disk
import csv

with open("1992_results.csv", "w") as _f:
    writer = csv.writer(_f)

    # write the column names
    writer.writerow(column_names)

    # now write the rows
    writer.writerows(rows)


# Finally, you can persist data to a database. Unlike the JSON and CSV approach, using a database is much more memory efficient. This is the principal reason why you want to use a database instead of a file on disk. Imagine capturing 10GB of data. This could potentially mean that you need 10GB of available memory to hold onto that data before saving it to disk.
# By using a database, you can save the data as the data is gathered. 
# 
# For the next cells, use a SQLite database to persist the data. Create the file-based database and the table needed.

# In[10]:


import sqlite3
connection = sqlite3.connect("1992_results.db")
db_table = 'CREATE TABLE results (id integer primary key, medal TEXT, athlete TEXT)'
cursor = connection.cursor()
cursor.execute(db_table)
connection.commit()


# In[11]:


# Now it is time to persist the data. Open the connection again
connection = sqlite3.connect("1992_results.db")
cursor = connection.cursor()
query = 'INSERT INTO results(medal, athlete) VALUES(?, ?)'

for tr in table.xpath('tr'):
    medal = tr.xpath('td/b/text()').extract()[0]
    athlete = tr.xpath('td/a/text()').extract()[0]
    cursor.execute(query, (medal, athlete)) 
    connection.commit()


# The data is now persisted in a file-based database that you can query. Verify that all works by creating a new connection and querying the database.
# 
# Update the _wikipedia_ project and spider to use some of these techniques to persist data. Next, try parsing all the files in the _html_ directory instead of just one and persist all results. Do you think you can parse other information as well? 
# 
# Try parsing the height and the results from all the other athletes, not just the top three places.
