from tkinter import *
from tkinter import ttk
import math

def TemaOscuro(*args):
    estilos.configure('mainframe.TFrame', background="#010924")
    
    estilos_label1.configure('label1.TLabel', background="#010924", foreground="white")
    estilos_label2.configure('label2.TLabel', background="#010924", foreground="white")
    
    estilos_botones_numeros.configure('botones_numeros.TButton', background="#00044A", foreground="white")
    estilos_botones_numeros.map('botones_numeros.TButton', background=[('active', '#020A90')])
    
    estilos_botones_borrar.configure('botones_borrar.TButton', background="#010924", foreground="white")
    estilos_botones_borrar.map('botones_borrar.TButton', background=[('active', '#000AB1')])
    
    estilos_botones_restantes.configure('botones_restantes.TButton', background="#010924", foreground="white")
    estilos_botones_restantes.map('botones_restantes.TButton', background=[('active', '#000AB1')])

def TemaClaro(*args):
    estilos.configure('mainframe.TFrame', background="#DBDBDB", foreground="black")
    
    estilos_label1.configure('label1.TLabel', background="#DBDBDB", foreground="black")
    estilos_label2.configure('label2.TLabel', background="#DBDBDB", foreground="black")
    
    estilos_botones_numeros.configure('botones_numeros.TButton', background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map('botones_numeros.TButton', background=[('active', '#B9B9B9')])
    
    estilos_botones_borrar.configure('botones_borrar.TButton', background="#CECECE", foreground="black")
    estilos_botones_borrar.map('botones_borrar.TButton', background=[('active', '#858585')])
    
    estilos_botones_restantes.configure('botones_restantes.TButton', background="#CECECE", foreground="black")
    estilos_botones_restantes.map('botones_restantes.TButton', background=[('active', '#858585')])
    

def IngresarValor(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == "(" or tecla == ")" or tecla == ".":
        entrada2.set(entrada2.get() + tecla)
        
    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-" :
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")
            
        entrada2.set("")
    
    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(str(resultado))#str se ha agregado de forma aleatoria, no es necesario.

def IngresarValoresTeclado(event):
    tecla = str(event.char)
    print(event)#en la consola se muestra la tecla presionada
    
    if tecla >= '0' and tecla <= '9' or tecla == "(" or tecla == ")" or tecla == ".":
        entrada2.set(entrada2.get() + tecla)
        
    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-" :
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")
            
        entrada2.set("")
    
    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(str(resultado))       
def raizCuadrada():
    entrada1.set("")
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(str(resultado))        

def borrar(*args):
    inicio = 0
    final = len(entrada2.get())
    
    entrada2.set(entrada2.get()[inicio:final-1])

def borrarTodo(*args):
    entrada1.set("")
    entrada2.set("")
    
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")  # TF de TFrame en mayúscula
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)



# estilos labels
estilos_label1 = ttk.Style()
estilos_label1.configure('label1.TLabel', font="arial 15", anchor="e")  # Cambiado a 'TLabel'

estilos_label2 = ttk.Style()
estilos_label2.configure('label2.TLabel', font='arial 40', anchor="e")  # Cambiado a 'TLabel'

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style='label1.TLabel')
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))

#estilos para los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('botones_numeros.TButton', font='arial 22', width=5, background="#FFFFFF", relief="flat")

