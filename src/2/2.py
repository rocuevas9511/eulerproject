fib_cache={}
def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n==1:
        value=1
    elif n ==2:
        value=2
    elif n>2:
        value= fib(n-1)+fib(n-2)

    fib_cache[n]=value
    return value

even=[]
for n in range(1,34):
    # print(n,":", fib(n))
    fibres=fib(n)
    if fibres<4000000 and fibres%2==0:
        even.append(fibres)

print(sum(even))

