from fastapi import FastAPI

app = FastAPI(title="SecureShop API")


@app.get("/")
def home():
    return {"message": "Welcome to SecureShop"}


@app.get("/products")
def products():
    return [
        {"id": 1, "name": "Laptop", "price": 75000},
        {"id": 2, "name": "Phone", "price": 45000},
    ] 

@app.get("/search")
def search_product(query: str):
    products = [
        {"id": 1, "name": "Laptop", "price": 75000},
        {"id": 2, "name": "Phone", "price": 45000},
    ]

    results = [
        product for product in products
        if query.lower() in product["name"].lower()
    ]

    return {"results": results}