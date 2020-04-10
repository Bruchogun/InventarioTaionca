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
    dataBase_stock=pd.read_csv('Base de datos.exe',header=0)
    lista=dataBase_stock['Código']
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

    #----------------------------------Information Verifier/DataBase_stock Saver-----------------------------------#
    
    dataBase_stock=pd.read_csv('Base de datos.exe',header=0)
    send_counter=0
    lista=dataBase_stock['Codigo']
    if (code==lista).any():
        send_counter=3
    while sellPriceODT.isdigit() and sellPricePub.isdigit() and priceCost.isdigit() and stock.isdigit() and send_counter<1 and measure !='Ninguna'and sellPriceODT != "" and sellPricePub != "" and priceCost != "" and stock != "" and code != "":
        dataBase_stock= open('Base de datos.exe','a',encoding="utf-8")
        dataBase_stock.write(code)
        dataBase_stock.write(',')
        dataBase_stock.write(description)
        dataBase_stock.write(',')
        dataBase_stock.write(sellPriceODT)
        dataBase_stock.write(',')
        dataBase_stock.write(sellPricePub)
        dataBase_stock.write(',')
        dataBase_stock.write(priceCost)
        dataBase_stock.write(',')
        dataBase_stock.write(stock)
        dataBase_stock.write(',')
        dataBase_stock.write(measure)
        dataBase_stock.write(',')
        dataBase_stock.write(today)
        dataBase_stock.write('\n')
        add_item_code.delete(0,1000)
        add_item_description.delete(0,1000)
        add_item_SellPriceODT.delete(0,1000)
        add_item_SellPricePub.delete(0,1000)
        add_item_PriceCost.delete(0,1000)
        add_item_Stock.delete(0,1000)
        actual_selection.set('Ninguna')
        send_counter=1
        dataBase_stock.close()
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

    #----------------------------------Information Verifier/DataBase_stock Saver-----------------------------------#
    dataBase_stock=pd.read_csv('Base de datos.exe',header=0)
    send_counter=0
    lista=dataBase_stock['Codigo']
    if code in lista.to_list():
        while sellPriceODT.isdigit() and sellPricePub.isdigit() and priceCost.isdigit() and stock.isdigit() and send_counter<1 and measure !='Ninguna'and sellPriceODT != "" and sellPricePub != "" and priceCost != "" and stock != "" and code != "":
            place=0
            for row in range(len(lista)):       
                if code == lista[row]: 
                    place=row
            dataBase_stock['Descripcion'][place]=description
            dataBase_stock['Precio de Venta a ODTs'][place]=sellPriceODT
            dataBase_stock['Precio de Venta al Publico'][place]=sellPricePub
            dataBase_stock['Precio de Costo'][place]=priceCost
            dataBase_stock['Existencias'][place]=stock
            dataBase_stock['Unidad de Medida'][place]=measure
            dataBase_stock['Ultima Fecha de Modificacion'][place]=today
            dataBase_stock.to_csv('Base de datos.exe', index=0)

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
    dataBase_stock=pd.read_excel('Registro de Contraseñas.xlsx','A')
    dataBase_stockPassword1=str(dataBase_stock['Contraseña'][0])
    dataBase_stockPassword2=str(dataBase_stock['Contraseña'][1])
    if password.get()==dataBase_stockPassword1 or password.get()==dataBase_stockPassword2:
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

    dataBase_stock=pd.read_csv('Base de datos.exe',header=0)
    lista=[]
    parameter=len(dataBase_stock['Codigo'])
    for row in range(parameter):
        for column in dataBase_stock:
            lista.append(dataBase_stock[column][row])
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

