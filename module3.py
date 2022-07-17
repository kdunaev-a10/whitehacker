N = 10
num_list = [4,6,8,3,5,9,1,0,2,7]
print(num_list)
for i in range(10):
    print(num_list[i])

for i in range(1,N):
    tmp = num_list[i]
    print("i", tmp, i)
    j = 0
    while tmp > num_list[j]:
        print("j", tmp,j)
        j += 1
    print("ij", i, j)
    for k in range(i-1,j-1,-1):
        print("k", tmp, k)
        num_list[k+1] = num_list[k]
        print("k", num_list)
    num_list[j] = tmp
    print("f", num_list)


import requests
import bs4

print("TEST")
print("TEST")

