from fastapi import APIRouter
from controllers.Note_controller import *
from models.Note_model import Note

router = APIRouter()
new_note = NoteController()


@router.post("/notes")
async def create_note(note: Note):
    return new_note.create_note(note)


@router.get("/notes/{id_note}", response_model=Note)
async def get_note(id_note: int):
    return new_note.get_note(id_note)


@router.get("/notes")
async def get_notes():
    return new_note.get_notes()


@router.put("/notes/{id_note}")
async def update_note(id_note: int, note: Note):
    return new_note.update_note(id_note, note)


@router.delete("/notes/{id_note}")
async def delete_note(id_note: int):
    return new_note.delete_note(id_note)