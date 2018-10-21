# python3

# Sum of Two Digits Problem
# Compute the sum of two single digit numbers.
# Input: Two single digit numbers. Output: The sum of these numbers.


def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
