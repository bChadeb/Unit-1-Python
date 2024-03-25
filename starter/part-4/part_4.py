### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# def create_book():
#     title = input("Title of book:")
#     author = input("Author of book:")
#     year = input("Year it was made:")
#     rating = input("Rating:")
#     pages = input("The amount of pages:")

#     dict = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return dict

# book = create_book
# print(book)

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# def create_book():
#     title = input("Title of book:")
#     author = input("Author of book:")
#     year = int(input("Year it was made:"))
#     rating = float(input("Rating:"))
#     pages = int(input("The amount of pages:"))

#     dict = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return dict

# book = create_book
# print(book)


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

def create_book():
    title = input("Title of book:")
    author = input("Author of book:")

    try:
        year = int(input("Year it was made:"))
    except:
        year = int(input("Enter the year number for when the book was made"))

    try:
        rating = float(input("Rating:"))
    except:
        rating = float(input("Enter the rating of the book:"))

    try:
        pages = int(input("The amount of pages:"))
    except:
        pages = int(input("Enter the number of pages"))

    dict = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return dict

book = create_book
print(book)




### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

def menu(book):
    choice = input("Hit 1 to add a new book. Hit 2 to see all of the books. Hit 3 to exit")
    if choice == "1":
        book.append(create_book())
    elif choice == "2":
        print(book)
    elif choice == "3":
        print("\nPlease hit a number from the options")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

start = True

while start:
    start = menu(start)