def solution(s):
    array = [['zero', 0], ['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5], ['six', 6], ['seven', 7],
             ['eight', 8], ['nine', 9]]

    for i in array:
        if i[0] in s:
            s = s.replace(i[0], str(i[1]))
    return int(s)

s = "one4seveneight"
print(solution(s))
