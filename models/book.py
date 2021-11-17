import psycopg2



class Book:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(database='mydatabase', user='myuser', password='1234', host='localhost', port='5432')
            self.cursor = self.conn.cursor()
            
        except:
            print('Database not connected')
            
        
            
    def get_all_book(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()
    
    def get_book(self, id):      
        self.cursor.execute(f"SELECT * FROM books WHERE id={id}")
        return self.cursor.fetchall()
    
    def create_book(self, name, user_id, pages):
        try:
            self.cursor.execute('INSERT INTO books(name, user_id, pages)'
                                'VALUES(%s,%s,%s)',
                                (name, user_id, pages))
            self.conn.commit()
            
        except:
            print(f"error {name} already exists")