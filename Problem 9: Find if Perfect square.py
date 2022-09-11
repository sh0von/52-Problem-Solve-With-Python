##Find if a number is perfect square
import math
T=int(input())
for i in range(T):
    n=int(input())
    root_value=math.sqrt(n)
    if math.ceil(root_value)==math.floor(root_value):
        print('Yes')
    else:
        print('No')