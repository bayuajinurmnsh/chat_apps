import sqlite3

# DON'T RUN THIS FILE IF file (db_name.db) has already exists

conn = sqlite3.connect("chatApps_db")
cursor = conn.cursor()

cursor.execute('''
          CREATE TABLE IF NOT EXISTS tbl_users
          ( [username] VARCHAR(16) PRIMARY KEY,
            [password] VARCHAR(16),
            [name] VARCHAR(30),
            [gender] VARCHAR(6),
            [birthdate] DATE,
            [created_date] DATETIME )
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS tbl_chat
          ( [chat_id] INTEGER PRIMARY KEY,
            [text_chat] TEXT,
            [id_sender] VARCHAR(16),
            [id_receiver] VARCHAR(16),
            [send_at] DATETIME
            )
          ''')

conn.commit()
