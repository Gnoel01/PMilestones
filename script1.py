import sqlite3

# define connection and cursor

connection = sqlite3.connect('user_contacts.db')

cursor = connection.cursor()
# create users table

command1 = """CREATE TABLE IF NOT EXISTS
users(first_name TEXT PRIMARY KEY, last_name TEXT)"""

cursor.execute(command1)

# create phone table

command2 = """CREATE TABLE IF NOT EXISTS
phone(phone_number INTEGER PRIMARY KEY, first_name TEXT, 
FOREIGN KEY(first_name) REFERENCES users(first_name))"""

cursor.execute(command2)

# add to users

cursor.execute("INSERT INTO users VALUES ('Sandra', 'Dean')")
cursor.execute("INSERT INTO users VALUES ('Kevin', 'Banks')")
cursor.execute("INSERT INTO users VALUES ('Brian', 'Charles')")

# add to phone

cursor.execute("INSERT INTO phone VALUES (7194564423, 'Sandra')")
cursor.execute("INSERT INTO phone VALUES (7195984613, 'Kevin')")
cursor.execute("INSERT INTO phone VALUES (7197682316, 'Brian')")

# get results

cursor.execute("SELECT * FROM phone")

results = cursor.fetchall()
print(results)

# update

cursor.execute("UPDATE phone SET phone_number = 7195985555 WHERE first_name = 'Kevin'")

# delete

cursor.execute("DELETE FROM phone WHERE first_name = 'Brian'")

# get results

cursor.execute("SELECT * FROM phone")

results = cursor.fetchall()
print(results)