import sqlite3
import queries

class Database:
    
    def __init__(self):
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
        #print('EXECUTING: ',    query)
        c.execute(query)
        conn.commit()
        conn.close()


    def get_item(self, selects, table, attribute, value):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        query = queries.select_generic_query % (selects, table, attribute)
        args = (value,)
        c.execute(query, args)
        result = c.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_all(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        results = []
        for query in queries.get_all_query:
            c.execute(query)
            for item in c.fetchall():
                results.append(item)
    
        conn.commit()
        conn.close()
        return results

    def delete_profile(self, selects,table):
        #   Selects = profile_id
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        query = queries.delete_profile_query % (table)
        c.execute(query)
        conn.commit()
        conn.close()
          
    def update_page(self,page_id,page_name,admin,category,description):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('UPDATE PAGE SET page_name = ?, admin = ?, category = ?,'
                  'description = ? WHERE page_id = ?',
        (page_name,admin,category,description,page_id))                                          
        conn.commit()
        conn.close()


    def get_next_id(self, table):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        query = queries.count_query % (table)
        c.execute(query)
        result = int(c.fetchone()[0])
        conn.commit()
        conn.close()
        return result
