# problem www.spoj.pl/problems/FCTRL/

__author__ = "zimyand"
__date__ = "$Aug 6, 2010 1:15:29 AM$"

def factorial_zeros_count(x):
    res = 0
    div = 5
    while(x >= div):
        res += x / div
        div *= 5
    return res

n = int(raw_input())
for i in range(n):
    x = int(raw_input())
    print factorial_zeros_count(x) 