print("Inside myMath.py")

def my_add(x,y):
    return x+y

def my_divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
