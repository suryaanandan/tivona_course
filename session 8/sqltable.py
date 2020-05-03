# Question 4

import pymysql

connection = pymysql.connect(host ="localhost", user = "root", password = "root", database = "SuperMarket")
cursor = connection.cursor()
cursor.execute("drop table if esists stocks")
cursor.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
connection.commit()

# Do this instead
t = ('RHAT',)
cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
cursor.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

connection.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connection.close()

print("Done!!")

