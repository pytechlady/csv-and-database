import unittest
from unittest import result
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.database = User()
        
    
    def test_create_table(self):
        result = '''CREATE TABLE user(id serial PRIMARY KEY, first_name varchar(50) NOT NULL, last_name varchar(50) NOT NULL)''';
        self.assertIsNotNone(self.database.create_table, result)
        
    
    def test_populate_table(self):
        result = '''INSERT INTO user(id, username, first_name, last_name) VALUES(6, 'Adele', 'Adebel', 'Retsy')''';
        self.assertIsNotNone(self.database.populate_table, result)
        
    def test_get_all_users(self):
        result = 'SELECT * FROM user';
        self.assertIsNotNone(self.database.get_all_users, result)
        
    def test_get_user(self):
        result = f'SELECT * FROM user WHERE id = 4';
        self.assertIsNotNone(self.database.get_user, result)
        
    def test_create_users(self):
        result = '''INSERT INTO user(username, first_name, last_name) VALUES('bessin', 'Arele', 'daraso')''';
        self.assertIsNotNone(self.database.create_user, result)
        
    def tearDown(self):
        self.database = User()
    