epsilon_0 = 0.00000000000885  #permitivitata vakua

def epsilon(epsilon_0, epsilon_r):
    if (epsilon_r > 0):
        return epsilon_0 * epsilon_r
    else:
        raise Exception("Sorry, no numbers below zero")


def force(q1, q2, r):
    if (q1 > 0) and (q2 > 0) and (r > 0):
        return (q1 * q2) / (4 * 3.14 * epsilon_0 * r ** 2)
    else:
        raise Exception("Sorry, no numbers below zero")