import sqlite3
import tensorflow as tf

#Assumes database is in top level data directory
con = sqlite3.connect('./data/database.sqlite')
con.row_factory = lambda cursor, row: row[0]
con.text_factory = str

#short = pd.read_sql_query(""" 
#                            SELECT Summary
#                            FROM Reviews
#                        """, con)
#print((short.head(20)))
reviews = con.execute('SELECT Text FROM Reviews').fetchall()


