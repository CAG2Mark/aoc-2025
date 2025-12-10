from typing import List
import z3

def count(jolts: list[int], buts, upper):
  bvars = [z3.Int("b" + str(i)) for i, b in enumerate(buts)]
  xvars = []
  for i in range(len(jolts)):
    cur = []
    for j, b in enumerate(buts):
      if i in b: cur.append(bvars[j])
    cur.append(jolts[i])
    xvars.append(cur)
  eqns = []
  
  s = z3.Solver()
  
  for ln in xvars:
    lhs = ln[:-1]
    rhs = ln[-1]
    eqns.append(sum(lhs) == rhs)
  
  for b in bvars:
    s.add(b >= 0)
  
  if upper != -1:
    s.add(sum(bvars) <= upper)
  
  try:
    s.add(*eqns)
    s.check()
    sm = 0
    for b in bvars:
      sm += s.model()[b].as_long()
    return (sm, True)
  except:
    return (0, False)

def count_search(jolts: list[int], buts):
  initial, good = count(jolts, buts, -1)
  if not good: return 0
  low = 0
  upper = initial
  while low != upper:
    mid = (low + upper) // 2
    res, good = count(jolts, buts, mid)
    if good: upper = min(mid, res)
    else: low = mid + 1
  return upper
  
def solve(inp: List[str]):
  tot = 0
  for i, ln in enumerate(inp):
    ln = ln.split(" ")
    cur = ln[0][1:-1]
    cur = [x == '#' for x in cur]
    buts = ln[1:-1]
    jolts = ln[-1][1:-1]
    jolts = [int(x) for x in jolts.split(",")]
    buts = [x[1:-1] for x in buts]
    buts = [tuple(int(x) for x in y.split(",")) for y in buts]
    print(len(jolts) - len(buts))
    tot += count_search(jolts, buts)
  return tot
