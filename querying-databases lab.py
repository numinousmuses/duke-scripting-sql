#!/usr/bin/env python
# coding: utf-8

# ## Querying databases
# We've already seen a couple of SQL queries when creating a database table and checking if data was present. Now we will go beyond those basics queries to do slightly more advanced queries, like searching and filtering.

# In[1]:


# Work with an in-memory SQLite database again
import sqlite3
connection = sqlite3.connect(':memory:')


# In[2]:


# Create a table again for holding a path and size, just like before
table = 'CREATE TABLE files (id integer primary key, path TEXT, bytes INTEGER)'
cursor = connection.cursor()
cursor.execute(table)
connection.commit()


# There is a _large_files.py_ file that has a `files` variable which holds a list of tuples with some sample data we can use to populate the database. Import that module and use the list to iterate over it and then populate the database
# 
# In this section you will use a special SQL syntax in SQLite to insert values from Python into the SQL query.

# In[3]:


from large_files import files

for metadata in files:
    query = 'INSERT INTO files(path, bytes) VALUES(?, ?)'
    # the execute() method accepts a query and optionally a tuple with values 
    # corresponding to the question marks in VALUES
    cursor.execute(query, metadata)
    connection.commit()


# So far we've seen `CREATE` and `INSERT`. Let's try a new SQL statement to make a selection. The `SELECT` statement produces a result from one or more tables and from one or many rows. 
# 
# Note the particular (and strict) order of SQL statements:
# 
# - `SELECT`
# - `FROM`
# - `WHERE`
# - `GROUP BY`
# - `HAVING`
# - `ORDER BY`
# 
# Since SQLite returns an iterator as a result always, then it is required to loop over the resulting object. Create a query to count the items in the `files` table. This query will use the `COUNT()` function that produces a number:

# In[4]:


query = 'SELECT COUNT(id) from files'

for i in cursor.execute(query):
    print(i)


# ## Extracting distinct row data
# Counting items is a good way of checking the amount of items that exist in the database. Without using `COUNT(id)` the previous query would've produced two thousand entries. Use the `LIMIT` statement to set the maximum number of entries that can be produced, then remove the `COUNT(id)` function and use `*` instead to use all rows

# In[5]:


query = 'SELECT * from files LIMIT(10)'
for i in cursor.execute(query):
    print(i)


# Using `*` means every row in the table. The table in this case is `files`. The next query specifies using the `id` row only. 
# 
# **Exercise:** Update the cell contents so that it shows paths instead.

# In[24]:


query = 'SELECT id FROM files LIMIT(10)'
for i in cursor.execute(query):
    print(i)


# In[9]:


query = 'SELECT id FROM files LIMIT(10)'
for i in cursor.execute(query):
    print(i, metadata)


# The next query uses ID and Bytes. Update the query once again to select two rows in the table: `bytes` and `path`.

# In[11]:


query = 'SELECT id,bytes FROM files LIMIT(2)'
for i in cursor.execute(query):
    print(i)


# ## Extracting distinct data
# You now know how to extract data from certain rows and how to limit that data. Next, we'll use more SQL statements to further find and filter out results so that you can get specific results.
# 
# **Exercise:** Use the next query to find 10 files that are bigger than 1mb (1000000 bytes) using a new statement (`WHERE`):

# In[13]:


query = 'SELECT path FROM files WHERE bytes>1000000 LIMIT(10)'
for i in cursor.execute(query):
    print(i)


# The query shows the paths but not the sizes. 
# 
# **Exercise:** Try updating the previous query to show both the path and the size. 

# In[20]:


query = 'SELECT path, bytes FROM files WHERE bytes>1000000 LIMIT(10)'
for i in cursor.execute(query):
    print(i)


# SQL has many helper functions, in this case the next query uses `MAX()` which can find the highest value in a column. Do you think that `LIMIT(10)` makes sense in this query? Why? What happens if you remove the `LIMIT(10)` clause?
# 
# **Exercise:** Remote the `LIMIT()` clause and check your results

# In[21]:


query = 'SELECT path,MAX(bytes) FROM files'
for i in cursor.execute(query):
    print(i)


# SQL queries can be compounded for more conditionals. In Python, you can make the query more readable by using triple quotes and adding the queries in a multi-line variable.
# 
# **Exercise:** Use other conditions to match different sizes and limit to a different number of entries returned

# In[23]:


query = """
SELECT path,bytes FROM files 
    WHERE bytes>2500000 
    AND bytes<3700000 LIMIT(100)
"""
for i in cursor.execute(query):
    print(i)


# ## Searching
# Sometimes you can't tell exactly what is it that you are looking for in a query. SQL allows for matching patterns. In the file paths situation, you might know that a specific file ends with `.zip` but you don't know where it is. 
# 
# **Exercise:** Use the `LIKE` operator to match and find a cache file related to an Address Book application.

# In[24]:


query = """
SELECT path,bytes FROM files 
    WHERE path LIKE '%AddressBook%'
"""
for i in cursor.execute(query):
    print(i)


# Using `%` means to match any text of zero or more characters. So `%AddressBook%` is very lenient for anything before it and after it. Try adding a condition that filters the result by size. Anything over 2MB (or 2000000 bytes) and see if you can reduce the amount of output.

# There are other variations for search like using an underscore (`_`). That means any single character. If you know that a file prefix or suffix is, you could use this to fine-tune your search.
# 
# **Exercise:** Use other search items for the paths found in your filesystem and try to match them
