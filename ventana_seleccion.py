import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def abrir_ventana_seleccion(parent):
    ventana_seleccion = tk.Toplevel(parent)
    ventana_seleccion.title("Selecciona una Simulación")
    ventana_seleccion.resizable(False, False) # Opcional: Evita que se redimensione

    def cerrar_ventana_seleccion():
        ventana_seleccion.destroy()
        parent.destroy()

    ventana_seleccion.protocol("WM_DELETE_WINDOW", cerrar_ventana_seleccion)

    fenomenos_imagenes = [
        ("Movimiento de Proyectiles", "imagenes/proyectiles.png"),
        ("Caída Libre", "imagenes/caida_libre.png"),
        ("Movimiento Armónico Simple", "imagenes/armonico.png"),
        ("Colisiones", "imagenes/colisiones.png"),
        # Añade más fenómenos e imágenes aquí
    ]

    def seleccionar_fenomeno(fenomeno):
        print(f"Simulación seleccionada: {fenomeno}")
        # Aquí iría la lógica para cargar la interfaz de la simulación del fenómeno seleccionado

    def volver_a_principal():
        ventana_seleccion.destroy()
        parent.deiconify()

    num_columnas = 2
    fila_actual = 0
    columna_actual = 0

    for fenomeno, ruta_imagen in fenomenos_imagenes:
        card_frame = ttk.Frame(ventana_seleccion, padding=5, borderwidth=1, relief="solid") # Marco para la "card" con borde
        card_frame.grid(row=fila_actual, column=columna_actual, padx=10, pady=10, sticky="nsew")

        try:
            imagen_pil = Image.open(ruta_imagen).resize((100, 100))
            imagen_tk = ImageTk.PhotoImage(imagen_pil)
            boton_fenomeno = ttk.Button(
                card_frame,
                image=imagen_tk,
                command=lambda f=fenomeno: seleccionar_fenomeno(f)
            )
            boton_fenomeno.image = imagen_tk
            boton_fenomeno.pack() # Empaqueta el botón dentro del frame

            etiqueta_fenomeno = ttk.Label(card_frame, text=fenomeno, anchor="center")
            etiqueta_fenomeno.pack(pady=5) # Empaqueta la etiqueta debajo del botón

        except FileNotFoundError as e:
            print(f"Error al cargar imagen en selección: {e}")
            etiqueta_error = ttk.Label(card_frame, text=f"Imagen no encontrada: {fenomeno}")
            etiqueta_error.pack(padx=5, pady=5)

        columna_actual += 1
        if columna_actual >= num_columnas:
            columna_actual = 0
            fila_actual += 1

    boton_volver = ttk.Button(ventana_seleccion, text="Volver", command=volver_a_principal)
    boton_volver.grid(row=fila_actual + 1, column=0, columnspan=num_columnas, padx=10, pady=10, sticky="ew")