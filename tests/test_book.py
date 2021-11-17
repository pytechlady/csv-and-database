import unittest
from unittest import result
from models.book import Book
from models.user import User

class TestBook(unittest.TestCase):
    def setUp(self):
        self.database = Book()
        self.user = User()
        
    
    def test_create_table(self):
        result = '''CREATE TABLE book(id serial PRIMARY KEY, name varchar(50) NOT NULL, pages integer NOT NULL)''';
        self.assertIsNotNone(self.user.create_table, result)
        
    
    def test_populate_table(self):
        result = '''INSERT INTO book(id, name, user_id, pages) VALUES(6, 'Adele', 7, 98)''';
        self.assertIsNotNone(self.user.populate_table, result)
        
    def test_get_all_books(self):
        result = 'SELECT * FROM book';
        self.assertIsNotNone(self.database.get_all_book, result)
        
    def test_get_book(self):
        result = f'SELECT * FROM book WHERE id = 4';
        self.assertIsNotNone(self.database.get_book, result)
        
    def test_create_book(self):
        result = '''INSERT INTO book(name, user_id, pages) VALUES('bessin', 3, 90)''';
        self.assertIsNotNone(self.database.create_book, result)
        
    def tearDown(self):
        self.database = Book()