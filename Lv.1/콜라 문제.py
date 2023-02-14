def solution(a, b, n):
    sum = 0
    while n > a:
        x = n % a
        sum += n // a * b
        n = x + n // a * b
    return sum

print(solution(3, 1, 20))