#階層(遞迴實現)

def factorial_recursive(n):
    if n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
    return 
print(factorial_recursive(5))
