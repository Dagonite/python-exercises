from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create a D6
die = Die()

# make some rolls, and store results in a list
results = [die.roll() for _ in range(1000)]

# analyze the results
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# visualize the results
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Results of rolling one D6 1000 times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="E01_d6.html")
