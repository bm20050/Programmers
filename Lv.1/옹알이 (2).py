def solution(babbling):
<<<<<<< HEAD
    # array = ["aya", "ye", "woo", "ma"]
    result = 0
    for i in babbling:
        temp  = ""
        while len(i) > 1:
            if  temp != i[:2] and i[:2] == 'ye' or i[:2] == 'ma':
                temp = i[:2]
                i = i[2:]
            elif temp != i[:3] and i[:3] == 'aya' or i[:3] == 'woo':
=======
    result = 0
    for i in babbling:
        temp = ""
        while len(i) > 1:
            if temp != i[:2] and (i[:2] == 'ye' or i[:2] == 'ma'):
                temp = i[:2]
                i = i[2:]
            elif temp != i[:3] and (i[:3] == 'aya' or i[:3] == 'woo'):
>>>>>>> origin/main
                temp = i[:3]
                i = i[3:]
            else:
                break
        if len(i) == 0:
            result += 1

<<<<<<< HEAD

    return result

babbling = ["aya", "yee", "u", "maa"]
babbling2 = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

print(solution(babbling))
print(solution(babbling2))
=======
    return result


babbling = ["mama", "yeye", "woowoo", "ayaaya"]

print(solution(babbling))
>>>>>>> origin/main
