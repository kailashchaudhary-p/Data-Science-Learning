#in the reshapin we eill change the array shape without effect the data 
import numpy as np
array=np.array([10,20,30,40,50,60])
new_array=array.reshape(3,2)
print(new_array)#this is the reshape the array
#it is creat a view of the array


#The flattering array it is use to convert the 2d or multidimention array to convert into the 1d array it is just opposite the reshaping array
#we will convert the new_array into 1d array
print(new_array.ravel())#this is create the view
print(new_array.flatten())#this is creat the copy