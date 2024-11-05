from logging import exception

"""
Calculates the ele_current, power and resistance
no below zero numbers
"""
def ele_currnet(U, R):

   if(R > 0) and (U > 0):
       return U / R
   else: raise Exception("Sorry, no numbers below zero")

"""
calculates the power, resistance and ele_current
no below zero numbers
"""
def power(I, R):
    if (R > 0) and (I > 0):
        return I * R
    else:
        raise Exception("Sorry, no numbers below zero")

"""
calculates the resistance, ele_current and power
no below zero numbers
"""
def resistance(U, I):
    if (I > 0) and (U > 0):
        return U / I
    else:
        raise Exception("Sorry, no numbers below zero")




