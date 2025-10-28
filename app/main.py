import asyncio
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

app = FastAPI()

from app.cache.redis import check_redis_connection
from app.routes.pasajeros import pasajeros

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    await check_redis_connection()
    yield
    # Shutdown code
    await app.state.redis_client.close() 

app = FastAPI(
    title="API de Pasajeros",
    description="Consulta de rutas de transporte público",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(pasajeros, prefix="/api", tags=["Pasajeros"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Pasajeros Movilizados"}