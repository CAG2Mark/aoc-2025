from typing import List

def norm(a):
  return (int(0 if a[0] == 0 else a[0] / abs(a[0])), int(0 if a[1] == 0 else a[1] / abs(a[1])))

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INV = {v: k for k, v in enumerate(DIR)}

def is_exterior(a, b, c):
  xd = norm((b[0] - a[0], b[1] - a[1]))
  yd = norm((c[0] - b[0], c[1] - b[1]))
  if xd == yd: return False
  inv = (INV[xd] - 1) % 4
  if yd == DIR[inv]: return True
  assert yd == DIR[(INV[xd] + 1) % 4]
  return False

def outlines(a, b, c):
  assert a[0] == b[0] or b[0] == c[0]
  assert a[1] == b[1] or b[1] == c[1]
  excl_x = a[0] if a[0] == b[0] else b[0]
  excl_y = a[1] if a[1] == b[1] else b[1]
  min_x = min(a[0], b[0], c[0])
  min_y = min(a[1], b[1], c[1])
  max_x = max(a[0], b[0], c[0])
  max_y = max(a[1], b[1], c[1])
  if excl_x == min_x:
    x = min_x + 1
    from_x = min_x + 1
    to_x = max_x
  else:
    x = max_x - 1
    from_x = min_x
    to_x = max_x - 1
  if excl_y == min_y:
    y = min_y + 1
    from_y = min_y + 1
    to_y = max_y
  else:
    y = max_y - 1
    from_y = min_y
    to_y = max_y - 1
  return ((from_x, y), (to_x, y)), ((x, from_y), (x, to_y))

def normalize_rect(a, b):
  min_x = min(a[0], b[0])
  min_y = min(a[1], b[1])
  max_x = max(a[0], b[0])
  max_y = max(a[1], b[1])
  return ((min_x, min_y), (max_x, max_y))

def rect_intc(a, b):
  a = normalize_rect(*a)
  b = normalize_rect(*b)
  min_x = max(a[0][0], b[0][0])
  max_x = min(a[1][0], b[1][0])
  min_y = max(a[0][1], b[0][1])
  max_y = min(a[1][1], b[1][1])
  if min_x > max_x or min_y > max_y: return None
  return ((min_x, min_y), (max_x, max_y))

def solve(inp: List[str]):
  vals = [tuple(int(a) for a in x.split(",")) for x in inp]
  L = len(vals)

  exts = set()
  bads = set()
  for i in range(L):
    a, b, c = vals[i % L], vals[(i + 1) % L], vals[(i + 2) % L]
    if is_exterior(a, b, c):
      for x in outlines(a, b, c): exts.add(x)
  for i in range(L - 1):
    a, b = vals[i % L], vals[(i + 1) % L]
    min_x = max(a[0], b[0])
    max_x = min(a[0], b[0])
    min_y = max(a[1], b[1])
    max_y = min(a[1], b[1])
    for e in exts:
      res = rect_intc(((min_x, min_y), (max_x, max_y)), e)
      if res is None: continue
      assert(res[0] == res[1])
      bads.add(res[0])
  
  def check_rect(rect):
    rect = normalize_rect(*rect)
    for e in exts:
      intc = rect_intc(rect, e)
      if intc is None: continue
      if intc[0] == intc[1]:
        if intc[0] in bads: continue
      return True
    return False
  
  m = 0
  for i in range(L):
    for j in range(i + 1, L):
      if check_rect((vals[i], vals[j])): continue
      x1, y1 = vals[i]
      x2, y2 = vals[j]
      area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
      if area > m: m = area
  return m
