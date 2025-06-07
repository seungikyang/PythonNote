import sys
input = sys.stdin.readline

n = int(input())

heights = [int(input().split()[1]) for _ in range(n)]
heights.append(0)  # 마지막 처리를 위해 0을 추가

stk = []
count = 0

for height in heights:
    # 높이가 줄어들면 스택에서 제거하고 count 증가
    while stk and stk[-1] > height:
        stk.pop()
        count += 1
    # 높이가 다르면 스택에 push
    if not stk or stk[-1] < height:
        stk.append(height)

print(count)