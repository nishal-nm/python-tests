num = 4

def rec_fact(x):
    if(x == 1):
        return 1
    else:
        return (x * fact(x-1))

def iter_fact(x):
    res = 1
    for i in range(1,x+1):
        res *= i
    return res

rec_fact(num)
iter_fact(num)