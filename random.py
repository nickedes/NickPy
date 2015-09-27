from time import time
from itertools import islice
# a, b = 1, 1000000000
a, b = input().split(' ')
a, b = int(a), int(b)
xor = a
start = time()
lis = range(b+1)
for num in islice(lis, a+1, b+1):
    xor ^= num
print(xor, "in ", time() - start)
