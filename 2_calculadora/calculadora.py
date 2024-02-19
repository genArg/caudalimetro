from tkinter import *

## define la ventana y el frame principal
o_calculadora=Tk()

o_frame=Frame(o_calculadora)
o_frame.pack()

## Defino variables globales
v_operacion="" # valor inicial vacio
v_resultado=0 # variable para almacenar el resultado de la operacion anterior

## define la pantalla
v_pantalla=StringVar()
o_pantalla=Entry(o_frame, textvariable=v_pantalla)
o_pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4) # columnspan define cuantas culumas ocupara
o_pantalla.config(background="black", fg="white", justify="right")

## metodos de la calculadora
def Metodo0(caracter):
   global v_operacion

   if v_operacion!="":
      v_pantalla.set(caracter)
      v_operacion=""
   else:
      v_pantalla.set(v_pantalla.get() + caracter)

def MetodoOperacion(caracter):
   global v_operacion
   global v_resultado

   v_resultado+=int(v_pantalla.get())
   v_operacion=caracter
   
   print(v_operacion)


# definimos los botones
o_boton_7=Button(o_frame,text="7", width=3, command=lambda:Metodo0("7"))
o_boton_7.grid(row=2,column=1)
o_boton_8=Button(o_frame,text="8", width=3, command=lambda:Metodo0("8"))
o_boton_8.grid(row=2,column=2)
o_boton_9=Button(o_frame,text="9", width=3, command=lambda:Metodo0("9"))
o_boton_9.grid(row=2,column=3)
o_boton_mult=Button(o_frame,text="x", width=3, command=lambda:MetodoOperacion("x"))
o_boton_mult.grid(row=2,column=4)

o_boton_4=Button(o_frame,text="4", width=3, command=lambda:Metodo0("4"))
o_boton_4.grid(row=3,column=1)
o_boton_5=Button(o_frame,text="5", width=3, command=lambda:Metodo0("5"))
o_boton_5.grid(row=3,column=2)
o_boton_6=Button(o_frame,text="6", width=3, command=lambda:Metodo0("6"))
o_boton_6.grid(row=3,column=3)
o_boton_div=Button(o_frame,text="/", width=3, command=lambda:MetodoOperacion("/"))
o_boton_div.grid(row=3,column=4)

o_boton_1=Button(o_frame,text="1", width=3, command=lambda:Metodo0("1"))
o_boton_1.grid(row=4,column=1)
o_boton_2=Button(o_frame,text="2", width=3, command=lambda:Metodo0("2"))
o_boton_2.grid(row=4,column=2)
o_boton_3=Button(o_frame,text="3", width=3, command=lambda:Metodo0("3"))
o_boton_3.grid(row=4,column=3)
o_boton_suma=Button(o_frame,text="+", width=3, command=lambda:MetodoOperacion("+"))
o_boton_suma.grid(row=4,column=4)

o_boton_punto=Button(o_frame,text=".", width=3, command=lambda:Metodo0("."))
o_boton_punto.grid(row=5,column=1)
o_boton_0=Button(o_frame,text="0", width=3, command=lambda:Metodo0("0"))
o_boton_0.grid(row=5,column=2)
o_boton_igual=Button(o_frame,text="=", width=3, command=lambda:MetodoOperacion("="))
o_boton_igual.grid(row=5,column=3)
o_boton_resta=Button(o_frame,text="-", width=3, command=lambda:MetodoOperacion("-"))
o_boton_resta.grid(row=5,column=4)


## Inicia el bucle principal
o_calculadora.mainloop()