from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Simulación de base de datos en memoria
class Database:
    products = []
    clients = []

# Modelos Pydantic para validación de datos
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

class Client(BaseModel):
    id: int
    name: str
    email: str

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Rutas para operaciones CRUD de productos
@app.get("/products/", response_model=List[Product])
def get_products():
    return Database.products

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int = Path(..., title="ID del producto que desea obtener")):
    for product in Database.products:
        if product['id'] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.post("/products/", response_model=Product)
def create_product(product: Product):
    Database.products.append(product.dict())
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    for idx, existing_product in enumerate(Database.products):
        if existing_product['id'] == product_id:
            Database.products[idx] = product.dict()
            return product
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int):
    for idx, product in enumerate(Database.products):
        if product['id'] == product_id:
            del Database.products[idx]
            return product
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# Rutas para operaciones CRUD de clientes
@app.get("/clients/", response_model=List[Client])
def get_clients():
    return Database.clients

@app.get("/clients/{client_id}", response_model=Client)
def get_client(client_id: int = Path(..., title="ID del cliente que desea obtener")):
    for client in Database.clients:
        if client['id'] == client_id:
            return client
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.post("/clients/", response_model=Client)
def create_client(client: Client):
    Database.clients.append(client.dict())
    return client

@app.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: int, client: Client):
    for idx, existing_client in enumerate(Database.clients):
        if existing_client['id'] == client_id:
            Database.clients[idx] = client.dict()
            return client
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.delete("/clients/{client_id}", response_model=Client)
def delete_client(client_id: int):
    for idx, client in enumerate(Database.clients):
        if client['id'] == client_id:
            del Database.clients[idx]
            return client
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# Si se ejecuta como script principal, iniciar el servidor con uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