estilos_botones_numeros.map('botones_numeros.TButton', background=[('active', '#B9B9B9')])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('botones_borrar.TButton', font="arial 22",width=5, relief="flat", background="#CECECE")
estilos_botones_borrar.map('botones_borrar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('botones_restantes.TButton', font="arial 22",width=5, relief="flat", background="#CECECE")
estilos_botones_restantes.map('botones_restantes.TButton', background=[('active', '#858585')])
# Definición de los botones
button0 = ttk.Button(mainframe, text="0", style="botones_numeros.TButton", command=lambda:IngresarValor('0'))
button1 = ttk.Button(mainframe, text="1", style="botones_numeros.TButton", command=lambda:IngresarValor('1'))
button2 = ttk.Button(mainframe, text="2", style="botones_numeros.TButton", command=lambda:IngresarValor('2'))
button3 = ttk.Button(mainframe, text="3", style="botones_numeros.TButton", command=lambda:IngresarValor('3'))
button4 = ttk.Button(mainframe, text="4", style="botones_numeros.TButton", command=lambda:IngresarValor('4'))
button5 = ttk.Button(mainframe, text="5", style="botones_numeros.TButton", command=lambda:IngresarValor('5'))
button6 = ttk.Button(mainframe, text="6", style="botones_numeros.TButton", command=lambda:IngresarValor('6'))
button7 = ttk.Button(mainframe, text="7", style="botones_numeros.TButton", command=lambda:IngresarValor('7'))
button8 = ttk.Button(mainframe, text="8", style="botones_numeros.TButton", command=lambda:IngresarValor('8'))
button9 = ttk.Button(mainframe, text="9", style="botones_numeros.TButton", command=lambda:IngresarValor('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="botones_borrar.TButton", command=lambda:borrar())
button_borrar_todo = ttk.Button(mainframe, text="C", style="botones_borrar.TButton", command=lambda:borrarTodo())
button_parentesis1 = ttk.Button(mainframe, text="(", style="botones_restantes.TButton", command=lambda:IngresarValor("("))
button_parentesis2 = ttk.Button(mainframe, text=")", style="botones_restantes.TButton", command=lambda:IngresarValor(")"))
button_punto = ttk.Button(mainframe, text=".", style="botones_restantes.TButton", command=lambda:IngresarValor("."))

button_division = ttk.Button(mainframe, text=chr(247), style="botones_restantes.TButton", command=lambda:IngresarValor("/"))
button_mutliplicacion = ttk.Button(mainframe, text="x", style="botones_restantes.TButton", command=lambda:IngresarValor("*"))
button_resta = ttk.Button(mainframe, text="-", style="botones_restantes.TButton", command=lambda:IngresarValor("-"))
button_suma = ttk.Button(mainframe, text="+", style="botones_restantes.TButton", command=lambda:IngresarValor("+"))

button_igual = ttk.Button(mainframe, text="=", style="botones_restantes.TButton", command=lambda:IngresarValor("="))
button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="botones_restantes.TButton", command=lambda:raizCuadrada())

# Colocar los botones en la pantalla
button_parentesis1.grid(column=0, row=2, sticky=(W,N,E,S))
button_parentesis2.grid(column=1, row=2, sticky=(W,N,E,S))
button_borrar_todo.grid(column=2, row=2, sticky=(W,N,E,S))
button_borrar.grid(column=3, row=2, sticky=(W,N,E,S))

button7.grid(column=0, row=3, sticky=(W,N,E,S))
button8.grid(column=1, row=3, sticky=(W,N,E,S))
button9.grid(column=2, row=3, sticky=(W,N,E,S))
button_division.grid(column=3, row=3, sticky=(W,N,E,S))

button4.grid(column=0, row=4, sticky=(W,N,E,S))
button5.grid(column=1, row=4, sticky=(W,N,E,S))
button6.grid(column=2, row=4, sticky=(W,N,E,S))
button_mutliplicacion.grid(column=3, row=4, sticky=(W,N,E,S))

button1.grid(column=0, row=5, sticky=(W,N,E,S))
button2.grid(column=1, row=5, sticky=(W,N,E,S))
button3.grid(column=2, row=5, sticky=(W,N,E,S))
button_suma.grid(column=3, row=5, sticky=(W,N,E,S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W,N,E,S))
button_punto.grid(column=2, row=6, sticky=(W,N,E,S))
button_resta.grid(column=3, row=6, sticky=(W,N,E,S))

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W,N,E,S))
button_raiz_cuadrada.grid(column=3, row=7, sticky=(W,N,E,S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)
    
root.bind('<KeyPress-o>', TemaOscuro)
root.bind('<KeyPress-c>', TemaClaro)
root.bind('<Key>', IngresarValoresTeclado)
root.bind('<KeyPress-b>', borrar)
root.bind('<KeyPress-d>', borrarTodo)
    
root.mainloop()






