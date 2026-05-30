def make_multiplier(num):

    def multiply(x):
        return x * num
    return multiply

# Closure Practice

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5)) 
print(triple(5))