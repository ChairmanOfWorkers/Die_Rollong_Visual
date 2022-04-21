import pygal

def create_hist(die, sides_num, roll_count, diagram_name):
	die.num_sides = int(sides_num)

	results = []
	for i in range(int(roll_count)):
		result = die.roll()
		results.append(result)

	frequences = []
	for value in range(1, die.num_sides+1):
		frequency = results.count(value)
		frequences.append(frequency)

	hist = pygal.Bar()
	x_label_count = []
	for i in range(1, die.num_sides+1):
		x_label_count.append(i)

	hist.title = f'Results for Die rolling for {roll_count} times'
	hist.x_labels = x_label_count
	hist.x_title = "Results"
	hist.y_title = "Frequency of results"

	hist.add('Die', frequences)
	hist.render_to_file(f'{diagram_name}.svg')