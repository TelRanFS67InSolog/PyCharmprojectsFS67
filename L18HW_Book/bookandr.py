class Book:
    def __init__(self, autor:str,title:str,pages:int,isbn:str ):
        self.__autor = autor
        self.__title = title
        self.__pages = pages
        self.__isbn = isbn

    def __str__ (self):
        return (f'Title: "{self.__title}" '
                f'Autor: {self.__autor} '
                f"Pages: {self.__pages} "
                f'ISBN: {self.__isbn} ')


    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        if autor is None:
            print('Имя автора не может быть пустым')
        else:
            self.__autor = autor

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title is None or title == '':
            print('Название не может быть пустым')
        else:
            self.__title = title

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self,pages):
        if pages < 1 or pages is None:
            print ("Количество страниц не может быть меньше 1")
        else: self.__pages = pages

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self,isbn):
        if isbn is None or isbn == '':
            print('ISBN не может быть пустым')
        else: self.__isbn = isbn