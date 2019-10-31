def verifyBrackets(oper):
    global pairs
    pairs = []
    index = 0
    for i in range(len(oper)):
        if index<0:
            return "Error!! More closing brackets than opening brackets"
        if oper[i]=="(":
            index += 1
            pairs.append(i)
        elif oper[i]==")":
            index -= 1
            pairs.append(-i)
    if index>0:
        return "Error!! More opening brackets than closing brackets"
    if index<0:
        return "Error!! More closing brackets than opening brackets"
    return True

priority = {"^":lambda a, b:a**b, "*":lambda a, b:a*b, "/":lambda a, b:a//b, "+":lambda a, b:a+b, "-":lambda a, b:a-b}
priority2 = [["^"], ["*", "/"], ["+", "-"]]
priority3 = [str(i) for i in range(0, 10)]

def verifyCalculation(oper):
    global oper2
    oper2 = oper
    for i in priority2:
        j = 1
        while j<len(oper2):
            if oper2[j] in i:
                index = j-1
                while index>-1 and oper2[index] in priority3:
                    index -= 1
                index2 = j+1
                while index2<len(oper2) and oper2[index2] in priority3:
                    index2 += 1
                try:
                    result = str(priority[oper2[j]](int(oper2[index+1: j]), int(oper2[j+1:index2])))
                    oper2 = oper2[:index+1] + result + oper2[index2:]
                    j -= j - index - 1
                except:
                    return "Error!! Operation {} isn't in between numbers".format(i)
            j += 1
    return True

def evaluation(oper):
    oper3 = "(" + oper + ")"
    result = verifyBrackets(oper3)
    if True!=result:
        return result
    index = 0
    while index<len(pairs):
        if pairs[index]<0:
            result = verifyCalculation(oper3[pairs[index-1]+1:-1*pairs[index]])
            if True!=result:
                return result
            oper3 = oper3[:pairs[index-1]] + oper2 + oper3[-1*pairs[index]+1:]
            dec = -1*pairs[index] - len(oper3[:pairs[index-1]] + oper2)+1
            for i in range(index+1, len(pairs)):
                if pairs[i]>0:
                    pairs[i] -= dec
                else:
                    pairs[i] += dec
            del pairs[index]
            del pairs[index-1]
            index -= 2
        index += 1
    return oper3

if __name__=="__main__":
    tempStr = input()
    print(evaluation(tempStr))

