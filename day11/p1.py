from typing import List
from collections import defaultdict
from functools import cache

def solve(inp: List[str]):
  edges = {}
  for ln in inp:
    src, tos = ln.split(": ")
    tos = tos.split()
    edges[src] = tos
  
  @cache
  def dp(cur, target):
    if cur == target: return 1
    sm = 0
    for n in edges[cur]:
      sm += dp(n, target)
    return sm
  
  return dp("you", "out")
