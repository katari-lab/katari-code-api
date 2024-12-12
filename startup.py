
from fastapi import FastAPI, Request
import os
import logging
from src.components.CodeComponent import CodeComponent
from contextlib import asynccontextmanager
import configparser
from starlette.responses import PlainTextResponse

def load_configurations(file_path: str):
    config = configparser.ConfigParser()
    config.read(file_path)
    
    if not os.path.exists(os.path.abspath(file_path)):
        raise ValueError(f"Configuration file not found: {os.path.abspath(file_path)}")
    
    for key, value in config["DEFAULT"].items():
        os.environ[key] = value

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("App initialization")
    yield

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    @app.get("/")
    async def read_root(request: Request):
        body_text = (await request.body()).decode("utf-8")
        logging.info(body_text)
        component = CodeComponent()
        response = component.code(body_text)
        return {"content": response}

    @app.post("/code")
    async def post_code(request: Request):
        body_text = (await request.body()).decode("utf-8")
        logging.info(body_text)
        component = CodeComponent()
        response = component.code(body_text)
        return PlainTextResponse(content=response)

    return app


app = create_app() 

if __name__ == "__main__":
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    ini_file_path = os.path.join(current_directory, "startup.ini")

    load_configurations(ini_file_path)
    setup_logging()    

    import uvicorn
    uvicorn.run("startup:app", host="0.0.0.0", port=8000, reload=True)
    # Run: uvicorn startup:app --host 0.0.0.0 --port 8000 --reload
