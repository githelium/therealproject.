import random
arr = []
for i in range(1,101):
    arr.append(i)
for n in range(1,101):
    na = 100 - n
    ran = random.randint(0,n)
    arr[ran],arr[na] = arr[na],arr[ran]
print(arr)