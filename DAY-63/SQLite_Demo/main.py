import sqlite3

# We need to create a connection to the database
db = sqlite3.connect("my_demo.db")

# Creating a cursor pointing to that database
cursor = db.cursor()

# Creating a table by using execute()
cursor.execute("create table if not exists employee(id integer primary key, name varchar(45), dept varchar(45), salary float)")

# Inserting data into the table
cursor.execute("insert into employee values(101, 'Sofia', 'Data & AI', 90000)")
cursor.execute("insert into employee values(102, 'Olivia', 'Business Intelligence', 50000)")
cursor.execute("insert into employee values(103, 'Ethan', 'Data Analytics', 60000)")
cursor.execute("insert into employee values(104, 'Liam', 'Data Engineering', 80000)")
cursor.execute("insert into employee values(105, 'Isabella', 'Custom Engineering', 75000)")
cursor.execute("insert into employee values(106, 'Noah', 'Gen AI', 78000)")
cursor.execute("insert into employee values(107, 'Ava', 'Security & Compliance', 89000)")
cursor.execute("insert into employee values(108, 'Jackson', 'Admin Support', 55000)")
cursor.execute("insert into employee values(109, 'Emma', 'Data Quality Management', 74000)")
cursor.execute("insert into employee values(110, 'Alex', 'Salesforce Automation', 60000)")


# We need to commit the changes to the database
db.commit()
