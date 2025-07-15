import sqlite3

def init_db():
    conn=sqlite3.connect("jeff.db")
    c=conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            user_id TEXT,
            username TEXT,
            date TEXT,
            question TEXT,
            answer TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_response(user_id, username, date, question, answer):
    conn = sqlite3.connect("jeff.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO responses (user_id, username, date, question, answer)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, username, date, question, answer))
    conn.commit()
    conn.close()

def get_responses_by_date(date):
    conn = sqlite3.connect("jeff.db")
    c = conn.cursor()
    c.execute("SELECT username, question, answer FROM responses WHERE date = ?", (date,))
    responses = c.fetchall()
    conn.close()
    return responses