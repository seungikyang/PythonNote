# print("9012")

T = int(input())

for _ in range(T):
    stk = []
    isVPS = True
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                isVPS = False
                break

    if len(stk) > 0:
        isVPS = False

    print("YES" if isVPS else "NO")
    