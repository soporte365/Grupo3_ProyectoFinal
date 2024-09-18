from fastapi import FastAPI

# from app.v1.database.db import get_db
from app.v1.router import usuario
from app.v1.router.transaccion import router as transaccion_router
from app.v1.router.pais import router as pais_router
from app.v1.router.emisor_receptor import router as emisor_receptor_router
from app.v1.router.transaccion_cliente import router as transaccion_cliente_router
from app.v1.router.mensaje import router as mensaje_router
from app.v1.router.transaccion_resumen import router as transaccion_resumen_router
from app.v1.services.middlewar import TimingMiddleware

app = FastAPI()
app.add_middleware(TimingMiddleware)
app.include_router(usuario.router)
app.include_router(transaccion_router)
app.include_router(pais_router)
app.include_router(emisor_receptor_router)
app.include_router(transaccion_cliente_router)
app.include_router(mensaje_router)
app.include_router(transaccion_resumen_router)


@app.get("/")
def read_root():
    integrantes = ["Carlos Torres", "Jose Figuera", "Rafael Perez"]
    return {
        "mensaje": "Bienvenido al proyecto Final FastApi",
        "integrantes": integrantes,
    }



