print('input angka (input number) : ',end ="")
y = int(input())


for x in range(1,y+1):
    n = ""
    for _ in range(y-x):
        n+="-"    
    for _ in range(x):
        n+="$"
    for _ in range(x-1):
        n+="$"    
    for _ in range(y-x):
        n+="-"
    print(n)
        
    