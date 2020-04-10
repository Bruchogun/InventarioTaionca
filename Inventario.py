#-----------------------------------Inicio------------------------------------#
import tkinter
import os
import ctypes
from datetime import date
import time
from tkinter import ttk 
from tkinter import messagebox
import pandas as pd
#-----------------------------------Tamaño-------------------------------------#
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
width =int(((width-450)/2))
height =int(((height-150)/2)-(height/10))

#--------------------------------------CodeCannotBeRepeated---------------------------------------#
def codevalidation(code):
    dataBase=pd.read_csv('Base de datos.exe',header=0)
    lista=dataBase['Código']
    if code==lista:
        answer=-1
    return(answer)
#----------------------------------Añadir Artículo-----------------------------------#
def write_Data_csvFile(add_item_code,add_item_description,add_item_SellPriceODT,add_item_SellPricePub,add_item_PriceCost,add_item_Stock,actual_selection,inventarioW,labelError):
    code=str(add_item_code.get())
    description=add_item_description.get()
    sellPriceODT=add_item_SellPriceODT.get()
    sellPricePub=add_item_SellPricePub.get()
    priceCost=add_item_PriceCost.get()
    stock=add_item_Stock.get()
    measure=actual_selection.get()
    today=str(date.today())

    #----------------------------------Information Verifier/DataBase Saver-----------------------------------#
    
    dataBase=pd.read_csv('Base de datos.exe',header=0)
    send_counter=0
    lista=dataBase['Codigo']
    if (code==lista).any():
        send_counter=3
    while sellPriceODT.isdigit() and sellPricePub.isdigit() and priceCost.isdigit() and stock.isdigit() and send_counter<1 and measure !='Ninguna'and sellPriceODT != "" and sellPricePub != "" and priceCost != "" and stock != "" and code != "":
        dataBase= open('Base de datos.exe','a',encoding="utf-8")
        dataBase.write(code)
        dataBase.write(',')
        dataBase.write(description)
        dataBase.write(',')
        dataBase.write(sellPriceODT)
        dataBase.write(',')
        dataBase.write(sellPricePub)
        dataBase.write(',')
        dataBase.write(priceCost)
        dataBase.write(',')
        dataBase.write(stock)
        dataBase.write(',')
        dataBase.write(measure)
        dataBase.write(',')
        dataBase.write(today)
        dataBase.write('\n')
        add_item_code.delete(0,1000)
        add_item_description.delete(0,1000)
        add_item_SellPriceODT.delete(0,1000)
        add_item_SellPricePub.delete(0,1000)
        add_item_PriceCost.delete(0,1000)
        add_item_Stock.delete(0,1000)
        actual_selection.set('Ninguna')
        send_counter=1
        dataBase.close()
    if send_counter == 0 :
        labelError.grid(row=8,column=1)
    elif send_counter == 3:
        labelError.grid(row=8,column=1)
    else:
        labelError.grid_forget()

