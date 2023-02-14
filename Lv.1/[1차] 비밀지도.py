def solution(n, arr1, arr2):
    a1 = []
    a2 = []
    answer = []
    for i in range(n):
        a1.append(bin(arr1[i])[2:].zfill(n))
        a2.append(bin(arr2[i])[2:].zfill(n))
    for i in range(n):
        temp = ""
        for j in range(n):
            if len(a1[i][2:]) < n:
                a1[i] = (n - len(a1)) * "0" + a1[2:]
            if len(a2[i][2:]) < n:
                a2[i] = (n - len(a2)) * "0" + a1[2:]
            if a1[i][j] == " " and a2[i][j] == " ":
                temp += " "
            else:
                temp += "#"
        answer.append(temp)

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))