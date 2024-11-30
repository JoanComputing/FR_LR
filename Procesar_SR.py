import os
import cv2
import numpy as np
from sr import make_model

# Rutas de las carpetas
input_dir = "tinyface"
output_dir = "tinyface_sr"

# Crear el modelo de superresolución
model = make_model()

def apply_super_resolution(input_path, output_path):
    """
    Aplica superresolución a una imagen y la guarda en el directorio de salida.
    """
    img = cv2.imread(input_path)
    if img is None:
        print(f"No se pudo leer la imagen: {input_path}")
        return
    
    # Convertir la imagen a RGB
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Normalizar la imagen
    image_normalized = (image_rgb - 127.5) / 127.5
    # Aplicar el modelo de superresolución
    image_upsampled = model.upscale_image(image_normalized)[0]
    # Desnormalizar y convertir a uint8
    image_upsampled = (image_upsampled * 127.5 + 127.5).numpy().astype(np.uint8)
    # Guardar la imagen procesada en la ruta de salida
    cv2.imwrite(output_path, cv2.cvtColor(image_upsampled, cv2.COLOR_RGB2BGR))

def process_directory(input_dir, output_dir):
    """
    Procesa recursivamente un directorio, aplicando superresolución a todas las imágenes.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, dirs, files in os.walk(input_dir):
        # Crear la estructura de carpetas en el directorio de salida
        relative_path = os.path.relpath(root, input_dir)
        output_subdir = os.path.join(output_dir, relative_path)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)
        
        # Procesar imágenes
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_subdir, file)
                print(f"Procesando: {input_path} -> {output_path}")
                apply_super_resolution(input_path, output_path)

# Aplicar el procesamiento al dataset completo
process_directory(input_dir, output_dir)

print("Proceso de superresolución completado.")