def edit_data(add_item_code,add_item_description,add_item_SellPriceODT,add_item_SellPricePub,add_item_PriceCost,add_item_Stock,actual_selection,inventarioW,labelError):
    code=str(add_item_code.get())
    description=add_item_description.get()
    sellPriceODT=add_item_SellPriceODT.get()
    sellPricePub=add_item_SellPricePub.get()
    priceCost=add_item_PriceCost.get()
    stock=add_item_Stock.get()
    measure=actual_selection.get()
    today=str(date.today())

    #----------------------------------Information Verifier/DataBase Saver-----------------------------------#
    dataBase=pd.read_csv('Base de datos.exe',header=0)
    send_counter=0
    lista=dataBase['Codigo']
    if code in lista.to_list():
        while sellPriceODT.isdigit() and sellPricePub.isdigit() and priceCost.isdigit() and stock.isdigit() and send_counter<1 and measure !='Ninguna'and sellPriceODT != "" and sellPricePub != "" and priceCost != "" and stock != "" and code != "":
            place=0
            for row in range(len(lista)):       
                if code == lista[row]: 
                    place=row
            dataBase['Descripcion'][place]=description
            dataBase['Precio de Venta a ODTs'][place]=sellPriceODT
            dataBase['Precio de Venta al Publico'][place]=sellPricePub
            dataBase['Precio de Costo'][place]=priceCost
            dataBase['Existencias'][place]=stock
            dataBase['Unidad de Medida'][place]=measure
            dataBase['Ultima Fecha de Modificacion'][place]=today
            dataBase.to_csv('Base de datos.exe', index=0)

            add_item_code.delete(0,1000)
            add_item_description.delete(0,1000)
            add_item_SellPriceODT.delete(0,1000)
            add_item_SellPricePub.delete(0,1000)
            add_item_PriceCost.delete(0,1000)
            add_item_Stock.delete(0,1000)
            actual_selection.set('Ninguna')
            send_counter=1
    else:
        send_counter=3
    if send_counter == 0 or send_counter==3:
        labelError.grid(row=8,column=1)
    else:
        labelError.grid_forget()
    
def send_button(password,add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,passwordW):
    dataBase=pd.read_excel('Registro de Contraseñas.xlsx','A')
    dataBasePassword1=str(dataBase['Contraseña'][0])
    dataBasePassword2=str(dataBase['Contraseña'][1])
    if password.get()==dataBasePassword1 or password.get()==dataBasePassword2:
        add_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW)
        passwordW.destroy()
    else:
        messagebox.showwarning('Error', 'Contraseña incorrecta')

def verification(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW):
    ancho=width+50
    alto=height+100
    passwordW = tkinter.Tk()
    passwordW.title('Contraseña')
    passwordW.geometry(f'400x80+{ancho}+{alto}')
    passwordLabel=tkinter.Label(passwordW, text='  Ingrese su contraseña: ')
    passwordLabel.grid(row=0,column=0)
    passwordBox=tkinter.Entry(passwordW)
    passwordBox.grid(row=0,column=1)
    passwordButton=tkinter.Button(passwordW,text='↑ Enviar ↑',command= lambda: send_button(passwordBox,add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,passwordW))
    passwordButton.grid(row=1,column=1)
    
    
def add_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button)
    #---------------------LABEL------------------------------------------------#
    add_item_labelCode=tkinter.Label(inventarioW,text='Código')
    add_item_labelCode.grid(row=0,column=0)
    add_item_labelDescription=tkinter.Label(inventarioW,text='Descripción del Artículo')
    add_item_labelDescription.grid(row=1,column=0)
    add_item_labelSellPriceODT=tkinter.Label(inventarioW,text="Precio de Venta a ODT's en $")
    add_item_labelSellPriceODT.grid(row=2,column=0)
    add_item_labelSellPricePub=tkinter.Label(inventarioW,text='Precio de venta al Público en $')
    add_item_labelSellPricePub.grid(row=3,column=0)
    add_item_labelPriceCost=tkinter.Label(inventarioW,text='Precio de Costo en $')
    add_item_labelPriceCost.grid(row=4,column=0)
    add_item_labelStock=tkinter.Label(inventarioW,text='Existencias Disponibles')
    add_item_labelStock.grid(row=5,column=0)
    #-------------------------BoxEntry-----------------------------------------#
    add_item_code=tkinter.Entry(inventarioW)
    add_item_code.grid(row=0,column=1)
    add_item_description=tkinter.Entry(inventarioW)
    add_item_description.grid(row=1,column=1)
    add_item_SellPriceODT=tkinter.Entry(inventarioW)
    add_item_SellPriceODT.grid(row=2,column=1)
    add_item_SellPricePub=tkinter.Entry(inventarioW)
    add_item_SellPricePub.grid(row=3,column=1)
    add_item_PriceCost=tkinter.Entry(inventarioW)
    add_item_PriceCost.grid(row=4,column=1)
    add_item_Stock=tkinter.Entry(inventarioW)
    add_item_Stock.grid(row=5,column=1)    

    #---------------------------DeployBar--------------------------------------#
    actual_selection=tkinter.StringVar(inventarioW)
    actual_selection.set('Ninguna')
    selection=tkinter.StringVar(inventarioW)
    measure_selection=['Unidad (Und)','Kilogramo (Kg)','Metro Cúbico (m^3)','Metro (m)']
    selection=tkinter.OptionMenu(inventarioW,actual_selection,*measure_selection)
    selection.grid(row=6,column=1)

    #-------------------------Buttons------------------------------------------#
    labelError=tkinter.Label(inventarioW,text='Los valores ingresados no son válidos.')
    send_button4=tkinter.Button(inventarioW,text='↑ Enviar ↑',command=lambda :write_Data_csvFile(add_item_code,add_item_description,add_item_SellPriceODT,add_item_SellPricePub,add_item_PriceCost,add_item_Stock,actual_selection,inventarioW,labelError))
    send_button4.grid(row=7,column=1)

