import matplotlib.pyplot as plt

plt.rcParams['figure.max_open_warning'] = len(plt.style.available)

input_values = range(1, 11)
squares      = [x**2 for x in input_values]

for style in plt.style.available:
    plt.style.use(style)

    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)
    ax.scatter(input_values, squares, c=squares, cmap=plt.cm.YlOrBr, s=200)
    fig.canvas.manager.set_window_title(f'Styled with {style}')

    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    ax.tick_params(labelsize=14)

plt.show()