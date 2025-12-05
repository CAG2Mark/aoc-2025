from typing import List


def solve(inp: List[str]):
  r = len(inp)
  c = len(inp[0])
  
  def cnt(i: int, j: int):
    tot = 0
    for y in range(max(0, i - 1), min(r, i + 2)):
      for x in range(max(0, j - 1), min(c, j + 2)):
        tot += inp[y][x] == '@'
    return tot
  
  ans = 0
  for i in range(r):
    for j in range(c):
      if inp[i][j] == '@' and cnt(i, j) < 5: ans += 1
  return ans

