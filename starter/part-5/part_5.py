### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# def create_book():
#     title = input("Title of book:")
#     author = input("Author of book:")

#     try:
#         year = int(input("Year it was made:"))
#     except:
#         year = int(input("Enter the year number for when the book was made"))

#     try:
#         rating = float(input("Rating:"))
#     except:
#         rating = float(input("Enter the rating of the book:"))

#     try:
#         pages = int(input("The amount of pages:"))
#     except:
#         pages = int(input("Enter the number of pages"))

#     with open("library.txt", "a") as f:
#         f.write(f"{title}, {author}, {year}, {rating}, {pages} \n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# def library_txt():
#     with open("library.txt", "r") as f:

#         for line in f:
#             title, author, year, rating, pages = line.strip().split(", ")
        
#         print(f"Title: {title}")
#         print(f"Author: {author}")
#         print(f"Year: {year}")
#         print(f"Rating: {rating}")
#         print(f"Pages: {pages}")


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def create_book():
    title = input("Title of book: ")
    author = input("Author of book: ")

    try:
        year = int(input("Year it was made: "))
    except ValueError:
        year = int(input("Enter the year number for when the book was made: "))

    try:
        rating = float(input("Rating: "))
    except ValueError:
        rating = float(input("Enter the rating of the book: "))

    try:
        pages = int(input("The amount of pages: "))
    except ValueError:
        pages = int(input("Enter the number of pages: "))

    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


def library_txt():
    with open("library.txt", "r") as f:

        for line in f:
            title, author, year, rating, pages = line.strip().split(", ")
        
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Year: {year}")
        print(f"Rating: {rating}")
        print(f"Pages: {pages}")


def find_author():
    book_author = input("Enter the author's name to find their books: ")

    found_books = []
    
    with open("library.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        title, author, year, rating, pages = line.strip().split(", ")
        
        if author.lower() == book_author.lower():
            book_details = {
                "Title": title,
                "Author": author,
                "Year": year,
                "Rating": rating,
                "Pages": pages
            }
            found_books.append(book_details)

    if found_books:
        print(f"\nBooks by {book_author}:")
        for book in found_books:
            for key, value in book.items():
                print(f"{key}: {value}")
    else:
        print(f"No books found by {book_author}.")

def find_rating():
    try:
         book_rating = float(input("Enter the rating to find books (e.g., 4.5): "))
    except:
        print("Invalid input. Please enter a valid rating.")
        return
    
    found_books = []
    
    with open("library.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        title, author, year, rating, pages = line.strip().split(", ")
        
        if float(rating) == book_rating:
            book_details = {
                "Title": title,
                "Author": author,
                "Year": year,
                "Rating": rating,
                "Pages": pages
            }
            found_books.append(book_details)

    if found_books:
        print(f"\nBooks with a rating of {book_rating}:")
        for book in found_books:
            for key, value in book.items():
                print(f"{key}: {value}")

    else:
        print(f"No books found with a rating of {book_rating}.")

def find_title():
    find_name_book = input("Enter the title to find the book: ")

    found_books = []
    
    with open("library.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        title, author, year, rating, pages = line.strip().split(", ")
        
        if title.lower() == find_name_book.lower():
            book_details = {
                "Title": title,
                "Author": author,
                "Year": year,
                "Rating": rating,
                "Pages": pages
            }
            found_books.append(book_details)

    if found_books:
        print(f"\nDetails for the book '{find_name_book}':")
        for book in found_books:
            for key, value in book.items():
                print(f"{key}: {value}")

    else:
        print(f"No book found with the title '{find_name_book}'.")

def main_menu():
    on = True

    while on:
        print("\nHome Library App")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Search by author")
        print("4. Search by rating")
        print("5. Search by title")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_book()
        elif choice == "2":
            library_txt()
        elif choice == "3":
            find_author()
        elif choice == "4":
            find_rating()    
        elif choice == "5":
            find_title()    
        elif choice == "6":
            print("Exiting the Home Library App")
            on = False
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main_menu()
