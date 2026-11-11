#========== 1 ===========

def print_list_reverse(m_list: list):
    for item in reversed(m_list):
        print(item, end=" ")

lst=["execute","cannot","pardon"]
print_list_reverse(lst)
print()

#=========== 2 ==============

def print_list_with_sym(m_list: list,sym):
    for item in m_list:
        print(item, end=sym)

lst_2 = [6,6,0,6]
print_list_with_sym(lst_2,"#")
print()

#============ 3 ================

def count_value(listOk: list, value:int)->int:
    count=0
    for item in listOk:
        if item == value:
            count+=1
    return count

lst_3=[6,6,0,6,8,-1]
print("quantity is ",count_value(lst_3,6))

#=============== 4 ===============

def list_sum(m_list:list)->int:
    sum=0
    for item in m_list:
        sum+=item
    return sum

lst_4 = [9,3,5,3,17]
print("sum of items in the lst_4 =",list_sum(lst_4))

#=============== 5 =================

def find_max_index(m_list: list):
    max=m_list[0]
    index=0
    for item in m_list:
        if item>max:
            max=item
            max_index = index
        index+=1
    return max_index

lst_5=[5,0,10,20,-5,4]
print("index of max value in the list is",find_max_index(lst_5))

#============ 6 ===============

def find_min_index_positive(m_list: list):
    i=0
    first_positive=0
    while i< len(m_list):
        if m_list[i]>0:
            first_positive = i
            break
        i+=1

    index=first_positive
    min_value = m_list[first_positive]
    min_index = first_positive

    for item in m_list[first_positive+1:len(m_list)]:
        index += 1
        if item<min_value and item>0 and item%2==0:
            min_value = item
            min_index = index

    if m_list[min_index]>0:
        return min_index
    else:
        return "Not found"

lst_6 = [-4,-5,-5,-5,-6,-1,-2,9,4,-10,-11,-1]
print("min positive value with index",f"{find_min_index_positive(lst_6)}")




