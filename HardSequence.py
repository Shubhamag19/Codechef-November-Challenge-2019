T = int(input())
for k in range(0, T):
    N = int(input())
    L = [None]*N
    L[0] = 0
    dictvalue = {0: 1}
    for i in range(1, N):
        val = L[i-1]
        if val in dictvalue and dictvalue[val] == 1:
            L[i] = 0
            dictvalue[0] += 1
        else:
            count = 0
            j = i-2
            while(1):
                newval = L[j]
                count += 1
                if newval == val:
                    L[i] = count
                    if count not in dictvalue:
                        dictvalue[count] = 1
                    else:
                        dictvalue[count] += 1
                    break
                else:
                    j -= 1
    x = L[-1]
    print(dictvalue[x])
