from fastapi import APIRouter, UploadFile, File
import os
from services.process_document import process_document

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    chunks = process_document(file_path)

    return {
        "message": "File uploaded and processed successfully",
        "chunks": len(chunks)
    }