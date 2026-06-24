def num(n):
    if n == 12:
        return 12
    else:
        print(n)
        return num(n + 1)
print(num(0))

# decorator fonction
def Dec(func):
    def hello(*args,**kwargs):
        print("Hello kaise ho?")
        result =  func(*args,**kwargs)
        return result
    return hello
@Dec
def add(a,b):
    return a + b 
print(add(2,3))

#genrator function
def count_upto(n):
    count = 1
    while count <= n :
        yield count 
        count += 1
h= count_upto(6)
print(next(h))
print(next(h))
print(next(h))
print(next(h))