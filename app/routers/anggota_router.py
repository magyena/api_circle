from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.anggota import Anggota
from app.schemas.anggota import AnggotaCreate, AnggotaOut

router = APIRouter(prefix="/anggota", tags=["Anggota"])


# Dependency untuk dapatkan session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[AnggotaOut])
def list_anggota(db: Session = Depends(get_db)):
    return db.query(Anggota).all()


@router.post("/", response_model=AnggotaOut)
def create_anggota(data: AnggotaCreate, db: Session = Depends(get_db)):
    anggota = Anggota(**data.dict())
    db.add(anggota)
    db.commit()
    db.refresh(anggota)
    return anggota