def stock_consume_validation(consume_code_Entry,consume_quantity_Entry,consume_ODT_Entry):
    code=str(consume_code_Entry.get())
    quantity=int(consume_quantity_Entry.get())
    odt=str(consume_ODT_Entry.get())
    today=str(date.today())

    dataBase_stock=pd.read_csv('Base de datos.exe',header=0)
    permission=0
    place="NaN"
    lista=dataBase_stock['Codigo']
    if code in lista.to_list() and odt != "":
        permission=permission+1
    for row in range(len(lista)):      
        if code == lista[row]: 
            place=row
    if  place != "NaN" and dataBase_stock['Existencias'][place]>=quantity:
        permission=permission+1
    
    if permission==2:
        dataBase_stock['Existencias'][place]=dataBase_stock['Existencias'][place]-quantity
        dataBase_stock.to_csv('Base de datos.exe', index=0)

        dataBase_movement= open("Operaciones de ODT.exe","a",encoding="UTF-8")
        dataBase_movement.write(code)
        dataBase_movement.write(",")
        dataBase_movement.write(odt)
        dataBase_movement.write(",")
        dataBase_movement.write(consume_quantity_Entry.get())
        dataBase_movement.write(",")
        dataBase_movement.write("Consumo")
        dataBase_movement.write(",")
        dataBase_movement.write(today)
        dataBase_movement.write("\n")
        dataBase_movement.close()
        
        consume_code_Entry.delete(0,1000)
        consume_quantity_Entry.delete(0,1000)
        consume_ODT_Entry.delete(0,1000)

        cost=(dataBase_stock['Precio de Venta a ODTs'][place])*quantity
        menssage_price=f'Se gastaron {cost}$ con esta acción.'
        messagebox.showinfo("Gasto realizado",menssage_price)
    else:
        messagebox.showwarning('Error', 'Favor revisar: \n  1)El código ingresado no existe. \n  2)La cantidad ingresada es mayor a la existente. \n  3)Hay un espacio en blanco.')

#------------------------------------Consumir Inventario-------------------------------------#
def stock_consume(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button)
    inventarioW.geometry(f'550x150+{width}+{height}')

    consume_code=tkinter.Label(inventarioW,text='Código')
    consume_code.grid(row=0,column=0)
    consume_quantity=tkinter.Label(inventarioW,text='Cantidad consumida')
    consume_quantity.grid(row=1,column=0)
    consume_quantity_advice=tkinter.Label(inventarioW,text='Debe ser un número entero', foreground= "gray")
    consume_quantity_advice.grid(row=1,column=2)
    consume_ODT=tkinter.Label(inventarioW,text="ODT de consumo")
    consume_ODT.grid(row=2,column=0)

    consume_code_Entry=tkinter.Entry(inventarioW)
    consume_code_Entry.grid(row=0,column=1)
    consume_quantity_Entry=tkinter.Entry(inventarioW)
    consume_quantity_Entry.grid(row=1,column=1)
    consume_ODT_Entry=tkinter.Entry(inventarioW)
    consume_ODT_Entry.grid(row=2,column=1)

    send_button=tkinter.Button(inventarioW,text='↑ Enviar ↑',command=lambda :stock_consume_validation(consume_code_Entry,consume_quantity_Entry,consume_ODT_Entry))
    send_button.grid(row=3,column=1)

#------------------------------------Función Inventario--------------------------------------#
def inventario():
    inventarioW = tkinter.Tk()
    inventarioW.title('Inventario')
    inventarioW.geometry(f'610x250+{width}+{height}')

    add_item_button=tkinter.Button(inventarioW, text='Añadir Artículo', font='Helvetica 10', command = lambda: verification(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW))
    add_item_button.place(relx=0.25,rely=0.25,relwidth=0.25, relheight=0.25)

    delete_item_button=tkinter.Button(inventarioW, text='Consumir Inventario\nPara ODT', font='Helvetica 10',command = lambda:stock_consume(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button))
    delete_item_button.place(relx=0.5,rely=0.5,relwidth=0.25, relheight=0.25)

    edit_item_button=tkinter.Button(inventarioW, text='Editar Artículo', font='Helvetica 10',command = lambda: edit_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW))
    edit_item_button.place(relx=0.25,rely=0.5,relwidth=0.25, relheight=0.25)

    view_item_button=tkinter.Button(inventarioW, text='Ver Stock', font='Helvetica 10', command = lambda: sotckView(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button))
    view_item_button.place(relx=0.5,rely=0.25,relwidth=0.25, relheight=0.25)

