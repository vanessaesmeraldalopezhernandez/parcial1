#Crea una aplicación en Python que permita gestionar una base de datos de productos varios.//
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["productos"]
collection = db["varios"]

#La aplicación debe permitir insertar, actualizar y eliminar productos.//

varios = {
    "nombre": "azucar",
    "precio": 3.50,
    "fecha de vencimiento": "12/09/2024"
}
resultado = collection.insert_one(varios)
print(resultado.inserted_id)

resultado = collection.update_one({"nombre": "palomitas", "precio": 2.00},
{"$set":{"nombre": "palomitas de queso","precio":2.75}})
print(resultado.modified_count)

resultado = collection.delete_one({"nombre": "palomitas de queso", "precio": 2.00})
print(resultado.deleted_count)

documentos = collection.find()
for documento in documentos:
    print(documento)

#La aplicación debe permitir consultar un producto en particular por su nombre//
db.collection.find({"nombre": "palomitas de queso"})
db.collection.find({"precio": 2.75})

documentos = collection.find()
for documento in documentos:
    print(documento)




