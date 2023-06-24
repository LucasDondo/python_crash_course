import matplotlib.pyplot as plt

from die import Die

# Create dies.
dies = [Die(), Die()]

# Roll them.
results = []
rolls   = 1_000_000
for roll_num in range(rolls):
    result = 0
    for die in dies:
        result += die.roll()
    results.append(result)

# Minimum and maximum possible results.
min_result = len(dies)
max_result = 0
for die in dies:
    max_result += die.num_sides
# Analyze results.
pos_results = [value for value in range(min_result, max_result + 1)]
appearances = [results.count(value) for value in pos_results]
for i in range(len(appearances)):
    appearances[i] += 10_000 - appearances[i] % 10_000

# Create figure.
fig, ax = plt.subplots()
ax.stem(pos_results, appearances)
#
ax.set_title(f"Rolling two D6 {rolls:,} times", fontsize=20, pad=20)
ax.set_xticks(pos_results)
ax.set_xlabel("Results", fontsize=14)
ax.set_yticks(appearances)
ax.set_ylabel("Appearances", fontsize=14)
fig.set_size_inches(11, 6)

# Show figure.
plt.show()