def solution(n, times):
    times.sort()
    lower = 1
    upper = 10**18
    while True:
        mid = (lower+upper)//2
        Sum = 0
        check = False
        repeatVal = 0
        for ele in times:
            if mid%ele==0:
                repeatVal = ele
                check = True
            Sum += mid//ele
        count = times.count(repeatVal)
        if n<=Sum<n+count and check:
            return mid
        elif Sum<n:
            lower = mid+1
        else:
            upper = mid-1
