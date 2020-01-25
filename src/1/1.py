def multiple(n):
    #count=0
    arr=[]
    for x in range(1,n) :
        if x%3==0 or x%5==0:
            # count+=1      
            arr.append(x)

    return arr

print(multiple(10))
print(sum(multiple(10)))


print(multiple(1000))
print(sum(multiple(1000)))
