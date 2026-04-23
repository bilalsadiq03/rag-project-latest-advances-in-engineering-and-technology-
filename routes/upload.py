from fastapi import APIRouter, UploadFile, File
import os
from services.process_document import process_document
from services.vector_store import create_vector_store, save_vector_store

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    chunks = process_document(file_path)

    vector_store = create_vector_store(chunks)
    save_vector_store(vector_store)

    return {
        "message": "File processed and stored in vectorDB",
        "chunks": len(chunks)
    }