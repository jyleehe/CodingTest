# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
#
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
#
# 예시:
# 입력: 8
# 출력: 92

###########################

n = int(input())
ans = 0

# cols = [] # col
# diag = [] # row + col
# diag_opp = [] # row - col

def dfs(row, N, cols, diag, diag_opp): # row 마다 하나의 퀸만 위치 가능.
    global ans
    if row == N:
        ans += 1
        return

    for i in range(N):
        tmp_dg = row + i # 퀸이 (row, i) 에 위치했을 때 대각 라인 검사
        tmp_dg_opp = row - i # 퀸이 (row, i) 에 위치했을 때 반대 대각 라인 검사
        if i not in cols and tmp_dg not in diag and tmp_dg_opp not in diag_opp:
            cols.append(i) # 세로 라인 안겹치면 추가
            diag.append(tmp_dg)
            diag_opp.append(tmp_dg_opp)
            dfs(row+1, N, cols, diag, diag_opp) # next row
            # backtracking
            cols.pop()
            diag.pop()
            diag_opp.pop()

dfs(0, n, [], [], [])
print(ans)