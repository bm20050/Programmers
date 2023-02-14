def solution(n):
    x = 0
    i = n
    while bin(n).count('1') != x:
        i += 1
        x = bin(i).count('1')
    return i


n = 78
print(solution(n))