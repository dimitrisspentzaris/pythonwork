from ast import literal_eval
f=open('file2.txt','r')
lista=input('Γραψε μια εξάδα αριθμών: ').split(',')
x=[listes.rstrip('\n') for listes in open('file2.txt',"r")]
print (x)
print (lista)
y=[int(listes) for listes in lista]
for listes in x:
    if literal_eval(listes)==y[0:4]:
        print ('ΣΩΣΤΟ!')
        break

