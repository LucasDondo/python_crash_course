import plotly.express as px

from die import Die

d8_1 = Die(8)
d8_2 = Die(8)

results = []

rolls = 1_000_000
for roll_num in range(rolls):
    result = d8_1.roll() + d8_2.roll()
    results.append(result)

pos_results = [value for value in range(2, d8_1.num_sides + d8_2.num_sides + 1)]
appearances = [results.count(value) for value in pos_results]

fig = px.bar(
    x=pos_results,
    y=appearances,
    labels={"x": "Result", "y": "Appearences"},
    title=f"Results of rolling two D8 dice {rolls:,} times",
)
fig.update_xaxes(dtick=1)
fig.show()
