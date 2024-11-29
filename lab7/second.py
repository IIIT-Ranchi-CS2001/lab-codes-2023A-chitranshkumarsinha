import random
import math
import matplotlib.pyplot as plt
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def get_prime_and_composite(num_list):
    primes = []
    composites = []
    for num in num_list:
        if is_prime(num):
            primes.append(num)
        elif num > 1: 
            composites.append(num)
    return primes, composites
def main():
    K = int(input("Enter the number of random numbers (K, minimum 10): "))
    if K < 10:
        print("K must be at least 10.")
        return
    N = int(input("Enter the upper limit for the random numbers (N): "))
    random_numbers = random.sample(range(1, N + 1), K)
    print(f"Generated random numbers: {random_numbers}")
    primes, composites = get_prime_and_composite(random_numbers)
    print(f"Prime numbers: {primes}")
    print(f"Composite numbers: {composites}")
    prime_squares = [p ** 2 for p in primes]
    composite_square_roots = [math.sqrt(c) for c in composites]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    ax1.scatter(primes, prime_squares, color='blue')
    ax1.set_title('Prime Numbers vs Their Squares')
    ax1.set_xlabel('Prime Numbers')
    ax1.set_ylabel('Squares of Prime Numbers')
    ax2.scatter(composites, composite_square_roots, color='green')
    ax2.set_title('Composite Numbers vs Their Square Roots')
    ax2.set_xlabel('Composite Numbers')
    ax2.set_ylabel('Square Roots of Composite Numbers')
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()