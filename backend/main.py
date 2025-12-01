from fastapi import FastAPI
from routes.create_product_route import router as create_new_product
from routes.get_all_products import router as get_all_products
from routes.get_product_by_id import router as get_product_by_id
from routes.get_filtered_by_date import router as get_filtered_by_date
from routes.get_expiring_in_days import router as products_expiringin

app = FastAPI()

app.include_router(create_new_product)
app.include_router(get_all_products)
app.include_router(get_product_by_id)
app.include_router(get_filtered_by_date)
app.include_router(products_expiringin)


@app.get("/")
def hellorushi():
    return {"msg": 1}
