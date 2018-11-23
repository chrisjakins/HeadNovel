import sqlite3
import queries

class Database:
    
    def __init__(self, name):
        # create a connection to the database
        self.conn = sqlite3.connect('headnovel.db')

    
    def init_tables(self):
        c = self.conn.cursor()
        c.execute(queries.create_profile_query)
        # add all create table statements here
        # then uncomment below lines
        self.conn.commit()
        self.conn.close()
