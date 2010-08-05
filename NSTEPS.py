# problem www.spoj.pl/problems/NSTEPS/

__author__ = "zimyand"
__date__ = "$Aug 6, 2010 1:56:43 AM$"

n = int(raw_input())
for i in range(int(n)):
    x, y = [int(st) for st in raw_input().split()]
    if x-y in [0, 2]:
        if x % 2 == 0: print x + y
        else: print x + y-1
    else:
        print "No Number"