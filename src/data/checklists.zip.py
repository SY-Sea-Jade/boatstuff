from numbers_to_zip_db import convert, sanitize_name
from numbers_parser import Document
from loguru import logger

doc = Document('src/numbers/checklists.numbers')
for sheet in doc.sheets:
    if sheet.name == 'Master List':
        for table in sheet.tables:
            rows = table.rows(values_only=True)
            headers = [sanitize_name(str(h)) for h in rows[0]]
            logger.info(f"Master List columns: {headers}")
            logger.info(f"Master List row count: {len(rows) - 1}")

convert('src/numbers/checklists.numbers')
