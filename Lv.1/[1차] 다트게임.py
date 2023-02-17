def solution(dartResult):
    answer = []

    for i in dartResult:
        if i.isdigit():
            if len(answer) >= 1 and i == '0' and answer[-1] == 1:
                answer.pop()
                answer.append(10)
            else:
                answer.append(int(i))
        elif i == 'S':
            continue
        elif i == 'D':
            answer[-1] = answer[-1] ** 2
        elif i == 'T':
            answer[-1] = answer[-1] ** 3
        elif i == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == '#':
            answer[-1] = answer[-1] * (-1)

    return sum(answer)



dartResult = "1S*2T*3S"
print(solution(dartResult))