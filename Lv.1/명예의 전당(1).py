def solution(k, score):
    array = []
    answer = []
    for i in score:
        array.append(i)
        array.sort(reverse=True)
        if len(array) > k:
            array.pop()
        answer.append(min(array))
    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))
