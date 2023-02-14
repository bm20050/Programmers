from itertools import combinations
def solution(nums):
    array = combinations(nums, 3)
    sumArray = []
    for i in array:
        sumArray.append(sum(i))
    result = 0
    for i in range(len(sumArray)):
        x = 0
        for j in range(2, sumArray[i]):
            x += 1
            if sumArray[i] % j == 0:
                break
        if x == sumArray[i] - 2:
            result += 1
    return result

nums = [1,2,7,6,4]
print(solution(nums))