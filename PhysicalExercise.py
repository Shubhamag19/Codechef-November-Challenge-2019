import math
T = int(input())
for k in range(0, T):
    x, y = input().split()
    x = int(x)
    y = int(y)
    N, M, K = input().split()
    NL = input().split()
    NLnew = [int(i) for i in NL]
    ML = input().split()
    MLnew = [int(i) for i in ML]
    KL = input().split()
    KLnew = [int(i) for i in KL]

    NM = NLnew+MLnew
    xval = NM[0:][::2]
    yval = NM[1:][::2]
    exval = KLnew[0:][::2]
    eyval = KLnew[1:][::2]
    length = int(len(NM)/2)

    dist1 = []
    for a in range(0, length):
        dist = math.sqrt((abs(x - xval[a]) ** 2) + (abs(y - yval[a]) ** 2))
        dist1.append(dist)
    lNLnew = int(len(NLnew)/2)
    lMLnew = int(len(MLnew)/2)
    endlen = int(len(KLnew)/2)

    rg = [[None] * lMLnew for z in range(lNLnew)]
    for b in range(0, lNLnew):
        for c in range(0, lMLnew):
            rg[b][c] = math.sqrt((abs(xval[b] - xval[lNLnew+c]) ** 2) + (abs(yval[b] - yval[lNLnew+c]) ** 2))
    gr = [[None] * lNLnew for zz in range(lMLnew)]
    for d in range(0, lMLnew):
        for e in range(0, lNLnew):
            gr[d][e] = math.sqrt((abs(xval[lNLnew+d] - xval[e]) ** 2) + (abs(yval[lNLnew+d] - yval[e]) ** 2))
    te = [[None] * endlen for zz in range(lNLnew+lMLnew)]
    for u in range(0, length):
        for v in range(0, endlen):
            te[u][v] = math.sqrt((abs(xval[u] - exval[v]) ** 2) + (abs(yval[u] - eyval[v]) ** 2))

    mindist = math.inf
    for first in range(0, lNLnew):
        for sec in range(0, lMLnew):
            for thir in range(0, endlen):
                if dist1[first] + rg[first][sec] + te[lNLnew+sec][thir] < mindist:
                    mindist = dist1[first] + rg[first][sec] + te[lNLnew+sec][thir]
    mindist2 = math.inf
    for fir in range(lNLnew, lNLnew+lMLnew):
        for se in range(0, lNLnew):
            for thi in range(0, endlen):
                if dist1[fir] + gr[fir-lNLnew][se] + te[se][thi] < mindist2:
                    mindist2 = dist1[fir] + gr[fir-lNLnew][se] + te[se][thi]
    if mindist < mindist2:
        print(mindist)
    else:
        print(mindist2)
