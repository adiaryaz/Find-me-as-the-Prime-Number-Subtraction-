def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def subtract_primes():
    first_prime = None
    total_subtraction = 0
    found_prime = False

    while True:
        user_input = input().strip().lower()
        if user_input == 'n':
            break
        elif user_input == 'y':
            try:
                number = int(input())
                if number < 0:
                    print("NoProceed")
                    return
                if is_prime(number):
                    if first_prime is None:
                        first_prime = number
                        total_subtraction = number 
                    else:
                        total_subtraction -= number  
                    found_prime = True
            except ValueError:
                print("NoProceed")
                return
        else:
            print("NoProceed")
            return

    if found_prime:
        print(total_subtraction)
    else:
        print(0)

if __name__ == "__main__":
    subtract_primes()