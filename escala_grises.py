import tkinter as tk #Exportamos la biblioteca para la interfaz
from tkinter import filedialog
from PIL import Image, ImageTk #Exportar para poder manipular imagenes

# Variable global para almacenar la imagen cargada
imagen_cargada = None

# Funciones de algoritmos
def grayscale_promedio_pixel(r, g, b):
    return (r + g + b) // 3 #Obtiene el promedio de la intensidad de los colores

def grayscale_tonalidad_pixel(r, g, b):
    return (max(r, g, b) + min(r, g, b)) // 2 #Hace el promedio entre el máximo y el mínimo

def grayscale_luminosidad_pixel(r, g, b):
    return int(0.21*r + 0.72*g + 0.07*b) #Calcula un promedio ponderado para obtener un gris que parezca más natural visualmente

def aplicar_algoritmo(algoritmo):
    global imagen_cargada
    if imagen_cargada:
        ancho, alto = imagen_cargada.size # Obtiene el ancho y alto de la imagen en pixeles
        # L indica que la imagen sera en escala de grises, donde cada píxel es un valor de 0 a 255
        nueva_img = Image.new("L", (ancho, alto))  # Imagen en escala de grises
        

        for y in range(alto):
            for x in range(ancho):
                r, g, b = imagen_cargada.getpixel((x, y))
                gris = algoritmo(r, g, b) # Llama a la funcion algoritmo que pasamos como parametro
                nueva_img.putpixel((x, y), gris)

        # Convertir a RGB para que Tkinter la muestre correctamente
        nueva_img = nueva_img.convert("RGB")

        # Mostrar la nueva imagen
        mostrar_imagen(nueva_img)

def mostrar_imagen(img):
    """Escala y muestra la imagen en el label"""
    img_mostrar = img.resize((300, 200))
    img_tk = ImageTk.PhotoImage(img_mostrar)
    lbl_imagen.config(image=img_tk)
    lbl_imagen.image = img_tk
    

# Funcion para cargar imagen
def cargar_imagen():
    global imagen_cargada, btn_cargar
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if ruta:
        img = Image.open(ruta)
        imagen_cargada = img.convert("RGB")  #IMPORTANTE tranformar la imagen a RGB

        mostrar_imagen(imagen_cargada)

        # Desaparecer boton de cargar imagen
        btn_cargar.pack_forget()

        # Mostrar los botones de algoritmos
        btn_promedio.pack(side="left", padx=10)
        btn_tonalidad.pack(side="left", padx=10)
        btn_luminosidad.pack(side="left", padx=10)

# Interfaz Tkinter
root = tk.Tk()
root.geometry("600x400")
root.title("Prueba")

# Contenedor principal
Contenedor = tk.Frame(root, bg="grey")
Contenedor.pack(expand=True, fill="both", pady=20)

# Frame para botones
frame_botones = tk.Frame(Contenedor, bg="lightgray", height=50)
frame_botones.pack(fill="x", pady=10)

# Boton para cargar imagen
btn_cargar = tk.Button(frame_botones, text="Cargar imagen", command=cargar_imagen)
btn_cargar.pack(side="left", padx=10)

# Botones de algoritmos (inicialmente ocultos)
btn_promedio = tk.Button(frame_botones, text="Promedio", command=lambda: aplicar_algoritmo(grayscale_promedio_pixel))
btn_tonalidad = tk.Button(frame_botones, text="Tonalidad", command=lambda: aplicar_algoritmo(grayscale_tonalidad_pixel))
btn_luminosidad = tk.Button(frame_botones, text="Luminosidad", command=lambda: aplicar_algoritmo(grayscale_luminosidad_pixel))

# Contenedor para la imagen
lbl_imagen = tk.Label(Contenedor, bg="white")
lbl_imagen.pack(pady=20)

root.mainloop()
