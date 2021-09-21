import sqlite3

# DON'T RUN THIS FILE IF file (db_name.db) has already exists

conn = sqlite3.connect("chatApps_db")
query = conn.cursor()

query.execute('''
          CREATE TABLE IF NOT EXISTS tbl_users
          ( [username] VARCHAR(16) PRIMARY KEY,
            [name] VARCHAR(30),
            [gender] VARCHAR(6),
            [birthdate] DATE,
            [created_date] DATETIME )
          ''')

query.execute('''
          CREATE TABLE IF NOT EXISTS tbl_chat
          ( [chat_id] INTEGER PRIMARY KEY,
            [text_chat] TEXT,
            [id_sender] VARCHAR(16),
            [id_receiver] VARCHAR(16),
            [send_at] DATETIME
            )
          ''')

conn.commit()
