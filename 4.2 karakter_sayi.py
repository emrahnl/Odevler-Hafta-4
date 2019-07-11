password=input("Enter a password: ")
capital_letter=0
lower_letter=0
digit_number=0
special_character=0

for c in password:
    if c.isupper():
        capital_letter=capital_letter+1
    elif c.islower():
        lower_letter=lower_letter+1
    elif c.isdigit():
        digit_number=digit_number+1
    else:
        special_character=special_character+1
        
print(capital_letter)
print(lower_letter)
print(digit_number)
print(special_character)

