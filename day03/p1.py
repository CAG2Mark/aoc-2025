from typing import List

def solve(inp: List[str]):
  sm = 0
  for ln in inp:
    m = 0
    for i in range(len(ln)):
      for j in range(i + 1, len(ln)):
        v = int(ln[i] + ln[j])
        if v > m: m = v
    sm += m
  return sm
