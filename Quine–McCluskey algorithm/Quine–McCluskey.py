#functions
def comTerm(t1, t2, N):
    count = 0
    res = ""
    for i in range(N):
        if t1[i]!=t2[i]:
            if count>0:
                return False
            count += 1
            res += "-"
        else:
            res += t1[i]

    if count==1:
        return res
    else:
        return False

def findSet(PIs, ones, dict, preIndex, piL, onesL, current):
    global candidates
    for i in range(preIndex+1, piL):
        e = PIs[i]
        Set = set(dict[e])
        if ones.union(Set)==Set:
            candidates.append(current+[e])
        else:
            findSet(PIs, ones.difference(Set), dict, i, piL, onesL, current+[e])

def numOperation(lst, n):
    val = len(lst) - 1
    for var in lst:
        v = var.count("-")
        if v==n+1:
            return -1
        val += n - v
    return val

#main logic
def tabular(vars, ones, donts):
    global candidates
    N = len(vars)

    # step 1 -- finding prime implicants
    table = [[] for i in range(N + 1)]
    dict = {}
    for num in ones:
        conv = str(bin(num))
        val = "0" * (N + 2 - len(conv)) + conv[2:]
        dict[val] = [num]
        table[val.count("1")].append(val)

    for num in donts:
        conv = str(bin(num))
        val = "0" * (N + 2 - len(conv)) + conv[2:]
        dict[val] = [num]
        table[val.count("1")].append(val)

    PIs = set([])
    old = table
    new = []
    while old:
        misses = [[True for l in old[0]]]
        lenO = len(old)
        for i in range(lenO - 1):
            new.append([])
            misses.append([True for l in old[i + 1]])
            for k in range(len(old[i])):
                term = old[i][k]
                missed = True
                for j in range(len(old[i + 1])):
                    term2 = old[i + 1][j]
                    res = comTerm(term, term2, N)
                    if res:
                        new[i].append(res)
                        dict[res] = dict[term] + dict[term2]
                        misses[i + 1][j] = False
                        missed = False
                if missed and misses[i][k]:
                    PIs.add(term)
        for i in range(len(old[lenO - 1])):
            if misses[lenO - 1][i]:
                PIs.add(old[lenO - 1][i])
        old = new
        new = []

    print("PIs:", PIs)
    print("and its corresponding values:", [sorted(dict[e]) for e in PIs])
    print()

    # step 2 -- finding EPIs
    dict2 = {i: 0 for i in ones}

    for ele in PIs:
        for i in dict[ele]:
            if i in dict2:
                dict2[i] += 1

    EPIs = set([])
    for key in dict2:
        if dict2[key] == 1:
            for ele in PIs:
                if key in dict[ele]:
                    EPIs.add(ele)
                    break
    print("EPIs:", EPIs)
    print("and its corresponding values:", [sorted(dict[e]) for e in EPIs])
    print()

    #step 3 - finding optimized boolean expression(s)
    candidates = []

    for num in donts:
        for e in dict:
            if num in dict[e]:
                dict[e].remove(num)

    ones = set(ones)

    for e in EPIs:
        PIs.discard(e)
        for ele in dict[e]:
            ones.discard(ele)


    if len(ones)>0:
        findSet(list(PIs), ones, dict, -1, len(PIs), len(ones), [])

    candidates.sort(key=lambda e:numOperation(e, N-1))

    res = []
    if len(candidates)>0:
        res.append(candidates[0])

        val = numOperation(candidates[0], N-1)

        for i in range(1, len(candidates)):
            if val==numOperation(candidates[i], N-1):
                res.append(candidates[i])
            else:
                break

    conv = [{"1":var, "0":var+str('\''), "-":""} for var in vars]

    epiexpression = ""
    for term in EPIs:
        for i in range(len(term)):
            epiexpression += conv[i][term[i]]
        epiexpression += " + "

    print("f =")
    if len(candidates) > 0:
        ans = []
        for equation in res:
            expression = epiexpression
            for term in equation:
                for i in range(len(term)):
                    expression += conv[i][term[i]]
                expression += " + "
            if len(expression)>3:
                ans.append(expression[:len(expression)-3])

        for answer in ans:
            print(answer)
    else:
        print(epiexpression[:len(epiexpression)-3])



if __name__=="__main__":
    #input
    print("Please omit commas between letters and numbers!!")
    print()
    print("f(__first input__) = sum(m(__second input__)) + d(__third input__)")
    print()
    vars = list(input("__first input__(enter space in between letters):").split())
    ones = list(map(int, input("__second input__(enter space in between numbers):").split()))
    donts = list(map(int, input("__third input__(enter space in between numbers):").split()))
    print()

    #test cases
    '''
    vars = ['a', 'b', 'c', 'd']
    ones = [4, 8, 10, 11, 12, 15]
    donts = [9, 14]
    '''
    '''
    vars = ['a', 'b', 'c', 'd']
    ones = [0, 2, 5, 6, 7, 8, 9, 13]
    donts = [1, 12, 15]
    '''
    '''
    vars = ['w', 'x', 'y', 'z']
    ones = [2,6,8,9,10,11,14,15]
    donts = []
    '''
    '''
    vars = ['a', 'b', 'c', 'd']
    ones = [0,1,2,5,6,7,8,9,10,14]
    donts = []
    '''
    '''
    vars = ['a', 'b', 'c', 'd']
    ones = [2,3,7,9,11,13]
    donts = [1,10,15]
    '''
    '''
    vars = ['a', 'b', 'c']
    ones = [0, 1, 2, 5, 6, 7]
    donts = []
    '''

    tabular(vars, ones, donts)







