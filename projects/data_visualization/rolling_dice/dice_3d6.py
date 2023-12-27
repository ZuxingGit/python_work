import plotly.express as px

from die import Die

# create a D6 and a D10
die_1 = Die()
die_2 = Die()
die_3 = Die()

# make some rolls and store results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
title = "Results of Rolling three D6 dice 50000 times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# further customize chart
fig.update_layout(xaxis_dtick=1)
fig.show()
