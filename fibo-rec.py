def fibo_rec(n):
    if n < 2:
        return 1
    return fibo_rec(n-2)+fibo_rec(n-1)

if __name__ =='__main__':
    n = 6
    result = fibo_rec(n)
    print(result)
