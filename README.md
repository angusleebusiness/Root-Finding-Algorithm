# Root-Finding Algorithm
one of my earliest python projects, finally uploaded to github.

## Newton's Method

the first root finding algorithm I ever encountered, this solver asks the user for a function, $$f(x)$$, how many decimals of precision, an initial guess, and the maximum iterations the program should do; it then recursively iterates through the Newton's method formula:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

If the max iteration is reached, the program terminates and outputs the current best approximation.

If the derivative of $$x_n$$ is equal to 0, the program terminates since Newton's method results in division by 0 error;

The program then reaches and outputs the approximation for the one of the roots of the function to the level of precision specified.
