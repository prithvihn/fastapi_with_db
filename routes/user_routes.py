from fastapi import FastAPI, APIRouter
router = APIRouter()
@router.get("/signup")
def signup():
    return {"message": "Signup route sucessfully created"}
@router.post("/login")
def login():
    return {"message": "Login route sucessfully created"}