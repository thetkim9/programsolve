def solution(n, costs):
    costs.sort(key=lambda e:e[2])
    ans = costs[0][2]
    Set = set([])
    Set.add(costs[0][0])
    Set.add(costs[0][1])
    for i in range(n):
        size = len(Set)
        for j in range(len(costs)):
            Set.add(costs[j][0])
            Set.add(costs[j][1])
            if size+1==len(Set):
                ans += costs[j][2]
                del costs[j]
                break
            elif size+2==len(Set):
                Set.remove(costs[j][0])
                Set.remove(costs[j][1])
    return ans
