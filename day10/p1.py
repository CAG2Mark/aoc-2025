from typing import List

def count(cur: list[bool], idx: int, buts) -> tuple[int, bool]:
  if idx == len(buts):
    return (0,all(not x for x in cur))
  ans = []
  a, good = count(cur, idx + 1, buts)
  if good: ans.append(a)
  s = cur.copy()
  for i in buts[idx]:
    s[i] = not s[i]
  b, good = count(s, idx + 1, buts)
  if good: ans.append(b + 1)
  if not ans: return (0, False)
  return (min(ans), True)
  
def solve(inp: List[str]):
  tot = 0
  for i, ln in enumerate(inp):
    ln = ln.split(" ")
    cur = ln[0][1:-1]
    cur = [x == '#' for x in cur]
    buts = ln[1:-1]
    jolts = ln[-1]
    buts = [x[1:-1] for x in buts]
    buts = [tuple(int(x) for x in y.split(",")) for y in buts]
    res, good = count(cur, 0, buts)
    if good: tot += res
  return tot
