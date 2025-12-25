# Function with out argument and return
def add() :
    a = 10
    b = 20
    c = a + b
    print(c)
add()
# Function with argument but not return
def add(a,b) :
    c = a + b
    print(c)
add(10,20) 
# Name using Recursion
def my_name(name,n):
    if n ==0 :
        return
    print(name)
    my_name(name,n-1)
    
my_name("Arpita",1)
# To check num is even or odd using a function
# Write a code to find the max of 3 numbers using function 
# Find a factorial usung a function
# Area of rectangle using function
# Check number is palindrome or not using function
# Check year is leap year or not using function
# To check num is even or odd using a function
def odd_even(num):
    if num % 2 == 0 :
        print("Number is even")
    else:
        print("Number is odd")
num = int(input("Enter a number :"))
odd_even(num)
# Write a code to find the max of 3 numbers using function 
def max(a,b,c):
    if a>b and a>c :
        print("a is greatest")
    elif b>a and b>c :
        print("b is greatest")
    else:
        print("c is greatest")
a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))
max(a,b,c)
# Find a factorial usung a function
def factf(num,fact):
    
    if fact == 0 :
        print(num)
        return
    
    num = num * fact
    factf(num,fact-1)
num = 1
fact = int(input("Enter number :"))
factf(num,fact)

# Area of rectangle using function
def area_rect(l,b):
     print(l*b)
l = int(input("Enter length"))
b = int(input("Enter breadth"))
area_rect(l,b)

# Check number is palindrome or not using function
def palindrome(num):
   
    s = str(num)
    
    if s == s[::-1]:
        return True
    else:
        return False
n = int(input("Enter a number: "))
if palindrome(n):
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")