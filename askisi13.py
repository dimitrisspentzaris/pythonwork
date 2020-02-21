def athrPsifiwn(cardnumber):
    mikos=len(cardnumber)
    athr1=0
    athr2=0
    if mikos ==0:
        return 0
    else:
        if mikos%2==0:
            teleytaio=int(cardnumber[-1])
            athr2+=teleytaio

            return athr2+athrPsifiwn(cardnumber[:-1])
        else:
            teleytaio=int(cardnumber[-1])
            teleytaio=2*teleytaio
            athr3=teleytaio//10 + teleytaio%10
            athr1+=athr3

        return athr1 + athrPsifiwn(cardnumber[:-1])

    
def elegxos():
    cardnumber=input("Enter 16 digit card number: ")
    synolo=athrPsifiwn(cardnumber)
    if synolo%10==0:
        print("Valid card number")
    else:
        print ("Invalid card number")


def main():
    elegxos()


main()

        
        
