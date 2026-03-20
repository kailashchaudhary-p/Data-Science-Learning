'''
in a big ammount of data we have 
some empty colum or rows in this case we use the handling missing 
there are three built in function 
1)np.innan->this is detect missing value
2)np.nan_to_num()->missing value replace 
3)np.naninf->this check to infinite vlaues in array
import
'''
#This the first built in function in handling missing
import numpy as np 
a1=np.array([56,11,61,np.nan,51,np.nan,55])
print(f"Missing value detected {np.isnan(a1)}")

#This is the seccond built in function in handling missing
a2=np.array([44,424,78,44,np.nan,np.nan])
b=np.nan_to_num(a2,nan=7 )
print(b)

#this is the third built in function in handling missing
import numpy as np

a3 = np.array([10, 20, np.inf, -np.inf, 50])

b1 = np.nan_to_num(a3, posinf=999, neginf=-999)

print(b1)