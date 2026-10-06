def paln(n):
    if n==n[::-1]:
        return "palindrome"
    else:
        return "not palindrome"