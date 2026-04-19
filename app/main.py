from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

# crear app
app = FastAPI(title="Mi API con JWT")

bearer_scheme = HTTPBearer()

# importar routers
from app.routes.Programs_routes import router as programs_router
from app.routes.Semesters_routes import router as semesters_router
from app.routes.Students_routes import router as students_router
from app.routes.Teacher_routes import router as teacher_router
from app.routes.Users_routes import router as users_router
from app.routes.Subjects_routes import router as subjects_router
from app.routes.Teacher_subject_routes import router as teacher_subject_router
from app.routes.Student_subject_routes import router as student_subject_router
from app.routes.Note_routes import router as note_router
from app.routes.Assists_routes import router as assists_router
from app.routes.Alerts_routes import router as alerts_router
from app.routes.Followups_routes import router as followups_router
from app.routes.Periods_routes import router as periods_router

# CORS
origins = [
    "https://alertas-backend.onrender.com",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://fastapi-code.vercel.app"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ruta base
@app.get("/")
def home():
    return {"message": "API funcionando correctamente"}

@app.get("/public/alerts")
def get_alerts_public():
    return get_alerts_public()

# incluir routers
app.include_router(programs_router)
app.include_router(semesters_router)
app.include_router(students_router)
app.include_router(teacher_router)
app.include_router(users_router)
app.include_router(subjects_router)
app.include_router(teacher_subject_router)
app.include_router(student_subject_router)
app.include_router(note_router)
app.include_router(assists_router)
app.include_router(alerts_router)
app.include_router(followups_router)
app.include_router(periods_router)

# crear tablas si no existen
from app.config.db_config import create_tables
create_tables()

# ejecutar servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=10000, reload=True)