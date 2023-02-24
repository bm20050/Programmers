def solution(n, lost, reserve):
    reserve.sort()
    for i in reserve:
        if i in lost:
            lost.remove(i)
            continue
        if i - 1 in lost and i - 1 not in reserve:
            lost.remove(i - 1)
        elif i + 1 in lost and i + 1 not in reserve:
            lost.remove(i + 1)

    return n - len(lost)


n = 5
lost = [2, 4]
reserve = [1, 3, 5]

print(solution(n, lost, reserve))
