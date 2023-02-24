def solution(N, stages):
    falseRate = []
    count = 0
    for i in range(1, N + 1):
        count += stages.count(i - 1)
        if len(stages) - count != 0:
            falseRate.append([stages.count(i) / (len(stages) - count), i])
        else:
            falseRate.append([0, i])
    falseRate.sort(key=lambda x: x[0], reverse=True)

    return [i[1] for i in falseRate]


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
