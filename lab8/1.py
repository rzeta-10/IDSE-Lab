# CS22B1093 ROHAN G

import numpy as np
from numpy import random
import os

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(f"{type(arr)}")

l1 = ['Charish','Rohan',2,5,7]
arr1 = np.array(l1)
print(arr1)
print(arr1.dtype)
print(arr1[1])

a = np.array([[1,2,3],[4,5,6]])
print(a.ndim)
print(a[1,2])

print('1st element of 1st row', a[0][0])
print(a[0:2,1:2])
print(a[0:2,2])

b = np.array(['Rohan','Pratyek'],dtype='S')
print(b.dtype)
print(b[1])

c = np.array([1.2,3.14,5.67,4.9,],dtype='i')
print(c)
print(c.dtype)
c1 = c.astype(float)
print(c1)
print(c1.dtype)

m = np.array([10,20,30,40,50,60,70,80,90,100])
m1 = m.reshape(2,5)
print(m1.ndim)
print(m1.shape)

l2 = np.array([[1,2,3],[4,5,6]])
for i in l2:
    for j in i:
        print(j)
        
l3 = np.array(['apple','orange','guava'])
print(np.sort(l3))

l4 = np.array([[13,24,2],[5,2,45]])
print(np.sort(l4))

l5 = random.randint(-10,24)
print(l5)

l6 = random.randint(100,size=(10))
print(l6)
print(type(l6))

l7 = random.choice([1,2,3,4,5],p=[0.2,0.2,0.2,0.2,0.2],size=(6))
print(l7)

l8 = np.array([1,2,3,4,5,6,7,8,9,10])
print(random.permutation(l8))

x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)
print(x-y)
print(x*y)
print(np.multiply(x,y))
print(x/y)
print(np.dot(x,y))
z = np.array([[4],[5],[6]])
print(x@z)

p = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('Addition is ',p[0,0]+p[1,2])
print(p[1::3])

q = np.array([10,20,40,60,90])
z = q.copy()
print(z)
r = q.view()
q[0] = 100
z[0] = -100
print(q)
print(z)
print(r)

z = np.concatenate((x,y))
print(z)
z = np.stack((x,y))
print(z)

x = np.array([1,2,3,4,5,6,7,8,2,3,2])
z = np.where(x==2)
print("Indexes where we can find 2 is : ",z)
z = np.where(x%2==0) and np.where(x%4==0)
print("Divisible by 2 and 4 is : ",z)

x = np.array([1,2,6,10])
z = np.searchsorted(arr,[3,5,7,8])
print(z)

x = np.array([1,2,3,4,5])
z = np.array([True,False,False,True,True])
print(x[z])

print(os.path)
