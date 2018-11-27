import sqlite3
import queries

class Database:
    
    def __init__(self):
        # create a connection to the database
        self.db_name = 'headnovel.db'

    
    def init_tables(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute(queries.create_profile_query)
        c.execute(queries.create_post_query)
        c.execute(queries.create_comment_query)
        c.execute(queries.create_like_query)
        c.execute(queries.create_message_query)
        c.execute(queries.create_page_query)
        self.populate(c)
        conn.commit()
        conn.close()


    def populate(self, c):
        for query in queries.random_insert_queries:
            c.execute(query)


    def insert_item(self, table, attributes, values):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        query = queries.insert_generic_query % (table, attributes, values)
        c.execute(query)
        conn.commit()
        conn.close()

    def get_user_id(self, username):
        return 10
