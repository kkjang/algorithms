#Given a set of Lego bricks of height 1, 2, 3, and 4, each colored differently, write a program to compute the number of ways of constructing a tower of height n≥1.

def lego(bricks, n):
  dp = [0] * (n+1)
  dp[0] = 1

  for i in range(1, n+1):
    for brick in bricks:
      if brick <= i:
        dp[i] += dp[i-brick]
  return dp[n]


def lego_2(n, cache={}):
  if n in cache:
    return cache[n]
  if n < 0:
    rv = 0
  elif n == 0:
    rv = 1
  else:
    rv = lego_2(n-1) + lego_2(n-2) + lego_2(n-3) + lego_2(n-4)
  cache[n] = rv
  return rv
  
