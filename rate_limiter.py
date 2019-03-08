import time

class RateLimiter:
  def __init__(self, rate, per):
    self.map = dict()
    self.rate = rate
    self.per = per

  def isAllow(self, clientID):
    limiter = self.map.setdefault(clientID, Limiter(self.rate, self.per))
    return limiter.is_allow()

class Limiter:
  def __init__(self, rate, per):
    self.rate = rate
    self.per = per
    self.allowance = rate
    self.last_time = time.time()

  def is_allow(self):
    cur_time = time.time()
    elapsed = cur_time - self.last_time
    self.last_time = cur_time
    self.allowance += elapsed * (self.rate / self.per)

    if self.allowance > self.rate:
      self.allowance = self.rate
    
    if self.allowance >= 1:
      self.allowance -= 1
      return True
    else:
      return False


foo = RateLimiter(2, 2)

print(foo.isAllow(1))
print(foo.isAllow(2))
print(foo.isAllow(1))
time.sleep(2)
print(foo.isAllow(1))
print(foo.isAllow(2))
print(foo.isAllow(2))
print(foo.isAllow(2))
