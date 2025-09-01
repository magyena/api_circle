from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from app.database import Base


class Anggota(Base):
    __tablename__ = "anggota"

    id = Column(Integer, primary_key=True, index=True)
    nama_lengkap = Column(String, nullable=False)
    nik = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=True)
    no_wa = Column(String, nullable=True)
    alamat = Column(Text, nullable=True)
    kelurahan = Column(String, nullable=True)
    kecamatan = Column(String, nullable=True)
    kabupaten = Column(String, nullable=True)
    provinsi = Column(String, nullable=True)
    kodepos = Column(String, nullable=True)
    pekerjaan = Column(String, nullable=True)
    jenis_kelamin = Column(String, nullable=True)
    foto_url = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
