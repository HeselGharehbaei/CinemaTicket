import random

def generate_credit_card_number(prefix="9973"):
    digits = [random.randint(0, 9) for _ in range(11)] 
    # luhn
    for i in range(10, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    checksum = (10 - sum(digits) % 10) % 10
    
    digits.append(checksum)

    card_number = prefix + ''.join(map(str, digits))
    
    return card_number

