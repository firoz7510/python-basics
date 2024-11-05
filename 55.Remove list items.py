#Remove List Items

#The remove() method removes the specified item.

#Remove "banana"?

thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

#if there are more than one item with the specified value,
# the remove() method removes the first occurance:

#Remove the first occurance of "banana":

thislist = ["apple","banana","cherry","banana","kiwi"]
thislist.remove("banana")
print(thislist)

