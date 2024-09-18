from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.v1.database.db import get_db
from app.v1.models import model
from app.v1.models.model import Tasas as TasaModel
from app.v1.schema.schema_tasa import Tasa

router = APIRouter(
    prefix="/tasas",  # Prefijo para todas las rutas de usuarios
    tags=["Tasas"]    # Etiqueta para agrupar las rutas en la documentación de Swagger
)

# regresa todas las tasas registradas
@router.get("/all")
def get_tasa(db: Session = Depends(get_db)):
    tasa = db.query(model.Tasas).all()
    return tasa

# crea una nueva tasa
@router.post("/ create", response_model=Tasa)
def create_tasas(tasas: Tasa, db: Session = Depends(get_db)):
    db_tasa = model.Tasas(**tasas.dict())
    db.add(db_tasa)
    db.commit()
    db.refresh(db_tasa)
    return db_tasa


@router.get("/{id}", response_model=Tasa)  # Usa el esquema Pydantic
def get_tasa_id(id: int, tasas: Tasa, db: Session = Depends(get_db)):
    """Obtener detalles de una tasa específica por su ID."""
    db_tasa = db.query(TasaModel).filter(TasaModel.id_transaccion == id).first()
    if tasas is None:
        raise HTTPException(status_code=404, detail="Tasa no encontrada")
    return tasas

@router.put("/{id}", response_model=Tasa)
def update_tasas(id: int, tasas: Tasa, db: Session = Depends(get_db)):
    """Actualizar una tasa específica por su ID."""
    db_tasa = db.query(TasaModel).filter(TasaModel.id_tasa == id).first()
    if db_tasa is None:
        raise HTTPException(status_code=404, detail="Tasa no encontrada")

    for key, value in tasas.dict(exclude_unset=True).items():
        setattr(db_tasa, key, value)

    db.commit()
    db.refresh(db_tasa)
    return db_tasa
