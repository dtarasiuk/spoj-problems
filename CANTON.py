# problem www.spoj.pl/problems/CANTON/

__author__ = "zimyand"
__date__ = "$Aug 6, 2010 1:51:27 AM$"

from math import ceil
from math import sqrt
t = int(input())
for i in range(t):
    n = input()
    l = ceil((1.0 + sqrt(1.0 + 8 * n)) / 2)-1
    p = n-(l-1) * l / 2
    if (l % 2 == 0): x = l-p + 1
    else: x = p
    print "TERM %s IS %d/%d" % (n, l + 1-x, x)