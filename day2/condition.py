s=eval(input("Enter the number"))
print(s)
if type(s) == tuple:
    print("It is a tuple")
else:
    print("it is not a tuple")

num=int(input("Enter the number: "))
if 10<=num<=1000:
   print("true")

s=input("enter character: ")
if s.isupper():
   print("It is an uppercase letter")
elif s.islower():
   print("It is a lowercase letter")
elif s.isdigit():
   print("It is a digit")
else:
   print("It is a special character")




a=input("Enter the number1: ")
b=input("Enter the number2:")
if a>b:
    print('a is greater')
elif b>a:
    print('b is greater')
else:
    print("both are equal")
    
    
num=int(input("Enter the number: "))
if 10<=num<=1000:
   print("true")
elif 1000<num<99999:
    print("true")
else:
    print("false")
    
ch=input("enter")
if ch.isalpha():
    if ch in "aeiouAEIOU":
        print("It is a vowel")
    else:
        print("It is a consonant")
else:
    print("It is not an alphabet")
    
s=eval(input("enter the numbers"))
print(s)
if type(s)==list:
    if len(s)%2==0:
        print(s)
    else:
        print("it is a list")
else:
    print("it is not a list")