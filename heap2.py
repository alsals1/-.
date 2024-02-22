# 힙에서는 루트 노드 원소만 삭제 가능
# 최대 힙: key 가 가장 큰 값
# 최소 힙: key 가 가장 작은 값 - 오름차순 정렬이 되어 나온다. 
# 힙의 종류에 따라 최대값과 최솟값을 구할 수 있다.....


# 루트 노드를 임시 보관
# 형제끼리는 대소 관계 X 자식 중 큰 것보다 부모가 커야한다.(최대힙)
# 최소 힙은 자식이 점점 커진다. 
# while 하며서 게속 바꾼다 ..

def deq():
    global last
    tmp = h[1] # 루트의 키 값 보관
    h[1]=h[last]
    last -= 1
    p=1
    c=p*2
    while c<=last: # 자식이 있다...
        if c+1 <= last and h[c]<h[c+1]:
            c+=1
        if h[p]<h[c]:
            h[p],h[c] = h[c],h[p]
            p = c
            c = p*2
                        
N = 10
h = [0]*11
last = 0

while(last>0):
    print()