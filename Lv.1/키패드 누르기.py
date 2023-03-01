def solution(numbers, hand):
    left = [1, 4, 7]
    right = [3, 6, 9]
    answer = ''
    l = 10
    r = 12
    for i in numbers:
        if i == 0:
            i = 11
        if i in left:
            l = i
            answer += 'L'
        elif i in right:
            r = i
            answer += 'R'
        else:
            a = abs(i - l)
            a = (a // 3) + (a % 3)

            b = abs(i - r)
            b = (b // 3) + (b % 3)

            if a == b:
                if hand == 'right':
                    r = i
                    answer += 'R'
                else:
                    l = i
                    answer += 'L'
            elif a > b:
                r = i
                answer += 'R'
            else:
                l = i
                answer += 'L'
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))
