#Remove items
#Note: You can remove items in a tuple.


#Tuples are unchangeable, you cant remove items in this,
# but you can use the same work around as we used foe changing and adding tuple items:

#Convert the tuple into a list, "apple", and convert it back into a tuple:

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)