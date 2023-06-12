import matplotlib.pyplot as plt

nums  = range(1, 5001)
cubes = [x**3 for x in nums]

fig, ax = plt.subplots()
ax.scatter(nums, cubes, c=cubes, cmap=plt.cm.Greys, s=10)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()