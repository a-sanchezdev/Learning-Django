from tkinter import*

operador = ''

precios_comida=[1.32,1.65,2.31,3.22,1.22,1.99,2.05,2.65,9.09,10.01,12.0]
precios_bebida=[0.25,0.99,1.21,1.54,1.08,1.10,2.00,1.58,2.55,5.90,4.23]
precios_postre=[1.54,1.68,1.32,1.97,2.55,2.14,1.94,1.74,0.67,1.70,9.10]


def click_boton(numero):
    global operador
    operador= operador+numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador =''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def revisar_check():
    x=0
    for c in cuadros_comida:
        if variables_comida[x].get()==1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get()=='0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x+=1

    x=0
    for c in cuadros_bebida:
        if variables_bebida[x].get()==1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get()=='0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x+=1

    x=0
    for c in cuadros_postre:
        if variables_postre[x].get()==1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get()=='0':
                cuadros_postre[x].delete(0,END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x+=1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p+=1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[p])
        p+=1

    
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida,2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida,2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre,2)}')
    var_costo_subtotal.set(f'$ {round(sub_total,2)}')
    var_costo_impuesto.set(f'$ {round(impuestos,2)}')
    var_costo_total.set(f'$ {round(total,2)}')


    
#iniciar tkinter
aplicacion = Tk()

#tamaño de ventana
aplicacion.geometry('1020x530+0+15')

#evitar responsividad
aplicacion.resizable(0,0)

#titulo de ventana
aplicacion.title('MI RESTAURANTE - SISTEMA DE FACTURACION')

#COLOR DE FONDO DE VENTANA

aplicacion.config(bg='burlywood2')

#panel superior

panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side = TOP)

#etiqueta de titulo
etiqueta_titulo = Label(panel_superior,text='Sistema de Facturacion',fg = 'azure4', font = ('Dosis',58),bg='burlywood',width=20)
etiqueta_titulo.grid(row=0,column=0)

#panel izquierdo

panel_izquierdo = Frame(aplicacion,bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel de costos
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT,bg='azure4')
panel_costos.pack(side=BOTTOM)

#panel comidas

panel_comida = LabelFrame(panel_izquierdo,text='Comidas',font=('Dosis',19,'bold'),
                          border=1,relief=FLAT,fg='azure4')
panel_comida.pack(side=LEFT)


#panel de bebidas
panel_bebida = LabelFrame(panel_izquierdo,text='Bebidas',font=('Dosis',19,'bold'),
                          border=1,relief=FLAT,fg='azure4')
panel_bebida.pack(side=LEFT)

#panel de postres
panel_postre = LabelFrame(panel_izquierdo,text='Postres',font=('Dosis',19,'bold'),
                          border=1,relief=FLAT,fg='azure4')
panel_postre.pack(side=LEFT)

#panel derecho
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_botones.pack()

#lista de productos

lista_comidas = ['pollo','cordero','salmon','merluza','kebab','pizza','enchiladas','mole','molletes','caldo de res','sushi']
lista_bebidas = ['agua','limonada','jugo','naranjada','cerveza','refresco','vino tinto','vino blanco','cerveza 2x1','bebida frutos rojos','vampiro']
lista_postres = ['helado','frutas','brownies','pay de queso','flan','mousse','pastel','pay de limon','struddent','galletas','cono']

#generar items comida
variables_comida=[]
cuadros_comida = []
texto_comida =[]
contador = 0
for comida in lista_comidas:
    #crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida=Checkbutton(panel_comida,
                       text=comida.title(),
                       font=('Dosis',10,'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=variables_comida[contador],
                       command=revisar_check)
    comida.grid(row=contador,column=0,sticky=W)
    #crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comida,
                                     font=('Dosis',8,'bold'),
                                           bd=1,
                                           width=5,
                                           state=DISABLED,
                                           textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,column=1,sticky=W)
    contador+=1

#generar items bebida
variables_bebida=[]
cuadros_bebida = []
texto_bebida =[]
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida=Checkbutton(panel_bebida,text=bebida.title(),font=('Dosis',10,'bold'),
                       onvalue=1,offvalue=0,
                       variable=variables_bebida[contador],
                       command=revisar_check)
    bebida.grid(row=contador,column=0,sticky=W)
    #crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebida,
                                     font=('Dosis',8,'bold'),
                                           bd=1,
                                           width=5,
                                           state=DISABLED,
                                           textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,column=1,sticky=W)
    contador+=1

#generar items bebida
variables_postre=[]
cuadros_postre = []
texto_postre =[]
contador = 0


for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre=Checkbutton(panel_postre,text=postre.title(),font=('Dosis',10,'bold'),
                       onvalue=1,offvalue=0,variable=variables_postre[contador],
                       command=revisar_check)
    postre.grid(row=contador,column=0,sticky=W)
      #crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postre,
                                     font=('Dosis',8,'bold'),
                                           bd=1,
                                           width=5,
                                           state=DISABLED,
                                        #    textvariable=texto_postre[contador]
                                           textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,column=1,sticky=W)
    contador+=1

#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal = StringVar()
var_costo_impuesto = StringVar()
var_costo_total = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo comida',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0,column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0,column=1,padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo bebida',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1,column=1,padx=41)

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo postre',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2,column=1,padx=41)


etiqueta_costo_subtotal = Label(panel_costos,
                              text='Costo subtotal',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_subtotal.grid(row=0,column=2)

texto_costo_subtotal = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_subtotal)

texto_costo_subtotal.grid(row=0,column=3,padx=41)

etiqueta_costo_impuesto = Label(panel_costos,
                              text='Costo impuesto',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_impuesto.grid(row=1,column=2)

texto_costo_impuesto = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_impuesto)

texto_costo_impuesto.grid(row=1,column=3,padx=41)

etiqueta_costo_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_total.grid(row=2,column=2)

texto_costo_total = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_total)

texto_costo_total.grid(row=2,column=3,padx=41)

#botones
botones = ['total','recibo','guardar','resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',12,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    
    botones_creados.append(boton)
    
    boton.grid(row=0,
               column=columnas)
    columnas+=1

botones_creados[0].config(command=total)

#area de recibo
    
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)


#calculadora

visor_calculadora = Entry(panel_calculadora,font=('Dosis',12,'bold'),
                          width=38,
                          bd=1)
visor_calculadora.grid(row=0,column=0,columnspan=4)

botones_calculadora=['7','8','9','+',
                     '4','5','6','-',
                     '1','2','3','x',
                     '=','Borrar','0','/']

botones_guardados=[]

fila = 1
columna=0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',12,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    
    botones_guardados.append(boton)
    
    boton.grid(row=fila,column=columna)
    if columna==3:
        fila+=1

    columna+=1
    if columna==4:
        columna=0


botones_guardados[0].config(command=lambda:click_boton('7'))
botones_guardados[1].config(command=lambda:click_boton('8'))
botones_guardados[2].config(command=lambda:click_boton('9'))
botones_guardados[3].config(command=lambda:click_boton('+'))
botones_guardados[4].config(command=lambda:click_boton('4'))
botones_guardados[5].config(command=lambda:click_boton('5'))
botones_guardados[6].config(command=lambda:click_boton('6'))
botones_guardados[7].config(command=lambda:click_boton('-'))
botones_guardados[8].config(command=lambda:click_boton('1'))
botones_guardados[9].config(command=lambda:click_boton('2'))
botones_guardados[10].config(command=lambda:click_boton('3'))
botones_guardados[11].config(command=lambda:click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda:click_boton('0'))
botones_guardados[15].config(command=lambda:click_boton('/'))


#evitar que la pantalla se cierre
aplicacion.mainloop()
