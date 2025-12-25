#print("Arpita")
#A = "Arpita"
#print(A)
#print(type(A))
#A = 10
#print(A)
#print(type(A))
"""A = "10"
A = int(A)
print(A)
print(type(A))"""
"""A = 10.78
A = int(A)
print(A)
print(type(A))"""
"""A = "10.78"
A = float(A)
print(A)
print(type(A))
A = 10
B = 20
C = A + B
print(C)
print(type(C))
A = "10"
B = "20"
C = A + B
print(C)
print(type(C))
A = 10
B = 20
C = A * B
print(C)
print(type(C))"""
"""A=int(input("Enter first number: "))
B=int(input("Enter second number: "))
X=float(input("Enter first number: "))
D=float(input("Enter second number: "))
C=A+B
Y=X+D
print("The sum is:",C)
print("The sum of",A,"and",B,"is:",C)
print(type(C))
print("The sum is:",Y)
print("The sum of",X,"and",D,"is:",Y)
print(type(Y))
C=A*B
Y=X*D
print("The product is:",C)
print("The product of",A,"and",B,"is:",C)
print(type(C))
print("The product is:",Y)
print("The product of",X,"and",D,"is:",Y)
print(type(Y))
C=A/B
Y=X/D
print("The division is:",C)
print("The division of",A,"and",B,"is:",C)
print(type(C))
print("The division is:",Y)
print("The division of",X,"and",D,"is:",Y)
print(type(Y))
C=A-B
Y=X-D
print("The difference is:",C)
print("The difference of",A,"and",B,"is:",C)
print(type(C))
C=A%B
Y=X%D
print("The modulus is:",C)
print("The modulus of",A,"and",B,"is:",C)
print(type(C))
C=A**B
Y=X**D
print("The exponent is:",C)
print("The exponent of",A,"and",B,"is:",C)
print(type(C))
C=A//B
Y=X//D
print("The floor division is:",C)
print("The floor division of",A,"and",B,"is:",C)
print(type(C))

#areas of different shapes
Side = int(input("Enter the side of the square: "))
L = int(input("Enter the length of the rectangle: "))
B = int(input("Enter the breadth of the rectangle: "))
Area_Square = Side * Side
Area_Circle = 3.14 * Side * Side
Area_rec = L * B
Area_triangle = 0.5 * L * B
print("The area of the square is:", Area_Square)
print("The area of the circle is:", Area_Circle)
print("The area of the rectangle is:", Area_rec)
print("The area of the triangle is:", Area_triangle)

#Assignment operator
A=10
b=20
A+=b
print("The value of A after A+=b is:",A)
#logical operators
X=int(input("Enter first number: "))
Y=int(input("Enter second number: "))
if X>Y:
    print(X,"is greater than",Y)
elif X<Y:
    print(Y,"is greater than",X)
else:
    print(X,"is equal to",Y)
Z=int(input("Enter third number: "))
if X>Y and X>Z:
    print(X,"is the greatest number")
elif Y>X and Y>Z:
    print(Y,"is the greatest number")
elif Z>X and Z>Y:
    print(Z,"is the greatest number")
else:
    print("All three numbers are equal")
if X>Y:
    greatest=X
elif Y>X:
    greatest=Y
else:
    greatest=X
if Z>greatest:
    greatest=Z
print("The greatest number among the three is:",greatest)

A=int(input("Enter first number: "))
B=int(input("Enter second number: "))
C=int(input("Enter third number: "))
if A>B:
    print(A,"is greater than",B)
if A<B:
    print(B,"is greater than",A)
if A>B or A<C:
    print(A,"is either greater than",B,"or less than",C)
    
#assignment operators
A=["apple","banana","cherry"]
print("banana" in A)
print("banana" not in A)

A=["abc","123","cherry"]
print(type(A))
print(type(A[1]))
M={"abc":20,"123":6,"cherry":2.5}
print(type(M))"""

