from fastapi import FastAPI, Request
import os
import logging
from src.components.CodeComponent import CodeComponent
from contextlib import asynccontextmanager
import configparser
from starlette.responses import PlainTextResponse

current_directory = os.path.dirname(os.path.abspath(__file__))
ini_file_path = os.path.join(current_directory, "./startup.ini")
config = configparser.ConfigParser()
config.read(ini_file_path)

if not os.path.exists(os.path.abspath(ini_file_path)):
    raise ValueError(os.path.abspath(ini_file_path))

for key, value in config["DEFAULT"].items():
    os.environ[key] = value

logging.basicConfig(
    level=logging.DEBUG,  # Minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Logs to a file
        logging.StreamHandler()         # Logs to the console
    ]
)

@asynccontextmanager
async def lifespan(app: FastAPI):        
    logging.info("init")    
    yield        

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root(request: Request):
    body = await request.body()
    body_text = body.decode("utf-8")
    logging.info(body_text)
    component = CodeComponent()    
    response = component.code(body_text)            
    return {"content": response}

@app.post("/code")
async def post_code(request: Request):
    body = await request.body()
    body_text = body.decode("utf-8")
    logging.info(body_text)
    component = CodeComponent()    
    response = component.code(body_text)                
    return PlainTextResponse(content=response)    

# uvicorn startup:app --host 0.0.0.0 --port 8000 --reload
