import matplotlib.pyplot as plot

x = [1, 2, 3,9]
y = [4, 5, 6,7]
plot.plot(x, y, marker='o')
plot.plot(y, x, marker='x')
plot.show()
