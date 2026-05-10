from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

# 🔥 CREAR APP
app = FastAPI(title="Mi API con JWT")

bearer_scheme = HTTPBearer()

# 🔥 IMPORTAR ROUTERS
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
from app.routes.reports_routes import router as reports_router

# 🔥 CORS
origins = [

    "http://localhost:5500",
    "http://127.0.0.1:5500",

    "https://fastapi-code.vercel.app",

    "https://fastapi-code-6c5123yc7-ronnyadriansabalzasobrino-uxs-projects.vercel.app"

]

app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

# 🔥 RUTA BASE
@app.get("/")
def home():

    return {

        "message": "API funcionando correctamente"

    }

# 🔥 INCLUIR ROUTERS
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
app.include_router(reports_router)

# 🔥 CREAR TABLAS
from app.config.db_config import create_tables

create_tables()

# 🔥 EJECUTAR SERVIDOR
if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=10000,
        reload=True
    )