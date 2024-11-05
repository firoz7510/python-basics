#global keyword
x = "beautiful"

def myfun():
    global x
    x = "fantastic"

myfun()

print("python is "+x)