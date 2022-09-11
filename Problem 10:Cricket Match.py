##Run Rate
import math
T=int(input())
for i in range (T):
    r1,r2,b=map(int, input().split())
    ballplayed=300-b
    crr=(r2/ballplayed)*6 ##current run rate
    rrr=(r1-r2+1)/b*6 ##required run rate
    print("{:.2f}".format(crr),"{:.2f}".format(rrr)) ##"{:.2f}" for 2 digits after decimal point