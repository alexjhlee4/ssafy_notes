import sys 
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst_house=[]
    dist  = [[[0] * (N) for _ in range(31)] for _ in range(31)]  
    for i in range(N):
        r, c, d = map(int, input().split())
        r = r+15
        c = c+15
        lst_house.append((r,c,d))

    for r in range(31):
        for c in range(31):
            for i in range(N):
                tr, tc, d=lst_house[i]
                dist[r][c][i] = abs(tr-r)+ abs(tc-c)

                
