from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import person_router, career_router, subject_router, person_career_router, person_subject_router

app = FastAPI()

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir routers
app.include_router(person_router.router, prefix="/persons", tags=["persons"])
app.include_router(career_router.router, prefix="/careers", tags=["careers"])
app.include_router(subject_router.router, prefix="/subjects", tags=["subjects"])
app.include_router(person_career_router.router, prefix="/person-careers", tags=["person-careers"])
app.include_router(person_subject_router.router, prefix="/person-subjects", tags=["person-subjects"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
