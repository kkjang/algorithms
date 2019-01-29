import random
def reservoir_sample(arr, k):
  reservoir = []
  for i in range(k):
    reservoir.append(arr[i])
  for i in range(k, len(arr)):
    sample = random.randint(1, i+1)
    if sample <= k:
      reservoir[sample-1] = arr[i]
  return reservoir

test = [40, 48, 26, 44, 15, 20, 40, 33, 42, 34, 1, 14, 24, 47, 27, 38, 6, 14, 36, 13]

print(reservoir_sample(test, 5))
