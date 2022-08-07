
# Here we are going to make a programme which recognize either a number is Prime or not.


from traceback import print_last


x = int(input("Insert a number  "))

if 0<x<2:
    print("Number is not prime")
else:

    for i in range(2,x):
        if (x%i==0):
            break
        print("number is not prime")
    else:
            print("Number is prime")