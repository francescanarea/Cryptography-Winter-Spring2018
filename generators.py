import math

base = 2
f = 17

arr = []

def check(num, arr):
    for i in arr:
        if(num == i):
            arr.remove(i)
            
for i in range(1, f):
    arr.append(i)

for i in range(1, f):
    num = math.pow(base, i)
    if(num >= f):
        num %= f
    check(num,arr)
    print(num)

if len(arr) == 0:
    print(str(base) + " is a generator of " + str(f))


