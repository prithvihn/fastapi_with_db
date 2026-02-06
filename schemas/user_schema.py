from pdyantic import BaseModel
class user_schema(BaseModel):
    name: str
    email: str
    password: str