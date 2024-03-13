def num(n):
    for i in range(1,n):
        if i % 3 ==0 and i % 5 ==0:
            print('FIZZBUZZ')
        elif i % 3==0 and i % 5!=0:
            print('FIZZ')
        elif i % 3!=0 and i % 5==0:
            print('BUZZ')
        else:
            print("This value"+str(i)+" is neither divisible by 3 nor 5")
num(30)


n=100
c=1
while c<n:

    if c % 3 ==0 and c % 5 ==0:
        print('FIZZBUZZ')
    elif c % 3==0 and c % 5!=0:
        print('FIZZ')
    elif c % 3!=0 and c % 5==0:
        print('BUZZ')
    else:
        print("This value"+str(c)+" is neither divisible by 3 nor 5")
    c+=1
