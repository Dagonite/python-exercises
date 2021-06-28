from itertools import permutations, product

from plotly import offline
from plotly.graph_objs import Bar, Layout

from die import Die

# create two D6 dice
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list
results = [die_1.roll() * die_2.roll() for _ in range(5000)]

# analyze the results
x_values = sorted(set(i * j for i, j in product(range(1, die_1.num_sides + 1), range(1, die_2.num_sides + 1))))
frequencies = [results.count(value) for value in x_values]

# visualize the results
data = [Bar(x=list(map(str, x_values)), y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title="The product of 5000 roles of two D6 dice",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot({"data": data, "layout": my_layout}, filename="d6_times_d6.html")
