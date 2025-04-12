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
                I.id,
                I.title,
                I.ingredients,
                I.instructions,
                U.id user_id,
                U.username
            FROM 
                items I, users U
            WHERE
                I.user_id = U.id
            AND
                I.id = ?
        """
    return db.query(sql, [item_id])[0]

def update_item(item_id, title, ingredients, instructions):
    sql = """UPDATE
                items
            SET
                title = ?,
                ingredients = ?,
                instructions = ?
            WHERE
                id = ? """
    db.execute(sql, [title, ingredients, instructions, item_id])

def remove_item(item_id):
    sql = """DELETE FROM items WHERE id = ?"""
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT
                id, title
            FROM
                items
            WHERE
                title LIKE ? OR ingredients LIKE ?
            ORDER BY
                id DESC
            """
    like = "%" + query + "%"
    return db.query(sql, [like, like])