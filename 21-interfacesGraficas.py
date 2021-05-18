#   Capítulo 21: Interfaces gráficas con tkinter
#   Apartado 1: Conceptos básicos de tkinter
import tkinter as tk

#   Tkinter funciona mediante Widgets. Los Widgets son
#   elementos predefinidos que podemos ir incrustando 
#   en nuestra aplicación. 
#   Por ejemplo, un botón, un input de texto, etcétera.
#   De hecho, la ventana principal de la aplicación 
#   es un widget. 

#   Colores: '#00a8e8'
palabras = "Dale like y suscríbete".split()
count = 0

root = tk.Tk()
palabra = tk.StringVar(root)
entrada = tk.StringVar(root)

root.configure(background="black")
tk.Wm.wm_title(root, "Hola Tkinter")

def cambiarPalabra():
    palabra.set("Suscríbete " + entrada.get())


tk.Button(
    root, 
    text = "Click Me",
    bg = '#00a8e8',
    fg = 'white',
    relief = 'flat',
    command = cambiarPalabra).pack(fill = tk.BOTH, expand = True)

tk.Label(root, textvariable = palabra, fg = 'white', bg = 'black').pack(fill = tk.BOTH, expand = True)

tk.Entry(root, textvariable = entrada, fg = 'white', bg = 'black', justify = 'center').pack(fill = tk.BOTH, expand = True)

root.mainloop()