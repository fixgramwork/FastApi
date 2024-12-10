# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

app = FastAPI()


DATABASE_URL = "http//root:1940@db:3306/hacking"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

class SQLInjection(Base):
    __tablename__ = "question"

    id = Column(String,nullable=False)
    password = Column(String,nullable=False)

    

@app.get("/SQL injection")
def SQL_injection():
    with open("/doc/SQL_injection.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.post("/SQLInjectionLogin")
def SQL_injection_login():


@app.get("/XSS")
def XSS():
    with open("/doc/XSS.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.post("/XSSLogin")
def XSSLogin():



@app.get("/Fileinjection")
def Fileinjection():
    with open("/doc/Fileinjection.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)