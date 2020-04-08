import tkinter
from Inventario import inventario
window = tkinter.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width =int(((screen_width-450)/2))
height =int(((screen_height-150)/2)-(screen_height/10))
window.geometry(f'450x150+{width}+{height}')
def main():
    window.title("Administración Taionca")

    add_item_button=tkinter.Button(window, text="Inventario", font="Helvetica 10", command = lambda: inventario())
    add_item_button.place(relx=0.25,rely=0.25,relwidth=0.25, relheight=0.25)

    delete_item_button=tkinter.Button(window, text="Soon", font="Helvetica 10")
    delete_item_button.place(relx=0.5,rely=0.5,relwidth=0.25, relheight=0.25)

    edit_item_button=tkinter.Button(window, text="Soon", font="Helvetica 10")
    edit_item_button.place(relx=0.25,rely=0.5,relwidth=0.25, relheight=0.25)

    view_item_button=tkinter.Button(window, text="Soon", font="Helvetica 10")
    view_item_button.place(relx=0.5,rely=0.25,relwidth=0.25, relheight=0.25)
main()

window.mainloop()