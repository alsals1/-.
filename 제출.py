import sys

sys.stdin = open('sample_input(1).txt')
# 
# # Othello 클래스 생성
class Othello:
		# 상하좌우/대각선 8개 방향 정보 저장
    dirs = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)] # 클래스 변수. 공통된것은 위에 빼서 메모리 절약
    

    def __init__(self, n):
				# 인스턴스 생성시 board 정보 생성 (크기는 입력 n일 때 n+2 * n+2로)
        self.board = [[0 for _ in range(n+2)] for _ in range(n+2)]
        self.board_size = n
        self.board[n // 2 + 1][n // 2 + 1], self.board[n // 2][n // 2] = 2, 2
        self.board[n // 2][n // 2 + 1], self.board[n // 2 + 1][n // 2] = 1, 1


    def do(self, i, j, c):
				# 돌을 넣을 때 좌표(i, j)와 돌 색 c 입력
				# 좌표에 돌을 입력
        self.board[i][j] = c 

				# 돌을 뒤집을지 여부를 확인할 방향 확인
        dir_lst = []
        for d in self.dirs:
            ni = i + d[0]
            nj = j + d[1]
            point = self.board[ni][nj]
            # 내가 놓은 돌과 다른 색상의 돌이 있는 방향을 방향 리스트에 저장
            if point != 0 and point != c: 
                dir_lst.append(self.dirs.index(d))
				
				# 돌을 뒤집어 줄 메서드 호출
        self.change_stones(i, j, c, dir_lst)

        return self.board    # 보드 반환

		# 돌을 뒤집는 메서드
    def _change_stones(self, i, j, c, dir_lst): # 클래스 내부에서만 쓰는 함수..
				
        for num in range(len(dir_lst)):    # 입력받은 방향 리스트를 순회
            temp_lst = []
            temp_point = self.board[i][j]    # 현재 좌표의 색을 저장
            ni, nj = i, j
            while temp_point:    # 현재 좌표가 0이 아닐 때 반복
								# ni, nj는 현재 가리키는 방향으로 1만큼씩 이동
                ni += self.dirs[dir_lst[num]][0]
                nj += self.dirs[dir_lst[num]][1]
                temp_point = self.board[ni][nj]    # 이동한 좌표
                if temp_point == 0:    # 0이면 돌인 안뒤집고 반복 종료
                    break
                elif temp_point != c:    # 놓은 돌과 다른 색상의 돌이면 좌표 저장
                    temp_lst.append([ni, nj])
                else:    # 놓은 돌과 같은 색상의 돌을 만나면 저장된 좌표를 전부 뒤집기
                    for e in temp_lst:
                        self.board[e[0]][e[1]] = c
                    break
        return self.board    # 보드 반환

    # 흑돌(1), 하얀돌(2)의 수를 세서 반환해주는 메서드
    def count_values(self):
        ones = 0
        twos = 0
        for e in self.board:    # 보드를 순회하며 돌 수를 세서 반환
            ones += e.count(1)
            twos += e.count(2)
        return ones, twos


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = Othello(N)    # 보드의 크기를 인자로 입력하며 오셀로(클래스) 보드 생성

    for _ in range(M):  # M만큼 반복하며 입력 값을 인자로 Othello 클래스의 do 메서드 호출
        x, y, stone = map(int, input().split())
        board.do(x, y, stone)
    
    result = board.count_values()    # 돌의 수를 각각 세는 메서드 호출하여 반환

    print(f'#{tc}', *result)
