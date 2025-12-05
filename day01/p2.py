from typing import List

def solve(inp: List[str]):
    tot = 0
    cur = 50
    for ln in inp:
        lr = -1 if ln[0] == "L" else 1
        cnt = int(ln[1:])
        for c in range(cnt):
            cur += lr
            cur %= 100
            if cur == 0: tot += 1
    return tot
