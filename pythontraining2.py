"""x=6
y=3
print("x&y:",x&y)
print("x|y:",x|y)
print("x^y:",x^y)
print("~x:",~x)
print("x<<2:",x<<2)
print("x>>2:",x>>2)

if x>0:
    print("x is a positive number")
else:
    print("x is a negative number")

if y>0:
    print("y is a positive number")
elif y==0:
    print("y is zero")
else:
    print("y is a negative number")

for i in range(1,6):
    print("Iteration number:",i)
print("Loop ended")"""

"""i=1 
while i>=10:
  print(i)
i=i+1

i=1
while i<=10:
  if i==8:
    break
  print(i,end=" ")
  i+=1"""

"""i=1
while i<=10:
  if i==8:
    i+=1
    continue
  print(i,end=" ")        
  i+=1"""

#voting eligibility
"""age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

    

#Finding the largest number among three numbers
A=int(input("Enter first number: "))
B=int(input("Enter second number: "))
C=int(input("Enter third number: "))
if A>=B and A>=C:
    print(A,"is the largest number")
elif B>=A and B>=C:
    print(B,"is the largest number")
else:
    print(C,"is the largest number")"""

X=int(input("Enter first number: "))

if X%2==0:
    print("the number is even")
else:
    print("the number is odd")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

n = 1
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
