import os
import pandas as pd

def listar_imagenes_a_excel(ruta_carpeta, nombre_archivo_excel):
    # Extensiones de imagen comunes
    extensiones_validas = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    
    try:
        # Obtener lista de archivos en la carpeta
        archivos = os.listdir(ruta_carpeta)
        
        # Filtrar solo los que son imágenes
        imagenes = [f for f in archivos if f.lower().endswith(extensiones_validas)]
        
        # Crear un DataFrame de Pandas
        df = pd.DataFrame(imagenes, columns=['Nombre del Archivo'])
        
        # Agregar una columna con la ruta completa (opcional pero recomendado)
        df['Ruta Completa'] = [os.path.join(ruta_carpeta, img) for img in imagenes]
        
        # Guardar a Excel
        df.to_excel(nombre_archivo_excel, index=False)
        print(f"Éxito: Se han listado {len(imagenes)} imágenes en '{nombre_archivo_excel}'.")
        
    except FileNotFoundError:
        print("Error: La carpeta especificada no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Configuración ---
# Cambia 'C:/MisImagenes' por la ruta de tu carpeta en Costa Rica
ruta_de_mi_carpeta = './misimagenes' 
nombre_salida = 'Lista_de_Imagenes.xlsx'

listar_imagenes_a_excel(ruta_de_mi_carpeta, nombre_salida)