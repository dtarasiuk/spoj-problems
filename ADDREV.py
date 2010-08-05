# problem www.spoj.pl/problems/ADDREV/

__author__ = "zimyand"
__date__ = "$Aug 6, 2010 1:48:03 AM$"

def rev(x):
    y = 0;
    while x > 0:
        y = y * 10 + x % 10
        x /= 10
    return y

n = int(input())
for i in range(n):
    x, y = [int(st) for st in raw_input().split()]
    print rev(rev(x) + rev(y)) 