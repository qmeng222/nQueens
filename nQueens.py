def nQueens(n):
  # init sets:
  col = set()
  posDiag = set()
  negDiag = set()

  # init board:
  res = []
  board = [["0"] * n for i in range(n)]

  def backTrack(r):
    if r == n:
      copy = ["".join(row) for row in board]
      res.append(copy)

    for c in range(n):
      if c in col or (r+c) in posDiag or (r-c) in negDiag:
        continue

      # update sets & board:
      col.add(c)
      posDiag.add(r+c)
      negDiag.add(r-c)
      board[r][c] = "1"

      backTrack(r+1)

      # reset sets & board:
      col.remove(c)
      posDiag.remove(r+c)
      negDiag.remove(r-c)
      board[r][c] = "0"

  backTrack(0)
  return res

# test case:
print(nQueens(4))