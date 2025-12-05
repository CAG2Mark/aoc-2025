from typing import List

def solve(inp: List[str]):
  r = inp[0].split(",")
  rs = [a.split("-") for a in r]
  rs = [(int(a), int(b)) for a, b in rs]
  sm = 0
  for a, b in rs:
    for i in range(a, b + 1):
      s = str(i)
      l = len(s)
      if s[:l//2] == s[l // 2:]: sm += i
  return sm
