power = 1
sum = 0

for i in range(1001):
  sum += i**power
  power += 1

result = str(sum)
print(result[len(result)-10:len(result)])