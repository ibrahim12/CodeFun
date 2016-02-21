g, r = map(int, input().split())

b = [int(_) for _ in input().split()]
# min_b = min(b)
max_b = max(b)

room_info = []

for i in range(r):
    p, c = map(int, input().split())
    if p <= max_b:
        room_info.append([p, c])


# b = sorted(b)
# room_info = sorted(room_info, key=lambda x : x[1])

import sys

def dfs(b_list, r_info, count):
    # print(b_list, r_info, count)
    if not b_list:
        return count

    if not r_info:
        return sys.maxsize

    t_count = sys.maxsize
    for j in range(len(b_list)):
        a_b = b_list[j]
        clone_b_list = b_list.copy()
        del clone_b_list[j]

        n = len(r_info)
        s_count = sys.maxsize

        for i in range(n):

            a_room = r_info[i]
            c_count = count
            if a_b >= a_room[0]:
               clone_r_info = r_info.copy()

               c_count += 1

               if clone_r_info[i][1] > 1:
                   clone_r_info[i][1] -= 1
               else:
                   del clone_r_info[i]

               s_count = min(s_count, dfs(clone_b_list, clone_r_info, c_count))
               # print(s_count)

        t_count = min(t_count, s_count)

    return s_count



count = dfs(b, room_info, 0)
print(count)


# print(room_info, g, r, b, min_b, max_b)



"""
3 4
60 75 50
40 1
70 2
40 1
40 1
"""