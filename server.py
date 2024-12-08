from chain import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="Langym",description="Registra numero e tipo de cliente da academia")

add_routes(app, chain, path="/register")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

