
try:
    import json
    f = open("eventos.json")
    with open("eventos.json",'r') as archivo:
         datos=json.load(archivo)
    datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
    datas = json.loads(datajs)#objeto python
    print('File exists')
    f.close()
    with open("eventos.json",'w') as archivo:
        json.load(datas,archivo)
        
except IOError:
    print('File does not exist')
    listaeventos=[]
    

    