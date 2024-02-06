import leather

def simple_chart(data, filepath):
    chart = leather.Chart('Simple pairs')
    chart.add_dots(data)
    chart.to_svg(filepath)

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

simple_chart(data, './examples/pairs.svg')