
# 1. Define a simple function

def greet(name):

    print(f"Hello {name}!")

    return

name = "Javier"

greet("Javier")

# 2. If/else statements

def goldilocks(length):

    if length > 150:

        print("Too large!")

    if length < 140: 
        
        print("Too small!")

    else:

        print("Just right!")

    return

goldilocks(145)


# 3. For loops

def square_list(list):

    list_squared = []  

    for i in list:

        list_squared.append(i**2)

    print(list_squared)

    return

list_squared = [1, 2, 3, 4, 5]

square_list(list_squared)

# 4. While loops

def fibonacci_stop(stop):

    a, b = 0, 1

    printer = []

    while a < stop:

        a, b = b, a+b

        printer.append(a)

    print(printer)

    return

fibonacci_stop(10)

# 5. Logical operators

def clean_pitch(pitch, status):

    new_pitch = []

    for i, val in enumerate(pitch):

        if status[i] == 1:

            new_pitch.append(-999)

        else:
            
            new_pitch.append(val)

    print("Pitch: ", pitch)
    print("Status: ", status)
    print("New pitch: ", new_pitch)

    return

pitch = [1, 92, 45, -8, 60]
status = [0, 1, 0, 0, 0]

clean_pitch(pitch, status)