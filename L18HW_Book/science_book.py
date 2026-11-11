from L18HW_Book.Book import Book


class ScienceBook(Book):
    def __init__(self, author, title, pages, isbn, year, genre, kindOfScience):
        super().__init__(author, title, pages, isbn, year, genre)
        self.__kindOfScience = kindOfScience

    def __str__(self):
        return super().__str__() + f"\nScince: {self.__kindOfScience}"

    @property
    def kindOfScience(self):
        return self.__kindOfScience

    @kindOfScience.setter
    def kindOfScience(self, kindOfScience):
        if kindOfScience is not None:
            self.__kindOfScience = kindOfScience
        print("There is not kind of science")
