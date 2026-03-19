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

#concatenation of arrays 
a2=np.array([10,20,30])
print(np.concatenate((a,a2)))

#removing array - when we delete the element from the array 
print(np.delete(a,5))

#stacking array - when we have multiple array and we will combine the all of array in onec is known as stacking array
from numpy import vstack,hstack
x=np.array([80,40,60,20])
y=np.array([25,55,45,75])
z=np.array([22,11,33,77])
print(vstack((x,y,z)))
print(hstack((x,y,z)))
