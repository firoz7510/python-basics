#Perform a case-insensitive sort of the list:

thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort(key=str.lower)
print(thislist)


thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort(key=str.upper)
print(thislist)