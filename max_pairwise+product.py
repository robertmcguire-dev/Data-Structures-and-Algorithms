""" Maximum Pairwise Product Problem.
Find the maximum product of two distinct numbers in a sequence
of non-negative integers.

Specification:
Input: A sequence of non-negative integers.
Output: The maximum value that can be obtained by multiplying
two different elements from the sequence.

Samples:
 >>> A = [7, 5, 14, 2, 8, 8, 10, 1, 2, 3]
 >>> MaxPairwiseProduct(A)
 140
 >>> # Explanation: To acieve the value 140 take the second largest value
 and the largest value in the array and multiply them together.
 >>> A = [1, 2, 3]
 6
 >>> Explanation: Here we just multyply the value 2 by the value 3 """


def MaxPairwiseProduct(A):
    A.sort()
    return A[-2] * A[-1]


print(MaxPairwiseProduct([7, 5, 14, 2, 8, 8, 10, 1, 2, 3]))
