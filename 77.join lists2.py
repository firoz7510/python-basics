#Another way to join two lists
# is by appending all the items from list2 into list1, one by one ?


#Append list2 into list1 ?

list1 = ["a","b","c"]
list2 = [1,2,3]

for i in list2:
    list1.append(i)

print(list1)