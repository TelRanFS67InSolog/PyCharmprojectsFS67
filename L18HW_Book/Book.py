class Book:
    genre = "roman"
    def __init__(self, author: str, title: str, pages: int, isbn: str, year: int, genre):
        self.__author = author
        self.__title = title
        self.__pages = pages
        self.__isbn = isbn
        self.__year = year
        self.__genre = genre

    def __str__(self)-> str:
        return (f"Author: {self.__author}\n"
                f"Title of book: {self.__title}\n"
                f"there are {self.__pages} pages in the book\n"
                f"isbn: {self.__isbn}\n"
                f"year: {self.__year}\n"
                f"genre: {self.__genre}")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if author is not None and type(author)==str:
            self.__author = author
        else:
            print("Error! Author cannot be None and can be with type string only!")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if (title is not None) and isinstance(title, str):
            self.__title = title
        else:
            print("Title cannot be None and can be with type string only!!")

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise ValueError("Pages must be an integer!!")
        if pages <=0 or pages is None:
            raise ValueError("Quantity of pages must be > 0 only and cannot be None!!")
        self.__pages = pages

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self,isbn):
        if isbn is not None:
            self.__isbn = isbn
        else:
            print("ISBN cannot be None")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
         if isinstance(year, int) and year<0:
             print("This is not an ordinary book, but ancient miths")
             self.__year = year
         if not isinstance(year, int):
             raise ValueError("Year must be an integer type!")
         self.__year = year

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        if genre is not None:
            self.__genre = genre
        print("Wrong genre")



