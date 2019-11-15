import math
import itertools
T = int(input())
class b(Exception): pass
for i in range(0, T):
    N = int(input())
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    try:
        for s in itertools.product(l, repeat=N):
            out = list(itertools.chain(*s))
            ln = [int(i) for i in out]
            sl = [i ** 2 for i in ln]
            sumval = sum(sl)
            sv = math.sqrt(sumval)
            if sv - math.floor(sv) == 0:
                ls = ''.join(map(str, s))
                ln = int(ls)
                print(ln)
                raise b
        print(-1)
    except b:
        pass
