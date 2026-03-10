from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# todos los routers
from routes.Programs_routes import router as programs_router
from routes.Semesters_routes import router as semesters_router
from routes.Students_routes import router as students_router
from routes.Teacher_routes import router as teacher_router
from routes.Users_routes import router as users_router
from routes.Subjects_routes import router as subjects_router
from routes.Teacher_subject_routes import router as teacher_subject_router
from routes.Student_subject_routes import router as student_subject_router
from routes.Note_routes import router as note_router
from routes.Assists_routes import router as assists_router
from routes.Alerts_routes import router as alerts_router
from routes.Followups_routes import router as followups_router
from routes.Periods_routes import router as periods_router

app = FastAPI()

origins = [
    "https://ep-square-flower-aiq3n3y4-pooler.c-4.us-east-1.aws.neon.tech",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# todos los routers
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)