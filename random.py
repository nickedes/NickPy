# from time import time
# from itertools import islice
# # a, b = 1, 1000000000
# a, b = input().split(' ')
# a, b = int(a), int(b)
# xor = a
# start = time()
# lis = range(b+1)
# for num in islice(lis, a+1, b+1):
#     xor ^= num
# print(xor, "in ", time() - start)

# XOR of first N natural no.s
# N = int(input())
# if (N % 2) == 0:
#     if (N % 4) == 0:
#         r = N
#     else:
#         r = N+1
# else:
#     if (N % 4) == 1:
#         r = 1
#     else:
#         r = 0
# print(r)
import math
R = 6371000
lat = [39.984683, 39.984686]
lon = [116.31845, 116.318417]
phi1 = math.radians(lat[0])
phi2 = math.radians(lat[1])
dphi = math.radians(lat[1] - lat[0])
dl   = math.radians(lon[1] - lon[0])
a = (math.sin(dphi/2)**2) + (math.cos(phi1) * math.cos(phi2) * math.sin(dl/2)**2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = R * c
print(d)