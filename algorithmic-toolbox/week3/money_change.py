""" Money Change
  Find the minimum number of coins needed to change the input value
  (an integer) into coins with denominations 1, 5, and 10.

  Specification
  Input: The input consists of a single integer m.
  Constraints: 1 <= m <= 10^3.
  Output: Output the minimum number of coins with denominations 1, 5, 10
  that changes m

  Samples
  >>> m = 2
  >>> money_change(m)
  2
  >>> # Explanation: To achieve the value 2 take the denominations 1 + 1.
  >>> m = 28
  >>> money_change(m)
  6
  >> # Explanation: To achive the value 6 take the denominations
  10 + 10 + 5 + 1 + 1 + 1."""


def get_change(m):
    count = 0
    while m > 0:
        if m % 10 == 0:
            count += 1
            m -= 10
        elif m % 5 == 0:
            count += 1
            m -= 5
        else:
            count += 1
            m -= 1
    return count


m = int(input())
print(get_change(m))
