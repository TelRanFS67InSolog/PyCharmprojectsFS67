from Book import Book


class FictionBook(Book):
    def __init__(self, author, title, pages, isbn, year, genre, rating):
        super().__init__(author, title, pages, isbn, year, genre)
        self.__rating = rating

    def __str__(self):
        return super().__str__() + f"\nrating: {self.__rating}"

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if rating is not None:
            self.__rating = rating
        print("Wrong rating")
