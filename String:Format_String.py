def print_formatted(number):
    arr=len(bin(number)[2:])+1
    for i in range(1,number+1):
        print(f"{i:>{arr-1}}{oct(i)[2:]:>{arr}}{hex(i)[2:].upper():>{arr}}{bin(i)[2:]:>{arr}}")
