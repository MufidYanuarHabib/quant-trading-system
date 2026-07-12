import math
from collections import Counter

print("====== MATH HELPER ======")
print("Example")
print("input: 100 101 102 103 104")
print()

data = list(map(float, input("Input all the data (seperated with space): ").split()))
print(data)
print()

def mean(data):
  mean_data = sum(data) / len(data)
  return mean_data

def median(data):
  data = sorted(data)
  n = len(data)

  if n % 2 == 1:
    return data[n // 2]
  else:
    mid1 = data[n // 2 - 1]
    mid2 = data[n // 2]
    return (mid1 + mid2) / 2

def mode(data):
  count = Counter(data)
  return count.most_common(1)[0][0]

def variance(data):
  n = len(data)
  avg = mean(data)
  total = 0

  for x in data:
    total += (x - avg) ** 2
  return total / n

def std(data):
  var = variance(data)
  return var ** 0.5

def log_return(data):
  p_t = data[-1]
  p_t_1 = data[-2]

  return math.log(p_t / p_t_1)

def z_score(data):
  x = data[-1]
  avg = mean(data)
  std_deviation = std(data)

  return (x - avg) / std_deviation

def data_range(data):
  range_data = max(data) - min(data)
  return range_data

def min_max(data):
  minimum = min(data)
  maximum = max(data)
  return minimum, maximum

minimum, maximum = min_max(data)

print("=" * 30)
print("===== RESULTS =====")
print("=" * 30)
print(f"{'Mean':<18}: {mean(data):.2f}")
print(f"{'Median':<18}:  {median(data):.2f}")
print(f"{'Mode':<18}: {mode(data):.2f}")
print(f"{'Variance':<18}: {variance(data):.2f}")
print(f"{'Standar Deviation':<18}: {std(data):.2f}")
print(f"{'Log Return':<18}: {log_return(data):.2f}")
print(f"{'Z-Score':<18}: {z_score(data):.2f}")
print(f"{'Range':<18}: {data_range(data):.2f}")
print(f"{'Mininum':<18}: {minimum}")
print(f"{'Maximum':<18}: {maximum}")
print("=" * 30)
