'''
#1. hello
def hello(x):
    print("Hello " + x)

hello('Igor')

#2. y = x + 1
import matplotlib.pyplot as plotlibrary

def f(x):
    return x + 1

xs = list(range(-3 ,3))
ys = []
for x in xs:
    ys.append(f(x))

plotlibrary.plot(xs, ys)
plotlibrary.show()


# 3. Square of x
import matplotlib.pyplot as plotlibrary

def f(x):
    return x**2

xs = list(range(-100, 100))
ys = []
for x in xs:
    ys.append(f(x))

plotlibrary.plot(xs,ys)
plotlibrary.show()

'''
# 4. odd or even
import matplotlib.pyplot as plotlibrary

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

xs = list(range(-5, 5))
ys = []

for x in xs:
    ys.append(f(x))

plotlibrary.bar(xs, ys)
plotlibrary.show()
