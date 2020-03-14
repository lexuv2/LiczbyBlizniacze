import math
f = open("pierw.txt",'w')


n = 1000000
pierw = [True for i in range(n + 1)]
i = 2
while (i * i < n):
    if (pierw[i] == True):
        for x in range(i*i, n+1, i):
            pierw[x] = False
    i += 1
for x in range(2, n):
    if pierw[x]:
        f.writelines(str(x)+" "+'\n')

#ZNAJDOWANIE LICZB Bliźniaczych Z LICZB PIERWSZYCH Z ZAKRESU 2:10^6
f = open("pierw.txt",'r')
tab = f.readlines()

licz = 0
for x in range(0,len(tab)-2):
    if (int(tab[x].replace('\n','')) - int(tab[x+1].replace('\n',''))) == -2:
        licz +=1



print(licz)



