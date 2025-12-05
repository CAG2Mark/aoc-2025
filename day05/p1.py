from typing import List

def solve(inp: List[str]):
  r = []
  for i, ln in enumerate(inp):
    if not ln: break
    a, b = ln.split("-")
    r.append((int(a), int(b)))
  
  sm = 0
  for j in range(i + 1, len(inp)):
    ln = inp[j]
    for a, b in r:
      if a <= int(ln) <= b:
        sm += 1
        break
  return sm
