📘 Assignment: Class Methods – Book Count Tracker
Objective
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

✅ Python Code

class Book:
    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment count whenever a new book object is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books


# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print("Total books:", Book.get_total_books())  # Output: Total books: 2
🧠 Explanation
total_books: A class variable shared across all instances of the class.

@classmethod increment_book_count(cls): Increases the total_books count whenever a new book is instantiated.

@classmethod get_total_books(cls): Returns the current count of books.

When you create a new Book, the count is automatically updated via the constructor (__init__).

