"""
Faça uma função recursiva que retorne True se uma string é palíndromo ou
False caso contrário
"""

def palindrome(string, ispalindrome=True):
    if not string:
        return ispalindrome
    
    if string[0] == string[-1]:
        return palindrome(string[1:-1], True)
    
    return False


print(palindrome('aaasaaa'))

