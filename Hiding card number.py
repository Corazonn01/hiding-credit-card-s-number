# hiding-credit-card-s-number
def hide_number(credit_card):
    return '*' * (len(credit_card) - 4) + credit_card[-4:] 

#(len(here credit_card) - 4) will hide with this sign "*" all of the numbers in the card execpt the last 4 (so the output will be "***********")
#credit_card[-4:] (the output will be **********7896, it will add the last 4 numbers)

your_card = input("Please enter your credite card number: ")
print(hide_number(your_card))
