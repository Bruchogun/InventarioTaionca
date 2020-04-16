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

    float(add_item_SellPriceODT.get())
    float(add_item_SellPricePub.get())
    float(add_item_PriceCost.get())
    float(add_item_Stock.get())
    #----------------------------------Information Verifier/DataBase_stock Saver-----------------------------------#
    
    dataBase_stock=pd.read_csv('Base de datos.exe',header=0)
    send_counter=0
    lista=dataBase_stock['Codigo']
    if (code==lista).any():
        send_counter=3
    while send_counter<1 and measure !='Ninguna'and sellPriceODT != "" and sellPricePub != "" and priceCost != "" and stock != "" and code != "":
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
    float(add_item_SellPriceODT.get())
    float(add_item_SellPricePub.get())
    float(add_item_PriceCost.get())
    float(add_item_Stock.get())

    dataBase_stock=pd.read_csv('Base de datos.exe',header=0)
    send_counter=0
    lista=dataBase_stock['Codigo']
    if code in lista.to_list():
        while send_counter<1 and measure !='Ninguna'and sellPriceODT != "" and sellPricePub != "" and priceCost != "" and stock != "" and code != "":
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
    
def send_button(password,add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,passwordW,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    dataBase_stock=pd.read_excel('Registro de Contraseñas.xlsx','A')
    dataBase_stockPassword1=str(dataBase_stock['Contraseña'][0])
    dataBase_stockPassword2=str(dataBase_stock['Contraseña'][1])
    if password.get()==dataBase_stockPassword1 or password.get()==dataBase_stockPassword2:
        add_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
        passwordW.destroy()
    else:
        messagebox.showwarning('Error', 'Contraseña incorrecta')

def verification(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    ancho=width+50
    alto=height+100
    passwordW = tkinter.Tk()
    passwordW.title('Contraseña')
    passwordW.geometry(f'400x80+{ancho}+{alto}')
    passwordLabel=tkinter.Label(passwordW, text='  Ingrese su contraseña: ')
    passwordLabel.grid(row=0,column=0)
    passwordBox=tkinter.Entry(passwordW)
    passwordBox.grid(row=0,column=1)
    passwordButton=tkinter.Button(passwordW,text='↑ Enviar ↑',command= lambda: send_button(passwordBox,add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,passwordW,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    passwordButton.grid(row=1,column=1)
    
    
def add_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
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
def cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    delete_item_button.destroy()
    add_item_button.destroy()
    edit_item_button.destroy()
    view_item_button.destroy()
    view_item_button5.destroy()
    view_item_button6.destroy()
    view_item_button7.destroy()
    view_item_button8.destroy()

#------------------------------------Ver Stock--------------------------------------#
def sotckView(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
   
    table=ttk.Treeview(inventarioW,height = 200, columns=6)
    tableScrollBar=ttk.Scrollbar(inventarioW, orient="vertical",command=table.yview)
    table.configure(yscroll=table.set)
    tableScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

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
    
#---------------------------------------Ver Operaciones---------------------------------------#
def actionsView(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
   
    table=ttk.Treeview(inventarioW,height = 200, columns=7)
    tableScrollBar=ttk.Scrollbar(inventarioW, orient="vertical",command=table.yview)
    table.configure(yscroll=table.set)
    tableScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    table['columns']=('Codigo','ODT','Cantidad','Unidad de medida','Acción','Dinero Equivalente','Ganancia Generada','Fecha')
    table.pack()
    table.heading('#0', text='Código', anchor = 'center' )
    table.column('#0',anchor='center')
    table.heading('#1', text='ODT', anchor = 'center' )
    table.column('#1',anchor='center')
    table.heading('#2', text="Cantidad", anchor = 'center' )
    table.column('#2',anchor='center')
    table.heading('#3', text='Unidad de medida', anchor = 'center' )
    table.column('#3',anchor='center')
    table.heading('#4', text='Acción', anchor = 'center' )
    table.column('#4',anchor='center')
    table.heading('#5', text='Dinero Equivalente $', anchor = 'center' )
    table.column('#5',anchor='center')
    table.heading('#6', text='Ganancia Generada $', anchor = 'center' )
    table.column('#6',anchor='center')
    table.heading('#7', text='Fecha', anchor = 'center' )
    table.column('#7',anchor='center')

    dataBase_stock=pd.read_csv('Operaciones de ODT.exe',header=0)
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
def edit_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
        if 1==1:
            cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
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
    quantity=float(consume_quantity_Entry.get())
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
    if  place != "NaN" and float(dataBase_stock['Existencias'][place])>=quantity:
        permission=permission+1
    
    if permission==2:
        costo=(float(dataBase_stock['Precio de Venta a ODTs'][place]))*quantity
        cost=str(costo)
        ganacia=(costo-(float(dataBase_stock['Precio de Costo'][place])))
        revenue=str(ganacia)
        measure=dataBase_stock['Unidad de Medida'][place]
        actual_stock=float(dataBase_stock['Existencias'][place])
        cantidad=float(quantity)
        dataBase_stock['Existencias'][place]=actual_stock-cantidad
        dataBase_stock.to_csv('Base de datos.exe', index=0)

        dataBase_movement= open("Operaciones de ODT.exe","a",encoding="UTF-8")
        dataBase_movement.write(code)
        dataBase_movement.write(",")
        dataBase_movement.write(odt)
        dataBase_movement.write(",")
        dataBase_movement.write(consume_quantity_Entry.get())
        dataBase_movement.write(",")
        dataBase_movement.write(measure)
        dataBase_movement.write(",")
        dataBase_movement.write("Consumo")
        dataBase_movement.write(",")
        dataBase_movement.write(cost)
        dataBase_movement.write(",")
        dataBase_movement.write(revenue)
        dataBase_movement.write(",")
        dataBase_movement.write(today)
        dataBase_movement.write("\n")
        dataBase_movement.close()
        
        consume_code_Entry.delete(0,1000)
        consume_quantity_Entry.delete(0,1000)
        consume_ODT_Entry.delete(0,1000)

        menssage_price=f'Se gastaron {cost}$ con esta acción.\nLa ganacia es de {revenue}$.'
        messagebox.showinfo("Gasto realizado",menssage_price)
    else:
        messagebox.showwarning('Error', 'Favor revisar: \n  1)El código ingresado no existe. \n  2)La cantidad ingresada es mayor a la existente. \n  3)Hay un espacio en blanco.')


def stock_consume_validation_pub(consume_code_Entry,consume_quantity_Entry,consume_ODT_Entry):
    code=str(consume_code_Entry.get())
    quantity=float(consume_quantity_Entry.get())
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
    if  place != "NaN" and float(dataBase_stock['Existencias'][place])>=quantity:
        permission=permission+1
    
    if permission==2:
        costo=(float(dataBase_stock['Precio de Venta al Publico'][place]))*quantity
        cost=str(costo)
        ganacia=(costo-(float(dataBase_stock['Precio de Costo'][place])))
        revenue=str(ganacia)
        measure=dataBase_stock['Unidad de Medida'][place]
        actual_stock=float(dataBase_stock['Existencias'][place])
        cantidad=float(quantity)
        dataBase_stock['Existencias'][place]=actual_stock-cantidad
        dataBase_stock.to_csv('Base de datos.exe', index=0)

        dataBase_movement= open("Operaciones de ODT.exe","a",encoding="UTF-8")
        dataBase_movement.write(code)
        dataBase_movement.write(",")
        dataBase_movement.write(odt)
        dataBase_movement.write(",")
        dataBase_movement.write(consume_quantity_Entry.get())
        dataBase_movement.write(",")
        dataBase_movement.write(measure)
        dataBase_movement.write(",")
        dataBase_movement.write("Consumo")
        dataBase_movement.write(",")
        dataBase_movement.write(cost)
        dataBase_movement.write(",")
        dataBase_movement.write(revenue)
        dataBase_movement.write(",")
        dataBase_movement.write(today)
        dataBase_movement.write("\n")
        dataBase_movement.close()
        
        consume_code_Entry.delete(0,1000)
        consume_quantity_Entry.delete(0,1000)
        consume_ODT_Entry.delete(0,1000)

        menssage_price=f'Se gastaron {cost}$ con esta acción.\nLa ganacia es de {revenue}$.'
        messagebox.showinfo("Gasto realizado",menssage_price)
    else:
        messagebox.showwarning('Error', 'Favor revisar: \n  1)El código ingresado no existe. \n  2)La cantidad ingresada es mayor a la existente. \n  3)Hay un espacio en blanco.')
#------------------------------------Consumir Inventario-------------------------------------#
def stock_consume(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
    inventarioW.geometry(f'550x150+{width}+{height}')

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

    send_button=tkinter.Button(inventarioW,text='↑ Enviar ↑',command=lambda :stock_consume_validation(consume_code_Entry,consume_quantity_Entry,consume_ODT_Entry))
    send_button.grid(row=3,column=1)

#------------------------Consumir Inventario al público---------------------------------------#
def stock_consume_pub(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8):

    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
    inventarioW.geometry(f'550x150+{width}+{height}')

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

    send_button=tkinter.Button(inventarioW,text='↑ Enviar ↑',command=lambda :stock_consume_validation_pub(consume_code_Entry,consume_quantity_Entry,consume_ODT_Entry))
    send_button.grid(row=3,column=1)

def supplier_validation(supplier_code_Entry,supplier_supplier_Entry,supplier_addres_Entry,supplier_cellphone1_Entry,supplier_cellphone2_Entry,supplier_cellphone3_Entry,supplier_cellphone4_Entry,supplier_cellphone5_Entry,supplier_name1_Entry,supplier_name2_Entry,supplier_name3_Entry,supplier_name4_Entry,supplier_name5_Entry,supplier_email1_Entry,supplier_email2_Entry,supplier_email3_Entry,supplier_email4_Entry,actual_selection):
    code=str(supplier_code_Entry.get())
    supplier=str(supplier_supplier_Entry.get())
    address=str(supplier_addres_Entry.get())
    cellphone1=str(supplier_cellphone1_Entry.get())
    cellphone2=str(supplier_cellphone2_Entry.get())
    cellphone3=str(supplier_cellphone3_Entry.get())
    cellphone4=str(supplier_cellphone4_Entry.get())
    cellphone5=str(supplier_cellphone5_Entry.get())
    name1=str(supplier_name1_Entry.get())
    name2=str(supplier_name2_Entry.get())
    name3=str(supplier_name3_Entry.get())
    name4=str(supplier_name4_Entry.get())
    name5=str(supplier_name5_Entry.get())
    email1=str(supplier_email1_Entry.get())
    email2=str(supplier_email2_Entry.get())
    email3=str(supplier_email3_Entry.get())
    email4=str(supplier_email4_Entry.get())
    today=str(date.today())
    
    option=actual_selection.get()

    dataBase_stock=pd.read_csv('Proveedores.exe',header=0)
    permission=0
    place="NaN"
    lista=dataBase_stock['Codigo']
    if option=="Editar":
        if code in lista.to_list():
            for row in range(len(lista)):      
                if code == lista[row]: 
                    place=row
                    if place != "NaN" and supplier==str(dataBase_stock['Proveedor'][place]):
                        dataBase_movement=pd.read_csv('Proveedores.exe',header=0)
                        dataBase_movement["Direccion"][place]=address
                        dataBase_movement["Telefono 1"][place]=cellphone1
                        dataBase_movement["Telefono 2"][place]=cellphone2
                        dataBase_movement["Telefono 3"][place]=cellphone3
                        dataBase_movement["Telefono 4"][place]=cellphone4
                        dataBase_movement["Telefono 5"][place]=cellphone5
                        dataBase_movement["Nombre 1"][place]=name1
                        dataBase_movement["Nombre 2"][place]=name2
                        dataBase_movement["Nombre 3"][place]=name3
                        dataBase_movement["Nombre 4"][place]=name4
                        dataBase_movement["Nombre 5"][place]=name5
                        dataBase_movement["Correo 1"][place]=email1
                        dataBase_movement["Correo 2"][place]=email2
                        dataBase_movement["Correo 3"][place]=email3
                        dataBase_movement["Correo 4"][place]=email4
                        dataBase_movement["Fecha de Registro"][place]=today
                        dataBase_movement.to_csv('Proveedores.exe', index=0)
                        actual_selection.set("Ninguna")
                        messagebox.showinfo("¡Atención!","La información fué ingresada correctamente.")
                        permission=2
    elif option=="Añadir":
        permission=permission+1
    
    if permission==1:

        dataBase_movement= open("Proveedores.exe","a",encoding="UTF-8")
        dataBase_movement.write(code)
        dataBase_movement.write(",")
        dataBase_movement.write(supplier)
        dataBase_movement.write(",")
        dataBase_movement.write(address)
        dataBase_movement.write(",")
        dataBase_movement.write(cellphone1)
        dataBase_movement.write(",")
        dataBase_movement.write(cellphone2)
        dataBase_movement.write(",")
        dataBase_movement.write(cellphone3)
        dataBase_movement.write(",")
        dataBase_movement.write(cellphone4)
        dataBase_movement.write(",")
        dataBase_movement.write(cellphone5)
        dataBase_movement.write(",")
        dataBase_movement.write(name1)
        dataBase_movement.write(",")
        dataBase_movement.write(name2)
        dataBase_movement.write(",")
        dataBase_movement.write(name3)
        dataBase_movement.write(",")
        dataBase_movement.write(name4)
        dataBase_movement.write(",")
        dataBase_movement.write(name5)
        dataBase_movement.write(",")
        dataBase_movement.write(email1)
        dataBase_movement.write(",")
        dataBase_movement.write(email2)
        dataBase_movement.write(",")
        dataBase_movement.write(email3)
        dataBase_movement.write(",")
        dataBase_movement.write(email4)
        dataBase_movement.write(",")
        dataBase_movement.write(today)
        dataBase_movement.write("\n")
        dataBase_movement.close()
        
        actual_selection.set("Ninguna")
        messagebox.showinfo("¡Atención!","La información fué ingresada correctamente.")
    if permission==0:
        messagebox.showwarning('Error', 'Favor revisar: \n  1)El código ingresado no existe (En caso de estar editando).\n  2)El proveedor ingresado no existe (En caso de estar editando).')
    else:
        supplier_code_Entry.delete(0,1000)
        supplier_supplier_Entry.delete(0,1000)
        supplier_addres_Entry.delete(0,1000)
        supplier_cellphone1_Entry.delete(0,1000)
        supplier_cellphone2_Entry.delete(0,1000)
        supplier_cellphone3_Entry.delete(0,1000)
        supplier_cellphone4_Entry.delete(0,1000)
        supplier_cellphone5_Entry.delete(0,1000)
        supplier_name1_Entry.delete(0,1000)
        supplier_name2_Entry.delete(0,1000)
        supplier_name3_Entry.delete(0,1000)
        supplier_name4_Entry.delete(0,1000)
        supplier_name5_Entry.delete(0,1000)
        supplier_email1_Entry.delete(0,1000)
        supplier_email2_Entry.delete(0,1000)
        supplier_email3_Entry.delete(0,1000)
        supplier_email4_Entry.delete(0,1000)
        actual_selection.set("Ninguna")
    permission=0

#-------------------------------------Proveedores--------------------------------------------#
def supplier(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
    inventarioW.geometry(f'570x400+{width}+{height}')

    supplier_code=tkinter.Label(inventarioW,text='Código')
    supplier_code.grid(row=0,column=0)
    supplier_supplier=tkinter.Label(inventarioW,text='Proveedor')
    supplier_supplier.grid(row=1,column=0)
    supplier_addres=tkinter.Label(inventarioW,text="Dirección")
    supplier_addres.grid(row=2,column=0)
    supplier_cellphone1=tkinter.Label(inventarioW,text="   Número telefónico 1")
    supplier_cellphone1.grid(row=3,column=0)
    supplier_cellphone2=tkinter.Label(inventarioW,text="   Número telefónico 2")
    supplier_cellphone2.grid(row=4,column=0)
    supplier_cellphone3=tkinter.Label(inventarioW,text="   Número telefónico 3")
    supplier_cellphone3.grid(row=5,column=0)
    supplier_cellphone4=tkinter.Label(inventarioW,text="   Número telefónico 4")
    supplier_cellphone4.grid(row=6,column=0)
    supplier_cellphone5=tkinter.Label(inventarioW,text="   Número telefónico 5")
    supplier_cellphone5.grid(row=7,column=0)
    supplier_email1=tkinter.Label(inventarioW,text="   Correo 1")
    supplier_email1.grid(row=8,column=0)
    supplier_email2=tkinter.Label(inventarioW,text="   Correo 2")
    supplier_email2.grid(row=9,column=0)
    supplier_email3=tkinter.Label(inventarioW,text="   Correo 3")
    supplier_email3.grid(row=10,column=0)
    supplier_email4=tkinter.Label(inventarioW,text="   Correo 4")
    supplier_email4.grid(row=11,column=0)
    supplier_name1=tkinter.Label(inventarioW,text="   Nombre")
    supplier_name1.grid(row=3,column=2)
    supplier_name2=tkinter.Label(inventarioW,text="   Nombre")
    supplier_name2.grid(row=4,column=2)
    supplier_name3=tkinter.Label(inventarioW,text="   Nombre")
    supplier_name3.grid(row=5,column=2)
    supplier_name4=tkinter.Label(inventarioW,text="   Nombre")
    supplier_name4.grid(row=6,column=2)
    supplier_name5=tkinter.Label(inventarioW,text="   Nombre")
    supplier_name5.grid(row=7,column=2)

    supplier_code_Entry=tkinter.Entry(inventarioW)
    supplier_code_Entry.grid(row=0,column=1)
    supplier_supplier_Entry=tkinter.Entry(inventarioW)
    supplier_supplier_Entry.grid(row=1,column=1)
    supplier_addres_Entry=tkinter.Entry(inventarioW)
    supplier_addres_Entry.grid(row=2,column=1)
    supplier_cellphone1_Entry=tkinter.Entry(inventarioW)
    supplier_cellphone1_Entry.grid(row=3,column=1)
    supplier_cellphone2_Entry=tkinter.Entry(inventarioW)
    supplier_cellphone2_Entry.grid(row=4,column=1)
    supplier_cellphone3_Entry=tkinter.Entry(inventarioW)
    supplier_cellphone3_Entry.grid(row=5,column=1)
    supplier_cellphone4_Entry=tkinter.Entry(inventarioW)
    supplier_cellphone4_Entry.grid(row=6,column=1)
    supplier_cellphone5_Entry=tkinter.Entry(inventarioW)
    supplier_cellphone5_Entry.grid(row=7,column=1)
    supplier_email1_Entry=tkinter.Entry(inventarioW)
    supplier_email1_Entry.grid(row=8,column=1)
    supplier_email2_Entry=tkinter.Entry(inventarioW)
    supplier_email2_Entry.grid(row=9,column=1)
    supplier_email3_Entry=tkinter.Entry(inventarioW)
    supplier_email3_Entry.grid(row=10,column=1)
    supplier_email4_Entry=tkinter.Entry(inventarioW)
    supplier_email4_Entry.grid(row=11,column=1)
    supplier_name1_Entry=tkinter.Entry(inventarioW)
    supplier_name1_Entry.grid(row=3,column=3)
    supplier_name2_Entry=tkinter.Entry(inventarioW)
    supplier_name2_Entry.grid(row=4,column=3)
    supplier_name3_Entry=tkinter.Entry(inventarioW)
    supplier_name3_Entry.grid(row=5,column=3)
    supplier_name4_Entry=tkinter.Entry(inventarioW)
    supplier_name4_Entry.grid(row=6,column=3)
    supplier_name5_Entry=tkinter.Entry(inventarioW)
    supplier_name5_Entry.grid(row=7,column=3)
    
    actual_selection=tkinter.StringVar(inventarioW)
    actual_selection.set('Ninguna')
    selection=tkinter.StringVar(inventarioW)
    option=['Añadir','Editar']
    selection=tkinter.OptionMenu(inventarioW,actual_selection,*option)
    selection.grid(row=12,column=1)

    send_button=tkinter.Button(inventarioW,text='↑ Enviar ↑',command=lambda :supplier_validation(supplier_code_Entry,supplier_supplier_Entry,supplier_addres_Entry,supplier_cellphone1_Entry,supplier_cellphone2_Entry,supplier_cellphone3_Entry,supplier_cellphone4_Entry,supplier_cellphone5_Entry,supplier_name1_Entry,supplier_name2_Entry,supplier_name3_Entry,supplier_name4_Entry,supplier_name5_Entry,supplier_email1_Entry,supplier_email2_Entry,supplier_email3_Entry,supplier_email4_Entry,actual_selection))
    send_button.grid(row=13,column=1)

#--------------------------------------Ver Proveedores----------------------------------------#
def viewSuppliers(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8):
    cleanOut(add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8)
   
    table=ttk.Treeview(inventarioW,height = 200, columns=18)
    tableScrollBar=ttk.Scrollbar(inventarioW, orient="vertical",command=table.yview)
    table.configure(yscroll=table.set)
    tableScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    tableScrollBarX=ttk.Scrollbar(inventarioW, orient="horizontal",command=table.xview)
    table.configure(xscroll=table.set)
    tableScrollBarX.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    table['columns']=('Codigo','Proveedor','Direccion','Telefono 1','Telefono 2','Telefono 3','Telefono 4','Telefono 5','Nombre 1','Nombre 2','Nombre 3','Nombre 4','Nombre 5','Correo 1','Correo 2','Correo 3','Correo 4','Fecha de Registro')
    table.pack()
    table.heading('#0', text='Código', anchor = 'center' )
    table.column('#0',anchor='center')
    table.heading('#1', text='Proveedor', anchor = 'center' )
    table.column('#1',anchor='center')
    table.heading('#2', text="Direccion", anchor = 'center' )
    table.column('#2',anchor='center')
    table.heading('#3', text='Telefono 1', anchor = 'center' )
    table.column('#3',anchor='center')
    table.heading('#4', text='Telefono 2', anchor = 'center' )
    table.column('#4',anchor='center')
    table.heading('#5', text='Telefono 3', anchor = 'center' )
    table.column('#5',anchor='center')
    table.heading('#6', text='Telefono 4', anchor = 'center' )
    table.column('#6',anchor='center')
    table.heading('#7', text='Telefono 5', anchor = 'center' )
    table.column('#7',anchor='center')
    table.heading('#8', text='Nombre 1', anchor = 'center' )
    table.column('#8',anchor='center')
    table.heading('#9', text='Nombre 2', anchor = 'center' )
    table.column('#9',anchor='center')
    table.heading('#10', text='Nombre 3', anchor = 'center' )
    table.column('#10',anchor='center')
    table.heading('#11', text='Nombre 4', anchor = 'center' )
    table.column('#11',anchor='center')
    table.heading('#12', text='Nombre 5', anchor = 'center' )
    table.column('#12',anchor='center')
    table.heading('#13', text='Correo 1', anchor = 'center' )
    table.column('#13',anchor='center')
    table.heading('#14', text='Correo 2', anchor = 'center' )
    table.column('#14',anchor='center')
    table.heading('#15', text='Correo 3', anchor = 'center' )
    table.column('#15',anchor='center')
    table.heading('#16', text='Correo 4', anchor = 'center' )
    table.column('#16',anchor='center')
    table.heading('#17', text='Fecha de Registro', anchor = 'center' )
    table.column('#17',anchor='center')

    dataBase_stock=pd.read_csv('Proveedores.exe',header=0)
    lista=[]
    parameter=len(dataBase_stock['Codigo'])
    for row in range(parameter):
        for column in dataBase_stock:
            lista.append(dataBase_stock[column][row])
        code=lista[0]
        del lista[0]
        table.insert('','end', text=code, values=(lista))
        lista.clear()

#------------------------------------Función Inventario--------------------------------------#
def inventario():
    inventarioW = tkinter.Tk()
    inventarioW.title('Inventario')
    inventarioW.geometry(f'610x250+{width}+{height}')

    add_item_button=tkinter.Button(inventarioW, text='Añadir Artículo', font='Helvetica 10',bg='light cyan', command = lambda: verification(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    add_item_button.place(relx=0.25,rely=0.25,relwidth=0.25, relheight=0.25)

    delete_item_button=tkinter.Button(inventarioW, text='Consumir Inventario\nPara ODT', font='Helvetica 10',bg='light cyan',command = lambda:stock_consume(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    delete_item_button.place(relx=0.5,rely=0.5,relwidth=0.25, relheight=0.25)

    edit_item_button=tkinter.Button(inventarioW, text='Editar Artículo', font='Helvetica 10',bg="PaleVioletRed",command = lambda: edit_item(add_item_button,delete_item_button,edit_item_button,view_item_button,inventarioW,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    edit_item_button.place(relx=0.25,rely=0.5,relwidth=0.25, relheight=0.25)

    view_item_button=tkinter.Button(inventarioW, text='Ver Stock', font='Helvetica 10',bg="PaleVioletRed", command = lambda: sotckView(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    view_item_button.place(relx=0.5,rely=0.25,relwidth=0.25, relheight=0.25)

    view_item_button5=tkinter.Button(inventarioW, text='Ver Operaciones', font='Helvetica 10',bg='light cyan', command = lambda: actionsView(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    view_item_button5.place(relx=0.5,rely=0,relwidth=0.25, relheight=0.25)

    view_item_button6=tkinter.Button(inventarioW, text='Consumir Inventario\nPara el Público', font='Helvetica 10',bg="PaleVioletRed", command = lambda: stock_consume_pub(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    view_item_button6.place(relx=0.5,rely=0.75,relwidth=0.25, relheight=0.25)

    view_item_button7=tkinter.Button(inventarioW, text='Ver Proveedores', font='Helvetica 10',bg="PaleVioletRed", command = lambda: viewSuppliers(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    view_item_button7.place(relx=0.25,rely=0,relwidth=0.25, relheight=0.25)

    view_item_button8=tkinter.Button(inventarioW, text='Añadir/Editar\nProveedores', font='Helvetica 10',bg='light cyan', command = lambda: supplier(inventarioW,add_item_button,delete_item_button,edit_item_button,view_item_button,view_item_button5,view_item_button6,view_item_button7,view_item_button8))
    view_item_button8.place(relx=0.25,rely=0.75,relwidth=0.25, relheight=0.25)
    