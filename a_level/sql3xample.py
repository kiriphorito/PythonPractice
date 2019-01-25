import sqlite3

# conn = sqlite3.connect("example.db")
#
# cursor = conn.cursor()
#
# result = cursor.execute("SELECT * FROM users")
#
# for record in result:
#     print(result)
#
# conn.close()
#
# def addUser(id, username, password):
#     conn = sqlite3.connect("example.db")
#     cursor = conn.cursor()
#     query = "INSERT INTO users VALUES (" + str(id) + ",'" + username + "','" + password + "')"
#     print(query)
#     try:
#         cursor.execute(query)
#         # pass
#     except:
#         print("Someone with this ID already exists!")
#     conn.commit()
#     conn.close()
#
#
# addUser(3, "Sam','password'); DROP TABLE users;", "password")
#


# def addUser(data):
#     with sqlite3.connect("example.db") as conn:
#         cursor = conn.cursor()
#         try:
#             cursor.executemany("INSERT INTO users VALUES (?,?,?)", data)
#             # pass
#         except:
#             print("Someone with this ID already exists!")
#
# data = [
#     (1,"Sam", "Password"),
#     (2,"Rae", "qwerty"),
#     (3,"Kiriphorito", "Kiri"),
# ]
#
#
# addUser(data)

def showAllUsers():
    with sqlite3.connect("example.db") as conn:
        cursor = conn.cursor()
        try:
            result = cursor.execute("SELECT * FROM users")
        except:
            print("There seems to be an error somewhere!")
        for record in result:
            print(record)


showAllUsers()