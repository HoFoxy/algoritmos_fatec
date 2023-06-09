a = 0
b = 1
count = 0

while count < 10:
    print(a)
    num_fib = a + b
    a = b
    b = num_fib
    count += 1