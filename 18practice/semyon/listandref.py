original = [
    ["Apple","Banana"],
    ["Milk","Cheese"]
]

copy_list=original.copy()

copy_list[0].append("Orange")
copy_list.append(["Bread"])

print(original)
print(copy_list)