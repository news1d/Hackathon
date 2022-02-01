from distutils.log import debug
import sqlite3


def get_idea():
    try:
        con = sqlite3.connect('db_of_ideas.db')
        cursor = sqlite3.cursor()
    except Exception as ex:
        print("db is not exist")
        exit(1)
    max_id = cursor.execute("""SELECT id FROM ideas ORDER BY id DESC LIMIT 1""").fetchone()
    return cursor.execute("""SELECT idea FROM ideas WHERE id = ?""",(random.randint(1,max_id[0]),)).fetchone()

def insert_idea(idea):
    try:
        con = sqlite3.connect('db_of_ideas.db')
        cursor = sqlite3.cursor()
    except Exception as ex:
        print("db is not exist")
        exit(1)
    cursor.execute("""INSERT INTO ideas(idea) VALUES (?)""",(idea)) #idea должен быть string
    con.commit()