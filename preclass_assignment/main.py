from functions import greet, goldilock, square_list, fibonacci_stop, clean_pitch

# Exercise 1
print("\n\nThe answer to exercise 1 is:")
greet("World")

# Exercise 2
print("\n\nThe answer to exercise 2 is:")

Bed1 = 130
print('If the bed is %d cm long' %Bed1)
goldilock(Bed1)

Bed2 = 140
print('If the bed is %d cm long' %Bed2)
goldilock(Bed2)

Bed3 = 151
print('If the bed is %d cm long' %Bed3)
goldilock(Bed3)

Bed4 = 150
print('If the bed is %d cm long' %Bed4)
goldilock(Bed4)

# Exercise 3
list = [1,2,3]
print("\n\nThe answer to exercise 3 is:")
print("The list is %s" %list)
print("The squared list is %s" %square_list(list))

# Exercise 4
print("\n\nThe answer to exercise 4 is:")
fib_stop = 30
results = fibonacci_stop(fib_stop)
print("The fibonacci sequence up to %d is\n %s" %(fib_stop, fibonacci_stop(fib_stop)))

# Exercise 5
x = [-1, 2, 6, 95, 55]
status = [1, 0, 0, 0, 1]
x_clean = clean_pitch(x, status)
print("\n\nThe answer to exercise 5 is:")
print("If the measured pitch is %s and the status is %s the following would be the output:" %(x, status))
print(x_clean)