# import sys

# sys.stdin = open('sample_input(1).txt')


for tc in range(1,1+int(input())):
    N, M = map(int, input().split()) # NxN,('4',6,8) M회 12
    NxN = [[0]*N for _ in range(N)]
    NxN[N//2][N//2] = 2
    NxN[(N//2)-1][(N//2)-1] = 2
    NxN[(N//2)][(N//2)-1] = 1
    NxN[(N//2)-1][N//2] = 1
    # print(NxN)
    # [[0, 0, 0, 0], [0, 2, 1, 0], [0, 1, 2, 0], [0, 0, 0, 0]]
    
    
    for _ in range(M):
        j, i, w_b = map(int, input().split())
        if w_b ==1 :
            NxN[i-1][j-1] = 1
        else:
            NxN[i-1][j-1] = 2
            
        dirs = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]] # 8방향
        
        for d in dirs:
            ni = i-1 + d[0]
            nj = j-1 + d[1]
            if 0<=ni<N and 0<=nj<N and NxN[ni][nj] !=0 and NxN[ni][nj] != w_b:
                change_check_list = []
                
                while NxN[ni][nj] != w_b:
                    change_check_list.append([ni,nj,NxN[ni][nj]])
                    ni += d[0]
                    nj += d[1]
                    print(f'ni는',ni)
                    print(f'nj는',nj)
                    print(change_check_list) 
                
        
                 
    