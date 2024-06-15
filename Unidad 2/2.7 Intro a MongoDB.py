from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mi_base_de_datos"]
coleccion = db["mi_coleccion"]

# 1. Inserción de documentos
def insertar_documentos():
    documentos = [
        {"nombre": "Juan", "edad": 28, "ciudad": "Madrid"},
        {"nombre": "Ana", "edad": 22, "ciudad": "Barcelona"},
        {"nombre": "Luis", "edad": 35, "ciudad": "Valencia"}
    ]
    resultado = coleccion.insert_many(documentos)
    print(f"Documentos insertados con los IDs: {resultado.inserted_ids}")

# 2. Lectura de documentos
def leer_documentos():
    documentos = coleccion.find()
    for doc in documentos:
        print(doc)

# 3. Actualización de documentos
def actualizar_documento(documento_id, nuevos_valores):
    resultado = coleccion.update_one({"_id": ObjectId(documento_id)}, {"$set": nuevos_valores})
    if resultado.matched_count:
        print(f"Documento con ID {documento_id} actualizado.")
    else:
        print(f"No se encontró el documento con ID {documento_id}.")

# 4. Eliminación de documentos
def eliminar_documento(documento_id):
    resultado = coleccion.delete_one({"_id": ObjectId(documento_id)})
    if resultado.deleted_count:
        print(f"Documento con ID {documento_id} eliminado.")
    else:
        print(f"No se encontró el documento con ID {documento_id}.")

# Ejemplo de uso
if __name__ == "__main__":
    print("Insertando documentos...")
    insertar_documentos()

    print("\nLeyendo documentos...")
    leer_documentos()

    print("\nActualizando documento...")
    # Reemplaza el ID con un ID válido de tu colección
    id_documento = "666df501dd2c9b64886a91ed"  # Usa un ObjectId válido
    nuevos_valores = {"edad": 30}
    actualizar_documento(id_documento, nuevos_valores)

    print("\nLeyendo documentos actualizados...")
    leer_documentos()

    print("\nEliminando documento...")
    # Reemplaza el ID con un ID válido de tu colección
    id_documento_a_eliminar = "666df501dd2c9b64886a91ef"  # Usa un ObjectId válido
    eliminar_documento(id_documento_a_eliminar)

    print("\nLeyendo documentos restantes...")
    leer_documentos()
