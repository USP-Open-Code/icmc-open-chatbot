from typing import Dict
import json
from io import BytesIO
from PyPDF2 import PdfReader


class DocumentReader:

    @staticmethod
    async def read_file(file) -> Dict[str, str]:
        try:
            document = {
                "name": file.filename,
                "extension":  file.filename.split('.')[-1]
            }
            content = await file.read()
            document["content"] = eval(
                f"DocumentReader._read_{document['extension']}"
            )(content)

        except Exception as e:
            raise ValueError(
                f"File type not supported: {file.content_type}\n{e}"
            )

        return document

    @staticmethod
    def _read_json(contents):
        return json.loads(contents)

    @staticmethod
    def _read_pdf(contents):
        pdf_document = PdfReader(BytesIO(contents))
        pdf_text = ""
        for page in pdf_document.pages:
            pdf_text += page.extract_text()
        return pdf_text

    @staticmethod
    def _read_plain(contents):
        return contents.decode('utf-8')
