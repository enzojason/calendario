import calendar
import locale
import datetime
import tkinter as tk
from centralizacion import centrar
locale.setlocale(locale.LC_ALL, '')
from tkinter import *

#ventana principal
raiz=tk.Tk()
raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("550x430")
centrar(raiz,550,430)
raiz.iconbitmap("calendario.ico") #Cambiar el icono
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar
raiz.config(bg="white")
frame1 = Frame(raiz, bg="white")
frame1.pack(ipadx= 50,ipady=51, fill=X)

frame2 = Frame(raiz,bg="white")
frame2.pack(ipadx=5,ipady=1, fill=X,padx=10)

frame3 = tk.Frame(raiz,bg="white")
frame3.pack(ipadx= 50,ipady=130 ,padx=10, fill=X)

#LABEL FECHA ACTUAL
x=datetime.datetime.now()
fecha=x.strftime("%A %d de %B %Y")
labelfecha=Label(raiz,text=fecha,bg="white")
labelfecha.place(x=310,y=15)
labelfecha.config(fg="black",font=("Verdana",12))
#datos de la fecha actual
d=x.strftime("%d")
dia_actual=int(d)            
m=x.strftime("%m")
mes=int(m)
a=x.strftime("%Y")
anio=int(a)

#label encabezado fecha
lunes=Label(raiz,text="Lunes",borderwidth=2,relief="solid")
lunes.place(x=10,y=78)
lunes.config(width=8,height=1)
lunes.config(fg="black",bg="white",font=("Verdana",11))

martes=Label(raiz,text="Martes",borderwidth=2,relief="solid")
martes.place(x=86,y=78)
martes.config(width=8,height=1)
martes.config(fg="black",bg="white",font=("Verdana",11))

Miercoles=Label(raiz,text="Miercoles",borderwidth=2,relief="solid")
Miercoles.place(x=161,y=78)
Miercoles.config(width=8,height=1)
Miercoles.config(fg="black",bg="white",font=("Verdana",11))

Jueves=Label(raiz,text="Jueves",borderwidth=2,relief="solid")
Jueves.place(x=237,y=78)
Jueves.config(width=8,height=1)
Jueves.config(fg="black",bg="white",font=("Verdana",11))

Viernes=Label(raiz,text="Viernes",borderwidth=2,relief="solid")
Viernes.place(x=313,y=78)
Viernes.config(width=8,height=1)
Viernes.config(fg="black",bg="white",font=("Verdana",11))

Sabado=Label(raiz,text="Sabado",borderwidth=2,relief="solid")
Sabado.place(x=389,y=78)
Sabado.config(width=8,height=1)
Sabado.config(fg="black",bg="white",font=("Verdana",11))

