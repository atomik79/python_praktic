from math import inf

def divide(first, sekond):
    if sekond == 0:
        return inf
    else:
        return first / sekond

dev = divide(20, 0)
print(dev)
