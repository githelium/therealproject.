import random
import time
arr = list(range(101))
for n in range(101):
    na = 100 - n
    ran = random.randint(0,n)
    arr[ran],arr[na] = arr[na],arr[ran]
oldarr = arr[:]
print(oldarr)
for i in range(100):

        # Last i elements are already in place
        for j in range(0, 101-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
time.sleep(3)