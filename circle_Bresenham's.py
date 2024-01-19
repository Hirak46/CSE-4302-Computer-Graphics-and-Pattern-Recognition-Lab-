import matplotlib.pyplot as plt

def draw_circle_bresenham(radius, xc, yc):
    points = []
    x = 0
    y = radius
    d = 3 - 2 * radius  # Initial decision parameter

    while x <= y:
        points.append((x + xc, y + yc))
        points.append((-x + xc, y + yc))
        points.append((x + xc, -y + yc))
        points.append((-x + xc, -y + yc))
        points.append((y + xc, x + yc))
        points.append((-y + xc, x + yc))
        points.append((y + xc, -x + yc))
        points.append((-y + xc, -x + yc))

        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

    return points

def plot_circle(points, title):
    x_values, y_values = zip(*points)
    plt.scatter(x_values, y_values)
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

# Example usage:
radius = 5
xc, yc = 0, 0

# Bresenham's Circle algorithm
bresenham_circle_points = draw_circle_bresenham(radius, xc, yc)
plot_circle(bresenham_circle_points, 'Bresenham\'s Circle Drawing')
