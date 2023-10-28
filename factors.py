import sys

def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return None

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        for line in file:
            number = int(line)
            factors = factorize(number)
            if factors:
                p, q = factors
                print(f"{number}={p}*{q}")

except FileNotFoundError:
    print(f"Error: File {input_file} not found.")

except ValueError:
    print(f"Error: Invalid input in file {input_file}.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

