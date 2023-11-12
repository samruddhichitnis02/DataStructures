# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(0) = 0

# factorial(n) = n * factorial(n - 1)

# factorial 
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    

print(factorial(5))
# 1st iteration :- 5 * factorial(4)
# 2nd iteration :- 5 * 4 * factorial(3)
# 3rd iteration :- 5 * 4 * 3 * 2 * factorial(2)
# 4th iteration :- 5 * 4 * 3 * 2 * factorial(1)
# 5th iterataion :- 5 * 4 * 3 * 2 * 1 -> last iteration

# Fibonacci Series using recursion
# f0 = 0
# f1 = 1
# f2 = f1 + f0 = 0 + 1 = 1
# f3 = f2 + f1 = 1 + 1 = 2
# f4 = f3 + f2 = 2 + 1 = 3

# fibonacci(n) = f(n - 1) + f(n - 2)

def fibonacci(n):
    if (n == 0) or (n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
# 1st iteration :- fibonacci(5) = fibonacci(4) + fibonacci(3)
# 2nd iteration :- fibonacci(4) = fibonacci(3) + fibonacci(2), fibonacci(3) = fibonacci(2) + fibonacci(1)
# 3rd iteration :- fibonacci(3) = fibonacci(2) + fibonacci(1), fibonacci(2) + fibonacci(1) + fibonacci(0) 
# In case of fibonacci series its better not to use recursion because it works on the same n more than once