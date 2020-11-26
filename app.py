nterms = 10
count = 0 
n1 = 0
n2 = 1
while count < nterms:
    if count <= 1:
        print(n1)
        print(n2)
        count += 2
    else:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        print(nth)
        count += 1
