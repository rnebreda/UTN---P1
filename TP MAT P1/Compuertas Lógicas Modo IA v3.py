import tkinter as tk

def dibujar_AND_tkinter():
    ventana = tk.Tk()
    ventana.title("Compuerta AND")
    canvas = tk.Canvas(ventana, width=200, height=100, bg='white')
    canvas.pack()

    # Dibuja el cuerpo de la compuerta AND
    canvas.create_rectangle(50, 20, 100, 80, outline="black", fill="lightgray")
    # Dibuja la parte curva (usando un arco grande y rellenando)
    canvas.create_arc(60, 20, 140, 80, start=-90, extent=180, outline="black", style=tk.ARC)
    
    # Entradas y salidas
    canvas.create_line(10, 40, 50, 40, arrow=tk.LAST)
    canvas.create_line(10, 60, 50, 60, arrow=tk.LAST)
    canvas.create_line(140, 50, 180, 50, arrow=tk.LAST)

    tk.Label(ventana, text="Compuerta AND", bg='white').place(x=70, y=85)
    ventana.mainloop()

dibujar_AND_tkinter()
