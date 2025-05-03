import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM items")
db.execute("DELETE FROM reviews")

user_count = 1000
item_count = 10**5
review_count = 10**6

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username) VALUES (?)",
               ["user" + str(i)])

for i in range(1, item_count + 1):
    db.execute("INSERT INTO items (title) VALUES (?)",
               ["recipe" + str(i)])

for i in range(1, review_count + 1):
    user_id = random.randint(1, user_count)
    item_id = random.randint(1, item_count)
    db.execute("""INSERT INTO reviews (item_id, user_id, rating, comment)
                  VALUES (?, ?, ?, ?)""",
               [item_id, user_id, "2", "message" + str(i)])

db.commit()
db.close()
