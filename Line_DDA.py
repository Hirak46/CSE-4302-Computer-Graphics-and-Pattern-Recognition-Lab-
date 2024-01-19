import matplotlib.pyplot as plt

def draw_line_DDA(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x, y = x1, y1

    for _ in range(steps):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points

def plot_line(points, title):
    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

# Example usage:
x1, y1 = 2, 3
x2, y2 = 9, 8

# DDA algorithm
dda_points = draw_line_DDA(x1, y1, x2, y2)
plot_line(dda_points, 'DDA Line Drawing')
