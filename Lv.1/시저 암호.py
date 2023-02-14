def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += " "
        elif i.isupper():
            answer += chr(((ord(i) + n - 65) % 26) + 65)
        else:
            print(ord('a'))
            answer += chr(((ord(i) + n - 97) % 26) + 97)

    return answer

print(solution("AB", 1))
