import plotly.express as px

from die import Die

# Create dies.
dies = [Die(), Die(), Die()]

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

# Create figure.
fig = px.bar(x      = pos_results,
             y      = appearances,
             labels = {'x': 'Result', 'y': 'Appearences'},
             title  = f'Results of rolling three D6 dies {rolls:,} times')
fig.update_xaxes(dtick = 1)

# Show figure.
fig.show()