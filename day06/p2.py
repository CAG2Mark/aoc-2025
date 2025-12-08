from typing import List

def solve(inp: List[str]):
  t = list(zip(*inp))
  ps = []
  cur = []
  curop = ""
  for ln in t:
    ln = ''.join(ln)
    if not ln.strip():
      ps.append((cur, curop))
      cur = []
      continue
    op = ln[-1]
    if op == "*" or op == "+":
      ln = ln[:-1]
      curop = op
    cur.append(int(ln.strip()))
  if cur:
    ps.append((cur, curop))
  sm = 0
  for items, op in ps:
    def f(a, b):
      if op == '+': return a + b
      return a * b
    cur = 0 if op == '+' else 1
    for i in items:
      cur = f(cur, i)
    sm += cur
  return sm
