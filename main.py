import datetime
import sqlite3 as sql

conn = sql.connect("order_details.db")
cur = conn.cursor()

# Customer table
cur.execute('''
CREATE TABLE IF NOT EXISTS customer (
    cus_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cus_name TEXT,
    address TEXT,
    phno TEXT,
    email TEXT
)
''')

# Orders table
cur.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cus_id INTEGER,
    payment_method TEXT,
    order_item TEXT,
    order_date TEXT,
    total INTEGER,

    FOREIGN KEY(cus_id)
    REFERENCES customer(cus_id)
)
''')

print("Welcome to the login page!!")

name = input("Enter your Name: ")
email = input("Enter your Email id: ")
add = input("Enter your Address: ")

while True:
    phno = input("Enter your Phone number: ")

    if phno.isdigit() and len(phno) == 10:
        break

    print("Invalid phone number")


cur.execute('''
INSERT INTO customer (cus_name, address, email, phno)
VALUES (?, ?, ?, ?)
''', (name, add, email, phno))

cus_id = cur.lastrowid

print("Welcome to our shop")

print('''
Shop items are:
1. Laptops
2. Mobiles
3. Watches
4. Music pods
5. Speakers
''')

x = int(input("Enter the index of what you want to purchase: "))
method = input("Enter the mode of payment: ")

p = datetime.date.today()

if x == 1:
    item = "Laptop"
    total = 85000

elif x == 2:
    item = "Mobiles"
    total = 25000

elif x == 3:
    item = "Watch"
    total = 5000

elif x == 4:
    item = "Music pod"
    total = 3000

elif x == 5:
    item = "Speakers"
    total = 6000

else:
    print("Invalid selection")
    conn.close()
    exit()


cur.execute('''
INSERT INTO orders
(cus_id, payment_method, order_item, order_date, total)

VALUES (?, ?, ?, ?, ?)
''', (cus_id, method, item, str(p), total))

conn.commit()

print("Order placed successfully!")

conn.close()
