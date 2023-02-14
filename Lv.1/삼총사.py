def solution(number):
    count = 0
    for i in range(len(number) - 2):
        for j in range(i, len(number) - 1):
            if i == j: continue
            for k in range(j, len(number)):
                if j == k or i == k: continue
                if number[i] + number[j] + number[k] == 0:
                    count += 1
    return count

print(solution([-2, 3, 0, 2, -5]))