Domingo=Label(raiz,text="Domingo",borderwidth=2,relief="solid")
Domingo.place(x=465,y=78)
Domingo.config(width=8,height=1)
Domingo.config(fg="black",bg="white",font=("Verdana",11))
#clase evento 
class Eventos():
    iniciar=0
    def __init__(self,titulo,fechayhora,importancia,fecha_recordatorio,duracion,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fechayhora=fechayhora
        self.descripcion=descripcion
        self.importancia=importancia
        self.duracion=duracion
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas
    def mostrarprincipal(n):
        if n=="1":
            return True
        
    try:
        import json
        f = open("eventos.json")
        f.close()
        ar=open("eventos.json",'r')
        l=ar.readline()
        ar.close
        if l=="{}" or l=="" or l=="[]" or l==" ":
            a=open("eventos.json",'w')
            a.write("")
            listaeventos=[]
            iniciar=0
        else:
            mostrarprincipal("1")
            with open("eventos.json",'r') as archivo:
                datos=json.load(archivo)
            datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
            datas = json.loads(datajs)#objeto python
            with open("eventos.json",'w') as archivo:
                json.dump(datas,archivo)
                listaeventos=datas
            iniciar=1

                
    except IOError:
        print('archivo no existe')
        a=open("eventos.json",'w')
        a.write("")
        listaeventos=[]
        

    listadias=[]
    repeticiones=1
    colores=["yellow","skyblue","springgreen","pink","green","blue","grey","white"]
    def agregar_evento():
        import json
        Eventos.listaeventos
        with open ("eventos.json",'w') as archivo:
            json.dump(Eventos.listaeventos,archivo)
    
    

class CalendarioPrincipal():
    def __init__(self,numero): 
        self.numero=numero
    x=datetime.datetime.now()
    diax=x.strftime("%d")
    dia_actual=int(diax)
    m=x.strftime("%m")
    mes_actual=int(m)
    a=x.strftime("%Y")
    anio=int(a)

    calendario=calendar.Calendar()
    mes = calendario.monthdayscalendar(anio,mes_actual)
    for a in range(len(mes)):
        semana=mes[a]
        for dias in semana:
            if dias==dia_actual:
                numero_de_semana=a  
                semana_actual=a

    numero_de_mes=mes_actual-1
    
    mesesnombre=list()
    for y in range(13):
        if y==0:
            pass
        else:
            mesesnombre.append(calendar.month_name[y])
    
    aniocompleto=list()
    aniocompleto.append(calendario.monthdayscalendar(2023,1))
    aniocompleto.append(calendario.monthdayscalendar(2023,2))
    aniocompleto.append(calendario.monthdayscalendar(2023,3))
    aniocompleto.append(calendario.monthdayscalendar(2023,4))
    aniocompleto.append(calendario.monthdayscalendar(2023,5))
    aniocompleto.append(calendario.monthdayscalendar(2023,6))
    aniocompleto.append(calendario.monthdayscalendar(2023,7))
    aniocompleto.append(calendario.monthdayscalendar(2023,8))
    aniocompleto.append(calendario.monthdayscalendar(2023,9))

    numero_de_mes=mes_actual-1
    opciones = {
    "Enero": ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'), 
    "Febrero": ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'),
    "Marzo":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Abril":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Mayo":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Junio":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'),
    "Julio":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Agosto":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Septiembre":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'),
    "Octubre":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Noviembre":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'),
    "Diciembre":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    }

    

#funcion que muestra el calendario SEMANAL
def mostrar_calendario_mensual():
    from centralizacion import centrar
    import tkinter as tk
    from tkinter import messagebox,ttk
    raizm = Toplevel(raiz)
    raizm.iconbitmap("calendario.ico") #Cambiar el icono
    raizm.resizable(0,0)
    raizm.focus_set()
    raizm.title("Calendario Mensual")
    raizm.geometry("500x400")
    raizm.config(bg="white")
    centrar(raizm,500,400)
    mif=Frame(raizm)
    mif.pack(padx=10,pady=100)
    mif.config(width="550",height="720")
    mif.config(bg="white")

    def mostrar(calendario):
        for f in range(len(calendario)):
            for c in range(0, 7):
                if calendario[f][c]==0:
                    pass
                else:
                    celda = Label(mif,height=2,width=8,text=calendario[f][c],bg="white")
                    celda.grid(padx=2, pady=2, row=f, column=c)
    
    anio=CalendarioPrincipal.anio
    mes=CalendarioPrincipal.mes_actual
    calendario=calendar.monthcalendar(anio,mes)
    mostrar(calendario)


from tkinter import ttk

#BOTON CAMBIAR EL CALENDARIO A MENSUAL
cambiar=ttk.Button(raiz,text="Calendario Mensual",command=mostrar_calendario_mensual)
cambiar.place(x=5,y=10)



def mostrar_calendario(numero_semana):
    mes=CalendarioPrincipal.aniocompleto[CalendarioPrincipal.numero_de_mes]
    semana=mes[numero_semana]
    CalendarioPrincipal.numero_de_semana=numero_semana
    y=0
    for x in semana:
        
        if x==0:
            celda=Label(frame2,height=2,width=6,text="-",bg="white",anchor="center")
        
        elif x==CalendarioPrincipal.dia_actual and CalendarioPrincipal.numero_de_mes==CalendarioPrincipal.mes_actual - 1:
                celda=Label(frame2,height=2,width=6,text=x,bg="white",anchor="center",borderwidth=2,relief="solid")
        else:
            celda=Label(frame2,height=2,width=6,text=x,bg="white",anchor="center")
        y=y+1
        celda.config(fg="black",bg="white",font=("Verdana",13))
        celda.grid(padx=1,pady=1,row=0,column=y,ipadx=1)
        
    for c in range(0, 7):
            cell =Label(frame3, width=10,bg="white")
            cell.grid(row=x, column=c)
     


def siguiente_semana():
    mm=len(CalendarioPrincipal.aniocompleto[CalendarioPrincipal.numero_de_mes])

    if CalendarioPrincipal.numero_de_semana + 1 == mm:
        c=CalendarioPrincipal.numero_de_mes + 1
        CalendarioPrincipal.numero_de_mes=c
        CalendarioPrincipal.numero_de_semana=0

        mostrar_calendario(CalendarioPrincipal.numero_de_semana)

    else:
        s=CalendarioPrincipal.numero_de_semana + 1
        mostrar_calendario(s)
        actualizar_datos()

def anterior_semana():
    mm=len(CalendarioPrincipal.aniocompleto[CalendarioPrincipal.numero_de_mes])
    
    if CalendarioPrincipal.numero_de_semana - 1 == mm:
        c=CalendarioPrincipal.numero_de_mes - 1
        CalendarioPrincipal.numero_de_mes=c
        CalendarioPrincipal.numero_de_semana=0
        mostrar_calendario(CalendarioPrincipal.numero_de_semana)
        

    else:
        s=CalendarioPrincipal.numero_de_semana - 1
        CalendarioPrincipal.numero_de_semana=s
        actualizar_datos()
        mostrar_calendario(s)
        


def actualizar_datos():
    import json
    import random
    f = open("eventos.json")
    f.close()
    ar=open("eventos.json",'r')
    l=ar.readline()
    ar.close
    if l=="{}" or l=="" or l=="[]" or l==" ":
        pass
    else:
        with open("eventos.json",'r') as archivo:
            datos=json.load(archivo)
        datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
        datas = json.loads(datajs)#objeto python

        dataseleccionada=[]
        diasse=[]
        numsse=[]
        for a in range(len(datas)):
            aa=(datas[a])
            for b in aa:
                c=aa[b]
                if b =="Fecha y hora":
                    import datetime
                    datetime_object = datetime.datetime.strptime(c, '%d/%m/%Y,%H:%M:%S')
                    di=datetime_object.strftime("%d")#conseguir dia
                    d=int(di)
                    dss=datetime_object.strftime("%w")#conseguir dia de la semana,0-6, 0 es domingo
                    ds=int(dss) - 1
                    me=datetime_object.strftime("%m")#conseguir mes 1-12
                    m=int(me)
                    
                    if m==CalendarioPrincipal.numero_de_mes+1:
                        mes=CalendarioPrincipal.aniocompleto[m-1]
                        for s in range(len(mes)):
                            sem=mes[s]
                            for i in range(len(sem)):
                                if s==CalendarioPrincipal.numero_de_semana:
                                    if sem[i]==d:
                                        diasse.append(d)
                                        numsse.append(ds)
                                        dataseleccionada.append(aa)

        tituloselect=[]
        for a in range(len(dataseleccionada)):
            aa=(dataseleccionada[a])
            for b in aa:
                c=aa[b]
                if b =="Titulo":
                    tituloselect.append(c)    

        importselect=[]
        for a in range(len(dataseleccionada)):
            aa=(dataseleccionada[a])
            for b in aa:
                c=aa[b]
                if b =="Importancia":
                    importselect.append(c)              
                                
        r=0        
        i=0              
        for u in diasse:
            import tkinter as tk
            from tkinter import messagebox,ttk     
            
            c=diasse.count(u)

            if c ==1 :
                if importselect[i]=="Importante":
                    cell =Label(frame3, width=10,height=2,text=tituloselect[i],bg="red")
                    cell.grid(row=0, column=numsse[i])
                    i+=1
                else:
                    cell =Label(frame3, width=10,height=2,text=tituloselect[i],bg=Eventos.colores[i])
                    cell.grid(row=0, column=numsse[i])
                    i+=1  

            else:
                if importselect[i]=="Importante":
                    cell =Label(frame3, width=10,height=2,text=tituloselect[i],bg="red")
                    cell.grid(row=r, column=numsse[i])
                    i+=1
                    r+=1
                else:
                    cell =Label(frame3, width=10,height=3,text=tituloselect[i],bg=Eventos.colores[i])
                    cell.grid(row=r, column=numsse[i])  
                    i+=1                             
                    r+=1
                                   


    
        
def mostrar_recordatorios():
    import tkinter as tk
    from tkinter import messagebox,ttk
    ventanamr = Toplevel(raiz)
    ventanamr.focus_set()
    ventanamr.title("Recordatorios")
    ventanamr.geometry("270x350")
    ventanamr.config(bg="white")
    centrar(ventanamr,270,350)
    ventanamr.resizable(0,0)
    fr=Frame(ventanamr)
    fr.config(bg="red")
    fr.pack(ipadx=0,ipady=0, fill=X,pady=30,padx=2)
    import json

    with open("eventos.json",'r') as archivo:
        datos=json.load(archivo)
    datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
    datas = json.loads(datajs)#objeto python 
    tits=list()
    fechayhorar=list()

    for a in range(len(datas)):
        aa=(datas[a])
        for b in aa:
            c=aa[b]
            if b =="Fecha Recordatorio":
                fechayhorar.append(c)
            elif b=="Titulo":
                tits.append(c)

    print("f",fechayhorar)

    for a in range(len(tits)):
        cell =Label(fr,width=15,height=3,text=tits[a],bg="white",padx=5)
        cell.grid(row=a, column=0)

    for b in range(len(tits)):
        celld =Label(fr,width=25,height=3,text=fechayhorar[b],bg="white",anchor="w")
        celld.grid(row=b, column=2)
    
    t=Label(ventanamr,text="Titulo",bg="white").place(x=40,y=5)
    Label(ventanamr,text="Fecha Recordatorio",bg="white").place(x=140,y=5)

      
actualizar_datos()
mostrar_calendario(CalendarioPrincipal.semana_actual)

     

from tkinter import ttk
#boton siguiente semana
sigue=ttk.Button(raiz,text="Semana Siguiente",command=siguiente_semana)
sigue.pack()
sigue.place(x=430,y=295)

#boton anterior semana
ante=ttk.Button(raiz,text="Semana Anterior",command=anterior_semana)
ante.pack()
ante.place(x=15,y=295)

def abrir_ventana():
    
    from centralizacion import centrar
    import tkinter as tk
    from tkinter import messagebox,ttk
    ventananueva = Toplevel(raiz)
    ventananueva.focus_set()
    ventananueva.title("Agregar evento")
    ventananueva.geometry("250x450")
    centrar(ventananueva,250,450)
    ##ventananueva.iconbitmap("calendario.ico")
    ##radioValue = tk.IntVar()
    radio = tk.IntVar()
    radio.set(1)
    varfecha = tk.IntVar()
    varfecha.set(2)
    #CREACION DE HORAS,DIAS Y MESES EN LISTA
    x=datetime.datetime.now()
    d=x.strftime("%d")
    dia_actual=int(d)            
    m=x.strftime("%m")
    a=x.strftime("%Y")
    h=x.strftime("%H")

    meses=list()
    horas=list()
    minutos=list()
    diass=list()
    for y in range(13):
        if y==0:
            pass
        else:
            meses.append(calendar.month_name[y])

    for z in range(24):
        if z==0:
            pass 
        else:
            horas.append(z)

    for r in range(60):
        if r==0:
            pass
        else:
            minutos.append(r)    

    for j in range(31):
        if j == 0:
            pass
        else:
            diass.append(j)

    #Label nuevo evento
    ne=Label(ventananueva,text="Nuevo Evento")
    ne.place(x=25,y=15)
    ne.config(font=("Verdana",17))
    
    #Label titulo
    titulol=Label(ventananueva,text="Titulo:")
    titulol.place(x=20,y=75)

    #Entrada titulo
    tituloe=ttk.Entry(ventananueva)
    tituloe.focus_set()
    tituloe.config(width=25)
    tituloe.place(x=65,y=75)
    


    

    #Label fecha 
    fecha=Label(ventananueva,text="Fecha:")
    fecha.place(x=20,y=115)
    fechan=x.strftime("%x")
    Label(ventananueva,text=fechan).place(x=65,y=115)
    #Label hora
    horal=Label(ventananueva,text="Hora:")
    horal.place(x=20,y=140)
    horaln=x.strftime("%X")
    Label(ventananueva,text=horaln).place(x=65,y=140)
    

    #label duracion
    duracionl=Label(ventananueva,text="Duración --->")
    duracionl.place(x=20,y=180)
    #entrada duracion horas
    horaed =ttk.Combobox(ventananueva,values=horas)
    horaed.place(x=95,y=180)
    horaed.config(width="3")
    horaed.insert(0,1)
    #entrada minutos
    minutosed =ttk.Combobox(ventananueva,values=minutos)
    minutosed.place(x=147,y=180)
    minutosed.config(width="3")
    minutosed.insert(0,"00")
    Label(ventananueva,text="hs").place(x=130,y=180)
    Label(ventananueva,text="min").place(x=185,y=180)
    
    #BOTONES importante y normal
    
    Radiobutton(ventananueva,
            text="Normal",
            variable=radio,
            value=1,
            ).place(x=10,y=215)

    Radiobutton(ventananueva,
            text="Importante",
            variable=radio,
            value=2,
            ).place(x=10,y=240)
    
    
    #LABEL RECORDATORIO
    Label(ventananueva,text="---------------Recordatorio---------------").place(x=10,y=270)
    dias=list()
    for a in range(dia_actual):
        dd=dia_actual-a
        dias.append(dd)

    #dias combox recordatorio
    diar= ttk.Combobox(
    ventananueva,
    state="readonly",
    values=dias,
    width="3",
    )
    diar.pack()
    diar.place(x=40,y=300)
    Label(ventananueva,text="Dia:").place(x=15,y=300)
    horasr=list()
    for x in range(24):
        if x==0:
            pass
        else:
            horasr.append(x)

    #entrada horas combobox
    horaer=ttk.Combobox(
    ventananueva,
    state="readonly",
    values=horasr,
    width=3,
    )
    horaer.pack
    horaer.place(x=120,y=300)
    Label(ventananueva,text="Hora:").place(x=90,y=300)

    #entrada minutos
    minutoser =ttk.Combobox(ventananueva,values=minutos)
    minutoser.place(x=190,y=300)
    minutoser.config(width="3")
    Label(ventananueva,text="Min:").place(x=165,y=300)

    #label descripcion
    Label(ventananueva,text="Descripción:").place(x=4,y=327)
    #texto descripcion
    descripcion_texto = Text(ventananueva, height=3,width=32)
    descripcion_texto.pack()
    descripcion_texto.place(x=4,y=350)
    
    def agregado():
        import json
        import datetime
        import tkinter as tk
        from tkinter import messagebox,ttk
        messagebox.showinfo(message="Evento Agregado", title="Calendario")
        titulo=tituloe.get()
        #fecha y hora actuales
        fechayhora=(fechan+","+horaln)

        #duracion
        horaf=horaed.get()
        minutof=minutosed.get()
        duracion='{}:{}'.format(horaf,minutof)

        #dia hora min recordatorio
        hora_recor=horaer.get()
        dia_recor=diar.get()
        mier=minutoser.get()

        diare=dia_recor+"/"+"3"+"/"+"2023"
        horar = hora_recor+":"+mier
        fecha_recordatorio=(diare+","+horar)

        descripcion=descripcion_texto.get("1.0","end")
        des=descripcion.rstrip()

        im=str(radio.get())
        if im=="1":
            importancia="Normal"
        elif im=="2":
            importancia="Importante"
       
        import json
        entry={"Descripcion":des,"Fecha Recordatorio":fecha_recordatorio,"Importancia":importancia,"Fecha y hora":fechayhora,"Titulo":titulo,"Duracion":duracion}
        Eventos.listaeventos.append(entry)
        Eventos.agregar_evento()
        Eventos.listadias.append(dia_actual)
        ventananueva.destroy()

    #BOTON AGREGAR LISTO
    boton_listo=ttk.Button(ventananueva,text="Agregar",command=agregado)
    boton_listo.pack()
    boton_listo.place(x=160,y=415)

    #funcion del boton salir
    def salir_vn():
        ventananueva.destroy()

    #BOTON SALIR
    boto_salir=ttk.Button(ventananueva,text="Salir",command=salir_vn)
    boto_salir.pack()
    boto_salir.place(x=20,y=415)   
    actualizar_datos()

from tkinter import messagebox
def error_archivo():
    messagebox.showwarning("Error", "No existen eventos")

def eliminar_evento():
    ar=open("eventos.json",'r')
    l=ar.readline()
    ar.close
    if l=="{}" or l=="" or l=="[]":
        error_archivo()
    else:
        from centralizacion import centrar
        import tkinter as tk
        from tkinter import messagebox,ttk

        ventanam = Toplevel(raiz)
        ventanam.focus_set()
        ventanam.title("Eliminar evento")
        ventanam.geometry("200x200")
        centrar(ventanam,200,200)
            
        import json
        with open("eventos.json",'r') as archivo:
            datos=json.load(archivo)
        datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
        datas = json.loads(datajs)#objeto python
        
        listats=[]
        
        for a in range(len(datas)):
            aa=(datas[a])
            for b in aa:
                c=aa[b]
                if b == "Titulo":
                    listats.append(c) 

        combotitulo=ttk.Combobox(ventanam,values=listats)
        combotitulo.place(x=50,y=80)
        combotitulo.config(width="12")

        

        def eliminar():
            #eliminar un evento
            from tkinter import messagebox
            messagebox.showinfo(message="Se ha eliminado un evento", title="Eliminar Evento")
            with open("eventos.json",'r') as archivo:
                datos=json.load(archivo)
            datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
            datas = json.loads(datajs)#objeto python
            
            for i in range(len(listats)):
                if listats[i] == combotitulo.get():
                        numero=i
            datas.pop(numero)
            Eventos.listaeventos.pop(numero)
            with open("eventos.json",'w') as archivo:
                json.dump(datas,archivo)

        #funcion del boton salir
        def salir_vm():
            ventanam.destroy()

        #boton salir
        bs=ttk.Button(ventanam,text="Salir",command=salir_vm)
        bs.pack()
        bs.place(x=10,y=140)

        #boton guardar
        bg=ttk.Button(ventanam,text="Elimnar",command=eliminar)
        bg.pack()
        bg.place(x=100,y=140)

        #Label 
        Label(ventanam,text="Seleccione el Evento \n a eliminar:").place(x=10,y=25)   
        actualizar_datos()
            

def modificar_evento():
    ar=open("eventos.json",'r')
    l=ar.readline()
    ar.close
    if l=="{}" or l=="" or l=="[]":
        error_archivo()
    else:
        from centralizacion import centrar
        import tkinter as tk
        from tkinter import messagebox,ttk

        ventanamod = Toplevel(raiz)
        ventanamod.focus_set()
        ventanamod.title("Modificar evento")
        ventanamod.geometry("180x180")
        centrar(ventanamod,180,180)
        #listas para combox de titulos y items para modificar
        import json
        with open("eventos.json",'r') as archivo:
            datos=json.load(archivo)
        datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
        datas = json.loads(datajs)#objeto python
        #mostrar y añadir a lista Titulos
        listatitulos=[]
        listaitems=[]
        for a in range(len(datas)):
            aa=(datas[a])
            for b in aa:
                c=aa[b]
                if b == "Titulo":
                    listatitulos.append(c)
            

        def selecciontitulo():
            f=Frame(ventanamod)
            f.pack()
            f.config(width="270",height="450")

            Label(f,text="Seleccione item a modificar").place(x=15,y=40)

            items=['Descripcion', 'Duracion', 'Fecha Recordatorio', 'Fecha y hora', 'Importancia', 'Titulo']
            #combox modificar
            comboitem=ttk.Combobox(ventanamod,values=items)
            comboitem.place(x=40,y=80)
            comboitem.config(width="14")

            #boton seleccionar item a modifica
            def mostrar_casillero():
                fe = Toplevel(raiz)
                fe.focus_set()
                fe.title("Modificar evento")
                fe.geometry("250x300")
                centrar(fe,250,300)
                a=comboitem.get()
                Label(fe,text="Ingrese el nuevo valor de \n"+a).place(x=20,y=20)
                horas=list()
                minutos=list()

                for z in range(24):
                    if z==0:
                        pass 
                    else:
                        horas.append(z)

                for r in range(60):
                    if r==0:
                        pass
                    else:
                        minutos.append(r)   
                     

                if a=="Fecha y hora":
                    #combo fecha
                    #label dias
                    Label(fe,text="Mes:").place(x=40,y=80)
                    Label(fe,text="Dias:").place(x=40,y=120)
                    def on_combobox_select(event):
                        combobox1.set("")
                        combobox1.config(values=CalendarioPrincipal.opciones[combobox.get()])

                    combobox = ttk.Combobox(
                    fe, width="11", state="readonly", values=tuple(CalendarioPrincipal.opciones.keys()))
                    combobox.place(x="80", y="80")
                    combobox.bind("<<ComboboxSelected>>", on_combobox_select)  
                    combobox1 = ttk.Combobox(
                    fe, width="4", state="readonly") 
                    combobox1.place(x="80",y="120")

                    #label horas
                    Label(fe,text="Hora:").place(x=40,y=160)

                    #horas
                    combohorafyh =ttk.Combobox(fe,values=horas)
                    combohorafyh.place(x=80,y=160)
                    combohorafyh.config(width="3")
                    combohorafyh.insert(0,1)
                    #minutos
                    combominutofyh =ttk.Combobox(fe,values=minutos)
                    combominutofyh.place(x=147,y=160)
                    combominutofyh.config(width="3")
                    combominutofyh.insert(0,"00")
                    Label(fe,text="hs").place(x=120,y=160)
                    Label(fe,text="min").place(x=185,y=160)                    
                   
     
                elif a=="Fecha Recordatorio":
                    nuevo.insert(END,"dd/mm/2023,hh:mm")

                else:
                    nuevo=Entry(fe,width="25")
                    nuevo.pack()
                    nuevo.place(x=22,y=100)
                    nuevo.focus_set()

                
                def guardarcambios():
                    fechayhora=combobox.get()+"/"+combobox1.get()+"/"+"2023"+","+combohorafyh.get()+":"+combominutofyh.get()+":"+"00"

                    fechayhoraelegida = datetime.datetime.strptime(fechayhora, '%d/%m/%Y,%H:%M:%S')
                    from tkinter import messagebox
                    messagebox.showinfo(message="Cambios Guardados", title="Modificar Calendario")
                    import json
                    with open("eventos.json",'r') as archivo:
                        datos=json.load(archivo)
                    datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
                    datas = json.loads(datajs)#objeto python
                    
                    
                    #elegir titulo a modificar y modificarlo
                    for i in range(len(listatitulos)):
                        if listatitulos[i] == combotitulo.get():
                            tituloelegido=i

                    #modifica el titulo en el entry nuevo
                    aa=(datas[tituloelegido])

                    for b in aa:
                        if b=="Fecha y hora":
                            
                            aa[b]=fechayhoraelegida
                        if b == comboitem.get():
                            #Aqui se pone en a el nuevo titulo a cambiar ejemplo puse un input
                            aa[b]=nuevo.get()

                    with open("eventos.json",'w') as archivo:
                        #guardar la modificacion
                        json.dump(datas,archivo, indent=4)
                        Eventos.listaeventos=[]
                        Eventos.listaeventos=[datas]


                    #boton salir
                    bs=ttk.Button(fe,text="Atras")
                    bs.pack()
                    bs.place(x=40,y=220)

                    #boton guardar
                    bg=ttk.Button(fe,text="Guardar",command=guardarcambios)
                    bg.pack()
                    bg.place(x=130,y=220)

            ci=ttk.Button(ventanamod,text="Aceptar",command=mostrar_casillero)
            ci.place(x=50,y=140)

        
        #Label modifcar evento
        Label(ventanamod,text="Seleccione el Evento \n a modificar:").place(x=10,y=25)   
        combotitulo=ttk.Combobox(ventanamod,values=listatitulos)
        combotitulo.place(x=50,y=80)
        combotitulo.config(width="12")
        #boton seleccionar
        bc=ttk.Button(ventanamod,text="Seleccionar",command=selecciontitulo)
        bc.place(x=50,y=140)
        actualizar_datos()
#boton modificar evento
boton2=ttk.Button(raiz,text="Modificar\n Evento",command=modificar_evento)
boton2.place(x=120,y=335)

#boton eliminar evento
boton3=ttk.Button(raiz,text="Eliminar\n Evento",command=eliminar_evento)
boton3.place(x=350,y=335)

    
#boton agregar evento
from tkinter import ttk
boton1=ttk.Button(raiz,text="Agregar\n Evento",command=abrir_ventana)
boton1.pack()
boton1.place(x=235,y=335)

#boton mostrar recordatorios
botonr=ttk.Button(raiz,text="Recordatorios",command=mostrar_recordatorios)
botonr.pack()
botonr.place(x=5,y=40)

col=Label(raiz,bg="red")
col.config(width=1,height=1)
col.place(x=25,y=400)
Label(raiz,text="Importante",bg="white").place(x=40,y=400)

coh=Label(raiz,bg="white",borderwidth=2,relief="solid")
coh.config(width=1,height=1)
coh.place(x=150,y=400)
Label(raiz,text="Dia Actual",bg="white").place(x=165,y=400)
raiz.mainloop()