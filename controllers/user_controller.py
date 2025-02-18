from fastapi import APIRouter, UploadFile, File, Form
from services.file_service import FileService
from repositories.firebase_repository import FirebaseRepository

router = APIRouter()
file_service = FileService(FirebaseRepository())

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    name: str = Form(...),
    email: str = Form(...)
):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    user_id = email.replace("@", "_").replace(".", "_")
    pdf_url = file_service.process_image_upload(file_path, user_id)

    user_data = {"name": name, "email": email, "pdf_url": pdf_url}
    file_service.storage.save_user_data(user_data)

    return {"message": "Archivo subido exitosamente", "pdf_url": pdf_url}