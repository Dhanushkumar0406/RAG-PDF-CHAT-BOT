from pathlib import Path

from pypdf import PdfReader


class PDFService:
    """
    Handles all PDF-related operations.
    """

    def extract_text(self, pdf_path: Path) -> str:
        """
        Extract all text from a PDF.
        """

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text