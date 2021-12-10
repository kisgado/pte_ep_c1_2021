from matplotlib.pyplot import *

n_points = 100
x, y, y2, y3 = [], [], [], []
for i in range(n_points):
    x.append(i)
    y.append(i)
    y2.append(i ** 2)
    y3.append(i ** 3)
plot(x, y, "ro", label="y = x")
plot(x, y2, "gs", label="y = x^2")
plot(x, y3, "bp", label="y = x^3")
axis([0, 20, 0, 90])
grid(True)
title("Cím")
xlabel("x tengely")
ylabel("y tengely")
legend()
show()
