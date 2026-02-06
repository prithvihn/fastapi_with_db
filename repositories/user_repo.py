from models import user
from sqlalchemy.orm import Session
class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    def add_user(self, user:User):

        self.db.add(user)
        self.db.commit()
        return new_user