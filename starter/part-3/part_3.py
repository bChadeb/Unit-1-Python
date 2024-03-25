my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def acc_dic(book_dict):
    string = f"{book_dict["title"]}, is written by {book_dict["author"]}, was made in the year {book_dict["year"]}. It has a mighty fine rating of {book_dict["rating"]} and contains {book_dict["pages"]}"
    return string

print(acc_dic(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def yo_mama(dict):
    string = f"The book: {dict['title']}"
    return string

def is_a(dict):
    string = f"The author: {dict['author']}"
    return string

def really(dict):
    string = f"The year it was published: {dict['year']}"
    return string

def cool(dict):
    string = f"The rating of the book: {dict['rating']}"
    return string

def person(dict):
    string = f"The amount of pages: {dict['pages']}"
    return string

print(yo_mama(my_book))
print(is_a(my_book))
print(really(my_book))
print(cool(my_book))
print(person(my_book))
# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def search_title(books, title):
    for book in books:
        if book["title"] == title:
            return book
        return None
    
