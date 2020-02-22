import re

with open("file1.txt","r") as f:
    lekseis=f.read().split()
    print(lekseis)
f.close()
lekseis.sort(reverse=True,key=len)
print (lekseis)
lekseis=lekseis[0:5]
fwnhenta=['αειυοωη']
teliko=[re.sub(r'[αειυοωη]','',leksi) for leksi in lekseis]
print (teliko)

