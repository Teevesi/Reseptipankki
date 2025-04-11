import db

def add_item(title, ingredients, instructions, user_id):
    sql = """INSERT INTO items (title, ingredients, instructions, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, ingredients, instructions, user_id])


def get_items():
    sql = "SELECT id, title FROM items ORDER BY title"
            
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT 
                I.title,
                I.ingredients,
                I.instructions,
                U.username
            FROM 
                items I, users U
            WHERE
                I.user_id = U.id
            AND
                I.id = ?
        """
    return db.query(sql, [item_id])[0]