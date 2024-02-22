import sys

sys.stdin = open('5178_input.txt')
for tc in range(1,int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    if N%2 == 0:
        tree.append(0)
        
    for _ in range(M):
        l, num = map(int, input().split())
        tree[l]=num
   
    for i in range((N-M),0,-1):
        tree[i]=tree[i*2]+tree[i*2+1]
    
    print(f'#{tc}', tree[L]) 