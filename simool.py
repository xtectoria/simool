import tkinter as tk

def iniciar_simulacion():
    print("¡Iniciando la simulación!")
    # Aquí iría la lógica para cargar la siguiente pantalla o iniciar la simulación

def mostrar_tutorial():
    print("Mostrando el tutorial...")
    # Aquí iría la lógica para mostrar la pantalla de tutorial

def salir():
    ventana.destroy()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("simul")
ventana.geometry("400x350")
ventana.configure(bg="#f0f0f0")

# Título principal con fuente moderna
titulo = tk.Label(ventana, text="SimuGraph", font=("Segoe UI", 24, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack(pady=10)

# Canvas para la animación de la caída libre
canvas_ancho = 100
canvas_alto = 100
canvas_caida = tk.Canvas(ventana, width=canvas_ancho, height=canvas_alto, bg="#f0f0f0", highlightthickness=0)
canvas_caida.pack(pady=10)

# Crear la pelota
radio_pelota = 15
pelota = canvas_caida.create_oval(canvas_ancho/2 - radio_pelota, 10, canvas_ancho/2 + radio_pelota, 10 + 2*radio_pelota, fill="orange")

# Función para animar la caída y el rebote
velocidad_y = 5  # Velocidad inicial vertical
gravedad = 0.5
amortiguacion = 1 # Factor de amortiguación para el rebote

def animar_caida():
    global velocidad_y

    coords = canvas_caida.coords(pelota)
    abajo_pelota = coords[3]
    arriba_pelota = coords[1]

    velocidad_y += gravedad
    canvas_caida.move(pelota, 0, velocidad_y)

    if abajo_pelota > canvas_caida.winfo_height():
        velocidad_y = -velocidad_y * amortiguacion
        # Evitar que la pelota se atasque ligeramente debajo
        canvas_caida.coords(pelota, coords[0], canvas_caida.winfo_height() - 2 * radio_pelota, coords[2], canvas_caida.winfo_height())
    elif arriba_pelota < 0 and velocidad_y < 0: # Si golpea el techo
        velocidad_y = -velocidad_y * amortiguacion
        canvas_caida.coords(pelota, coords[0], 0, coords[2], 2 * radio_pelota)

    ventana.after(30, animar_caida) # Intervalo más corto para una animación más fluida

animar_caida()

# Botones del menú
boton_iniciar = tk.Button(ventana, text="Nueva Simulación", command=iniciar_simulacion, width=20, height=2, bg="#4CAF50", fg="white", font=("Segoe UI", 10))
boton_iniciar.pack(pady=5)

boton_tutorial = tk.Button(ventana, text="Tutorial", command=mostrar_tutorial, width=20, height=2, bg="#2196F3", fg="white", font=("Segoe UI", 10))
boton_tutorial.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=salir, width=20, height=2, bg="#f44336", fg="white", font=("Segoe UI", 10))
boton_salir.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()