#------------------------------------Limpiar Pantalla--------------------------------------#
def cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button):
    delete_item_button.destroy()
    add_item_button.destroy()
    edit_item_button.destroy()
    view_item_button.destroy()

#------------------------------------Ver Stock--------------------------------------#
def sotckView(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button)

    table=ttk.Treeview(inventarioW,height = 50, columns=6)
    table['columns']=('Descripcion','Precio de Venta a ODTs','Precio de Venta al Publico','Precio de Costo','Existencias','Unidad de medida','Ultima Modificacion')
    table.pack()
    table.heading('#0', text='Código', anchor = 'center' )
    table.column('#0',anchor='center')
    table.heading('#1', text='Descripción', anchor = 'center' )
    table.column('#1',anchor='center')
    table.heading('#2', text="Precio de Venta a ODT's", anchor = 'center' )
    table.column('#2',anchor='center')
    table.heading('#3', text='Precio de Venta al Público', anchor = 'center' )
    table.column('#3',anchor='center')
    table.heading('#4', text='Precio de Costo', anchor = 'center' )
    table.column('#4',anchor='center')
    table.heading('#5', text='Existencias', anchor = 'center' )
    table.column('#5',anchor='center')
    table.heading('#6', text='Unidad de Medida', anchor = 'center' )
    table.column('#6',anchor='center')
    table.heading('#7', text='Última Modificación', anchor = 'center' )
    table.column('#7',anchor='center')

    dataBase=pd.read_csv('Base de datos.exe',header=0)
    lista=[]
    parameter=len(dataBase['Codigo'])
    for row in range(parameter):
        for column in dataBase:
            lista.append(dataBase[column][row])
        code=lista[0]
        del lista[0]
        table.insert('','end', text=code, values=(lista))
        lista.clear()
    
