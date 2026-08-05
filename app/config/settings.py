from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    LLM_MODEL: str = "gpt-4o-mini"
    VECTOR_DIM: int = 1536

    class Config:
        env_file = ".env"

settings = Settings()
