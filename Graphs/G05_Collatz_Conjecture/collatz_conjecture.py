import matplotlib.pyplot as plt


def collatz_conjecture(x):
    """
    Return a list of values that make up a single Collatz conjecture sequence,
    with 'x' being the start value.
    """
    values = []

    def calc(x):
        values.append(int(x))
        if x == 1:
            return values

        if x % 2:
            return calc(3 * x + 1)

        return calc(x / 2)

    return calc(x)


# setup the graph
plt.style.use("seaborn")
fig, ax = plt.subplots()

# plot the lines
for x in range(1, 1001):
    y = collatz_conjecture(x)
    ax.plot(range(1, len(y) + 1), y, linewidth=2)

# set chart title and label axes
ax.set_title("Collatz Conjecture", fontsize=20)
ax.set_xlabel("Iterations", fontsize=14)
ax.set_ylabel("Values", fontsize=14)

# set size of tick labels
ax.tick_params(axis="both", labelsize=12)

plt.savefig("collatz.png", bbox_inches="tight")
