from book import Book
import json
from pathlib import Path

class LibraryInventory:
    def __init__(self, file_name="books.json"):
        self.file_name = file_name
        self.books = []
        self.load()

    def load(self):
        file_path = Path(self.file_name)

        if not file_path.exists():
            file_path.write_text("[]")

        data = json.loads(file_path.read_text())
        self.books = [Book(**item) for item in data]

    def save(self):
        file_path = Path(self.file_name)
        data = [book.to_dict() for book in self.books]
        file_path.write_text(json.dumps(data, indent=4))

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save()

    def show_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(book)
