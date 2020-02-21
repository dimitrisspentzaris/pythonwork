arithmos=int(input("Enter a number:"))
ypoloipo=0
while arithmos>10:
    arithmos*=3
    arithmos+=1
    arithmos2=arithmos
    while arithmos2>0:
        psifio=arithmos2%10
        ypoloipo=ypoloipo + psifio
        arithmos2=arithmos2//10
        if arithmos2==0:
            break
    print (ypoloipo)
    arithmos=ypoloipo
    ypoloipo=0

    
