def caching_fibonacci():
    cash={}
    def fibonacci(n):
            m = n
            if n not in cash:
                if n <= 1:
                    cash[m] = n
                    return cash[m]
                else:
                    n = fibonacci(n-1)+fibonacci(n-2)
                    cash[m] = n
                    print(cash)
                return cash[m]
            else:
                return cash[n]
    return fibonacci 
    
fib = caching_fibonacci()
print(fib(10))
print(fib(10))
print(fib(10))
print(fib(10))
print(fib(15))
print(fib(15))
print(fib(1))
print(fib(11))

