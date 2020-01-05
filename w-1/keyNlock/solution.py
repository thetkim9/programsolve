import numpy as np
def solution(key, lock):
    #1 region of interest
    M = len(key)
    N = len(lock)
    roiXmin = 21
    roiXmax = 0
    roiYmin = 21
    roiYmax = 0
    for i in range(N):
        for j in range(N):
            if lock[i][j]==0:
                roiXmin = min(roiXmin, j)
                roiXmax = max(roiXmax, j)
                roiYmin = min(roiYmin, i)
                roiYmax = max(roiYmax, i)
    x = roiXmax - roiXmin + 1
    y = roiYmax - roiYmin + 1
    if M<x or M<y:
        return False
    #2 rotated key matrices
    rotated = []
    rot0 = np.array(key)
    rotated.append(rot0.tolist())
    for i in range(3):
        rot0 = np.rot90(rot0)
        rotated.append(rot0.tolist())
    #3 region of calculation
    answer = False
    for i in range(N-y+1):
        for j in range(N-x+1):
            xShift = j - roiXmin
            yShift = i - roiYmin
            for matrix in rotated:
                answer = True
                for a in range(N):
                    for b in range(N):
                        if b+xShift<0 or b+xShift>M-1 or a+yShift<0 or a+yShift>M-1:
                            continue
                        if lock[a][b]+matrix[a+yShift][b+xShift]!=1:
                            answer = False
                            break
                if answer:
                    return answer
    return answer
