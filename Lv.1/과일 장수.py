def solution(k, m, score):
    score.sort(reverse=True)
    sum = 0
    for i in range(len(score)):
        if i % m == m - 1:
            sum += score[i]
    return sum * m


k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]

print(solution(k, m, score))
