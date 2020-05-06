def comb(data, r, start, progress):
  if r == 0:
    yield progress
    return

  for i in range(start, len(data)):
    yield from comb(data, r - 1, i + 1, progress + [data[i]])
    
for e in comb("ABCD", 3, 0, []):
    print(e)