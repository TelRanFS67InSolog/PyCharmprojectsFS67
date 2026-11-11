#======== reverse in column ========

def print_reverse_column(st: str):
    for l in reversed(st):
        print(l)

print_reverse_column("Hello")

#======== string with symbols after each letter ===========

def print_str_with_sym(st: str, sym: str):
    for l in st:
        print(l, end=sym)

print_str_with_sym("Hello",'#')
print()

#============= find char ============

def find_char(s: str, sym: str)-> int:
    count=0
    for l in s:
        if l == sym:
            count+=1
    return count

print(find_char('abbcd0b0b','b'))

#============ find_index =========

def find_index(s: str, sub: str)->int:
    index = 0

    while index<(len(s)-len(sub)) and s[index:index+len(sub)] != sub:
        index+=1
    if s[index:index+len(sub)] == sub:
        return index
    else:
        return -1

print(find_index("parformance","anca"))

#=========== find_index 2 ============

def find_index2(s: str, sub: str)->int:
    index = 0
    while index<(len(s)-len(sub)):
        if s[index] == sub[0]:
            if s[index:index+len(sub)] == sub:
                return index
        else:
            index+=1

    if s[index:index+len(sub)] == sub:
        return index
    else:
        return -1

print(find_index2("performance", "anc"))




