import json
with open("eventos.json",'r') as archivo:
    datos=json.load(archivo)

    datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
    datas = json.loads(datajs)#objeto python


listafeho=[]
listafechas=list()
for a in range(len(datas)):
    aa=(datas[a])
    for b in aa:
        c=aa[b]
        if b =="Fecha y hora":
            listafechas.append(c)
import datetime
listadiasfechas=list()
listanumsem=list()
for b in listafechas:
    datetime_object = datetime.datetime.strptime(b, '%d/%m/%Y,%H:%M:%S')
    c=datetime_object.strftime("%d")
    listadiasfechas.append(c)
    ns=datetime_object.strftime("%w")#	Weekday as a number 0-6, 0 is Sunday
    n=int(ns)
    if n==0:
        nss=7
    else:
        nss=n
    listanumsem.append(nss)

print(listadiasfechas)
print(listanumsem)