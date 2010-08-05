# problem www.spoj.pl/problems/FCTRL2/

__author__ = "zimyand"
__date__ = "$Aug 6, 2010 1:38:36 AM$"

def factorial(x):
    if x < 2: return 1
    else: return x * factorial(x-1)

n = int(raw_input())
for i in range(n):
    x = int(raw_input())
    print factorial(x) 