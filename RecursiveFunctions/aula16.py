"""
Faça uma função recursiva para inverter uma string.
"""

def reverse(string):
    if not string:
        return ''
    
    return string[-1] + reverse(string[:-1])

print(reverse('abracadabra'))
