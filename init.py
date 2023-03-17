import calendar
import locale
import datetime
import tkinter as tk
from centralizacion import centrar
locale.setlocale(locale.LC_ALL, '')
from tkinter import *
#clase evento 
class Eventos():
    def __init__(self,titulo,fecha,hora,importancia,fecha_recordatorio,duracion=1,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fecha=fecha
        self.hora=hora
        self.descripcion=descripcion
        self.importancia=importancia
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas
    
    def guardar_evento(self):
        import json
        datos={"Titulo":self.titulo,"Fecha":self.fecha,"Hora":self.hora,"Importancia":self.importancia,"Fecha Recordatorio":self.fecha_recordatorio,"Descripcion":self.descripcion}
        with open("eventos.json",'a') as archivo:
            json.dump(datos,archivo)
            
raiz=tk.Tk()
raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("500x400")
centrar(raiz,550,400)
raiz.iconbitmap("calendario.ico") #Cambiar el icono
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar

#LABEL FECHA ACTUAL
x=datetime.datetime.now()
fecha=x.strftime("%A %d de %B %Y")
labelfecha=Label(raiz,text=fecha)
labelfecha.place(x=310,y=15)
labelfecha.config(fg="black",font=("Verdana",12))

#frame calendario
from tkinter import *
mi_Frame=Frame()
mi_Frame.pack(padx=10,pady=100)
mi_Frame.config(width="550",height="420")
mi_Frame.config(bg="grey")

#label encabezado fecha
encabezado=Label(raiz,text="Lunes     Martes     Miercoles  Jueves   Viernes     Sabado    Domingo")
encabezado.place(x=20,y=75)
encabezado.config(fg="black",bg="white",font=("Verdana",11))

from tkinter import ttk
#BOTON CAMBIAR EL CALENDARIO A MENSUAL
cambiar=ttk.Button(raiz,text="Calendario Mensual")
cambiar.place(x=5,y=10)
"""
#funcion siguiente y anterior semana
def siguiente_semana():
    numero=3
    mostrar_calendario(anio,mes,numero)

#BOTON SIGUIENTE SEMANA
siguiente=ttk.Button(raiz,text="Siguiente Semana",command=siguiente_semana)
siguiente.place(x=430,y=300)
#BOTON ANTERIOR SEMANA
anterior=ttk.Button(raiz,text="Anterior Semana")
anterior.place(x=15,y=300)
"""
#funcion que muestra el calendario SEMANAL
def mostrar_calendario(anio,mes,numero_semana):
    calendario=calendar.Calendar()
    meses= calendario.monthdayscalendar(anio,mes)
    semana=meses[numero_semana]
    for x in semana:
        celda=Label(mi_Frame,height=9,width=6,text=x,bg="grey")
        celda.config(fg="black",bg="white",font=("Verdana",13))
        celda.grid(padx=1,pady=1,row=0,column=x)

#datos de la fecha actual
x=datetime.datetime.now()               
m=x.strftime("%m")
mes=int(m)
a=x.strftime("%Y")
anio=int(a)
d=x.strftime("%d")
dia_actual=int(d)


#calcular numero de semana
def calcular_semana(anio,mes):
    calendario=calendar.Calendar()
    meses = calendario.monthdayscalendar(anio,mes)
    for a in range(len(meses)):
            semana=meses[a]
            for dias in semana:
                if dias==dia_actual:
                    numero_de_semana=a
    return numero_de_semana

def abrir_ventana():
    from centralizacion import centrar
    import tkinter as tk
    from tkinter import messagebox,ttk
    ventananueva = Toplevel(raiz)
    ventananueva.focus_set()
    ventananueva.title("Agregar evento")
    ventananueva.geometry("270x450")
    centrar(ventananueva,270,450)
    ##ventananueva.iconbitmap("calendario.ico")
    ##radioValue = tk.IntVar()
    ##radioValue.set(1)
    
    #CREACION DE HORAS,DIAS Y MESES EN LISTA
    meses=list()
    horas=list()
    minutos=list()
    anios=[2020,2021,2022,2023,2024]
    

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

    #Label nuevo evento
    ne=Label(ventananueva,text="Nuevo Evento")
    ne.place(x=5,y=5)
    ne.config(font=("Verdana",17))
    
    #Label titulo
    titulol=Label(ventananueva,text="Titulo:")
    titulol.place(x=55,y=55)
    #Entrada titulo
    tituloe=ttk.Entry(ventananueva)
    tituloe.focus_set()
    tituloe.config(width=19)
    tituloe.place(x=95,y=55)

    #label mes
    mesl=Label(ventananueva,text="Mes:")
    mesl.place(x=62,y=80)
    #combo meses
    combo_meses = ttk.Combobox(
    ventananueva,
    state="readonly",
    values=meses,
    width="10",)
    combo_meses.pack()
    combo_meses.place(x=95,y=80)

    #label Dia
    dial=Label(ventananueva,text="Dia:")
    dial.place(x=65,y=135)
    #dias configuracion
    calendario=calendar.Calendar()
    dias=list()
    mes = calendario.monthdayscalendar(2023,3)
    for a in range(len(mes)):
        semana=mes[a]
        for dia in semana:
            if dia==0:
                pass
            else:
                dias.append(dia)

    #combo dias
    combo_dias = ttk.Combobox(
    ventananueva,
    state="readonly",
    values=dias,
    width="2",)
    combo_dias.pack()
    combo_dias.place(x=93,y=135)
    
   

    #label años
    aniol=Label(ventananueva,text="Año:")
    aniol.place(x=62,y=105)
    #combo años
    combo_anios = ttk.Combobox(
    ventananueva,
    state="readonly",
    values=anios,
    width="7",
    )
    combo_anios.pack()
    combo_anios.place(x=95,y=107)
    combo_anios.set(2023)


    #label horas evento
    horal=Label(ventananueva,text="Hora:")
    horal.place(x=128,y=135)
    #combo horas
    combo_horas=ttk.Combobox(
    ventananueva,
    state="readonly",
    values=horas,
    width=2,
    )
    combo_horas.pack
    combo_horas.place(x=163,y=135)
    #combo minutos evento
    Label(ventananueva,text=":").place(x=197,y=135)
    combo_min=ttk.Combobox(
    ventananueva,
    state="readonly",
    values=minutos,
    width=2,
    )
    combo_min.pack
    combo_min.place(x=206,y=135)
    
    #label duracion
    duracionl=Label(ventananueva,text="Duración:")
    duracionl.place(x=40,y=180)
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
    radioValue = tk.IntVar()
    Radiobutton(ventananueva,
            text="Normal",
            variable=radioValue,
            value=1,
            ).place(x=10,y=215)

    Radiobutton(ventananueva,
            text="Importante",
            variable=radioValue,
            value=2,
            ).place(x=10,y=240)


    #LABEL RECORDATORIO
    Label(ventananueva,text="---------------Recordatorio---------------").place(x=10,y=270)
    #entrada dias combobox
    diar= ttk.Combobox(
    ventananueva,
    state="readonly",
    values=dias,
    width="3",
    )
    diar.pack()
    diar.place(x=95,y=300)
    
    #entrada horas combobox
    horaer=ttk.Combobox(
    ventananueva,
    state="readonly",
    values=horas,
    width=3,
    )
    horaer.pack
    horaer.place(x=167,y=300)

    #label de dia y hora
    Label(ventananueva,text="Dia:").place(x=65,y=300)
    Label(ventananueva,text="Hora:").place(x=133,y=300)

    #label descripcion
    descripcion=Label(ventananueva,text="Descripción:").place(x=4,y=331)
    #texto descripcion
    descripcion_texto = Text(ventananueva, height=3,width=32)
    descripcion_texto.pack()
    descripcion_texto.place(x=4,y=350)

    def agregado():
    #titulo,importancia,fecha_recordatorio,fecha_hora,descripcion):
        import json
        import tkinter as tk
        from tkinter import messagebox,ttk
        messagebox.showinfo(message="Evento Agregado", title="Calendario")
        

        titulo=tituloe.get()
        
        diac=combo_dias.get()
        mesc=combo_meses.get()
        aniosc=combo_anios.get()

        fecha=diac+"/"+mesc+"/"+aniosc
    
        horac=combo_horas.get()
        minc=combo_min.get()
        horaevento=horac+":"+minc
        
        hora=horaed.get()
        minuto=minutosed.get()
        duracion='{}:{}'.format(hora,minuto)
        
        hora_recor=horaer.get()
        dia_recor=diar.get()

        fecha_recordatorio="dia:"+dia_recor+","+"hora:"+hora_recor

        descripcion=descripcion_texto.get("1.0","end")
        des=descripcion.strip()

        if radioValue==2:
            impor="Importante"
        if radioValue==1:
            impor="Normal"
        else:
            impor="Normal"
        t=Eventos(titulo,fecha,horaevento,impor,fecha_recordatorio,duracion,descripcion)
        t.guardar_evento()
        t=0
        ventananueva.destroy()
    
    
    def salir():
        ventananueva.quit()

    #BOTON AGREGAR LISTO
    boton_listo=ttk.Button(ventananueva,text="Agregar",command=agregado)
    boton_listo.pack()
    boton_listo.place(x=160,y=415)

    #BOTON SALIR
    boto_salir=ttk.Button(ventananueva,text="Salir",command=salir)
    boto_salir.pack()
    boto_salir.place(x=20,y=415)

#botonagregar
boton1=Button(raiz,text="Agregar\nEvento",command=abrir_ventana)
boton1.config(width=7,height=3)
boton1.place(x=210,y=320)


numerosemana=calcular_semana(anio,mes)
mostrar_calendario(anio,mes,numerosemana)
raiz.mainloop()