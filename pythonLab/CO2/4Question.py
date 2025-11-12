import math
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

even_square_numbers = []


for num in range(start, end + 1):
    
    if 1000 <= num <= 9999:
        
        digits = str(num)
        if all(int(d) % 2 == 0 for d in digits):
            
            root = int(math.sqrt(num))
            if root * root == num:
                even_square_numbers.append(num)


print("Four-digit numbers with all even digits and perfect squares:")
print(even_square_numbers)
