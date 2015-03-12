#Project Euler 22
 
f=open('p022_names.txt','r')
names = f.read()
f.close()
names = names.split(',')
names.sort()
position=1
totalNameScore = 0
for i in names:
    nameValue = 0
    for j in i[1:-1]:
        nameValue += (ord(j)-64)
    totalNameScore += position*nameValue
    position +=1
print totalNameScore
