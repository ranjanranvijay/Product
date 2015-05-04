#Find the largest palindrome made from the product of two 3-digit numbers.
# Answer = 906609

def palindrom():
    pel = 0
    num = 100
    num2 = 100
    while num<=999:
        while num2<=999:
            pel_num = num * num2
            pel_num_str = str(pel_num)[::-1]
            if str(pel_num) == pel_num_str:
                if pel_num > pel:
                    pel = pel_num
            num2 = num2 +1
        num2 =100
        num = num + 1
        
    print (pel)
palindrom()
            
        
        