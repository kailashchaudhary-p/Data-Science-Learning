import json
import datetime
D=datetime.datetime.now()
x='{"hello":"kaise ho"}'
y= json.loads(x)
print(y)
print(type(y))

b=[1,2,3,4,5]
a=json.dumps(b)
print(a)
print(type(a))
T=datetime.datetime.now()
print("Time taken to execute the code is ",T-D)

