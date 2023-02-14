# 짝지어 제거하기
def solution(s):
    x = ""
    temp = ""
    flag = 1
    while flag == 1:
        for i in range(len(s)):
            if temp == s[i]:
                x = x[:-1]
                x += s[i+1:]
                flag = 1
                break
            else:
                x += s[i]
                flag = 0
            temp = s[i]
        s = x
        x = ""
        if (len(s) == 0):
            return 1
    return 0


print(solution("cdcd"))