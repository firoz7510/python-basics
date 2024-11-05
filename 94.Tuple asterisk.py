#Using Asterisk*

#If the number of variable is less than the number of values,
# you can add an * to the variable name
# and the values will be assigned to the variable as a list

#Assign the rest of the values as a list called "red":

fruits = ("apple","banana","cherry","kiwi","orange")

green, blue,*red = fruits

print(green)
print(blue)
print(*red)