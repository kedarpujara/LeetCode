def add_digits(digit):    
    curr_sum = 0
    while digit >= 10:        
        for num in str(digit):            
            curr_sum += int(num)
        digit = curr_sum
        curr_sum = 0
    return digit
print(add_digits(55))