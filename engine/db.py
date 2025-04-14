import csv
import sqlite3
from winreg import QueryValue, QueryValueEx

con =sqlite3.connect("jarvis.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
# cursor.execute(query)
# 

# 

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)


# query = "INSERT INTO web_command VALUES (null, 'youtube', 'https:\\www.youtube.com\\')"
# cursor.execute(query)
# con.commit()

# cursor.execute("DELETE FROM web_command WHERE id = 6")  => this is used to delete the extry rows if inserted

#testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])

# Create a table with the desired columns


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0,18]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))
# Insert Single contacts (Optional)

# ```bash
# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890')"
# cursor.execute(query)
# con.commit()
# Commit changes and close connection
# con.commit()
# con.close()

#for searching
# query = 'shiva'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + QueryValue + '%', QueryValueEx + '%'))
# results = cursor.fetchall()
# print(results[0][0])

