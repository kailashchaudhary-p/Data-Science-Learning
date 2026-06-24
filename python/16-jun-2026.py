#lambda function
square = lambda x: x**2
print(square(5))

#Map function
no =[1,2,3,4,5]
squared_no=list(map(lambda x: x**2,no))
print(squared_no)

#Filter function
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x: x%2==0,numbers))
print(even_numbers)