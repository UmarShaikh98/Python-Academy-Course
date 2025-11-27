n = int(input("Enter the height of the pyramid: "))
for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i) 
        
total = sum(range(1, n + 1))    
print(f"TOTAL sum of all numbers from 1 to {n} is: {total}")