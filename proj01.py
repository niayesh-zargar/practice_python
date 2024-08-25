n = int (input("enter n:")) # max is 170 in vscode
if n%2==0 : #even
    i = 1 ; t = n//2
    while  i <= n:
        print("-"*t+ "*"*i + "-"*t)
        i +=2 ; t -=1
    i = n+1 ; t = 0 
    while i >0 :
        print("-"*t+ "*"*i + "-"*t)
        i -=2 ; t +=1

elif n%2!= 0 : #odd
    i = 1 ; t = n // 2
    while i <= n:
        print("-"*t + "*"*i + "-"*t)
        i += 2 ; t -= 1
    i = i-4 ; t = t+2 
    while i>0 :
        print("-"*t+ "*"*i + "-"*t)
        i -=2 ; t +=1 
    