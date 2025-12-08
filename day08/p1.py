from typing import List
from collections import defaultdict

# credit: https://medium.com/@conniezhou678/mastering-dara-algorithm-part-28-understanding-union-find-in-python-155da9e04ccb
class UnionFind:
  def __init__(self, size):
    self.parent = list(range(size))
    self.rank = [1] * size

  def find(self, p):
    if self.parent[p] != p:
      self.parent[p] = self.find(self.parent[p])  # Path compression
    return self.parent[p]

  def union(self, p, q):
    rootP = self.find(p)
    rootQ = self.find(q)

    if rootP != rootQ:
      if self.rank[rootP] > self.rank[rootQ]:
        self.parent[rootQ] = rootP
      elif self.rank[rootP] < self.rank[rootQ]:
        self.parent[rootP] = rootQ
      else:
        self.parent[rootQ] = rootP
        self.rank[rootP] += 1

def size(s, graph, visited):
  if s in visited: return 0
  st = [s]
  cnt = 0
  while st:
    cur = st.pop()
    visited.add(cur)
    cnt += 1
    for n in graph[cur]:
      if n in visited: continue
      st.append(n)
  return cnt
   
def solve(inp: List[str]):
  # kruskal
  edges = []
  nums = [tuple(int(x) for x in y.split(",")) for y in inp]
  
  uf = UnionFind(len(nums))
  
  graph = defaultdict(lambda: [])
  for i, (x1, y1, z1) in enumerate(nums):
    for j, (x2, y2, z2) in enumerate(nums):
      if i >= j: continue
      dist = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
      edges.append((dist, i, j))
  
  edges.sort()
  bnd = 1000
  i = 0
  for w, a, b in edges:
    if i >= bnd: break
    i += 1
    if uf.find(a) == uf.find(b):
      continue
    graph[a].append(b)
    graph[b].append(a)
    uf.union(a, b)
  
  visited = set()
  vals = []
  for i in range(len(nums)):
    res = size(i, graph, visited)
    if res == 0: continue
    vals.append(res)
  vals.sort()
  vals.reverse()
  return vals[0] * vals[1] * vals[2]
  