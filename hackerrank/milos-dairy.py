t = int(input())

def get_lowest(cur, mem):
    for i in range(cur, 0, -1):
        if i not in mem:
            return i

    return -1

for k in range(t):
    n = int(input())
    num = [int(_) for _ in input().split()]

    out = 'YES'

    if n == 1:
        out = 'YES'

    else:

        mem = {num[0]: True}
        for i in range(1, n):
            if not (num[i] > num[i-1] or get_lowest(num[i-1], mem) == num[i]) :
               out = 'NO'
               break

            mem[num[i]] = True

    print(out)


"""
3
4
2 4 3 5
4
4 1 2 3
1
4
2 3 4 1
"""