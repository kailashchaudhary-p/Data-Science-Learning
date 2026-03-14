#the creation of an array 
import numpy as np
list=np.array([4,8,6,4])#in this we convert the list into numpy array
print(f"{list} This the list convert into numpy array")


#create array with defult value
defult_value=np.zeros(3)
print(f"{defult_value} this the array with the defult value")

#the ones 
ones=np.ones((2,3))
print(f"{ones} this is the ones")

#Sequence of number 
sequence_of_number=np.arange(4,85,8)
print(f"{sequence_of_number} this the sequence number array")

#full shape array
full_shape=np.full((3,3),4)
print(f"{full_shape} this is a full shape array")

#Identity matrices this is the dignal matrices
Identify=np.eye(4)
print(f"{Identify} this is the identify matrux which is also known as dignal matrices")