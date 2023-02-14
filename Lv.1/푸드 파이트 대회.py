def solution(food):
    answer = ""
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            answer += str(i)
    rev = answer[::-1]
    answer+= '0' + rev

    return answer


food = [1, 3, 4, 6]
print(solution(food))