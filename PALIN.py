# problem www.spoj.pl/problems/PALIN/

__author__ = "zimyand"
__date__ = "$Aug 6, 2010 2:01:56 AM$"

def rev(x):
    return x[::-1]

def increasable(x):
    i = 0
    while(i < len(x) / 2 and x[i] == x[len(x)-i-1]):
        i += 1
    return x[i] <= x[len(x)-i-1]


n = int(raw_input())
for i in range(n):
    x = raw_input()
    half_len = (len(x) / 2) + (len(x) % 2)
    l = x[:half_len]
    if increasable(x): l = str(int(l) + 1)
    
    print l + rev(l)[len(x) % 2:]