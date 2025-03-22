def is_prime(n):
    """Sprawdza, czy liczba n jest liczbą pierwszą."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Znajduje największy wspólny dzielnik dwóch liczb."""
    while b:
        a, b = b, a % b
    return a


def calculate_mean(numbers):
    """Oblicza średnią arytmetyczną dla liczb w liście."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


from math import gcd

def lcm(a, b):
    """Oblicza najmniejszą wspólną wielokrotność (LCM) dwóch liczb."""
    return abs(a * b) // gcd(a, b) if a and b else 0

def generate_fibonacci(n):
    """Generuje listę pierwszych n liczb ciągu Fibonacciego."""
    if n <= 0:
        return []
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

from my_awesome_lib.math_tools import generate_fibonacci
print(generate_fibonacci(5))  # Output: [0, 1, 1, 2, 3]


