
# FastAPI File Validation Service

## Overview

This project implements a secure file upload validation service using FastAPI.

The service validates:
- Authentication header
- File type
- File size

For valid CSV uploads, it processes the file and returns computed statistics.

---

## Endpoint

POST `/upload`

---

## Authentication

The request must include the following header:

X-Upload-Token-3519: 3mv2974ebizgp8vf

If the header is missing or incorrect, the API returns:

401 Unauthorized

---

## File Upload Requirements

- Content-Type: multipart/form-data
- Field name: `file`
- Allowed file types:
  - .csv
  - .json
  - .txt
- Maximum file size:
  - 59 KB (60416 bytes)

---

## Validation Errors

| Condition | HTTP Status Code |
|------------|------------------|
| Missing or incorrect token | 401 Unauthorized |
| Invalid file type | 400 Bad Request |
| File too large | 413 Payload Too Large |

---

## Success Response (CSV only)

For valid CSV files, the API returns:

```json
{
  "email": "24f2008471@ds.study.iitm.ac.in",
  "filename": "data.csv",
  "rows": 40,
  "columns": ["id", "name", "value", "category"],
  "totalValue": 20293.77,
  "categoryCounts": {"A":13,"C":7,"D":10,"B":10}
}
