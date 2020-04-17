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

#input
print("f(__first input__) = sum(m(__second input__)) + d(__third input__)")
vars = list(input("__first input__(enter space in between letters):").split())
ones = list(map(int, input("__second input__(enter space in between numbers):").split()))
donts = list(map(int, input("__third input__(enter space in between numbers):").split()))
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

N = len(vars)

#step 1 -- finding prime implicants
table = [[] for i in range(N+1)]
dict = {}
for num in ones:
    conv = str(bin(num))
    val = "0"*(N+2-len(conv))+conv[2:]
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
    for i in range(lenO-1):
        new.append([])
        misses.append([True for l in old[i + 1]])
        for k in range(len(old[i])):
            term = old[i][k]
            missed = True
            for j in range(len(old[i+1])):
                term2 = old[i+1][j]
                res = comTerm(term, term2, N)
                if res:
                    new[i].append(res)
                    dict[res] = dict[term] + dict[term2]
                    misses[i+1][j] = False
                    missed = False
            if missed and misses[i][k]:
                PIs.add(term)
    for i in range(len(old[lenO-1])):
        if misses[lenO-1][i]:
            PIs.add(old[lenO-1][i])
    old = new
    new = []

print("PIs:", PIs)
print("and its corresponding values:", [sorted(dict[e]) for e in PIs])

#step 2 -- finding EPIs
vals = []
for ele in PIs:
    vals += [i for i in dict[ele]]
vals = set(vals)
for ele in donts:
    vals.discard(ele)

dict2 = {i:0 for i in vals}

for ele in PIs:
    for i in dict[ele]:
        if i in dict2:
            dict2[i] += 1

EPIs = []
for key in dict2:
    if dict2[key]==1:
        for ele in PIs:
            if key in dict[ele]:
                EPIs.append(ele)
                break
print("EPIs:", EPIs)
print("and its corresponding values:", [sorted(dict[e]) for e in EPIs])






