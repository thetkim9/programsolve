c, k, t = map(int, input().split())

num = [c, 1]

maxNum = 0
def findBiggest(num, k, t):
    global maxNum
    value = num[0]*num[1]
    if (t==0):
        maxNum = max(maxNum, value)
    else:
        #addition
        findBiggest([num[0]+k, num[1]], k, t-1)
        #separation
        for i in range(2, int(value**0.5)+1):
            if (value%i==0):
                findBiggest([i, value//i], k, t-1)

findBiggest(num, k, t)
print(maxNum)

