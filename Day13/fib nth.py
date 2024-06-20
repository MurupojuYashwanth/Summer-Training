def fibonacci_recursive(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = 2
print(fibonacci_recursive(n)) #op 3
