from typing import List

def check_spls(s: str):
  for i in range(1, len(s)):
    if len(s) % i: continue
    cnt = len(s) // i
    spls = [s[j * i : (j + 1) * i] for j in range(cnt)]
    bad = False
    for j in range(len(spls) - 1):
      if spls[j] != spls[j + 1]:
        bad = True
        break
    if bad: continue
    return True
  return False

def solve(inp: List[str]):
  r = inp[0].split(",")
  rs = [a.split("-") for a in r]
  rs = [(int(a), int(b)) for a, b in rs]
  sm = 0
  for a, b in rs:
    for i in range(a, b + 1):
      s = str(i)
      if check_spls(s):
        sm += i
  return sm
