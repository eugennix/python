# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(num):
    return str(num) == str(num)[::-1]


largestPalindrome = 0
maxLimit = 999
minLimit = 99

x1 = maxLimit
while x1 > minLimit:
    x2 = maxLimit
    while x2 >= x1:
        xxProduct = x1 * x2
        if largestPalindrome < xxProduct:
            if is_palindrome(xxProduct):
                print(" >> " + str(x1) + " * " + str(x2) + " = " + str(xxProduct))
                largestPalindrome = xxProduct
                break
        else:
            break
            # other x2 make product < current largestPalindrome
            # so skip its
        x2 -= 1
    x1 -= 1

print("the largest palindrome\n" + str(largestPalindrome))