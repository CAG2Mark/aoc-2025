from typing import List

def solve(inp: List[str]):
  v = [x.split() for x in inp]
  for i in range(len(v) - 1):
    v[i] = [int(x) for x in v[i]]
  
  cols = len(v[0])
  sm = 0
  
  for c in range(cols):
    def f(a, b):
      if v[-1][c] == '+': return a + b
      return a * b
    cur = 0 if v[-1][c] == '+' else 1
    for i in range(len(v) - 1):
      cur = f(cur, v[i][c])
    sm += cur
  return sm
