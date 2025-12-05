from typing import List
from functools import cache

@cache
def dp(ln: str, idx: int, cur_len: int) -> int:
  if idx >= len(ln):
    if cur_len != 0: return -1
    return 0
  if cur_len == 0: return 0
  v1 = dp(ln, idx + 1, cur_len - 1)
  v2 = dp(ln, idx + 1, cur_len)
  if v1 == -1: return v2
  return max(int(ln[idx] + str(v1)), v2)

def solve(inp: List[str]):
  sm = 0
  for ln in inp:
    sm += dp(ln, 0, 12) / 10
  return sm
