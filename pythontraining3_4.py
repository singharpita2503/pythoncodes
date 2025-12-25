#functions
#lambda function 
"""list=[10,20,30,40,50]
print(list)
print(len(list))
print(list[2])
print(list[-3])
print(list[1:3])

cars=["Ford","BMW","TATA"]
print(cars)
print(cars[1])
print(cars[-1])
print(cars[0:-2])
print(len(cars))
print(type(cars))
#append
cars.append("Honda")
print(cars)
cars.pop(-2)
print(cars)
#remove
cars.remove("BMW")
print(cars)
#clear
cars.clear()
print(cars)
#index function
obj=["abc","xyz","mno"]
x= obj.index("abc")
print(x)
#sort
sort=sorted(obj, key=len)
print(sort)
#reverse
obj.reverse()
print(obj)
#copy
obj.copy()
print(obj)

#questions
#convert list into string
list=[1,2,3,4,5]
obj=str(list)
print(obj)
# check given element is present or not
obj=int(input("Enter the number: "))
if obj in list:
    print("true")
else :
    print("false")
#using membership operator
obj=["a","b","c","d"]
print("a"in obj)
print("b" not in obj)
# add two list using operator
a=[1,2,3,4,5]
b=[6,7,8,9,10]
x= a + b
print(x)
# add two list using list function (extend) 
x=[1,2,3,4,5]
y=[6,7,8,9,10]
x.extend(y)
print(x)
# get max value from list max()
n=[1,2,3,4,5]
b= max(n)
print(b)
# get min value from list min()
n=[1,2,3,4,5]
b= min(n)
print(b)
# count no. of character in list count c
n=[1,2,3,4,5]
b= n.count(3)
print(b)"""
#convert tuple into list
"""x=(1,2,3,4)
a= list(x)
print(a)"""

#strings
"""s="Nagpur"
print(s*10)
print(s)
print(s[1])
print(s[-3])
print(s[1:3])"""

str="your name"
print(str.capitalize())

str="your name"
print(str.isidentifier())
print(str.casefold())
print(str.center(70))
print(str.lower())
print(str.endswith("name"))
print(str.endswith("Name"))
print(str.startswith("your"))
print(str.startswith("Your"))
print(str.index("name"))
str1="easy1234"
str2="easy@123"
print(str1.isalnum())
print(str2.isalnum())
print(str1.isdigit())
print(str2.isdecimal())
print(str2.isalpha())
print(str1.isspace())
print(str1.swapcase())
str3=" Python "
print(str3,"programming")
print(str3.strip(),"Programming")
a="I love Java"
print("original string",a)
a=a.replace("Java","Python")
print("new string",a)
print(a)
mylist=a.split()
print(mylist)
x="6"
y="Arpita"
mylist="{} {}".format(x,y)
print(mylist)