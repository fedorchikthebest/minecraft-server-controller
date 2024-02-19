import sqlite3

con = sqlite3.connect('./config.db')
cur = con.cursor()
password = str(cur.execute('''SELECT znach FROM settings
                            WHERE name == "password"''').fetchone()[0])
port = cur.execute('''SELECT znach FROM settings
                            WHERE name == "port"''').fetchone()[0]
con.close()
