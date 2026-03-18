#in array modification we will add the data ,merging,removing or some other opration will be run
import numpy as np
a=np.array([1,2,3,4,5,6,7,8])

#the syntex of insert the data in the 1d array is np.insert(array name,index of arrray, value of an element,axis is none for 1d array)
#in 2d or 3d or etc array we will give the axis 
b=np.insert(a,5,50) 
print(b)

#append it is also use to add the element in array
c=np.append(a,[40,5])
print(c)#it is add the elment in the last

#