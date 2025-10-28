from fastapi import APIRouter, HTTPException
from typing import List
from app.models.ruta_model import RutaModel
from app.db.mongo import db

pasajeros = APIRouter(
    prefix="/pasajeros",
    tags=["Pasajeros"]
)

@pasajeros.get("/", response_model=List[RutaModel])
async def obtener_rutas():
    """Obtiene todas las rutas desde MongoDB."""
    try:
        rutas = await db.passengers.find().to_list(1000)
        return rutas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@pasajeros.get("/{codigo_ruta}", response_model=RutaModel)
async def obtener_ruta_por_codigo(codigo_ruta: str):
    """Obtiene una ruta específica según su código."""
    ruta = await db.passengers.find_one({"codigo_ruta": codigo_ruta})
    if ruta:
        return ruta
    raise HTTPException(status_code=404, detail="Ruta no encontrada")