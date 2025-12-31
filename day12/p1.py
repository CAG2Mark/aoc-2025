from typing import List

def solve(inp: List[str]):
  cnts = [7, 7, 6, 5, 7, 7]
  ret = 0
  for ln in inp:
    size, objs = ln.split(": ")
    objs = objs.split()
    r, c = size.split("x")
    size = int(r) * int(c)
    tot1 = 0
    tot2 = 0
    for i, o in enumerate(objs):
      tot1 += int(o) * cnts[i]
      tot1 += int(o) * 9 
    if size - tot1 < 0: continue
    if size - tot2 >= 0: ret += 1
    else: print("bad")
  return ret
