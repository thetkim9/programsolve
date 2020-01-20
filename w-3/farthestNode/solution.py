from collections import defaultdict

def solution(n, edges):
    edict = defaultdict(list)
    d = [0] + [50001 for i in range(n-1)]
    queue = [1]
    visited = set([])
    for edge in edges:
        edict[edge[0]].append(edge[1])
        edict[edge[1]].append(edge[0])
    dmax = 0
    while queue:
        cur = queue.pop(0)
        visited.add(cur)
        outv = list(set(edict[cur]) - visited - set(queue))
        if not outv:
            dmax = max(dmax, d[cur-1])
            continue
        queue += outv
        for v in outv:
            d[v-1] = min(d[cur-1] + 1, d[v-1])
    return d.count(dmax)
