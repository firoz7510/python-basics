#List comprehension

#List comprehension offers a shorter syntax
# when you want to create a new list based on the values of an existing list.

# the syntax
#  newlist = [expression for item in iterable if condition == True]



#you want a new list , containing only the fruits with the letter "a" in the name.

#without list comprehension
# you will have to write a for statement with a conditional state inside:

fruits = ["apple", "banana", "cherry","kiwi", "mango"]
newlist = []


for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#Create a new list , containing only the fruits with the letter "a" in the name ?

fruits = ["apple", "banana", "cherry","kiwi", "mango"]

newlist= [x for x in fruits if "a" in x]    #print range condition
print(newlist)