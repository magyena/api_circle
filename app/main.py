from fastapi import FastAPI
from app.routers import anggota_router

app = FastAPI(title="API Komunitas")

app.include_router(anggota_router.router)


@app.get("/")
def root():
    return {"message": "API Komunitas 🚀"}
