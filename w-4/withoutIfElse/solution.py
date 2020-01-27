x = [0, 0, 0]
x[0], x[1], x[2] = map(int, input().split())
dict = {i:0 for i in range(1, 7)}
for i in x:
    dict[i] += 1
dict2 = {0:0, 1:0, 2:1000, 3:10000}
dict3 = {0:0, 1:0, 2:100, 3:1000}
dict4 = {i:0 for i in range(1, 16001)}
dict4[0] = 100*max(x)
answer = 0
for key in dict:
    answer += dict3[dict[key]]*key
answer += dict4[answer]
print(answer + dict2[max(dict.values())])
