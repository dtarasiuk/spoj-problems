# problem www.spoj.pl/problems/TOANDFRO/

__author__ = "zimyand"
__date__ = "$Aug 6, 2010 1:54:47 AM$"

n = input()
while(n):
    s = raw_input()
    res = ""
    for j in range(n):
        for i in range(len(s) / n):
            res = res + s[i * n + (i % 2) * (n-j-1) + ((i + 1) % 2) * j]
    print res
    n = input() 