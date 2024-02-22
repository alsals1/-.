def enq(n):
    global last
    last += 1
    # 마지막 노드 추가 (완전 이진 트리 유지)
    
    h[last] = n
    # 마지막 노드에 데이터 삽입
    
    c = last
    # 부모>자식 비교위해서
    p = c//2
    # 부모 번호 계산
    
    while p>=1 and h[p]>h[c]: # 이런 상황이면 자리 바꿔야해 부모가 있는데 더 작으면 교환해
        h[p], h[c] = h[c], h[p] # 교환
        c = p
        p = c//2
        
    return h, 'last는 c =', last, 'p는', p


N = 10 # 노드 10개
h = [0]*(N+1) # 0 부터 N 까지의 인덱스
last = 0
tree = [2,5, 3, 6, 4]

for t in tree:
    print(enq(t))