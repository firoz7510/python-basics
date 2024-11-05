#Update Tuples


#change tuple values
#change a tuple is created, you cannot change its values.
#Tuple are unchangeable, or immutable as it also called.

# You can convert a Tuple into list
# change the list, and convert the list to be able to change it?

# Convert the Tuple into a list to be able to change it?

x = ("apple","banana","cherry")

y = list(x)
print(y)
y[1] = "kiwi"

x = tuple(y)
print(x)