# Exercise 1
def greet(name):
    return print("Hello, " + name + "!")

# Exercise 2
def goldilock(x):
    if x < 140:
        return print("Too small!")
    elif x > 150:
        return print("Too large!")
    else:
        return print("Just right. :)")
    
# Exercise 3
def square_list(list):
    for i in range(len(list)):
        list[i] = list[i] ** 2
    return list

# Exercise 4
def fibonacci_stop(stop):
    fib = [0,1]
    fib_new = 0
    while fib_new < stop:
        fib_new = fib[-1] + fib[-2]
        fib.extend([fib_new])
    return fib[:-1]

# Exercise 5
def clean_pitch(x, status):
    x_clean = [None] * len(x)
    for i in range(len(x)):
        if (x[i] < 0) and status[i] == 1:
            x_clean[i] = -999
        elif (x[i] < 0) and status[i] == 0:
            x_clean[i] = x[i]
        elif (x[i] > 90) and status[i] == 1:
            x_clean[i] = -999
        elif (x[i] > 90) and status[i] == 0:
            x_clean[i] = x[i]
        else:
            x_clean[i] = x[i]
    return x_clean
