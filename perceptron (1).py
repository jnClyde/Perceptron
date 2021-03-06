import numpy as np

def h(x, w, b):
    q = np.dot(x.T, w) + b
    if (q < 0):
        return 0
    return 1

##5 - без потери одной "1"
xt = [[1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1]]
xt.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
##5 - без одной "1"
xt.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1])
xt.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1])
xt.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0])
xt.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1])
xt.append([1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1])
xt.append([1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1])
xt.append([1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1])
xt.append([1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
xt.append([1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
xt.append([1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
xt.append([0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])


xt.append([0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
xt.append([1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1])
xt.append([1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1])
xt.append([1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1])
xt.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1])
xt.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1])
xt.append([1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1])
xt.append([1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1])
xt.append([1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1])


mt = len(xt)
xt = np.array(xt)


##1-9,0
x = [[0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]]
x.append([1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1])
x.append([1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1])
x.append([1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1])
x.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
x.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1])
x.append([1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1])
x.append([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1])
x.append([1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1])
x.append([1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1])

m = len(x)
x = np.array(x)
y =np.array( [0, 0, 0, 0, 1, 0, 0, 0, 0, 0])

w = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
b = 5

for i in range(0, 1000):
    for j in range(0, m):
        newY = h(x[j], w, b)
        if (y[j] < newY):
            w = w - x[j]
            b -=1
        if (y[j] > newY):
            w = w + x[j]
            b +=1
print("Test")
for i in range(0, mt):
    print(h(xt[i], w, b), " ", xt[i])
print("Result")


print("0-9")
for i in range(0, m):
    print(h(x[i], w, b), " ", x[i])
print("Result")
print(y)


          
