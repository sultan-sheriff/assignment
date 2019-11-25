N=int(input("enter the number : "))
for i in range(1,N):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)
    
