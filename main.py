from models.user import User
from models.book import Book
from grades import Grades


user = User()
book = Book()
grade = Grades()


user.create_table()
user.populate_table()
print(user.get_all_users())
print(user.get_user(25))
user.create_user('Bezos', 'Adebisi', 'Oyelola')
user.update_record_of_user('Faourkass', 'nabue', 'john', 81)
user.delete_user(8)



print(book.get_all_book())
print(book.get_book(98))
book.create_book('Baby by me', 26, 150)
book.update_book_record('Baby come back', 200, 26, 79)
book.delete_book(98)


grade.create_table
grade.open_csv_file
print(grade.read_all())
grade.add_student('Tolu', 'Yaya', '224-667-123', 60, 30, 45, 70, 77, 'D')
grade.update_record(56, 33, 62, 40, 67, 'D', "234-56-7890")
grade.delete_record('123-45-6789')
print(grade.scored_above_50())
print(grade.scored_below_50())
print(grade.scored_above_45_in_test_1)


