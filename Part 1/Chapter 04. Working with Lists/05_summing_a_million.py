a_million_numbers = list(range(1, 1000001))

min = min(a_million_numbers)
max = max(a_million_numbers)
sum = sum(a_million_numbers)

print(f"The minimum is {min}")
print("The highest is {:,}".format(max))

print("The sum of all the numbers from {:,} and {:,} is... {:,}".
      format(min, max, sum))
