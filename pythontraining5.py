#list ordered collection
#set unordered collection
#SET AND TUPLE
fruit_set={"Apple","Banana","Grapes","Mango"}
print(fruit_set)
fruit_set.add("cherry")
print(fruit_set)
fruit_set.update(["Fig","Orange"])
print(fruit_set)
fruit_set.remove("Apple")
print(fruit_set)
#QUESTIONS
#discard
#join two set using Union() function
#search particular element in set
#clear set
#deleted set
#print common element in set using and operator or operator
fruit_set.discard("Fig")
print(fruit_set)
#fruit_set.deleted()
#fruit_set.clear()
#print(fruit_set)
Set1={"cat","dog","rat","goat"}
Set2={1,2,3,4,5}
a=Set1.union(Set2)
print(a)
print(2 in Set2)
print(Set1 & Set2)
print(Set1 | Set2)
my_set = {1, 2, 3}
del my_set
my_tuple = (1, 2, 3)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[2])
print(my_tuple[-3])
print(my_tuple[1:3])
cars=("Ford","BMW","TATA")
print(cars)
print(cars[1])
print(cars[-1])
print(cars[0:-2])
print(len(cars))
print(type(cars))
my_tuple = (10, 20, 30, 40)

for item in my_tuple:
    print(item)
flower_tuple=("Lily","Rose","Jasmine")
print("i like",flower_tuple[0])
#Questions
#check length
#access value of tuple using loop
#tuple add using + operator 
#using membership operator in or not in 
#print using negative index 
#print range in tuple 
#get maximum values from tuple 
#get minimum values from tuple
#convert list into tuple

#dictionary
Dict={"Name":"ABC"}
print(Dict)
#roll:123
#percent:90.3
#print(roll)
#get()
#Key:Value
#Access only values in dictionary
#update dictionaries
#print only key in dictionary
#delete particular ele in dictionary
#clear 
#delete dict
#create nested dict
#add new element
#change vlaues of dict
Dict = {"Name": "ABC", "roll": 123, "percent": 90.3}

print(Dict["Name"])
print(Dict.get("roll"))
print(Dict.keys())
print(Dict.values())
print(Dict.items())

Dict.update({"percent": 95})
del Dict["roll"]

print(Dict)
Dict={"Riya":"20","Shreya":"25","Rounak":"26"}
print(Dict.clear())
#create nested dict
student= {
    "Name":"abc",
    "Roll": 150,
    "Marks": {"Maths": 95 , "Physics":90}
}
student["city"]="pune"#add new element
student["Roll"]=123#change values of dict
student["Marks"]["Science"]= 94

print(student)
"""largest = second = float('-inf')

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print(second)"""
#create a list of numbers from 1 to 10, then remove the numbers 5 from the list
#write a program to find the second largest number of a list
#how can you check if an element exist in a list 
#create a tuple containig numbers from 1 to 5 can you modify one of the element of a tuple
#how do you access the last element of a tuple
#what is tuple unpacking
#convert a list into a tuple and then back to a list 
#write a code to merge a dictionary
#write a program to sort dictionary by its value
#write a program to convert a tuple of tuple into dictionary
#write a program to sort a dictionary by its values
"""numbers = list(range(1, 11))
numbers.remove(5)
print(numbers)
nums = [10, 25, 40, 30, 20]
nums = list(set(nums))
nums.sort()
print(nums[-2])
nums = [10, 25, 40, 30, 20]
list=[1,2,3,4,5]
if 2 in list:
    print("Element exists")
else:
    print("Element not exist")
t = (1, 2, 3, 4, 5)
print(t[-1])
#unpacking
t = (10, 20, 30)
a, b, c = t
print(a)
print(b)
print(c)"""

l=[1,2,3,4,5]
x= tuple(l)
new_list = list(x)
print(x)
print(new_list)
