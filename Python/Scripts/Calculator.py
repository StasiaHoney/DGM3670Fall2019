#######################################
def Add(values):
    '''
    Adds two numbers together and returns result
    input: list of float/int values
    return: float/int
    '''
    sum = float(values[0])
    for val in values[1:]:
        sum += float(val)

    return sum


Add([1, 2, 3, 4, 5.6, 7, 8, 10])


######################################
def Subtract(values):
    '''
    Takes a list of values, subtracts them and returns the result
    input: a list of float/int values
    return: float/int
    '''
    sub = float(values[0])

    for val in (range(len(values))):
        sub -= float(values[val])

    return sub


Subtract([1, 2, 3, 4, 5, 6])


########################################
def Multiplication(values):
    '''
    Takes a list of values, multiplies them and returns the result
    input: a list of float/int values
    return: float/int
    '''
    multi = float(values[0])
    for val in values[1:]:
        multi = float(multi * val)
    return multi


Multiplication([2.9, 3, 4, 5, 6.6])


########################################
def Division(values):
    '''
    Takes a list of values, divides them and returns the result
    input: a list of float/int values
    return: float/int
    '''
    div = values[0]
    for val in values[1:]:
        div = float(div / val)
    return div


Division([2, 3])


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


#########################################
def Median(values):
    '''
    Takes a list of values and finds the median
    input: float/int value, float/int power
    return: float/int
    '''
    import math
    for val in values:
        float(val)
    values.sort()
    size = len(values)
    median = 0.0
    if (size % 2 != 0):
        temp = size / 2
        median = float(values[temp])
    if (size % 2 == 0):
        temp = size / 2
        medainAlt = (temp - 1)
        median = float(values[temp] + values[medainAlt])
        median = float(median / 2)
    return median


Median([1, 2, 3, 4, 5, 6])


##########################################
def Mean(values):
    '''
    Takes a list of values and finds the mean
    input: float/int value, float/int power
    return: float/int
    '''

    sum = Add(values)
    float(sum)
    mean = float(sum / (len(values)))
    return mean


Mean([1, 2, 3, 4, 5, 6])


###########################################
def Mode(values):
    '''
    Takes a list of values and finds the mean
    input: float/int value, float/int power
    return: float/int
    '''
    import statistics
    return statistics.mode(values)


Mode([1, 2, 3, 4, 4, 5, 6])
