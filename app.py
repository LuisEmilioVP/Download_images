import os
import shutil
import threading
import json

def copiar_imagen(ruta_origen, ruta_destino, nombre_archivo):
    # Copiar el archivo desde la ruta de origen a la ubicación deseada
    shutil.copy(ruta_origen, ruta_destino)
    print(f"Copiada: {nombre_archivo}")
    return nombre_archivo

def main():
    # Obtener lista de archivos en el directorio local_Images
    archivos = os.listdir("local_Images")
    # Lista para mantener los hilos
    hilos = []
    nombres_archivos = []
    for archivo in archivos:
        # Procesar solo archivos de imagen
        if archivo.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            ruta_origen = os.path.join("local_Images", archivo)  # Ruta de origen del archivo local
            ruta_destino = os.path.join(os.path.dirname(__file__), archivo)  # Ruta de destino en el directorio actual
            # Crear un hilo para cada copia de imagen
            t = threading.Thread(target=copiar_imagen, args=(ruta_origen, ruta_destino, archivo))
            t.start()
            hilos.append(t)
            nombres_archivos.append(archivo)
    
    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Registra los nombres de los archivos copiados en un archivo JSON
    with open('descargas.json', 'w') as json_file:
        json.dump(nombres_archivos, json_file, indent=4)  # Indentación para que sea legible

if __name__ == "__main__":
    main()
