import time 
from sympy import symbols, diff, sympify, factorial, expand 
import matplotlib.pyplot as plt

def run_taylor_approximator():
    """
    This function prompts the user for a function, degree, and center point,
    then calculates and displays the Taylor polynomial approximation.
    """
    # provide user with input format
    print("Please write your function in the following format:")
    print("u**2 for u^2")
    print("exp(u) for e^u")
    print("a * x, where a is a constant, for ax")

    try:
        # query user for input
        f_str = input("Enter f(x) = ")
        f = sympify(f_str)

        degree = int(input("Enter degree of taylor polynomial(will affect accuracy): "))
        centering = float(input("Enter where to center your taylor polynomial: "))
        
        x = symbols('x') # initialize x as a symbolic variable
        
        # We will build the Taylor polynomial term by term using a for loop.
        # The previous attempt using sympy.Sum with a symbolic 'n' for the
        # derivative order was causing the issue.
        taylor_polynomial = 0
        for n in range(degree + 1):
            # Calculate the nth derivative of the function
            f_prime_n = diff(f, x, n)
            
            # Evaluate the derivative at the centering point
            f_prime_n_at_centering = f_prime_n.subs(x, centering)
            
            # Calculate the nth term of the Taylor series
            term = (f_prime_n_at_centering / factorial(n)) * (x - centering)**n
            
            # Add the term to the polynomial
            taylor_polynomial += term

        print(f"\nThe Taylor polynomial of degree {degree} centered at x={centering} for f(x) = {f_str} is:")
        # expand() makes the output more readable
        print(expand(taylor_polynomial))
        
        x_values = np.linspace(centering - 100, centering + 100, 800) # 400 points between -5 and 5
        taylor_polynomial_y_values = [taylor_polynomial.subs(x, x_val) for x_val in x_values]
        plt.plot(x_values,  taylor_polynomial_y_values, color='blue', label='Taylor Polynomial')
        plt.plot(x_values, (f.subs(x, fx_val) for fx_val in x_values), color='red', label=f'Original Function: {f}')  
        plt.title('Comparison of Taylor Polynomial and Original Function')
        plt.legend()
        plt.grid(True)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')      
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your input and try again.")


while True:
    run_taylor_approximator()
    choice = input("\nType 1 to approximate another function, or 2 to exit: ")
    if choice.strip() == "2":
        print("Exiting program in...")
        for i in range(5):
            print(f"{5 - i}!")
            time.sleep(1)
        break
