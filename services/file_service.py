from services.pdf_service import PDFService
from interfaces.storage_interface import StorageInterface
import os

class FileService:
    def __init__(self, storage: StorageInterface):
        self.pdf_service = PDFService()
        self.storage = storage

    def process_image_upload(self, image_path: str, user_id: str):
        output_pdf = image_path.replace(".jpg", ".pdf")
        self.pdf_service.convert_to_pdf(image_path, output_pdf)

        file_url = self.storage.upload_file(output_pdf, f"pdfs/{user_id}.pdf")
        os.remove(output_pdf)

        return file_url
