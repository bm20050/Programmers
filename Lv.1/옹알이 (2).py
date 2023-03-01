def solution(babbling):
    result = 0
    for i in babbling:
        temp = ""
        while len(i) > 1:
            if temp != i[:2] and (i[:2] == 'ye' or i[:2] == 'ma'):
                temp = i[:2]
                i = i[2:]
            elif temp != i[:3] and (i[:3] == 'aya' or i[:3] == 'woo'):
                temp = i[:3]
                i = i[3:]
            else:
                break
        if len(i) == 0:
            result += 1

    return result


babbling = ["mama", "yeye", "woowoo", "ayaaya"]

print(solution(babbling))
