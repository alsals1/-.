#%%
class MaxHeap:
    def __init__(self, heap_size) -> None:
        self.last = 0
        self.heap_size = heap_size
        self.heap = [0] * (self.heap_size + 1)

    def enq(self,n):
        self.last += 1       # 마지막 정점 추가
        self.check_size()
        self.heap[self.last] = n  # 마지막 정점에 key 추가

        c = self.last
        p = c // 2      # 완전이진트리에서 부모 정점 번호
        while p and self.heap[p] < self.heap[c]: # 부모가 있고, 부모 < 자식 인경우 자리 교환
            self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
            c = p
            p = c//2

    def deq(self):
        
        tmp = self.heap[1]           # 루트 백업
        self.heap[1] = self.heap[self.last]    # 삭제할 노드의 키를 루트에 복사
        self.last -= 1               # 마지막 노드 삭제
        p = 1                   # 루트에 옮긴 값을 자식과 비교
        c = p * 2               # 왼쪽 자식
        while c <= self.last:        # 자식이 하나라도 있으면
            if c+1 <= self.last and self.heap[c] < self.heap[c+1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
                c += 1                      # 비교 대상을 오른쪽 자식으로 정함
            if self.heap[p] < self.heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
                self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
                p = c               # 자식을 새로운 부모로
                c = p * 2           # 왼쪽 자식 번호를 계산
            else:                   # 부모가 더 크면
                break               # 비교 중단,
        return tmp
    
    def check_size(self):
        if self.last > self.heap_size + 1 :
            pre_size = self.heap_size
            self.heap_size += int(self.heap_size * 0.2) + 10
            self.heap += [0] * (self.heap_size - pre_size)
            
    def __len__(self):
        return self.last
    
    def __str__(self) :
        return f'{self.heap[1:self.last]}'

heap = MaxHeap(100)

heap.enq(2)
heap.enq(5)
heap.enq(7)
heap.enq(3)
heap.enq(4)
heap.enq(6)
print(heap)
while len(heap):
    print(heap.deq())
