import sqlite3
from movie_list_objects import Category, Movie


def connect_to_db():
    db_file = "movies_list.sqlite"
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row


def close(conn):
    if conn:
        conn.close()


def make_category(row):
    return Category(row['categoryID'], row['categoryName'])


def make_movie(row):
    return Movie(row['movieID'], row['name'], row['year'], row['minutes'], make_category(row))


def get_categories(conn):
    query = """SELECT categoryID, categoryName FROM Category"""
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()

    categories = []
    for row in results:
        categories.append(make_movie(row))
    return categories


def get_category(conn, category_id):
    try:
        query = """SELECT categoryID, name AS categoryName FROM Category WHERE categoryID = ?"""
        cur = conn.cursor()
        cur.execute(query, (category_id,))
        row = cur.fetchone()
        if row:
            return make_category(row)
        else:
            return None
    except:
        print("1. Animation\n2. Comedy\n3.History\n")


def make_movie_list(list_movies):
    movies = []
    for row in list_movies:
        movies.append(make_movie(row))
    return movies


def get_movies_by_category(conn, category_id):
    query = """SELECT movieid, Movie.name, `year`, minutes, Movie.categoryID, Category.Name AS categoryName FROM Movie JOIN Category ON Movie.CategoryID = Category.categoryID FROM movies WHERE """
    cur = conn.cursor()
    cur.execute(query, (category_id,))
    results = cur.fetchall()

    return make_movie_list(results)


def add_movie(conn, movie):
    query = """INSERT INTO Movie (categoryID, name, year, minutes) VALUES (?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(query, (movie.category.id, movie.name, movie.year, movie.minutes))
    conn.commit()


def display_welcome():
    print("The Movie List program\n")
    display_menu()


def display_menu():
    print("COMMAND MENU")
    print("cat - View movies by category")
    print("year - View movies by year")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program\n")


def display_categories(conn):
    print("CATEGORIES")
    categories = get_categories(conn)
    for category in categories:
        print(f"{category.id}, {category.name}\n")


def add_menu():
    name = input("Name: ")
    year = input("Year: ")
    minutes = int(input("Minutes: "))
    category_id = int(input("Category ID: "))

    movie = Movie(name, year, minutes, category_id)
    add_movie(conn, movie)
    print(f"{name} was added to the database. \n")


def main():
    conn = connect_to_db()
    display_welcome()
    display_categories(conn)
    while True:
        command = input("Command: ").lower()
        if command == "add":
            add_movie(conn)
        elif command == "cat":
            pass
        elif command == "exit":
            break
        else:
            print("Not a valid command. Try again. \n")
            display_menu()
    close(conn)
    print("Bye!")


if __name__ == "__main__":
    main()

# c = conn.cursor()
#
# query = """CREATE TABLE IF NOT EXISTS movies (
#     id INTEGER PRIMARY KEY,
#     `Name` VARCHAR(50),
#     `Year` INT,
#     Mins INT,
#     Category VARCHAR(20)
#     );"""
# print(query)
# c.execute(query)
# print("Table has been created")
#
#
# def title():
#     print("The Movie List program")
#
#
# def menu():
#     print("COMMAND MENU")
#     print("cat - View movies by category")
#     print("year - View movies by year")
#     print("add - Add a movie")
#     print("del - Delete a movie")
#     print("exit - Exit program")
#
#
# def categories():
#     print("CATEGORIES")
#     print("1. Animation")
#     print("2. Comedy")
#     print("3. History")
#
#
# def add_movie():
#     name = input("Name: ")
#     year = input("Year: ")
#     mins = input("Minutes: ")
#     category = input("Category ID: ")
#     c.execute("""INSERT INTO movies VALUES (name, `year`, mins, category)""")
#     conn.commit()


