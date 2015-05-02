
n = 1
l =[]
while n<1000:
        if n%3==0 or n%5 == 0:
                l.append(n)
        n+=1
t = sum(l)
print (t)
     