#master_or_visa
#Ma Tang Hao 6C23 18
#validate visa/mastercard
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
        return 'Visa'
    if length == 16 and 51<=int(cardnumber[0:2])<=55:
        return 'MasterCard'

    #belong to neither
    return 'it is neither mastercard or visa'

def validate(card):
    #master or visa?
    result=master_or_visa(card)
    if result == 'Visa' or result == 'MasterCard':
        #Luhn algorithm
        addup = 0
        for i in card[::2]:
            double = int(i) * 2
            if double > 9 : double -= 9
            addup += double
        for i in card[1::2]:
            addup += int(i)
        if addup % 10 == 0:
            return 'Valid ' + result
        else:
            return 'Invalid ' + result

    else: #if not a valid card
        return result
    
            
#main
card=input('plz input a cardnumber? \n')
print(validate(card))
