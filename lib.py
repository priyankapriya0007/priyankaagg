class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f'Book "{title}" added.')

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\nBooks in Library:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def delete_book(self, book_number):
        if 0 < book_number <= len(self.books):
            removed_book = self.books.pop(book_number - 1)
            print(f'Book "{removed_book.title}" removed.')
        else:
            print("Invalid book number.")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("\nSearch Results:")
            for book in found_books:
                print(book)
        else:
            print(f'No books found with title containing "{title}".')

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")
            library.add_book(title, author, year)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            book_number = int(input("Enter book number to delete: "))
            library.delete_book(book_number)
        elif choice == '4':
            title = input("Enter title to search: ")
            library.search_book(title)
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
