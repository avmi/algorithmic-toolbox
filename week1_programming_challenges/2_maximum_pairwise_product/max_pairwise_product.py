# python3

# Maximum Pairwise Product Problem
# Find the maximum product of two distinct numbers in a sequence of non-negative integers.
# Input: A sequence of non-negative integers.
# Output: The maximum value that can be obtained by multiplying two different elements from the sequence.


def max_pairwise_product(numbers):
    n = len(numbers)

    index1 = -1
    index2 = -1

    for i in range(n):
        if index1 == -1 or numbers[i] > numbers[index1]:
            index1 = i

    for i in range(n):
        if i != index1 and (index2 == -1 or numbers[i] > numbers[index2]):
            index2 = i

    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
