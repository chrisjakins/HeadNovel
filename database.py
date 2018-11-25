import sqlite3
import queries

class Database:
    
    def __init__(self):
        # create a connection to the database
        self.conn = sqlite3.connect('headnovel.db')

    
    def init_tables(self):
        c = self.conn.cursor()
        c.execute(queries.create_profile_query)
        c.execute(queries.create_post_query)
        c.execute(queries.create_comment_query)
        c.execute(queries.create_like_query)
        c.execute(queries.create_message_query)
        c.execute(queries.create_page_query)
        self.conn.commit()
        self.conn.close()
