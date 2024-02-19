from tkinter import *
from tkinter import filedialog # modulo necesario para abrir y guardar documentos

o_root=Tk()

def AbreFichero():

   v_fichero=filedialog.askopenfilename(title="Abrir'7421+", initialdir="C:", filetypes=(("ficherosss pdf","*.pdf"),
      ("Ficheros textooo","*.txt"),("todoo ficheroo","*.*")))
   
   print(v_fichero) # debuelve la direccion del fichero

Button(o_root, text="abrir un fichero", command=AbreFichero).pack()

o_root.mainloop()