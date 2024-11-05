#The format() method takes unlimited number of arguments,
# and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.6
myorder = " i want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno,price))