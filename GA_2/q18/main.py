from fastapi import FastAPI, File, UploadFile, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import csv
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    x_upload_token_3519: str = Header(None)
):
    if x_upload_token_3519 != "3mv2974ebizgp8vf":
        raise HTTPException(status_code=401, detail="Unauthorized")

    allowed_extensions = [".csv", ".json", ".txt"]
    if not any(file.filename.endswith(ext) for ext in allowed_extensions):
        raise HTTPException(status_code=400, detail="Invalid file type")

    contents = await file.read()

    if len(contents) > 59 * 1024:
        raise HTTPException(status_code=413, detail="File too large")

    if file.filename.endswith(".csv"):
        text_data = contents.decode("utf-8")
        csv_reader = csv.DictReader(io.StringIO(text_data))
        rows = list(csv_reader)
        row_count = len(rows)
        columns = csv_reader.fieldnames

        total_value = 0
        category_counts = {}

        for row in rows:
            total_value += float(row["value"])
            category = row["category"]
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1

        return {
            "email": "24f2008471@ds.study.iitm.ac.in",
            "filename": file.filename,
            "rows": row_count,
            "columns": columns,
            "totalValue": round(total_value, 2),
            "categoryCounts": category_counts
        }
