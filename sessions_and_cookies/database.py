import sqlite3
import bcrypt


def initialise():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Users(
            email TEXT NOT NULL PRIMARY KEY,
            hashedpassword TEXT,
            name TEXT)''')
    conn.commit()
    conn.close()


def add_user(email, password, name):
    conn = sqlite3.connect('database.db')
    with conn:
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
        query = "INSERT INTO users (email, hashedpassword, name) VALUES (?,?,?)"
        cursor.execute(query, (email, hashed_password, name))
        return True


def get_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    conn.close()
    return users


def check_user(email, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = "SELECT hashedpassword FROM users WHERE email = '" + email + "'"
    cursor.execute(query)

    hashed_password = cursor.fetchone()[0]

    # If there is no username returned
    if hashed_password is None:
        return False

    # If there is a user
    if bcrypt.checkpw(password.encode('utf8'), hashed_password.encode('utf8')):
        return True

    return False


def change_pass(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

    query = ("UPDATE users SET password = '"+hashed_password+"' WHERE username ='"+username+"' ")
    cursor.execute(query)
    conn.commit()
    conn.close()


def add_art(art_name, description, price, quantity):
    conn = sqlite3.connect('database.db')
    with conn:
        cursor = conn.cursor()
        query = "INSERT INTO art " \
                "(art_name, description, price , quantity) " \
                "VALUES " \
                "('" + art_name + "','" + description + ",'" + price + "','" + quantity + "')"
        cursor.execute(query)


def delete_art(art_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM art WHERE art_id='" + art_id + "'")
    conn.commit()
    conn.close()


def check_art(art_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM art WHERE art_id = '" + art_id + "'")

    quantity = cursor.fetchone()

    if quantity is None:
        return False

    else:
        return True


def add_comment(username, comment, artID):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comments (username, comment, artID) VALUES ('" +username+ "','"+comment+"','"+artID+"')")
    conn.close()


def delete_comment(commentID):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM art WHERE commentID='" + commentID + "'")
    conn.close()

initialise()