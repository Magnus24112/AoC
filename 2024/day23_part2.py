from collections import defaultdict
from time import perf_counter
start = perf_counter()
# https://www.geeksforgeeks.org/maximal-clique-problem-recursive-solution/

with open('input_day23.txt') as file:
    data = set(tuple(line.strip().split('-')) for line in file.readlines())

def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph
        )
        X.add(v)


neighbours = defaultdict(set)
for name1, name2 in data:
    neighbours[name1].add(name2)
    neighbours[name2].add(name1)

neighbours = {key: set(neighbours[key]) for key in neighbours} # consistent sorting

all_cliques = list(bron_kerbosch(set(), set(neighbours.keys()), set(), neighbours))
max_clique = max(all_cliques, key=len)

print(','.join(sorted(max_clique)), len(max_clique))
print(perf_counter() - start)