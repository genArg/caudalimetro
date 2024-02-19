from tkinter import *
from tkinter import messagebox # las ventanas emergente no pertenecen a la librebreria estandard de tkinter

o_root=Tk()

## funcion que presenta la ventana emergente
def InfoAdicional():
   messagebox.showinfo("procesador de pablo", "procesador de texto")

def InfoLicencia():
   messagebox.showwarning("procesador de pablo", "procesador de texto")

def SalirApp():
   valor=messagebox.askquestion("salir","desea salir") # debuelve yes o no

   if valor=="yes":
      o_root.destroy() # comando que cierra la ventana

def CerrarApp():
   valor=messagebox.askokcancel("salir","desea salir") # debuelve True o False

   if (valor):
      o_root.destroy() # comando que cierra la ventana

def ReintentarApp():
   valor=messagebox.askretrycancel("salir","desea salir") # debuelve True o False

   if(not valor):
      o_root.destroy() # comando que cierra la ventana


o_barra_menu=Menu(o_root) # crea el menu

## añado el munu a la vantana
o_root.config(menu=o_barra_menu, width=300, height=300)

m_menu1=Menu(o_barra_menu, tearoff=0) # crea una opcion en el menu, y elimina una linea por defecto
m_menu1.add_command(label="submenu 1.1_licencia", command=InfoLicencia) # añade una opcion dentro de la opcion menu1
m_menu1.add_command(label="submenu 1.2_salir", command=SalirApp)
m_menu1.add_separator() # añade un separador
m_menu1.add_command(label="submenu 1.3_cerrar", command=CerrarApp)

m_menu2=Menu(o_barra_menu) # crea una opcion en el menu
m_menu2.add_command(label="2.1_info_adicional", command=InfoAdicional)
m_menu2.add_command(label="2.2_reintentar", command=ReintentarApp)

## añade los menus creados a la barra de herramienta con un nombre
o_barra_menu.add_cascade(label="menu 1", menu=m_menu1)
o_barra_menu.add_cascade(label="menu 2", menu=m_menu2)


o_root.mainloop()