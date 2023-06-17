import plotly.express as px

from random_walk import RandomWalk

rw = RandomWalk()
rw.walk()

fig = px.scatter(x=rw.x_values, y=rw.y_values)
fig.update_layout(xaxis_visible=False, yaxis_visible=False)

fig.show()