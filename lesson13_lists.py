
# m_list = [9, 2, 17, -3, 6, 11]
#find min value and return it
# min_value = m_list[0]
def find_min(m_list: list)-> int:
    min_value = m_list[0]
    index = 0
    for item in m_list:
        if item < min_value:
            min_value = item
            index_min=index
        index+=1
    return index_min

res = find_min([9, 0, 4, -1, 4, -5, 100, 11])
print(res)

