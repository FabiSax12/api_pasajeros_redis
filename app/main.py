from fastapi import FastAPI

app = FastAPI()

from app.routes.pasajeros import pasajeros

app = FastAPI(
    title="API de Pasajeros",
    description="Consulta de rutas de transporte público",
    version="1.0.0"
)

app.include_router(pasajeros, prefix="/api", tags=["Pasajeros"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Pasajeros Movilizados"}