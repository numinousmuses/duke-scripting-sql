#!/usr/bin/env python
# coding: utf-8

# In this practice notebook, you'll interact with SQLite, a fully compliant SQL database that is supported by Python without any extras needed. We will go through some of the details of connecting to a SQLite database and the differences between some of the options for creating one.

# ## Connecting to SQlite
# There are different ways to connect to a SQLite database. For most connections to databases including SQLite you will need a connection object and a cursor. The connection allows you to communicate with the database while the cursor is what executes the query.
# Start by connecting to an in-memory database first.

# In[1]:


# SQLite can run in-memory, no file will be created, and when the program ends, the database goes away
import sqlite3
connection = sqlite3.connect(':memory:')


# You now have a connection object, and a running database that lives in-memory while this program runs. The next step is to create some tables for the database

# ## Creating a table

# In[2]:


# define the query to create a table to hold file paths and sizes in bytes for those files
table = 'CREATE TABLE files (id integer primary key, path TEXT, bytes INTEGER)'


# There are two steps for executing the query. First we use the cursor to execute it, and then we commit the result to the database.

# In[4]:


cursor = connection.cursor()
cursor.execute(table)
connection.commit()


# Try running the previous code block again. What happens? Is there an error? Why do you think there is an error?

# ## Adding data 
# Now add a single entry into the database. The steps are to execute the query with the cursor and then commit with the `connection` object.
# 
# **Exercise:** Try adding more entries to the database, ensure that there aren't any errors

# In[6]:


cursor.execute('INSERT INTO files (path, bytes) VALUES("/home/user/.zshrc", 101)')
connection.commit()


# You can query the database with a minimal instruction to check if the addition was succesful. The query is done with the cursor, just like before. And the resulting object that the cursor returns is an iterable that you can use to loop over the results:

# In[7]:


result = cursor.execute('SELECT * from files')
for line in result:
    print(line)


# The SQLite database in this notebook is ephemeral: since it was created in-memory, it will go away (along with the data) once you terminate the program.
