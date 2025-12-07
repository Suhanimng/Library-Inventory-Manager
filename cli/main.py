"""
Name: Suhani
Date: 7/12/2025
Program: Library System
"""

from library_manager.inventory import LibraryInventory

def menu():
    print("\n------ Library Menu ------")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book by Title")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    return input("Enter your choice: ")


def main():
    library = LibraryInventory()

    while True:
        choice = menu()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
            print("Book added successfully.")

        elif choice == "2":
            print("\nBooks in Library:\n")
            books = library.show_books()  # If show_books prints, no need to loop

        elif choice == "3":
            keyword = input("Enter title to search: ")
            results = library.search_by_title(keyword)

            if results:
                for book in results:
                    print(book)
            else:
                print("No matching book found.")

        elif choice == "4":
            isbn = input("Enter ISBN to issue: ")
            book = library.search_by_isbn(isbn)

            if book and book.issue():
                library.save()
                print("Book issued successfully.")
            else:
                print("Book is not available or does not exist.")

        elif choice == "5":
            isbn = input("Enter ISBN to return: ")
            book = library.search_by_isbn(isbn)

            if book:
                book.return_book()
                library.save()
                print("Book returned successfully.")
            else:
                print("Book not found.")

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()
