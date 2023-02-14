def solution(t, p):
    count = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:len(p)]) <= int(p):
            count += 1
    return count

print(solution("314159", "271"))