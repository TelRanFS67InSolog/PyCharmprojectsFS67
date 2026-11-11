# =============== 1 ==================
#from lesson_14_sets_dict import m_list

contacts = {"Hanna": '052-3333333'}
contacts.update({"Alex": '055-47474747'})
contacts["Olga"] = '054-5454545'

def print_contacts(cont: dict):
    for item in cont:
        print(item, ": ", cont[item], sep='', end=' ')

print_contacts(contacts)
print()

# ============== 2 ================

n="hello"

def count_symbols(s:str):
    c_sym={}
    for i in s:
        if i in c_sym:
            c_sym[i] +=1
        else:
            c_sym[i] = 1
    return c_sym

print(count_symbols(n))

# ================= 3 ==================

def find_max_score(students: dict):
    scores = list(students.values())
    print(scores)
    max_score=scores[0]
    for score in scores:
         if score > max_score:
             max_score = score
    successful = {}
    for item in students:
        if students[item]==max_score:
            successful.update({item: max_score})
    return successful

students = {"Hanna": 87, "Alex": 89, "Gretta": 55, "Igor": 63, "Zina": 89}
print(find_max_score(students))

# ============== 4 ================

n_list = [5,3,8,1,9,3,5,5,0,2,3,1,1,1,10]
#n_list = [1,2,3,2,1,2,3,3,2,1,0,0]

def remove_dublicates(lst: list):
    for i in lst[0::]:
        d=i+1
        while d<len(lst):
            if lst[i]==lst[d]:
                lst.pop(d)
            d+=1
    return lst

print(remove_dublicates(n_list))

print(set(n_list))

#=============== 5 =================

def find_min_max_average(lst: list):
    min = lst[0]
    max=lst[0]
    for i in range(1, len(lst)):
        if lst[i]>max:
            max= lst[i]
        if lst[i]<min:
            min = lst[i]

    return tuple((min,(min+max)/2,max))

print(find_min_max_average(n_list))


#=============== 6 ================

friends_of_hanna = ["Petr", "Vasiliy", "Olga"]
friends_of_oleh = ["Vasiliy", "Olga", "Dmitriy"]

def mutual_friends_and_annas(hanna,oleh):
    # set_hanna=set()
    # set_mutual=set()
    # for person_h in hanna:
    #     #for person_o in oleh:
    #     if person_h in oleh:
    #         set_mutual.add(person_h)
    #     else: set_hanna.add(person_h)
    set_mutual=set(hanna) & set(oleh)
    set_hanna=set(hanna) - set(oleh)
    return set_mutual, set_hanna

print(mutual_friends_and_annas(friends_of_hanna, friends_of_oleh))

#==================== 7 =====================

def counter_repetition(lst:list):
    counter = {}
    for item in lst:
        if item in counter:
            counter[item]+=1
        else:
            counter[item]=1
    return set(counter.keys()), counter

c_list = ["bread", "milk", "yogurt", "cucumber", "milk", "bread", "tomatoes", "meat","meat"]
print(counter_repetition(c_list))

from collections import Counter

counter = Counter(c_list)
print(set(counter.keys()), counter)

from random import*
print(['developer','fu, tester'][randint(0,1)])














