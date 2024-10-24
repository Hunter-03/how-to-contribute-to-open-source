import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is Armstrong
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    return digit_sum == num

# Function to check if a number is Harshad
def is_harshad(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

# Function to check if a number is Neon
def is_neon(num):
    square = num ** 2
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == num

# Function to calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        next_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)
    return fib_seq[:n]

# Menu-driven program
def main():
    while True:
        print("\nNumber Operations Menu:")
        print("1. Check Prime Number")
        print("2. Check Armstrong Number")
        print("3. Check Harshad Number")
        print("4. Check Neon Number")
        print("5. Calculate Factorial")
        print("6. Generate Fibonacci Sequence")
        print("7. Exit")
        
        choice = int(input("Enter your choice (1-7): "))
        
        if choice == 1:
            num = int(input("Enter a number to check if it's prime: "))
            if is_prime(num):
                print(f"{num} is a Prime number.")
            else:
                print(f"{num} is not a Prime number.")
        
        elif choice == 2:
            num = int(input("Enter a number to check if it's an Armstrong number: "))
            if is_armstrong(num):
                print(f"{num} is an Armstrong number.")
            else:
                print(f"{num} is not an Armstrong number.")
        
        elif choice == 3:
            num = int(input("Enter a number to check if it's a Harshad number: "))
            if is_harshad(num):
                print(f"{num} is a Harshad number.")
            else:
                print(f"{num} is not a Harshad number.")
        
        elif choice == 4:
            num = int(input("Enter a number to check if it's a Neon number: "))
            if is_neon(num):
                print(f"{num} is a Neon number.")
            else:
                print(f"{num} is not a Neon number.")
        
        elif choice == 5:
            num = int(input("Enter a number to calculate its factorial: "))
            print(f"Factorial of {num} is {factorial(num)}.")
        
        elif choice == 6:
            n = int(input("Enter the number of terms for the Fibonacci sequence: "))
            fib_sequence = fibonacci(n)
            print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")
        
        elif choice == 7:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

# Run the main program
if __name__ == "__main__":
    main()
