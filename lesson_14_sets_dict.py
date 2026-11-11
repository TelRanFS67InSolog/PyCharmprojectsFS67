# set
m_set = {"kiwi", "mango", "banana", "orange", "apple"}
print(m_set)
#{'apple', 'banana', 'kiwi', 'orange', 'mango'}
#{'orange', 'kiwi', 'banana', 'apple', 'mango'}
#{'orange', 'banana', 'apple', 'mango', 'kiwi'}
m_set.add("lemon")
print(m_set)
m_set.clear()
print(m_set)
m_set.add("lemon")
print(m_set)
m_set.add("mango")
print(m_set)
m_set.add("lemon")
print(m_set)
# set doesnt contain dublicats!!!!!!
m_list=list(m_set)
print(m_list)
m_list.append("lemon")
print(m_list)
new_set=set(m_list)
print(new_set)
new_set.add("ananas")
print(new_set)
z = new_set.pop()
print(z)

students = {"Haim":4, "Victor":2, "Hanna":4, "Alex": 6}
print(students)
print(students.get("Hanna")) #4
print(students["Victor"])
print(students.pop("Haim"))
students["Olga"]=5
print(students)
students["Victor"] += 3
print(students)
students.update({"Haim": 7})
print(students)
keys = students.keys()
print(keys)
for key in keys:
    print(key, end = "->")
    print(students[key])
students.update({"Haim": True})
print(students)

s="hello money hello bye bye happy hello hello"
# [hello, money, hello, bye, bye, happy, hello, hello]
def word_count(st: str)->dict:
    words = st.split(" ")
    counter = {}
    for item in words:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    print(counter)

word_count(s)

#============================

contacts = {"Hanna": "052-3452834",
            "Alex": "055-5454637",
            "Olga": "052-8906745"}

print((type(contacts)))
keys = contacts.keys()
print(type(keys))
keys = list(keys)
print((type(keys)))
print(keys)

#    0     1    2
#['Hanna', 'Alex', 'Olga']
# item
#
for item in keys:
    print(item, end="->")
    print(contacts[item])

# ==================

"""
s -> "hello  world"
      x
"""

def count_symbols(s: str):
    counter = {}
    for x in s:
        counter[x] = counter.get(x, 0) + 1
        # if x in counter:
        #     counter[x] += 1
        # else:
        #     counter[x] = 1

    print(counter)

count_symbols("Hello world")
