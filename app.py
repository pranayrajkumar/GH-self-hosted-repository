from fastapi import FastAPI

app = FastAPI(title="Self-Hosted App")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Hello from your self-hosted EC2 runner!",
        "environment": "production"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