#----------------------------------------Editar Artículo-------------------------------------#
def edit_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW):
        if 1==1:
            cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button)
            #---------------------LABEL------------------------------------------------#
            add_item_labelCode=tkinter.Label(inventarioW,text='Código')
            add_item_labelCode.grid(row=0,column=0)
            add_item_labelDescription=tkinter.Label(inventarioW,text='Descripción del Artículo')
            add_item_labelDescription.grid(row=1,column=0)
            add_item_labelSellPriceODT=tkinter.Label(inventarioW,text="Precio de Venta a ODT's en $")
            add_item_labelSellPriceODT.grid(row=2,column=0)
            add_item_labelSellPricePub=tkinter.Label(inventarioW,text='Precio de venta al Público en $')
            add_item_labelSellPricePub.grid(row=3,column=0)
            add_item_labelPriceCost=tkinter.Label(inventarioW,text='Precio de Costo en $')
            add_item_labelPriceCost.grid(row=4,column=0)
            add_item_labelStock=tkinter.Label(inventarioW,text='Existencias Disponibles')
            add_item_labelStock.grid(row=5,column=0)
            #-------------------------BoxEntry-----------------------------------------#
            add_item_code=tkinter.Entry(inventarioW)
            add_item_code.grid(row=0,column=1)
            add_item_description=tkinter.Entry(inventarioW)
            add_item_description.grid(row=1,column=1)
            add_item_SellPriceODT=tkinter.Entry(inventarioW)
            add_item_SellPriceODT.grid(row=2,column=1)
            add_item_SellPricePub=tkinter.Entry(inventarioW)
            add_item_SellPricePub.grid(row=3,column=1)
            add_item_PriceCost=tkinter.Entry(inventarioW)
            add_item_PriceCost.grid(row=4,column=1)
            add_item_Stock=tkinter.Entry(inventarioW)
            add_item_Stock.grid(row=5,column=1)    

            #---------------------------DeployBar--------------------------------------#
            actual_selection=tkinter.StringVar(inventarioW)
            actual_selection.set('Ninguna')
            selection=tkinter.StringVar(inventarioW)
            measure_selection=['Unidad (Und)','Kilogramo (Kg)','Metro Cúbico (m^3)','Metro (m)']
            selection=tkinter.OptionMenu(inventarioW,actual_selection,*measure_selection)
            selection.grid(row=6,column=1)

            #-------------------------Buttons------------------------------------------#
            labelError=tkinter.Label(inventarioW,text='Los valores ingresados no son válidos.')
            send_button4=tkinter.Button(inventarioW,text='↑ Enviar ↑',command=lambda :edit_data(add_item_code,add_item_description,add_item_SellPriceODT,add_item_SellPricePub,add_item_PriceCost,add_item_Stock,actual_selection,inventarioW,labelError))
            send_button4.grid(row=7,column=1)
        else:
            messagebox.showwarning('Error', 'Usted no tiene acceso a esta opción')

#------------------------------------Consumir Inventario-------------------------------------#
def stock_consume(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button)
    
    consume_code=tkinter.Label(inventarioW,text='Código')
    consume_code.grid(row=0,column=0)
    consume_quantity=tkinter.Label(inventarioW,text='Cantidad consumida')
    consume_quantity.grid(row=1,column=0)
    consume_ODT=tkinter.Label(inventarioW,text="ODT de consumo")
    consume_ODT.grid(row=2,column=0)
    consume_code_Entry=tkinter.Entry(inventarioW)
    consume_code_Entry.grid(row=0,column=1)
    consume_quantity_Entry=tkinter.Entry(inventarioW)
    consume_quantity_Entry.grid(row=1,column=1)
    consume_ODT_Entry=tkinter.Entry(inventarioW)
    consume_ODT_Entry.grid(row=2,column=1)

#------------------------------------Función Inventario--------------------------------------#
def inventario():
    inventarioW = tkinter.Tk()
    inventarioW.title('Inventario')
    inventarioW.geometry(f'500x300+{width}+{height}')

    add_item_button=tkinter.Button(inventarioW, text='Añadir Artículo', font='Helvetica 10', command = lambda: verification(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW))
    add_item_button.place(relx=0.25,rely=0.25,relwidth=0.25, relheight=0.25)

    delete_item_button=tkinter.Button(inventarioW, text='Consumir Inventario', font='Helvetica 10',command = lambda:stock_consume(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button))
    delete_item_button.place(relx=0.5,rely=0.5,relwidth=0.25, relheight=0.25)

    edit_item_button=tkinter.Button(inventarioW, text='Editar Artículo', font='Helvetica 10',command = lambda: edit_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW))
    edit_item_button.place(relx=0.25,rely=0.5,relwidth=0.25, relheight=0.25)

    view_item_button=tkinter.Button(inventarioW, text='Ver Stock', font='Helvetica 10', command = lambda: sotckView(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button))
    view_item_button.place(relx=0.5,rely=0.25,relwidth=0.25, relheight=0.25)

