import os
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    """Defines enterprise configuration defaults loaded from system environment variables."""
    TITLE: str = "Enterprise Core API Service"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "High-performance production API deployed via automated CI/CD pipeline."
    ENVIRONMENT: str = os.getenv("APP_ENV", "Production")
    
    # Network Layer Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False

settings = AppSettings()
