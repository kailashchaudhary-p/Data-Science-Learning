#the mathematically opration perfoms withought loops. we use the broadcasting .
import numpy as np
a=np.array([12,20,55,44])#we have one shop which is the price of all product store in the arrsy 
b=10 
c=a - (a*b/100)
print(c)
#next opration
m=a*10
print(m)
#next opration
a1=np.array([[1,2,3,4],[88,99,44,77]])
result=a1+a
print(result)