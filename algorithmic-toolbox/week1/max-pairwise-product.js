/* Maximum Pairwise Product Problem.
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
 >>> Explanation: Here we just multyply the value 2 by the value 3 */

const MaxPairwiseProduct = (A) => {
  let i
  let index1 = 1
  let index2 = 1
  for (i = 2; i < A.length; i++) {
    if (A[i] > A[index1]) {
      index1 = i
    }
  }
  for (i = 2; i < A.length; i++) {
    if ((A[i] !== A[index1]) && (A[i] > A[index2])) {
      index2 = i
    }
  }
  return A[index1] * A[index2]
}

console.log(MaxPairwiseProduct([7, 5, 14, 2, 8, 8, 10, 1, 2, 3]))
