class Solution(object):
    def isP(self, s):
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length - 1 - i]:
                return False
        return True

    def longestPalindrome(self, s):
        dp = []
        if len(s) == 0:
            maxP = ""
        else:
            maxP = s[0]
        length = len(s)
        for i in range(length-1):
            tempS2 = s[i:i + 2]
            if self.isP(tempS2):
                dp.append([i, i + 1])
            if i < length - 2:
                tempS3 = s[i:i + 3]
                if self.isP(tempS3):
                    dp.append([i, i + 2])
        for ele in dp:
            indexRemain = min(ele[0], length - ele[1] - 1)
            indexL = ele[0]
            indexR = ele[1]+1
            for i in range(1, indexRemain + 1):
                if s[ele[0] - i] != s[ele[1] + i]:
                    indexL = ele[0] - i + 1
                    indexR = ele[1] + i
                    break
                elif i==indexRemain:
                    indexL = ele[0] - i
                    indexR = ele[1] + i + 1
            result = s[indexL:indexR]
            if len(maxP) < len(result):
                maxP = result
        return maxP
