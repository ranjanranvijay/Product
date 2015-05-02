def prime_fact(first_prime, num):
    while first_prime * first_prime < num:
        if num%first_prime == 0:
            num = num/first_prime
        first_prime = first_prime + 1
        
    print (num)
prime_fact(2, 600851475143 )

            