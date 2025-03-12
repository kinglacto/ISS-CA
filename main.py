def is_narc(n): # added :
    """Check if a number is narc."""
    num_str = str(n)  # changed == to =
    num_digits = len(num_str) # changed == to =
    
    sum_of_powers = sum([int(digit) ** num_digits for digit in num_str]) # make it a list
    
    return sum_of_powers == n

def print_narcis_numbers(start, end):  # added ,
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):  # changed function name
        if (is_narc(num)):  # added :
            print(num)

print_narcis_numbers(1000, 5000)  # changed function name
