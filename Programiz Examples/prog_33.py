def fibo_rec(n):
    if n <= 1:
        return n
    
    else :
        return n + fibo_rec(n-1)