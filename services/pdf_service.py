import img2pdf
from pathlib import Path

class PDFService:
    def convert_to_pdf(self, image_path: str, output_path: str):
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(image_path))
        return output_path