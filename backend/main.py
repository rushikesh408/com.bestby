from fastapi import FastAPI
from routes.create_product_route import router as create_new_product

app = FastAPI()

app.include_router(create_new_product)


@app.get("/")
def hellorushi():
    return {"msg": 1}
