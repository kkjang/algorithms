def justify(words, K):
  begin = 0
  res = ""
  while begin < len(words):
    end = begin + 1
    count = len(words[begin])
    while end < len(words):
      if count + len(words[end]) + 1 > K:
        break
      count += len(words[end]) + 1
      end += 1
    if end == len(words):
      res += words[begin]
      for index in range(begin+1, end):
        res += f" {words[index]}"
      for space in range(K-count):
        res += " "
    else:
      spaces_to_add = K - count
      num_between = end - begin - 1 
      spaces_between = (spaces_to_add // num_between) if num_between > 0 else 0
      extra = spaces_to_add - (num_between * spaces_between)
      res += words[begin]
      for index in range(begin+1, end):
        res += " " * (spaces_between + (1 if extra > 0 else 0))
        extra -= 1
        res += f" {words[index]}"
      res += "\n"
    begin = end
  return res
      

print(justify(["a", "large", "fat", "stupid", "dog", "accidentally", "tripped", "over", "the", "skinny", "cat"], 20))
