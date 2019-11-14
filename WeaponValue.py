T = int(input())
for k in range(0, T):
    N = int(input())
    S = list(range(0, N))
    Snew = []
    if N>1:
        for i in range(0, N):
            temp = input()
            S[i] = [int(i) for i in str(temp)]
        for j in range(0, 10):
            if S[0][j] != S[1][j]:
                Snew.append(1)
            else:
                Snew.append(0)
        for i in range(1, N-1):
            for j in range(0, 10):
                if Snew[j] != S[i+1][j]:
                    Snew[j] = 1
                else:
                    Snew[j] =0
        print(sum(Snew))
    else:
        temp = input()
        SS = [int(i) for i in str(temp)]
        print(sum(SS))
