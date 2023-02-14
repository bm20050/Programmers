def solution(a, b):
    array = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = b
    for i in range(a - 1):
        sum += month[i]

    return array[(sum + 4) % 7]

print(solution(5, 24))