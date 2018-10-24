fp = open('mushroom.dat',encoding='utf8')
list=[]
size = 0
dict = {}
rowNum=0
for line in fp:
   line=line.strip(' \n')
   list.append(line.split(' '))
   rowNum+=1
for i in range(0,rowNum):
    for t in list[i]:
        if(dict.get(t)):
            dict[t]+=1
        else:
            tmpDict={t:1}
            dict.update(tmpDict)
print(dict)
print(rowNum)