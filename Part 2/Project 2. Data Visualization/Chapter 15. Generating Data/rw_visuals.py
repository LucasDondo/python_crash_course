import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points),
               cmap=plt.cm.Greys, edgecolors='none', s=1)
    ax.scatter(0, 0, c='black', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='white', edgecolors='none',
               s=50)
    ax.set_aspect('equal')

    ax.set_axis_off()

    plt.show()

    keep_running = input('Make another walk? (Y/N): ')
    if keep_running.lower() == 'n':
        break