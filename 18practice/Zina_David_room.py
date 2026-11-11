import webbrowser

shopping_list = [
    {
        "name": "Round table IKEA KRAGSTA",
        "price": 595,
        "shop": "IKEA Israel",
        "link": "https://www.ikea.com/il/he/p/kragsta-coffee-table-white-20286638/"
    },
    {
        "name": "LEGO shelf IKEA BERGSHULT 80x20",
        "price": 75,
        "shop": "IKEA Israel",
        "link": "https://www.ikea.com/il/he/p/bergshult-shelf-white-70421238/"
    },
    {
        "name": "Shelf bracket IKEA RAMSHULT",
        "price": 25,
        "shop": "IKEA Israel",
        "link": "https://www.ikea.com/il/he/"
    },
    {
        "name": "Toy storage IKEA TROFAST",
        "price": 427,
        "shop": "IKEA Israel",
        "link": "https://www.ikea.com/il/he/cat/trofast-system-19027/"
    },
    {
        "name": "Storage box IKEA DRONA",
        "price": 29,
        "shop": "IKEA Israel",
        "link": "https://www.ikea.com/il/he/cat/storage-boxes-baskets-10550/"
    },
    {
        "name": "Kids punching bag",
        "price": 79,
        "shop": "Super-Pharm Israel",
        "link": "https://shop.super-pharm.co.il/"
    }
]

print("ROOM SHOPPING LIST")
print("------------------------------")

for i in range(len(shopping_list)):
    item = shopping_list[i]

    print(i + 1, "-", item["name"])
    print("Price:", item["price"], "NIS")
    print("Shop:", item["shop"])
    print()

choice = int(input("Choose product number: "))

if 1 <= choice <= len(shopping_list):
    item = shopping_list[choice - 1]

    print()
    print("Opening:", item["name"])
    print("Shop:", item["shop"])
    print("Price:", item["price"], "NIS")
    print("Link:", item["link"])

    webbrowser.open(item["link"])

else:
    print("Wrong product number")
