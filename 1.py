n=int(input("enter values "))
m=0
if(n>1):
    for i in range(n):
        t=int(input())
        if(t>m):
            m=t
print(f"greatest number is" ,m if m>0 else "enter values") 
