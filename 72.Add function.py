 #without argument and no return type
def add():
    num1=int(input("enter number1"))
    num2=int(input("enter number2"))
    sum=num1+num2
    print(sum)
add()
def add(num1,num2):
    sum=num1+num2
    print(sum)
add(20,30)

#with argument and no return type


#with argument and return type
def add(num1,num2):
    sum=num1+num2
    return sum
data=add(2,5)
print(data)