from tkinter import *

o_root=Tk()

v_opcion_uno=IntVar()
v_opcion_dos=IntVar()
v_opcion_tres=IntVar()

def MiMetodo():
   v_opcion_elegida=""

   if(v_opcion_uno.get()==1):
      v_opcion_elegida+=" opcion 1"

   if(v_opcion_dos.get()==1):
      v_opcion_elegida+=" opcion 2"
      
   if(v_opcion_tres.get()==1):
      v_opcion_elegida+=" opcion 3"
   
   o_etiqueta_final.config(text=v_opcion_elegida)


Checkbutton(o_root, text="opcion 1", variable=v_opcion_uno, onvalue=1, offvalue=0, command=MiMetodo).pack()
Checkbutton(o_root, text="opcion 2", variable=v_opcion_dos, onvalue=1, offvalue=0, command=MiMetodo).pack()
Checkbutton(o_root, text="opcion 3", variable=v_opcion_tres, onvalue=1, offvalue=0, command=MiMetodo).pack()

o_etiqueta_final=Label(o_root)
o_etiqueta_final.pack()

o_root.mainloop()