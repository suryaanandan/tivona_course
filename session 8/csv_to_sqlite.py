# Question 3

import csv
import sqlite3

connection = sqlite3.connect('BookSore.db')

cursor = connection.cursor()

# Create table
cursor.execute('DROP TABLE IF EXISTS Dooks_Details')
cursor.execute("CREATE TABLE Dooks_Details (book_id text PRIMARY KEY, title text, author text, binding text, pages text, price text, isbn text, image_url text)")
connection.commit()


# Load the CSV file into CSV reader
csvfile = open('100books.csv')
books = csv.reader(csvfile, delimiter=',', quotechar='|')

# Iterate through the CSV reader, inserting values into the database
for book in books:
    cursor.execute('INSERT INTO  Dooks_Details VALUES (?,?,?,?,?,?,?,?)',  (book[0], book[1], book[2], book[3], book[4],book[5], book[6], book[7]))
print("Table created and values inserted successfully")
# Close the csv file, commit changes, and close the connection

csvfile.close()

connection.commit()

connection.close()

