#Return  "orange" instead of "banana" ?

fruits = ["apple","banana","cherry","kiwi","mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

                #3rd method -->range and multiple condition

#[ print(1)  condition1 print(2) range]


list = ["small" if 0<=i<=10 else "medium" if 11<=i<=20 else "large" for i in range(31)]
print(list)

