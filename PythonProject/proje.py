import os
class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if books:
            for book in books:
                print(book.strip(","))
        else:
            print("No books available. \n")

    def add_book(self):
        book_title = input("Enter book title: ")
        author = input("Enter author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{book_title}, {author}, {release_date}, {num_pages}\n"
        self.file.write(book_info)
        self.file.flush()
        print("Book added successfully.\n")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        # Read the file and create a list of books
        self.file.seek(0)
        books = self.file.readlines()

        # Find the index of the book to be removed
        index_to_remove = None
        for i, book in enumerate(books):
            if book.startswith(title_to_remove + ','):
                index_to_remove = i
                break

        if index_to_remove is not None:
            # Remove the book from the list
            del books[index_to_remove]

            # Clear the file content
            self.file.seek(0)
            self.file.truncate()

            # Write the updated list back to the file
            for book in books:
                self.file.write(book)

            self.file.flush()
            print(f"Book '{title_to_remove}' removed successfully. \n")
        else:
            print(f"Book '{title_to_remove}' not found. \n")



lib = Library()

while True:
    
    print("* MENU *")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) End the program")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice== '4':
        os.exit()
    else:
        print("Invalid choice. \n")
        

