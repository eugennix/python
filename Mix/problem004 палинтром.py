# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(num):
    return str(num) == str(num)[::-1]


largestPalindrome = 0
maxLimit = 10000
minLimit = 1000

x1 = minLimit
while x1 < maxLimit:
    x2 = x1
    while x2 < maxLimit:
        xxProduct = x1 * x2
        if largestPalindrome < xxProduct:
            if is_palindrome(xxProduct):
                print(" >> " + str(x1) + " * " + str(x2) + " = " + str(xxProduct))
                largestPalindrome = xxProduct
        x2 += 1
    x1 += 1

print("the largest palindrome made from the product of two 3-digit numbers\n" + str(largestPalindrome))
