import psycopg2



class User:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(database='mydatabase', user='myuser', password='1234', host='localhost', port='5432')
            self.cursor = self.conn.cursor()
            
        except:
            print('Database not connected')
            
        
    def create_table(self):
        with open('schema.sql', 'r') as fd:
            file_name = fd.read()
            self.cursor.execute(file_name)
            self.conn.commit()
            self.conn.close()
            
    def populate_table(self):
        with open('seeder.sql') as fd:
            seeder_values = fd.read()
            self.cursor.execute(seeder_values)
            self.conn.commit()
            self.conn.close()
            
    def get_all_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()
    
    def get_user(self, id):
        self.cursor.execute(f"SELECT * FROM users WHERE id={id}")
        return self.cursor.fetchall()
    
    def create_user(self, username, firstname, lastname):
        self.cursor.execute('INSERT INTO users(username, first_name, last_name)'
                            'VALUES(%s,%s, %s)',
                            (username,firstname,lastname))
        self.conn.commit()