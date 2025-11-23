n = int(input())
sum = 10**(n-1)
for i in range(n,1,-1):
    sum = sum + i
    
print(sum)
        