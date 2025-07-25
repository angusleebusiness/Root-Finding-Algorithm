

import math # necessary if the user inputs a function like cos(x)
from sympy import symbols, diff, sympify # run pip install sympy in your vm import necessary functions

# provide user with input format
print("please write in the following format")
print("u**2 for u^2")
print("exp(u) for e^u")
print("a * x, where a is a constant, for ax")

# query user for input
f = sympify(input("Enter f(x) = ")) # might later implement replacement of ^2 to **2 and e^ to exp()
init_guess = float(input("Enter initial guess(may affect final answer if multiple roots exist): "))
precision = int(input("Enter desired level of precision in decimal places(may impact solver speed):"))
max_iterations = int(input("Enter desired max iterations: "))
x = symbols('x') # initialize x as a symbolic variable
f_prime = diff(f,x) # take derivative of f(x)
current_iteration = 0 # allows capping of iterations

# create recursive function for newton's method
def newtons_method(f, f_prime, test_value, precision, max_iterations): 
    global current_iteration # ensures current_iteration can be modified by the function
    
    # check if max iterations has been reached: terminates if yes
    if current_iteration == max_iterations:
        print(f"max iterations reached; current best guess: x = {test_value}")
        return
    
    # check if the derivative = 0; in which case, x_1 would be undefined and newton's method would fail    
    if f_prime.subs(x, test_value) == 0:
        print(f"Derivative is zero at x = {test_value}. Newton's method cannot proceed.")
        return
    
    # approximates the root using newton's method and the current guess: then prints to log progress
    x_1 = test_value - (f.subs(x,test_value) / f_prime.subs(x,test_value))
    print(f"current guess: x = {x_1}")
    
    # checks if the absolute difference between x_1 and test_value is less than the desired precision: terminates and gives final answer if yes
    if abs(test_value - x_1) < 10**(-precision):
        print(f"the final guess with {precision} decimal places of precision is: x = {x_1}")
        return

    else:
        
        test_value = x_1
        current_iteration = current_iteration + 1
        newtons_method(f, f_prime, test_value, precision, max_iterations)
        
newtons_method(f, f_prime, init_guess, precision, max_iterations)
