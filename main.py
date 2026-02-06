from fastapi import FastAPI

app = FastAPI(title="CI/CD Test App")

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI CI/CD test running"}

@app.get("/health")
def health():
    return {"health": "healthy"}
#new123456
