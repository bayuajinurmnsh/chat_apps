import sqlite3
from sqlite3 import Error


def create_connection():
    # create a database connection to the SQLite database
    conn = None
    try:
        conn = sqlite3.connect('chatApps_db')
    except Error as e:
        # error handling if db error
        print(e)
    return conn


def select_all_users():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_users")

    rows = cur.fetchall()
    output = []
    for row in rows:
        user_data = {}
        user_data['username'] = row[0]
        user_data['password'] = row[1]
        user_data['name'] = row[2]
        user_data['gender'] = row[3]
        user_data['birthdate'] = row[4]
        user_data['created_date'] = row[5]
        output.append(user_data)
    return output


def get_specified_user(username):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_users WHERE username=?", (username,))
    rows = cur.fetchall()
    if len(rows) > 0:
        output = []
        for row in rows:
            output.append(row[0])
        data = output[0]
        return data
    else:
        data = 0
        return data


def insert_user(data):
    # check data before insert
    sql = ''' INSERT INTO tbl_users(username, password, name, gender, birthdate, created_date)
              VALUES(?,?,?,?,?,?) '''
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    data_changes = conn.total_changes
    if data_changes != 0:
        return True
    else:
        return False
