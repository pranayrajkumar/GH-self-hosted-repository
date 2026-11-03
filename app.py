import logging
import time
from fastapi import FastAPI, Request
from config import settings
from routes import router

# Configure Enterprise-Grade Structured Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] CoreService: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("EnterpriseAPI")

# Initialize FastAPI Application Context
app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url="/docs",       # Swagger UI interactive presentation panel
    redoc_url="/redoc"      # Alternative presentation documentation layer
)

# Operational Middleware: Logs transit latency for performance tracking
@app.middleware("http")
async def track_transaction_latency(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    latency = time.time() - start_time
    logger.info(f"Method={request.method} Path={request.url.path} Latency={latency:.4f}s Status={response.status_code}")
    response.headers["X-Process-Time"] = str(latency)
    return response

# Register Application Routers
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Initializing Application Layer on {settings.HOST}:{settings.PORT}")
    uvicorn.run("app:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
