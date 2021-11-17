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