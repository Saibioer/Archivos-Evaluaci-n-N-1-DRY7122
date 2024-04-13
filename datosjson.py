import json

def abrir_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no se encuentra.")

if __name__ == "__main__":
    ruta_archivo = "myfile.json"
    json_file = abrir_json(ruta_archivo)

    if json_file:
        print("Contenido del archivo JSON:")
        print(json_file)
