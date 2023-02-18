def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    count = 0
    z = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            count += 1

    return [rank[count + z], rank[count]]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))