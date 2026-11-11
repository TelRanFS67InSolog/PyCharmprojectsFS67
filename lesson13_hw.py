# ============= 1 vice verse method ============

def find_max(lst: list)->int:
    max_value = lst[len(lst)-1]
    index_max = len(lst)-1
    count = len(lst)-1
    for item in reversed(lst):
        if item>max_value:
            max_value = item
            index_max = count
        count-=1
    return index_max

res1 = find_max([1,0,-3,7,15,-9,30])
print(res1)

#============= 2 ==============

def list_evens_sum(lst: list):
    sum = 0
    for item in lst:
        if item%2==0:
            sum+=item
    return sum

res2=list_evens_sum([1,2,3,4,5,6,7,8])
print('sum of evens =', res2)

#============= 3 ==============

def print_reverse_char(s:str, sym: str):
    for i in reversed(s):
        print(i, end = sym)

res3 = print_reverse_char("Elephant",'&')
print(res3)

#=========== 6 ===============

import math
def find_min_positive_odd_numberindex(lst: list)->int:
    index_min=-1
    value_min=math.inf
    for i in range(0,len(lst)):
        if lst[i]<0:
            continue
        if lst[i]<value_min and lst[i]>0 and lst[i]%2==1:
            value_min = lst[i]
            index_min = i
    return index_min

lst_s=[1,7,10,0,-3,2,6,9,3,1]
res = find_min_positive_odd_numberindex(lst_s)
print(res)

# ============== 6_version2 ==============

def find_min_positive_odd_numberindex2(lst: list)->int:
    index_min=-1
    value_min=-1
    count = 0

    for i in lst:
        if i < value_min and i > 0 and i % 2 == 1:
            value_min=i
            index_min=count
        if i>0 and i%2==1 and value_min==-1:
            value_min=i
            index_min=count
        count+=1
    return index_min

lst_s2=[1,7,10,0,-3,2,6,9,3,1]
res6 = find_min_positive_odd_numberindex2(lst_s2)
print(res6)

#================ 6 ================

def find_index_minpositive(m_list: list):
    min_value = None
    for item in m_list:
        if item>=0:
            if min_value == None or item<min_value:
                min_value = item
    return min_value




