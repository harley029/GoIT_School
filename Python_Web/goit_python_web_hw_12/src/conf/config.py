from fastapi.security import OAuth2PasswordBearer


class Config:
    DB_URL = "sqlite+aiosqlite:///./contacts.sqlite"


config = Config()

SECRET_KEY = "X4vPQSP1jouTUM9N74yO42KuIsXVqgaU"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")
