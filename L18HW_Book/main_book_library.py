from Book import Book
from L18HW_Book.fictionBook import FictionBook
from L18HW_Book.science_book import ScienceBook

book1 = Book("Platon","Apologia Sokrata", 258, "11243HB", 125, "philosophy")
print(book1)
book1.pages = 12
print(book1)
book1.pages = 3
print(book1)
book1.isbn = "123"
print("isbn:",book1.isbn)

book2 = Book("Gerbert Wels", 1234, 309, "asdgfh112", 1949, "fiction")
print(book1,book2)
book2.author = 2346
#print(book1,book2)
book2.title = "Kogda spyashchiy prosnetsya"
print("?",type(book2.title))
print("2 title ",book2.title)
print(book1,book2)
book2.author = 134
print("000",book2.genre)

try:
    book2.pages = -678,6
except ValueError:
    print(ValueError)
print(book2)

print("!!!",book2.pages)
print(book2)

try:
    book1.year = 127,5
except ValueError:
    print(ValueError)
print("***",book1)

fb = FictionBook("Pushkin", "Onegin", 456, "asd1235", 1825, "roman", 5.0)

print(fb)


sb = ScienceBook("ababagalamaga", "BabushkaIdedushka", 1,"345wer", 2026, "Science", "Nothing")

print(sb)