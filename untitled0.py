import json
with open("eventos.json",'r') as archivo:
    datos=json.load(archivo)
datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
data = json.loads(datajs)#objeto python

listats=[]

print(data)

