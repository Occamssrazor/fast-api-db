import psycopg2
from psycopg2 import Error
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from pydantic import BaseModel, validator
from typing import Optional

def db_connect():
    try:
        dbname = 'postgres'
        user = 'postgres'
        password = 'qweasdzxc123'
        host = 'db_service'
        port = '5432'
        conn = psycopg2.connect(
                dbname=dbname, user=user, password=password, host=host, port=port
               )
        return conn
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Ошибка подключения к базе данных: {e}")


def db_create_user(conn, email, first_name, last_name):
    try:
        sql_statement = """
        INSERT INTO USERS (Email, FirstName, LastName)
        VALUES (%s, %s, %s);
        """
        cursor = conn.cursor()
        cursor.execute(sql_statement, (email, first_name, last_name))
        conn.commit()
        print('OK user')
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка при создании пользователя: {e}")
    finally:
        cursor.close()

app = FastAPI()
router = APIRouter(prefix="/profiles")

profiles_db = {}
conn = db_connect()

class User(BaseModel):
  email: str
  first_name: str
  last_name: str

  @validator('email')
  def validate_email(cls, value):
    if "@" not in value:
      raise ValueError("Неверный формат эмейла")
    return value

@router.post("/", response_model=User, status_code=201)
async def create_profile(user: User, conn: Optional[psycopg2.extensions.connection] = Depends(db_connect)):
  if user.email in profiles_db:
    raise HTTPException(status_code=409, detail="Профиль уже существует")
  profiles_db[user.email] = user
  db_create_user(conn, user.email, user.first_name, user.last_name)
  return user

@router.get("/{email}", response_model=User)
async def get_profile(email: str):
  if email not in profiles_db:
    raise HTTPException(status_code=404, detail="Профиль не найден")
  return profiles_db[email]

@router.get("/", response_model=list[User])
async def get_all_profiles():
  return list(profiles_db.values()) 

@app.get("/")
async def root():
  return {"message": "Добро пожаловать! Введите почту человека через /profiles/ для поиска профиля в базе"}

app.include_router(router)

