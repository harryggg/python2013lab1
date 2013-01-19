#master_or_visa
#Ma Tang Hao 6C23 18
#categorize an input cardnumber into visa/mastercard
def master_or_visa(n):
    #strip space and -
    cardnumber=n.replace(' ','').replace('-','') 
    #check for invalid char
    try:
        x=int(cardnumber)
    except(ValueError):
        return 'Input Wrong. contains invalid character.'
    length = len(n)
    #categorize
    if (length == 13 or length == 16) and (cardnumber[0]=='4'):
        return 'It is Visa'
    if length == 16 and 51<=int(cardnumber[0:2])<=55:
        return 'It is MasterCard'

    #belong to neither
    return 'It is neither'

#main

card=input('plz input your card number?\n')
print(master_or_visa(card))
