from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal, engine, Base
from app.models.anggota import Anggota
from app.schemas.anggota import AnggotaOut
from app.routers import anggota_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(title="API Komunitas")

app.include_router(anggota_router.router)


@app.get("/")
def root():
    return {"message": "API Komunitas 🚀"}


from fastapi import FastAPI
from app.routers import anggota_router

app = FastAPI(title="API Komunitas")

app.include_router(anggota_router.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "API Komunitas 🚀"}


# Endpoint GET semua anggota
@app.get("/anggota", response_model=List[AnggotaOut])
def get_all_anggota(db: Session = Depends(get_db)):
    anggota_list = db.query(Anggota).all()
    return anggota_list
