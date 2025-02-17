#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print ([])
        return
    
    fibonacci_list = [0, 1]
    for _ in range(2, length):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    
    print(fibonacci_list[:length])
