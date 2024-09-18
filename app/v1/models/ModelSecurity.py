from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from passlib.context import CryptContext

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    u_email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Para el hashing de contraseñas
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, password: str) -> bool:
        return self.pwd_context.verify(password, self.hashed_password)

    def set_password(self, password: str):
        self.hashed_password = self.pwd_context.hash(password)
