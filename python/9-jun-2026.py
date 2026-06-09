#Operators

#Arithmetic Operators
a = 10
b = 20
print(a+b) #addition
print(a-b)#subtraction
print(a*b)#multiplication
print(a/b)#division
print(a//b)#floor devision
print(a%b)#modulus
print(a**b)#power

#Comparison operaters
x=5
y=10
print(x==y)#equal to
print(x!=y)#not equal to 
print(x>y)#greater than
print(x<y)#less than
print(x>=y)#greater than or equal to
print(x<=y)#less than or equal to

#logical operators
p=50
q=45
print(p>40 and q>40)#logical and
print(p>40 or q>40)#logical or
print(not (p>40))#logical not

#Assignment operators 
c=70
c+=7 #c=c+7
print(c)#77
c*=3
print(c)#231

#membership operators
s='hello world'
print('h' in s)#True
print('z' not in s)#True

#identity operators
m = [1, 2]
n = a

print(a is b)      # True
print(a is not b)  # False