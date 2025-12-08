from typing import List

def solve(inp: List[str]):
  hgt = len(inp)
  arr = [[x for x in ln] for ln in inp]
  cnt = 0
  for i in range(len(inp[0])):
    if arr[0][i] != 'S': continue
    arr[1][i] = '|'
    break
  for i in range(1, hgt - 1):
    row = arr[i]
    for j in range(len(row)):
      if row[j] != '|': continue
      if arr[i + 1][j] != '^': arr[i + 1][j] = '|'
      else:
        arr[i + 1][j - 1] = '|'
        arr[i + 1][j + 1] = '|'
        cnt += 1
  return cnt
