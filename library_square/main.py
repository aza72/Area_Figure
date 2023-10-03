import math

def Area_Circle( r):
    if r>0:
        pi=3.14
        s=pi*r**2
        print(s)


def Area_Triangle(a,b,c):
    if a > 0 and b > 0 and c > 0:
        p=(a+b+c)/2
        st= math.sqrt( p*(p-a)*(p-b)*(p-c))
        print(st)