def Add(values):
    '''
    Adds two numbers together and returns result
    input: list of float/int values
    return: float/int
    '''

    sum = 0

    for val in values:
        sum += val

    return sum


Add([1, 2, 3, 4, 5.6, 7, 8, 10])


########################################
def Power(value, power):
    import math
    '''
    Takes a float/int value and raises to the power value and returns result
    input: float/int value, float/int power
    return: float/int
    '''
    return math.pow(value, power)
Power(3, 2)

######################################
def Subtract(values):
    '''
    Takes a list of values, subtracts them and returns the result
    input: a list of float/int values
    return: float/int
    '''

    sub=values[0]

    for val in (range(len(values)) - 1):
        sub-=values[val]

    return sub

Subtract(1, 2, 3, 4 , 5, 6)