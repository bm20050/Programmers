def solution(cards1, cards2, goal):
    i = 0
    j = 0
    for x in goal:
        if x == cards1[i]:
            if i < len(cards1) - 1:
                i += 1
        elif x == cards2[j]:
            if j < len(cards2) - 1:
                j += 1
        else:
            return "No"
    return "Yes"

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))