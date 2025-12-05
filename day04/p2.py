from typing import List


def solve(inp_s: List[str]):
  inp = [[x for x in s] for s in inp_s]
  
  r = len(inp)
  c = len(inp[0])
  
  def cnt(i: int, j: int):
    tot = 0
    for y in range(max(0, i - 1), min(r, i + 2)):
      for x in range(max(0, j - 1), min(c, j + 2)):
        tot += inp[y][x] == '@'
    return tot
  
  def find_all():
    for i in range(r):
      for j in range(c):
        if inp[i][j] == '@' and cnt(i, j) < 5: yield (i, j)
  
  ans = 0
  while True:
    removed = 0
    for i, j in find_all():
      inp[i][j] = '.'
      removed += 1
      ans += 1
    if removed == 0: break
  
  return ans

