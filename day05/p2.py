from typing import List

def solve(inp: List[str]):
  r = []
  for i, ln in enumerate(inp):
    if not ln: break
    a, b = ln.split("-")
    r.append((int(a), int(b)))

  coords = []
  for a, b in r:
    coords.append(a)
    coords.append(b + 1)
  coords.sort()
  
  idxs = list(enumerate(coords))
  mpTo = {a: b for b, a in idxs}
  mp = {a: b for a, b in idxs}
  
  s = set()
  
  for a, b in r:
    a = mpTo[a]
    b = mpTo[b + 1]
    for i in range(a, b):
      s.add(i)
  
  s = list(s)
  s.sort()
  
  sm = 0
  for a in s:
    sm += mp[a + 1] - mp[a]
    
  return sm
