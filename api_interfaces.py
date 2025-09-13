from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello World"}

@router.get("/monitor")
def monitor():
    return {"message": "Hello World"}

@router.get("/monitor/{show_id}")
def monitor_show(show_id: str):
    return {"message": "Hello World"}