def solution(X, Y):
    s = ""
    X = list(X)
    Y = list(Y)

    for i in range(9, -1, -1):
        xcount = X.count(str(i))
        ycount = Y.count(str(i))
        s += str(i) * min(xcount, ycount)

    if len(s) == 0:
        return "-1"
    if s[0] == "0":
        return "0"
    return s


X = "123"
Y = "2345"

print(solution(X, Y))