#Display Fibonacci Sequence Using Recursion
def fibo_rec(n):
    if n <= 1 :
        return n
    else:
        return(fibo_rec(n-1)+fibo_rec(n-2))
    