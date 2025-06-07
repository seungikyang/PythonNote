import sys
input = sys.stdin.readline

stk = []

PSs = input().strip()
tot = 0

for i in range(len(PSs)):
    if PSs[i] == '(':
        stk.append(PSs[i])
    else:
        if PSs[i-1] == '(':
            stk.pop()
            tot += len(stk)
        else:
            stk.pop()
            tot += 1
print(tot)