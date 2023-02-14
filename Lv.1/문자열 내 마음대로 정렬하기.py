def solution(strings, n):
    sorted(strings, key=lambda x: x[n])
    strings.sort()
    return strings




strings = ["abce", "abcd", "cdx"]
n = 2
strings2 = ["sun", "bed", "car"]
n2 = 1
print(solution(strings, n))
print(solution(strings2, n2))