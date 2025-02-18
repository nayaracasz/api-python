from fastapi import FastAPI
from controllers import user_controller

app = FastAPI(title="API SOLID con Firebase")

app.include_router(user_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)