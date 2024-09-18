import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

#env_path = Path('F:\partes/rafa/app') / '.env'
env_path = Path('./app') / '.env' #genera error si se cambia de lugar
load_dotenv(dotenv_path=env_path.resolve())


class Settings(BaseSettings):

    db: str = os.getenv('DB')
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
    db_url: str = f"{db}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    # fue agregado oauth
    #secret_key: str = os.getenv('SECRET_KEY')



settings = Settings()

