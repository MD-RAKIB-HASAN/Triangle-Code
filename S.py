class NegativeError(Exception):
    pass

def triangular(x, y, z):
    if x <= 0 or y <= 0 or z <= 0 :
        raise NegativeError
    
    # To Check smaller sides is greater than the largest side
    s = sorted([x, y, z])
    if s[0] + s[1] > s[2] and s[0] + s[2] > s[1] and s[1] + s[2] > s[0]:
        return True
    else:
        return False

def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value <= 0:
                raise NegativeError("Must be positive.")
            
            if value != float(user_input):
                raise ValueError("Must positive.")
           
            return value
        except ValueError:
            print("Invalid input....")
            

try:
    x = get_positive_integer("'x': ")
    y = get_positive_integer("'y': ")
    z = get_positive_integer("'z': ")

    if triangular(x, y, z):
        print("It's Triangle.")
    else:
        print("Not Triangle.")
except NegativeError as e:
    print(e)
except ValueError as e:
    print(e)
