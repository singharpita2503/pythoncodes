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