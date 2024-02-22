def enque(arr):
    global last
    for num in arr:
        last += 1
        tree[last] = num
        c = last
        p = last // 2
        while p >= 1 and tree[c] < tree[p]:
            tree[c], tree[p] = tree[p], tree[c]
            c = p
            p = c // 2


def postorder(node):
    global sumAnc
    if node >= 1:
        p = node // 2
        postorder(p)
        sumAnc += tree[p]


for tc in range(1, int(input()) + 1):
    n = int(input())
    tree = [0] * (n + 1)
    arr = list(map(int, input().split()))
    last = sumAnc = 0
    enque(arr)
    postorder(n)
    print(f'#{tc} {sumAnc}')