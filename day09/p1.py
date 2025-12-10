from typing import List

def solve(inp: List[str]):
  vals = [list(int(x) for x in a.split(",")) for a in inp]
  L = len(vals)
  m = 0
  for i in range(L):
    
    for j in range(i + 1, L):
      x1, y1 = vals[i]
      x2, y2 = vals[j]
      area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
      if area > m: m = area
  return m
