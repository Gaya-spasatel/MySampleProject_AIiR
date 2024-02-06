import leather

def simple_chart(data, header, color, filepath):
    chart = leather.Chart(header)
    chart.add_line(data, stroke_color=color)
    chart.to_svg(filepath)

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

simple_chart(data, 'Simple pairs', '#000000', './examples/pairs.svg')