from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AnggotaBase(BaseModel):
    nama_lengkap: str
    nik: str
    email: Optional[str] = None
    no_wa: Optional[str] = None
    alamat: Optional[str] = None
    kelurahan: Optional[str] = None
    kecamatan: Optional[str] = None
    kabupaten: Optional[str] = None
    provinsi: Optional[str] = None
    kodepos: Optional[str] = None
    pekerjaan: Optional[str] = None
    jenis_kelamin: Optional[str] = None
    foto_url: Optional[str] = None


class AnggotaCreate(AnggotaBase):
    pass


class AnggotaOut(AnggotaBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
