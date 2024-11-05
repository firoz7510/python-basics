#You can Use index numbers {0}
#to be sure the arguements are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.5
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
