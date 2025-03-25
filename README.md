# Nutricost V2 API

A FastAPI-based REST API for managing items with pricing information.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload
```

## TODO
- Add cost entries

The API will be available at `http://localhost:8000/api/v1`