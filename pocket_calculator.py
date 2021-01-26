def initialize():
    global current_value
    current_value = 0
    global i
    i = 0
    global values
    values = []

def add_to_list():
    global i
    i = i +1
    global current_value
    global values
    values.append(current_value)

def display_current_value():
    #function that prints current value
    print("Current Value:", current_value)


def add(value):
    #function that adds value to current value
    global current_value
    current_value = current_value + value
    add_to_list()

def multiply(value):
    #multiplies current value by value
    global current_value
    current_value = current_value * value
    add_to_list()

def divide(value):
    #divides current value by value
    global current_value
    current_value = current_value / value
    add_to_list()

def save():
    #saves current_value as a variable to be recalled later
    global saved_value
    saved_value = current_value

def recall():
    #recalls saved value
    global current_value
    current_value = saved_value

def undo():
    global i
    global current_value
    global values
    i = i -1
    current_value = values[i]

def get_current_value():
    return current_value



if __name__ == '__main__':
    # #problem 1
    # current_value = 0
    # print(current_value)
    #
    #
    # #problem 2 (made function display_current_value)
    # display_current_value()
    #
    #
    # #problem 3
    # add(5)
    # display_current_value()
    #
    # #problem 4
    # #creates error message because current_value is local variable and is not defined
    #
    #
    # #problem 5
    # multiply(5)
    # display_current_value()
    # divide(6)
    # display_current_value()


    #problem 6
    # save()
    # display_current_value()
    # add(5)
    # display_current_value()
    # recall()
    # display_current_value()

    #problem 7
    values = []
    current_value = 0
    values.append(current_value)
    i = 0
    add(5)
    display_current_value()
    multiply(6)
    display_current_value()
    undo()
    display_current_value()
    print(values)



