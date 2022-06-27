print('input mountain count : ', end='')
i = int(input())
print('input mountain size : ', end='')
y = int(input())


for x in range(1,y+1):
    n = ""
    for _ in range(i):
        for _ in range(y-x):
            n+="-"    
        for _ in range(x+1):
            n+="$"
        for _ in range(x-1):
            n+="$"    
        for _ in range(y-x):
            n+="-"

        
    print(n)